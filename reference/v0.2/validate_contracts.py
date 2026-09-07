"""GRE 0.2.0 offline reference semantics. No network, DB, runtime authorization or dispatch.

Stored synthetic snapshots use the retained core invariants; PilotHarness demonstrates a
bounded provider-review/acceptance/activation sequence against caller-supplied test time.
Every identity, source, policy and review in fixtures is assumed, never authenticated here.
"""
from __future__ import annotations
from copy import deepcopy
from pathlib import Path
import argparse
import json
from jsonschema import Draft202012Validator, FormatChecker
from foundation_checks import (ContractError, ContractIndex, digest, instant, iter_refs,
    load_json, record_ref, ref_key, require, validate_bundle as validate_foundation)

HERE = Path(__file__).resolve().parent
PILOT_MODES = {'ASSESS', 'PREPARE', 'TRANSFER', 'CONTROL', 'OBSERVE'}
GRE_ACTIONS = {'provider.place', 'assessment.deliver', 'evidence.request', 'payment.reconcile', 'case.close', 'source.writeback'}

def packet_digest(disclosure):
    return digest({k: v for k, v in disclosure.items() if k != 'packet_digest'})

def current(index, reference, now):
    r = index.current(reference, now)
    require(not r['valid_from'] or instant(r['valid_from']) <= instant(now), 'NOT_YET_VALID')
    require(not r['valid_until'] or instant(now) < instant(r['valid_until']), 'EXPIRED_RECORD')
    return r

def current_grant(index, reference, now, principal=None, actor=None, action=None):
    r = current(index, reference, now)
    require(r['status'] in {'ACTIVE','LIMITED'} and not r['revoked_at'], 'AUTHORITY_INACTIVE')
    require(r['valid_from'] and r['valid_until'] and instant(now) < instant(r['recheck_at']), 'AUTHORITY_REVIEW_REQUIRED')
    require(current(index,r['verification_ref'],now)['result']=='VERIFIED_FOR_SCOPE', 'AUTHORITY_UNVERIFIED')
    if principal: require(r['principal_ref']==principal, 'AUTHORITY_PRINCIPAL_MISMATCH')
    if actor: require(r['grantee_actor_id']==actor, 'AUTHORITY_ACTOR_MISMATCH')
    if action: require(action in r['allowed_actions'] and action not in r['prohibited_actions'], 'AUTHORITY_ACTION_DENIED')
    return r

