"""Shared offline invariants derived from v0.1; no effect dispatcher. See provenance in README."""
from __future__ import annotations
import argparse
from collections import defaultdict
from copy import deepcopy
from datetime import datetime
import hashlib
import json
from pathlib import Path

import rfc8785
from jsonschema import Draft202012Validator, FormatChecker

HERE = Path(__file__).resolve().parent
TERMINAL_SERVICES = {'FULFILLED','PARTIALLY_FULFILLED','WITHDRAWN','TRANSFERRED','FAILED'}
CASE_TRANSITIONS = {
    'PLACEMENT': {'CONSTRUCTION','ASSESSMENT','CLOSURE'},
    'CONSTRUCTION': {'ASSESSMENT','CLOSURE'},
    'ASSESSMENT': {'CONSTRUCTION','DECISION','CLOSURE'},
    'DECISION': {'ASSESSMENT','EXECUTION','ESCALATION','CLOSURE'},
    'EXECUTION': {'ASSESSMENT','ESCALATION','RESOLUTION','CLOSURE'},
    'ESCALATION': {'ASSESSMENT','EXECUTION','RESOLUTION','CLOSURE'},
    'RESOLUTION': {'ASSESSMENT','EXECUTION','CLOSURE'},
    'CLOSURE': {'ASSESSMENT','RESOLUTION','CLOSED'},
    'CLOSED': {'ASSESSMENT','PLACEMENT'},
}

class ContractError(ValueError):
    def __init__(self, code, detail=''):
        self.code, self.detail = code, detail
        super().__init__(f'{code}: {detail}')

def fail(code, detail=''): raise ContractError(code, detail)
def require(condition, code, detail=''):
    if not condition: fail(code, detail)
def instant(value): return datetime.fromisoformat(value.replace('Z','+00:00'))
def digest(value): return 'sha256:' + hashlib.sha256(rfc8785.dumps(value)).hexdigest()
def ref_key(value): return value['type'], value['id'], value['version']
def record_key(value): return value['record_type'], value['record_id'], value['record_version']
def record_ref(value): return {'type':value['record_type'],'id':value['record_id'],'version':value['record_version']}
def money_key(m): return m['currency'], m['exponent']
def units(m): return int(m['units'])
def same_currency(*amounts):
    require(len({money_key(m) for m in amounts}) <= 1, 'CURRENCY_MISMATCH')

def _unique_object(pairs):
    result={}
    for key,value in pairs:
        require(key not in result,'DUPLICATE_JSON_KEY',key)
        result[key]=value
    return result

def load_json(path):
    def invalid_constant(value): fail('INVALID_JSON_NUMBER',value)
    return json.loads(Path(path).read_text(),object_pairs_hook=_unique_object,parse_constant=invalid_constant)

def iter_refs(value):
    if isinstance(value,dict):
        if set(value)=={'type','id','version'}:
            yield value
        else:
            for child in value.values(): yield from iter_refs(child)
    elif isinstance(value,list):
        for child in value: yield from iter_refs(child)

class ContractIndex:
    def __init__(self,bundle):
        self.bundle=bundle
        self.tenant=bundle['tenant_id']
        self.records={}
        self.histories=defaultdict(list)
        for record in bundle['records']:
            key=record_key(record)
            require(key not in self.records,'DUPLICATE_RECORD',str(key))
            require(record['tenant_id']==self.tenant,'TENANT_MISMATCH',record['record_id'])
            self.records[key]=record
            self.histories[key[:2]].append(record)
        for records in self.histories.values(): records.sort(key=lambda x:x['record_version'])

    def get(self,reference):
        key=ref_key(reference)
        require(key in self.records,'MISSING_REFERENCE',str(key))
        return self.records[key]

    def latest(self,kind,identifier,at):
        candidates=[r for r in self.histories.get((kind,identifier),[]) if instant(r['recorded_at'])<=instant(at)]
        require(candidates,'NO_RECORD_AT_TIME',identifier)
        return max(candidates,key=lambda r:r['record_version'])

    def current(self,reference,at):
        r=self.latest(reference['type'],reference['id'],at)
        require(r['record_version']==reference['version'],'STALE_REFERENCE',reference['id'])
        return r

    def latest_all(self,kind,at):
        for (entity_type,identifier),versions in self.histories.items():
            if entity_type==kind and any(instant(r['recorded_at'])<=instant(at) for r in versions):
                yield self.latest(kind,identifier,at)