def current_gate(index, case, service, corridor, now, actor):
    """Bounded Trade profile gate. Entitlements are never classification or legal approval."""
    c = current(index, record_ref(case), now)
    s = current(index, record_ref(service), now)
    p = current(index, record_ref(corridor), now)
    f, release = c['classification'], p['release_profile']
    require(f['matter_family']=='TRADE' and f['status']=='CONFIRMED' and f['purpose']=='BUSINESS'
        and f['obligated_party_type']=='BUSINESS' and not f['natural_person_involved']
        and f['claim_type']=='COMMERCIAL_GOODS_SERVICES' and f['claimant_type']=='BUSINESS', 'CLASSIFICATION_HOLD')
    require((f['creditor_country'],f['obligor_country'])==('IN','US') and
        (p['origin_country'],p['destination_country'])==('IN','US'), 'CORRIDOR_SCOPE_DENIED')
    require((f['matter_family'],f['profile_id'],f['profile_version'])==
        (release['matter_family'],release['profile_id'],release['profile_version']), 'PROFILE_MISMATCH')
    require(s['service_mode'] in PILOT_MODES and s['service_mode'] in release['service_modes'], 'SERVICE_MODE_UNRELEASED')
    require(s['case_id']==c['record_id'] and s['status'] in {'ACTIVE','WAITING'}, 'SERVICE_INACTIVE')
    require('provider.place' in s['allowed_actions'],'SERVICE_SCOPE_DENIED')
    require(instant(s['window']['starts_at'])<=instant(now) and
        (not s['window']['ends_at'] or instant(now)<instant(s['window']['ends_at'])), 'SERVICE_WINDOW_ENDED')
    require(p['status'] in {'PILOT_ENABLED','COMMERCIALLY_SUPPORTED'}, 'PRODUCT_UNRELEASED')
    require(release['legal_review'] in {'COUNSEL_REVIEW_CURRENT','APPROVED_WITH_CONDITIONS'} and
        not release['conditions'] and not p['unresolved_applicability'] and
        instant(now)<instant(p['review_due_at']), 'LEGAL_REVIEW_REQUIRED')
    require(release['release_evidence_refs'] and actor in release['actor_ids'] and
        release['executor_pattern']=='DIRECT_PROVIDER', 'RELEASE_ACTOR_DENIED')
    require(not any(h['status']=='ACTIVE' for h in c['state']['holds']), 'ACTIVE_HOLD')
    require(p['source_lifecycle'], 'SOURCE_REVIEW_REQUIRED')
    for source in p['source_lifecycle']:
        require(source['status']=='CURRENT' and instant(source['effective_from'])<=instant(now) and
            (not source['effective_until'] or instant(now)<instant(source['effective_until'])), 'SOURCE_REVIEW_REQUIRED')
    # This harness represents only the named provider.place policy/capability profile.
    policy=current(index,record_ref(index.latest('policy_snapshot','policy_offer',now)),now)
    require(policy['case_id']==c['record_id'] and policy['action_type']=='provider.place' and
        policy['decision']=='ALLOW' and not policy['conditions'] and not policy['unresolved_issues'] and
        instant(policy['evaluated_at'])<=instant(now)<instant(policy['expires_at']), 'CURRENT_POLICY_DENIED')
    for reference in policy['material_refs']: current(index,reference,now)
    passport=current(index,c['passport_ref'],now)
    for reference in passport['assertion_refs']+passport['rights_refs']+[passport['financial_position_ref']]:
        current(index,reference,now)
    capability=current(index,record_ref(index.latest('capability','capability_offer',now)),now)
    require(capability['status'] in {'PILOT_ENABLED','COMMERCIALLY_SUPPORTED'} and
        'provider.place' in capability['allowed_actions'] and p['corridor_id'] in capability['corridor_ids'] and
        instant(now)<instant(capability['reassess_at']), 'CAPABILITY_UNAVAILABLE')
    for reference in capability['assurance_refs']:
        require(current(index,reference,now)['result']=='VERIFIED_FOR_SCOPE','CAPABILITY_ASSURANCE_INVALID')
    return c, s, p

def check_disclosure(index, work, now):
    d = work['disclosure']
    require(d['packet_digest']==packet_digest(d), 'DISCLOSURE_DIGEST_MISMATCH')
    require(d['access_state']=='ACTIVE' and instant(now)<instant(d['expires_at']), 'DISCLOSURE_ACCESS_ENDED')
    require(d['recipient_ref']==work['provider_ref'], 'DISCLOSURE_RECIPIENT_MISMATCH')
    require(d['included_refs'] or d['redacted_refs'], 'EMPTY_DISCLOSURE')
    policy = current(index,d['permission_basis_ref'],now)
    require(policy['disposition']=='ACTIVE' and policy['service_processing'] and
        d['purpose'] in policy['permitted_purposes'] and d['recipient_ref'] in policy['disclosure_party_refs'], 'DISCLOSURE_NOT_PERMITTED')
    disclosed=d['included_refs']+d['redacted_refs']
    require(not set(map(ref_key,disclosed)) & set(map(ref_key,d['withheld_refs'])), 'WITHHELD_DATA_DISCLOSED')
    require(set(map(ref_key,disclosed))=={ref_key(x['source_ref']) for x in d['recipient_mappings']}, 'RECEIVER_MAPPING_MISSING')
    require(len({x['receiving_id'] for x in d['recipient_mappings']})==len(disclosed), 'RECEIVER_MAPPING_COLLISION')
    for reference in disclosed:
        e=current(index,reference,now)
        require(e['disposition']=='RETAINED','SOURCE_UNAVAILABLE')
        require(not set(e.get('disclosure_labels',[])) & {'PRIVILEGED','RESTRICTED','LEGAL_HOLD','TRADE_SECRET'}, 'RESTRICTED_DISCLOSURE')
        ep=current(index,e['data_policy_ref'],now)
        require(ep['disposition']=='ACTIVE' and ep['service_processing'] and d['purpose'] in ep['permitted_purposes'] and d['recipient_ref'] in ep['disclosure_party_refs'], 'SOURCE_DISCLOSURE_DENIED')
        require(not ep['retention_until'] or instant(now)<instant(ep['retention_until']), 'SOURCE_RETENTION_ENDED')
    return deepcopy(disclosed)