def check_schema(bundle,schema_path=None):
    schema=load_json(schema_path or HERE/'recovery-contracts.schema.json')
    Draft202012Validator.check_schema(schema)
    validator=Draft202012Validator(schema,format_checker=FormatChecker())
    errors=list(validator.iter_errors(bundle))
    if errors:
        # Select the applicable entity schema for a readable closed-object diagnostic.
        for r in bundle.get('records',[]):
            kind=r.get('record_type')
            if kind in schema['$defs']:
                entity_validator=Draft202012Validator({**schema,'$ref':'#/$defs/'+kind},format_checker=FormatChecker())
                for e in entity_validator.iter_errors(r):
                    fail('SCHEMA_INVALID',f'{r.get("record_id")}: {list(e.path)}: {e.message}')
        e=errors[0]
        fail('SCHEMA_INVALID',f'{list(e.path)}: {e.message[:300]}')
    return schema

def check_financial_position(index,p):
    obligation=index.get(p['obligation_ref'])
    names=['asserted_principal','supported_charges','valid_credits','effective_releases','reconciled_debtor_payments','asserted_outstanding']
    amounts=[p[n] for n in names]
    same_currency(*amounts,*[line['amount'] for line in obligation['lines']])
    require(money_key(amounts[0])==(obligation['currency'],obligation['exponent']),'CURRENCY_MISMATCH')
    line_totals=defaultdict(int)
    for line in obligation['lines']: line_totals[line['kind']]+=units(line['amount'])
    for name,kind in [('asserted_principal','PRINCIPAL'),('supported_charges','SUPPORTED_CHARGE'),('valid_credits','CREDIT')]:
        require(units(p[name])==line_totals[kind],'OBLIGATION_TOTAL_MISMATCH',name)
    paid=0
    for reference in p['allocation_refs']:
        a=index.get(reference)
        require(a['obligation_ref']==p['obligation_ref'],'ALLOCATION_OBLIGATION_MISMATCH')
        require(instant(a['effective_at'])<=instant(p['as_of']),'FUTURE_ALLOCATION')
        payment=index.get(a['payment_ref'])
        same_currency(p['asserted_principal'],a['amount'],payment['amount'])
        require(payment['source_kind']=='DEBTOR_PAYMENT','NON_DEBTOR_PROCEEDS_AS_RECOVERY')
        if a['kind']=='APPLY':
            require(payment['status']=='RECONCILED' and payment['reconciled_at'] is not None,'UNRECONCILED_PAYMENT')
            require(instant(payment['reconciled_at'])<=instant(p['as_of']),'FUTURE_RECONCILIATION')
            paid+=units(a['amount'])
        else:
            require(a['reverses_ref'] is not None,'MISSING_REVERSAL_BASIS')
            original=index.get(a['reverses_ref'])
            require(original['kind']=='APPLY' and original['obligation_ref']==a['obligation_ref'],'INVALID_REVERSAL_BASIS')
            require(payment['status'] in {'REVERSED','REFUNDED'},'UNCONFIRMED_REVERSAL')
            require(units(a['amount'])<=units(original['amount']),'EXCESS_REVERSAL')
            require(a['reverses_ref'] in p['allocation_refs'],'REVERSAL_WITHOUT_ORIGINAL')
            paid-=units(a['amount'])
    require(paid>=0 and paid==units(p['reconciled_debtor_payments']),'PAYMENT_TOTAL_MISMATCH')
    releases=0
    for reference in p['release_agreement_refs']:
        agreement=index.get(reference)
        release=agreement['terms']['release']
        same_currency(p['effective_releases'],release['amount'],agreement['terms']['amount'])
        require(agreement['status']=='FULFILLED','RELEASE_BEFORE_FULFILLMENT')
        require(release['kind']=='CONDITIONAL_REMAINDER_RELEASE','UNSUPPORTED_RELEASE_PROFILE')
        require(agreement['release_effective_at'] is not None and instant(agreement['release_effective_at'])<=instant(p['as_of']),'RELEASE_CONDITION_PENDING')
        require(agreement['release_basis_refs'],'MISSING_RELEASE_EVIDENCE')
        # Test the trigger when it occurred. A later reversal is not automatic waiver revival.
        trigger_paid=0
        for a in index.latest_all('allocation',agreement['recorded_at']):
            if a['obligation_ref']==p['obligation_ref'] and instant(a['effective_at'])<=instant(agreement['release_effective_at']):
                trigger_paid += units(a['amount']) * (1 if a['kind']=='APPLY' else -1)
        require(trigger_paid>=units(agreement['terms']['amount']),'RELEASE_BEFORE_PAYMENT')
        releases+=units(release['amount'])
    require(releases==units(p['effective_releases']),'RELEASE_TOTAL_MISMATCH')
    expected=units(p['asserted_principal'])+units(p['supported_charges'])-units(p['valid_credits'])-releases-paid
    require(expected>=0 and expected==units(p['asserted_outstanding']),'BALANCE_EQUATION_FAILED')

def validate_bundle(bundle,schema_path=None):
    check_schema(bundle,schema_path)
    index=ContractIndex(bundle)
    for reference in iter_refs(bundle): index.get(reference)
    for versions in index.histories.values():
        # A bundle can be a scoped export: gaps are allowed, backwards time is not.
        for prior,current in zip(versions,versions[1:]):
            require(instant(prior['recorded_at'])<=instant(current['recorded_at']),'VERSION_TIME_REVERSED')
            require(prior['created_at']==current['created_at'],'CREATION_TIME_CHANGED')
            if current['record_type']=='action_intent':
                require(prior['binding']==current['binding'],'ACTION_BINDING_MUTATED')
            if current['record_type']=='agreement':
                require(prior['terms']==current['terms'],'AGREEMENT_TERMS_MUTATED')
    for r in bundle['records']:
        kind=r['record_type']
        require(instant(r['created_at'])<=instant(r['recorded_at']),'RECORDED_BEFORE_CREATED',r['record_id'])
        for reference in iter_refs(r):
            require(instant(index.get(reference)['recorded_at'])<=instant(r['recorded_at']),'FUTURE_REFERENCE',r['record_id'])
        if r['valid_from'] and r['valid_until']:
            require(instant(r['valid_from'])<instant(r['valid_until']),'INVALID_VALIDITY_INTERVAL')
        policy=index.get(r['data_policy_ref'])
        require(policy['record_type']=='data_policy','INVALID_DATA_POLICY')
        if kind=='decision_episode':
            require(instant(r['information_cutoff'])<=instant(r['recorded_at']),'FUTURE_DECISION_CUTOFF')
            for reference in r['available_fact_refs']+[r['passport_ref'],r['case_ref']]:
                fact=index.get(reference)
                require(instant(fact['recorded_at'])<=instant(r['information_cutoff']),'FUTURE_INFORMATION_IN_DECISION')
            if r['selection_rule']!='STOCHASTIC_POLICY':
                require(r['selection_probability'] is None,'INVENTED_PROPENSITY')
            else:
                require(r['selection_probability'] is not None,'MISSING_SELECTION_PROBABILITY')
            if r['selected_alternative_id']:
                chosen=[a for a in r['alternatives'] if a['alternative_id']==r['selected_alternative_id']]
                require(len(chosen)==1 and chosen[0]['eligible'],'INELIGIBLE_SELECTED_ROUTE')
            for a in r['alternatives']:
                for key in ['gross_proceeds_range','incremental_cost_range']:
                    require(len(a[key])==2,'INVALID_RANGE')
                    same_currency(*a[key])
                    require(units(a[key][0])<=units(a[key][1]),'REVERSED_RANGE')
                if a['probability_status']=='ABSTAINED': require(a['probability'] is None,'INVENTED_ROUTE_PROBABILITY')
        elif kind=='action_intent':
            require(r['binding_digest']==digest(r['binding']),'ACTION_DIGEST_MISMATCH')
        elif kind=='agreement':
            require(r['terms_digest']==digest(r['terms']),'TERMS_DIGEST_MISMATCH')
            parties={r['proposer_ref']['id'],r['counterparty_ref']['id']}
            if r['status'] in {'ACCEPTED','PERFORMING','FULFILLED'}:
                accepted={a['party_ref']['id'] for a in r['acceptances']}
                require(parties<=accepted,'MISSING_PARTY_ACCEPTANCE')
            for a in r['acceptances']:
                require(a['terms_digest']==r['terms_digest'],'ACCEPTANCE_TERMS_MISMATCH')
                grant=index.current(a['authority_ref'],a['accepted_at'])
                require(grant['status'] in {'ACTIVE','LIMITED'} and not grant['revoked_at'],'ACCEPTANCE_AUTHORITY_INACTIVE')
                require(grant['principal_ref']['id']==a['party_ref']['id'],'ACCEPTANCE_PRINCIPAL_MISMATCH')
                require('settlement.accept' in grant['allowed_actions'],'ACCEPTANCE_AUTHORITY_MISSING')
                require(grant['valid_from'] and instant(grant['valid_from'])<=instant(a['accepted_at']),'ACCEPTANCE_AUTHORITY_NOT_YET_VALID')
                require(grant['valid_until'] and instant(a['accepted_at'])<instant(grant['valid_until']),'ACCEPTANCE_AUTHORITY_EXPIRED')
            if r['release_effective_at']:
                require(r['status']=='FULFILLED' and r['release_basis_refs'],'RELEASE_WITHOUT_BASIS')
        elif kind=='execution_receipt':
            action=index.get(r['action_ref'])
            require(r['binding_digest']==action['binding_digest'],'RECEIPT_BINDING_MISMATCH')
            if r['result']=='RESULT_UNKNOWN':
                require(r['reconciliation_required'] and r['remediation_owner_id'],'UNKNOWN_RESULT_UNOWNED')
            if r['result']=='SUCCEEDED': require(r['source_refs'] and r['observed_at'],'SUCCESS_WITHOUT_OBSERVATION')
        elif kind=='service_request':
            if r['status']=='FULFILLED':
                require(r['deliverable_refs'] and r['fulfilled_conditions'],'SERVICE_COMPLETION_WITHOUT_DELIVERABLE')
            if r['status']=='TRANSFERRED': require(r['transfer_acceptance_ref'],'UNACCEPTED_SERVICE_TRANSFER')
        elif kind=='work_order':
            if r['status'] in {'ACCEPTED','ACTIVE','COMPLETED'}:
                require(r['response_ref'] and r['conditions_resolved'],'PROVIDER_NOT_ACCEPTED')
                require(index.get(r['eligibility_ref'])['result']=='VERIFIED_FOR_SCOPE','PROVIDER_INELIGIBLE')
        elif kind=='waiting_requirement':
            if r['status']=='SATISFIED':
                require(not r['outstanding_requirements'] and r['response_refs'],'WAITING_REQUIREMENT_UNSATISFIED')
        elif kind=='financial_position': check_financial_position(index,r)
        elif kind=='outcome_observation':
            require(instant(r['window_start'])<=instant(r['window_end']),'INVALID_OBSERVATION_WINDOW')
            if r['resolution_kind']=='ASSESSMENT_DELIVERED':
                require(r['debtor_recovery']['status'] in {'UNKNOWN','NOT_APPLICABLE','PENDING'},'ASSESSMENT_AS_RECOVERY')
            if r['financial_position_ref'] and r['debtor_recovery']['status']=='OBSERVED':
                position=index.get(r['financial_position_ref'])
                require(r['debtor_recovery']['value']==position['reconciled_debtor_payments'],'RECOVERY_OBSERVATION_MISMATCH')
            if r['attribution']=='DESCRIPTIVE_ONLY':
                require(r['attribution_basis'],'MISSING_ATTRIBUTION_LIMIT')
        elif kind=='case' and r['state']['lifecycle_stage']=='CLOSED':
            require(r['state']['closure_state']!='OPEN','CLOSED_WITH_OPEN_DISPOSITION')
            require(r['closure_basis_refs'],'CLOSURE_WITHOUT_BASIS')
            for reference in r['service_request_refs']:
                service=index.current(reference,r['recorded_at'])
                require(service['status'] in TERMINAL_SERVICES,'ACTIVE_SERVICE_AT_CLOSURE')
            for service in index.latest_all('service_request',r['recorded_at']):
                if service['case_id']==r['record_id']:
                    require(service['status'] in TERMINAL_SERVICES,'ACTIVE_SERVICE_AT_CLOSURE')
            require(r['state']['completion']['operational']['status']=='SATISFIED','OPERATIONAL_CLOSEOUT_PENDING')
            for name,dimension in r['state']['completion'].items():
                if dimension['status'] in {'PENDING','REOPENED','EXCEPTED'}:
                    require(dimension['owner_id'],'UNOWNED_COMPLETION_DUTY',name)
            if r['state']['closure_state']=='SERVICE_SCOPE_COMPLETE':
                # Completion of scope deliberately imposes no zero-balance condition.
                require(r['state']['payment_state']!='RECONCILED_PAID' or r['state']['completion']['financial']['status']=='SATISFIED','UNSUPPORTED_PAID_CLAIM')
        if 'due' in r and r['due']['basis']=='LEGAL':
            require(r['due']['basis_refs'],'LEGAL_DEADLINE_WITHOUT_BASIS')
        if kind=='event':
            require(r['payload_digest']==digest(r['payload_refs']),'EVENT_PAYLOAD_DIGEST_MISMATCH')
            require(not r['causation_ref'] or r['causation_ref']['id']!=r['record_id'],'EVENT_CAUSAL_CYCLE')
            if r['event_type']=='case.state_changed':
                require(r['state_before_ref'] and r['state_after_ref'],'TRANSITION_STATES_MISSING')
                before,after=index.get(r['state_before_ref']),index.get(r['state_after_ref'])
                require(r['subject_ref']==r['state_after_ref'],'TRANSITION_SUBJECT_MISMATCH')
                authority_verified=False
                if r['authority_ref']:
                    grant=index.current(r['authority_ref'],r['occurred_at'])
                    authority_verified=bool(grant['status'] in {'ACTIVE','LIMITED'} and not grant['revoked_at'] and grant['valid_from'] and grant['valid_until'] and instant(grant['valid_from'])<=instant(r['occurred_at'])<instant(grant['valid_until']))
                    if after['state']['lifecycle_stage']=='CLOSED':authority_verified=authority_verified and 'case.close' in grant['allowed_actions']
                check_case_transition(before,after,reason=','.join(r['reason_codes']),authority_verified=authority_verified)
    # External transaction identity is unique across logical Payment IDs, not versions.
    payment_identities={}
    for (kind,identifier),versions in index.histories.items():
        if kind!='payment': continue
        first=versions[0]
        destination=index.get(first['destination_binding_ref'])
        key=(destination['system'],first['external_transaction_id'],first['source_kind'])
        require(key not in payment_identities,'DUPLICATE_PAYMENT_IDENTITY')
        payment_identities[key]=identifier
    # Apply allocation limits across all linked cases in the tenant at every ledger point.
    allocation_times=sorted({r['recorded_at'] for r in bundle['records'] if r['record_type']=='allocation'})
    for at in allocation_times:
        sums=defaultdict(int)
        reversed_sums=defaultdict(int)
        for a in index.latest_all('allocation',at):
            p=index.get(a['payment_ref'])
            same_currency(a['amount'],p['amount'])
            if a['kind']=='APPLY': sums[p['record_id']]+=units(a['amount'])
            else:
                original=index.get(a['reverses_ref'])
                require(original['payment_ref']['id']==p['record_id'] or p['reversal_of_ref'] and p['reversal_of_ref']['id']==original['payment_ref']['id'],'REVERSAL_PAYMENT_MISMATCH')
                reversed_sums[original['record_id']]+=units(a['amount'])
                require(reversed_sums[original['record_id']]<=units(original['amount']),'EXCESS_REVERSAL')
        for payment_id,total in sums.items():
            payment=index.latest('payment',payment_id,at)
            require(total<=units(payment['amount']),'PAYMENT_OVERALLOCATED')
    for checkpoint in bundle['checkpoints']:
        case=index.get(checkpoint['case_ref'])
        require(instant(case['recorded_at'])<=instant(checkpoint['at']),'FUTURE_CHECKPOINT')
        service=index.current(checkpoint['service_request_ref'],checkpoint['at'])
        require(service['status']==checkpoint['expected_service_result'],'CHECKPOINT_SERVICE_MISMATCH')
        if checkpoint['financial_position_ref']:
            position=index.get(checkpoint['financial_position_ref'])
            require(position['asserted_outstanding']==checkpoint['expected_outstanding'],'CHECKPOINT_BALANCE_MISMATCH')
    return index

def retry_disposition(receipt):
    if receipt['result'] in {'RESULT_UNKNOWN','PARTIALLY_COMPLETED','ACKNOWLEDGED'}:
        return 'RECONCILE_EXISTING_OPERATION'
    if receipt['result']=='SUCCEEDED': return 'DO_NOT_REDISPATCH'
    return 'REVIEW_FAILURE_AND_REAUTHORIZE_IF_NEEDED'

def check_case_transition(before,after,*,reason,authority_verified,late_entry_verified=False):
    require(before['record_id']==after['record_id'] and before['tenant_id']==after['tenant_id'],'TRANSITION_IDENTITY_MISMATCH')
    require(after['record_version']==before['record_version']+1,'TRANSITION_VERSION_CONFLICT')
    a,b=before['state']['lifecycle_stage'],after['state']['lifecycle_stage']
    require(a==b or b in CASE_TRANSITIONS[a] or late_entry_verified,'ILLEGAL_LIFECYCLE_TRANSITION')
    require(bool(reason),'TRANSITION_REASON_REQUIRED')
    if a=='CLOSED' or b in {'EXECUTION','ESCALATION','CLOSED'}:
        require(authority_verified,'TRANSITION_AUTHORITY_REQUIRED')
    return True