def check_transfer_authority(index,work,case,service,corridor,now,actor):
    grant=current_grant(index,service['authority_ref'],now,service['principal_ref'],actor,'provider.place')
    require(case['record_id'] in grant['case_ids'] and corridor['corridor_id'] in grant['corridor_ids'] and
        work['route'] in grant['routes'] and 'PORTAL' in grant['channels'] and
        work['provider_ref'] in grant['recipient_refs'] and 'PREPARE' in grant['execution_modes'] and
        set(map(ref_key,case['obligation_refs']))<=set(map(ref_key,grant['obligation_refs'])), 'AUTHORITY_SCOPE_DENIED')
    return grant

def check_profile(index, work, case, corridor, now):
    p=current(index,work['provider_acceptance_profile_ref'],now)
    require(p['provider_ref']==work['provider_ref'] and p['declaration_ref'] and
        p['authorship'] in {'PROVIDER_AUTHORED','PROVIDER_APPROVED'}, 'PROFILE_NOT_PROVIDER_DECLARED')
    require(case['classification']['matter_family'] in p['supported_families'] and
        case['classification']['claim_type'] in p['claim_types'] and corridor['corridor_id'] in p['corridor_ids'], 'PROVIDER_SCOPE_DENIED')
    require(p['capacity_state']=='AVAILABLE' and instant(now)<instant(p['review_due_at']), 'PROVIDER_UNAVAILABLE')
    require(p['credential_refs'], 'PROVIDER_CREDENTIALS_MISSING')
    for r in p['credential_refs']:
        require(current(index,r,now)['result']=='VERIFIED_FOR_SCOPE', 'PROVIDER_INELIGIBLE')
    return p

def validate_bundle(bundle):
    index=validate_foundation(bundle,HERE/'recovery-contracts.schema.json')
    for r in bundle['records']:
        k=r['record_type']
        if k=='work_order':
            require(r['disclosure']['packet_digest']==packet_digest(r['disclosure']), 'DISCLOSURE_DIGEST_MISMATCH')
            if r['status']=='ACTIVE': require(r['provider_work_state']=='ACTIVE','WORK_STATE_MISMATCH')
            if r['status']=='ACCEPTED': require(r['acceptance_state']=='ACCEPTED' and r['conditions_resolved'],'WORK_STATE_MISMATCH')
            if r['status']=='DECLINED': require(r['acceptance_state']=='REJECTED','WORK_STATE_MISMATCH')
            if r['preflight_state']=='READY': require(r['preflight_profile_ref']==r['provider_acceptance_profile_ref'] and r['preflight_packet_digest'], 'PREFLIGHT_VERSION_MISMATCH')
            if r['acceptance_state'] in {'ACCEPTED','CONDITIONAL','REJECTED'}: require(r['response_ref'] and r['accepted_packet_digest'], 'PROVIDER_RESPONSE_MISSING')
            if r['acceptance_state']=='CONDITIONAL': require(r['validation_delta'] or any(c['status']=='OPEN' for c in r['execution_conditions']), 'CONDITIONAL_WITHOUT_DELTA')
            if r['provider_work_state']=='ACTIVE':
                require(r['acceptance_state']=='ACCEPTED' and r['activation_at'] and r['cutover_at'] and
                    r['direct_appointment_ref'] and r['independent_validation_ref'] and r['conditions_resolved'] and
                    all(c['status']=='SATISFIED' and c['evidence_refs'] for c in r['execution_conditions']), 'ACTIVATION_INCOMPLETE')
        elif k=='service_request':
            if r['service_mode'] in PILOT_MODES: require(set(r['allowed_actions'])<=GRE_ACTIONS, 'GRE_COLLECTION_SCOPE_DENIED')
            if r['status']=='TRANSFERRED':
                matches=[w for w in index.latest_all('work_order',r['recorded_at']) if w['service_request_ref']['id']==r['record_id']]
                require(any(w['acceptance_state']=='ACCEPTED' and w['activation_at'] for w in matches), 'TRANSFER_WITHOUT_ACTIVATION')
        elif k=='payment':
            destination=index.get(r['destination_binding_ref'])
            require(destination.get('funds_role') in {'CREDITOR_DIRECT','AUTHORIZED_INSTITUTION'}, 'GRE_CUSTODY_DENIED')
            if r.get('observation_source')=='PROVIDER_REPORT': require(r['status']=='REPORTED' and r['reconciled_at'] is None, 'REPORT_NOT_TRUSTED_PAYMENT')
        elif k=='execution_receipt':
            a=index.get(r['action_ref']);attribution=r['attribution']
            require(attribution['principal_ref']==a['binding']['principal_ref'] and
                attribution['performer_id']==a['binding']['executor_id'],'RECEIPT_ATTRIBUTION_MISMATCH')
            if r['result']=='RESULT_UNKNOWN': require(attribution['source_status']=='UNKNOWN','UNCERTAINTY_ERASED')
        elif k=='evidence_assertion' and r.get('correction'):
            old=index.get(r['correction']['supersedes_ref'])
            require(old['record_id']==r['record_id'] and old['record_version']<r['record_version'], 'CORRECTION_LINEAGE_INVALID')
        elif k=='outcome_observation':
            for dimension in r.get('quality_dimensions',[]):
                if dimension['status']=='OBSERVED':
                    require(dimension['value'] is not None and dimension['source_refs'] and dimension['denominator']>0,'QUALITY_OBSERVATION_WITHOUT_BASIS')
                else: require(dimension['value'] is None,'QUALITY_MISSINGNESS_ERASED')
        elif k=='case' and r.get('inactive_private_context'):
            p=r['inactive_private_context'];require(r['classification']['matter_family']=='PRIVATE_RESOLUTION','PRIVATE_CONTEXT_FAMILY_MISMATCH')
            require(not set(map(ref_key,p['shared_refs'])) & set(map(ref_key,p['requester_private_refs']+p['respondent_private_refs'])), 'PRIVATE_CONTEXT_LEAK')
    return index

class PilotHarness:
    """Single-threaded reference transitions only. Mutations append snapshots in memory."""
    def __init__(self,bundle):
        self.bundle=deepcopy(bundle);self.index=validate_bundle(self.bundle);self.effects=[]
    def latest(self,kind,id,now):return self.index.latest(kind,id,now)
    def append(self,r,now,**changes):
        new=deepcopy(r);new.update(changes,record_version=r['record_version']+1,recorded_at=now)
        self.bundle['records'].append(new);self.index=ContractIndex(self.bundle);return new
    def context(self,now):
        w=self.latest('work_order','work_demo',now)
        c=self.latest('case',w['case_ref']['id'],now)
        s=self.latest('service_request',w['service_request_ref']['id'],now)
        p=self.latest('corridor_pack','corridor_pack_demo',now)
        return w,c,s,p
    def preflight(self,now,actor='actor_operator'):
        w,c,s,p=self.context(now);current_gate(self.index,c,s,p,now,actor)
        require(w['provider_work_state']=='NOT_STARTED' and w['acceptance_state'] in {'PENDING','CONDITIONAL'},'PLACEMENT_STATE_CONFLICT')
        check_transfer_authority(self.index,w,c,s,p,now,actor)
        profile=check_profile(self.index,w,c,p,now);disclosed=check_disclosure(self.index,w,now)
        missing=set(profile['required_evidence_ids'])-{r['id'] for r in disclosed}
        delta=[{'requirement_id':x,'reason':'Named profile requirement missing','status':'OPEN','source_refs':[]} for x in sorted(missing)]
        return self.append(w,now,preflight_profile_ref=record_ref(profile),preflight_packet_digest=w['disclosure']['packet_digest'],preflight_state='DELTA' if missing else 'READY',validation_delta=delta)
    def respond(self,response,now,actor='actor_provider'):
        require(response in {'ACCEPTED','CONDITIONAL','REJECTED'},'INVALID_PROVIDER_RESPONSE')
        w,c,s,p=self.context(now);current_gate(self.index,c,s,p,now,actor)
        require(actor=='actor_provider','PROVIDER_ACTOR_MISMATCH')
        require(w['provider_work_state']=='NOT_STARTED' and w['acceptance_state'] in {'PENDING','CONDITIONAL'},'PLACEMENT_STATE_CONFLICT')
        profile=check_profile(self.index,w,c,p,now)
        require(w['preflight_profile_ref']==record_ref(profile),'STALE_PREFLIGHT')
        require(w['preflight_packet_digest']==w['disclosure']['packet_digest'],'PREFLIGHT_PACKET_CHANGED')
        require(instant(now)<instant(w['offer_expires_at']),'OFFER_EXPIRED')
        check_disclosure(self.index,w,now)
        if response=='ACCEPTED':require(w['preflight_state']=='READY','PROVIDER_DELTA_OPEN')
        if response=='CONDITIONAL':require(w['validation_delta'] or any(x['status']=='OPEN' for x in w['execution_conditions']),'CONDITIONAL_WITHOUT_DELTA')
        # Imported signed response evidence is synthetic. Authentication is an unimplemented adapter gate.
        return self.append(w,now,acceptance_state=response,accepted_packet_digest=w['disclosure']['packet_digest'],response_ref={'type':'evidence_item','id':'ev_provider_eligibility','version':1},status={'ACCEPTED':'OFFERED','CONDITIONAL':'ACCEPTED_WITH_CONDITIONS','REJECTED':'DECLINED'}[response])
    def appoint(self,grant_ref,now,actor='actor_creditor'):
        w,c,s,p=self.context(now);current_gate(self.index,c,s,p,now,actor)
        require(actor=='actor_creditor','CREDITOR_DECISION_REQUIRED')
        grant=current_grant(self.index,grant_ref,now,s['principal_ref'],'actor_provider')
        require(grant['grantor_ref']==s['principal_ref'] and grant['grantee_organization_ref']==w['provider_ref'],'DIRECT_APPOINTMENT_MISMATCH')
        require(c['record_id'] in grant['case_ids'] and set(w['permitted_actions'])<=set(grant['allowed_actions']) and not set(w['permitted_actions'])&set(grant['prohibited_actions']),'APPOINTMENT_SCOPE_DENIED')
        return self.append(w,now,direct_appointment_ref=grant_ref)
    def fulfill_conditions(self,now,validation_ref,source_refs):
        w,*_=self.context(now)
        require(current(self.index,validation_ref,now)['result']=='VERIFIED_FOR_SCOPE' and source_refs,'VALIDATION_MISSING')
        for r in source_refs:current(self.index,r,now)
        return self.append(w,now,independent_validation_ref=validation_ref,execution_conditions=[{**x,'status':'SATISFIED','evidence_refs':source_refs} for x in w['execution_conditions']],conditions_resolved=True)
    def activate(self,now,actor='actor_provider'):
        w,c,s,p=self.context(now);current_gate(self.index,c,s,p,now,actor)
        profile=check_profile(self.index,w,c,p,now)
        require(w['preflight_profile_ref']==record_ref(profile),'STALE_PREFLIGHT')
        require(w['acceptance_state']=='ACCEPTED' and instant(now)<instant(w['offer_expires_at']),'PLACEMENT_NOT_ACCEPTED')
        require(w['accepted_packet_digest']==w['disclosure']['packet_digest'],'ACCEPTED_PACKET_CHANGED')
        require(w['preflight_packet_digest']==w['disclosure']['packet_digest'],'PREFLIGHT_PACKET_CHANGED')
        require(w['direct_appointment_ref'],'DIRECT_APPOINTMENT_REQUIRED')
        g=current_grant(self.index,w['direct_appointment_ref'],now,s['principal_ref'],actor)
        require(g['grantee_organization_ref']==w['provider_ref'] and c['record_id'] in g['case_ids'] and set(w['permitted_actions'])<=set(g['allowed_actions']),'APPOINTMENT_SCOPE_DENIED')
        require(p['corridor_id'] in g['corridor_ids'] and w['route'] in g['routes'] and
            not set(w['permitted_actions'])&set(g['prohibited_actions']), 'APPOINTMENT_SCOPE_DENIED')
        require((g['budget_cap']['currency'],g['budget_cap']['exponent'])==(w['budget_cap']['currency'],w['budget_cap']['exponent']) and int(w['budget_cap']['units'])<=int(g['budget_cap']['units']),'APPOINTMENT_BUDGET_EXCEEDED')
        require(w['conditions_resolved'] and all(x['status']=='SATISFIED' and x['evidence_refs'] for x in w['execution_conditions']) and w['independent_validation_ref'],'EXECUTION_CONDITIONS_OPEN')
        require(current(self.index,w['independent_validation_ref'],now)['result']=='VERIFIED_FOR_SCOPE','VALIDATION_MISSING')
        require(not w['conflicting_mandate_refs'],'CONFLICTING_MANDATE')
        check_disclosure(self.index,w,now)
        rights=self.latest('rights_interest','rights_owner',now)
        require(current(self.index,record_ref(rights),now)['status']=='VERIFIED_FOR_SCOPE' and rights['holder_ref']==s['principal_ref'],'RIGHTS_UNVERIFIED')
        for effect in self.effects:
            if effect['state']=='QUEUED':effect['state']='CANCELLED_BEFORE_DISPATCH'
            elif effect['state'] in {'SENT','IN_FLIGHT','RESULT_UNKNOWN'}:effect.update(reconciliation_required=True,remediation_owner_id=s['owner_id'])
        w=self.append(w,now,status='ACTIVE',provider_work_state='ACTIVE',activation_at=now,cutover_at=now,external_copy_state='RETAINED_OR_UNKNOWN')
        self.append(s,now,status='TRANSFERRED',transfer_acceptance_ref=w['response_ref'],fulfilled_conditions=['Independent acceptance, direct appointment, conditions and cutover recorded'],deliverable_refs=[record_ref(w)])
        return w
    def expire_offer(self,now):
        w,*_=self.context(now);require(instant(now)>=instant(w['offer_expires_at']) and not w['activation_at'],'OFFER_NOT_EXPIRED')
        return self.append(w,now,acceptance_state='EXPIRED',status='CANCELLED')
    def recall(self,now):
        w,*_=self.context(now);d=deepcopy(w['disclosure']);d['access_state']='REVOKED';d['packet_digest']=packet_digest(d)
        return self.append(w,now,disclosure=d,provider_work_state='UNKNOWN',status='RETURN_PENDING',cessation_acknowledgment='REQUESTED',external_copy_state='RETAINED_OR_UNKNOWN')
    def export(self,now):
        w,*_=self.context(now);return check_disclosure(self.index,w,now)
    def correction_recipients(self,correction,now):
        targets=[]
        for ref in correction['recipient_work_order_refs']:
            w=current(self.index,ref,now);check_disclosure(self.index,w,now);targets.append(w['provider_ref'])
        return targets
    def check_new_gre_effect(self,now,action='provider.place'):
        require(action in GRE_ACTIONS,'GRE_COLLECTION_SCOPE_DENIED')
        w,c,s,p=self.context(now);current_gate(self.index,c,s,p,now,'actor_operator')
        current_grant(self.index,s['authority_ref'],now,s['principal_ref'],'actor_operator',action)
        check_transfer_authority(self.index,w,c,s,p,now,'actor_operator')
        require(action in s['allowed_actions'],'SERVICE_SCOPE_DENIED')
        require(not w['cutover_at'],'GRE_ROLE_ENDED')
        return True

def affected_work_orders(index,profile_ref,now):
    """Return stale profile bindings only; historical snapshots are not changed."""
    latest=index.latest(profile_ref['type'],profile_ref['id'],now)
    return [record_ref(w) for w in index.latest_all('work_order',now)
        if w['provider_acceptance_profile_ref']['id']==latest['record_id'] and
        (w['provider_acceptance_profile_ref']!=record_ref(latest) or w['preflight_profile_ref']!=record_ref(latest))]

def permitted_private_view(case,actor):
    p=case['inactive_private_context'];shared=deepcopy(p['shared_refs'])
    if actor==p['requester_id']:return shared+deepcopy(p['requester_private_refs'])
    if actor==p['respondent_id']:return shared+deepcopy(p['respondent_private_refs'])
    return []  # Sponsor/payer receives no implicit participant evidence.

def check_data_use(policy,purpose):
    require(purpose in {'service_processing','tenant_evaluation','pooled_benchmarking','model_training'} and policy[purpose],'DATA_USE_DENIED')

def validate_compositions(compositions,index):
    schema=load_json(HERE/'recovery-contracts.schema.json')
    validator=Draft202012Validator({**schema,'$ref':'#/$defs/ContractCompositions'},format_checker=FormatChecker())
    require(not list(validator.iter_errors(compositions)),'COMPOSITION_SCHEMA_INVALID')
    require(len({v['contract_type'] for v in compositions['views']})==6,'COMPOSITION_MISSING_OR_DUPLICATE')
    for reference in iter_refs(compositions):index.get(reference)
    return True

def main():
    parser=argparse.ArgumentParser();parser.add_argument('path',nargs='?',default=str(HERE/'worked-trade.json'));args=parser.parse_args()
    b=load_json(args.path);index=validate_bundle(b)
    validate_compositions(load_json(HERE/'contract-compositions.json'),index)
    print(f'VALID: {len(b["records"])} synthetic records and six compositions, contract {b["contract_version"]}; no runtime or release verification')
if __name__=='__main__':main()
