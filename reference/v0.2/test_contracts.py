"""Behavioral conformance for represented offline Foundation + Trade semantics."""
from copy import deepcopy
import json
from pathlib import Path
import unittest
from validate_contracts import *

T='2026-09-03T12:00:00Z'
END='2026-10-02T12:00:00Z'
R=lambda kind,id,version=1:{'type':kind,'id':id,'version':version}

def fixture():return load_json(HERE/'worked-trade.json')
def one(bundle,kind,id=None):return next(r for r in bundle['records'] if r['record_type']==kind and (id is None or r['record_id']==id))
def grant_for_provider(h):
    g=deepcopy(h.latest('authority_grant','grant_operator',T));g.update(record_id='grant_provider',grantee_actor_id='actor_provider',grantee_organization_ref=R('party','party_provider'),recorded_at=T)
    h.bundle['records'].append(g);h.index=ContractIndex(h.bundle);return record_ref(g)
def accepted(h):h.preflight(T);h.respond('ACCEPTED',T)
def activation_ready(h):
    accepted(h);h.appoint(grant_for_provider(h),T);h.fulfill_conditions(T,R('verification_record','verification_provider'),[R('evidence_item','ev_mandate')])

class PilotConformance(unittest.TestCase):
    def rejected(self,code,call):
        with self.assertRaises(ContractError) as e:call()
        self.assertEqual(code,e.exception.code)
    def test_foundation_shapes_sources_money_and_checkpoints(self):
        b=fixture();i=validate_bundle(b)
        self.assertEqual('7800000',i.get(R('financial_position','position_demo'))['asserted_outstanding']['units'])
    def test_six_contract_compositions_resolve_sources_and_cannot_mint_authority(self):
        i=validate_bundle(fixture());views=load_json(HERE/'contract-compositions.json')
        self.assertTrue(validate_compositions(views,i))
        envelope=next(v for v in views['views'] if v['contract_type']=='AuthorityEnvelope')
        envelope['allowed_actions']=['funds.instruct']
        self.rejected('COMPOSITION_SCHEMA_INVALID',lambda:validate_compositions(views,i))
    def test_complete_trade_path_transfer_is_not_cash_or_case_closure(self):
        h=PilotHarness(fixture());activation_ready(h);w=h.activate(T)
        self.assertEqual(('ACCEPTED','ACTIVE'),(w['acceptance_state'],w['provider_work_state']))
        self.assertEqual('TRANSFERRED',h.latest('service_request','service_operate',T)['status'])
        self.assertEqual('7800000',h.latest('financial_position','position_demo',T)['asserted_outstanding']['units'])
        self.assertNotEqual('CLOSED',h.latest('case','case_demo',T)['state']['lifecycle_stage'])
        validate_bundle(h.bundle)
    def test_assessment_deliverable_does_not_imply_payment(self):
        h=PilotHarness(fixture());s=h.latest('service_request','service_assess',T)
        self.assertEqual('FULFILLED',s['status']);self.assertEqual('0',h.latest('financial_position','position_demo',T)['reconciled_debtor_payments']['units'])
    def test_trade_rejects_consumer_mixed_unknown_and_natural_person(self):
        for change in [{'matter_family':'CONSUMER_CREDIT'},{'purpose':'MIXED'},{'purpose':'UNKNOWN'},{'natural_person_involved':True},{'obligated_party_type':'NATURAL_PERSON'}]:
            with self.subTest(change=change):
                b=fixture()
                for c in b['records']:
                    if c['record_type']=='case':c['classification'].update(change)
                self.rejected('CLASSIFICATION_HOLD',lambda:PilotHarness(b).preflight(T))
    def test_network_entitlement_cannot_enable_inactive_families(self):
        for name in ['worked-consumer-inactive.json','worked-private-inactive.json']:
            with self.subTest(fixture=name):
                b=load_json(HERE/name);validate_bundle(b)
                self.rejected('CLASSIFICATION_HOLD',lambda:PilotHarness(b).preflight(T))
    def test_availability_and_legal_review_are_separate_gates(self):
        for field,value,code in [('status','DESIGNED','PRODUCT_UNRELEASED'),('legal_review','UNREVIEWED','LEGAL_REVIEW_REQUIRED')]:
            b=fixture();c=one(b,'corridor_pack')
            if field=='status':c[field]=value
            else:c['release_profile'][field]=value
            self.rejected(code,lambda:PilotHarness(b).preflight(T))
    def test_current_source_withdrawal_blocks_new_action(self):
        b=fixture();one(b,'corridor_pack')['source_lifecycle'][0]['status']='WITHDRAWN'
        self.rejected('SOURCE_REVIEW_REQUIRED',lambda:PilotHarness(b).preflight(T))
    def test_current_case_policy_can_block_previously_prepared_work(self):
        b=fixture();one(b,'policy_snapshot')['decision']='DENY'
        self.rejected('CURRENT_POLICY_DENIED',lambda:PilotHarness(b).preflight(T))
    def test_receipt_preserves_uncertainty_and_actual_transmitter(self):
        b=fixture();r=one(b,'execution_receipt');self.assertEqual('RESULT_UNKNOWN',r['result'])
        self.assertTrue(r['reconciliation_required']);self.assertEqual('actor_operator',r['attribution']['transmitter_id'])
        r['remediation_owner_id']=None
        self.rejected('UNKNOWN_RESULT_UNOWNED',lambda:validate_bundle(b))
        b=fixture();one(b,'execution_receipt')['attribution']['performer_id']='actor_provider'
        self.rejected('RECEIPT_ATTRIBUTION_MISMATCH',lambda:validate_bundle(b))
    def test_expired_authority_blocks_new_preflight(self):
        b=fixture();one(b,'authority_grant','grant_operator')['valid_until']='2026-09-03T10:00:00Z'
        self.rejected('EXPIRED_RECORD',lambda:PilotHarness(b).preflight(T))
    def test_expired_or_corrected_mandate_verification_blocks_new_preflight(self):
        b=fixture();one(b,'verification_record','verification_mandate')['valid_until']='2026-09-03T10:00:00Z'
        self.rejected('EXPIRED_RECORD',lambda:PilotHarness(b).preflight(T))
        h=PilotHarness(fixture());v=h.latest('verification_record','verification_mandate',T)
        h.append(v,T,result='NOT_VERIFIED')
        self.rejected('STALE_REFERENCE',lambda:h.preflight(T))
    def test_review_disclosure_precedes_and_does_not_authorize_execution(self):
        h=PilotHarness(fixture());w=h.preflight(T)
        self.assertEqual('READY',w['preflight_state']);self.assertIsNone(w['direct_appointment_ref'])
        self.assertEqual('NOT_STARTED',w['provider_work_state'])
        self.rejected('PLACEMENT_NOT_ACCEPTED',lambda:h.activate(T))
    def test_provider_delta_conditional_acceptance_retains_open_requirements(self):
        b=fixture();one(b,'provider_acceptance_profile')['required_evidence_ids'].append('ev_cure')
        h=PilotHarness(b);w=h.preflight(T);self.assertEqual('DELTA',w['preflight_state'])
        w=h.respond('CONDITIONAL',T);self.assertEqual('ev_cure',w['validation_delta'][0]['requirement_id'])
        self.rejected('PLACEMENT_NOT_ACCEPTED',lambda:h.activate(T))
    def test_accepted_placement_still_requires_direct_appointment(self):
        h=PilotHarness(fixture());accepted(h);self.rejected('DIRECT_APPOINTMENT_REQUIRED',lambda:h.activate(T))
    def test_direct_appointment_still_requires_execution_conditions(self):
        h=PilotHarness(fixture());accepted(h);h.appoint(grant_for_provider(h),T)
        self.rejected('EXECUTION_CONDITIONS_OPEN',lambda:h.activate(T))
    def test_wrong_provider_or_principal_cannot_receive_mandate(self):
        h=PilotHarness(fixture());accepted(h)
        self.rejected('AUTHORITY_ACTOR_MISMATCH',lambda:h.appoint(R('authority_grant','grant_operator'),T))
    def test_transfer_requires_case_corridor_route_recipient_and_service_act_scope(self):
        for field,value in [('case_ids',['case_other']),('corridor_ids',['corridor_other']),('routes',['EVIDENCE_CURE']),('recipient_refs',[R('party','party_creditor')]),('channels',['INTERNAL']),('obligation_refs',[R('obligation','obligation_other')])]:
            with self.subTest(field=field):
                b=fixture();one(b,'authority_grant','grant_operator')[field]=value
                if field=='obligation_refs':
                    other=deepcopy(one(b,'obligation'));other['record_id']='obligation_other';b['records'].append(other)
                self.rejected('AUTHORITY_SCOPE_DENIED',lambda:PilotHarness(b).preflight(T))
        b=fixture();one(b,'service_request','service_operate')['allowed_actions']=['assessment.deliver']
        self.rejected('SERVICE_SCOPE_DENIED',lambda:PilotHarness(b).preflight(T))
    def test_disposed_source_cannot_enter_permitted_disclosure(self):
        b=fixture();one(b,'evidence_item','ev_contract')['disposition']='DISPOSED'
        self.rejected('SOURCE_UNAVAILABLE',lambda:PilotHarness(b).preflight(T))
    def test_rejection_and_silence_are_not_successful_transfer(self):
        h=PilotHarness(fixture());h.preflight(T);w=h.respond('REJECTED',T)
        self.assertEqual('DECLINED',w['status']);self.assertEqual('ACTIVE',h.latest('service_request','service_operate',T)['status'])
        h=PilotHarness(fixture());w=h.expire_offer('2026-09-11T00:00:00Z')
        self.assertEqual('EXPIRED',w['acceptance_state']);self.assertTrue(w['owner_id'])
    def test_profile_version_change_identifies_affected_work_without_rewriting_history(self):
        h=PilotHarness(fixture());w=h.preflight(T);frozen=deepcopy(w)
        p=h.latest('provider_acceptance_profile','provider_profile_demo',T)
        h.append(p,'2026-09-03T13:00:00Z',required_evidence_ids=p['required_evidence_ids']+['ev_cure'])
        affected=affected_work_orders(h.index,record_ref(p),'2026-09-03T14:00:00Z')
        self.assertEqual([record_ref(w)],affected);self.assertEqual(frozen,h.index.get(record_ref(w)))
        self.rejected('STALE_REFERENCE',lambda:h.respond('ACCEPTED','2026-09-03T14:00:00Z'))
    def test_undeclared_profile_authorship_fails_closed_shape(self):
        b=fixture();one(b,'provider_acceptance_profile')['authorship']='GRE_ASSUMED'
        self.rejected('SCHEMA_INVALID',lambda:validate_bundle(b))
    def test_profile_capacity_and_credential_expiry_are_current_checks(self):
        b=fixture();one(b,'provider_acceptance_profile')['capacity_state']='UNKNOWN'
        self.rejected('PROVIDER_UNAVAILABLE',lambda:PilotHarness(b).preflight(T))
        b=fixture();one(b,'verification_record','verification_provider')['valid_until']='2026-09-03T10:00:00Z'
        self.rejected('EXPIRED_RECORD',lambda:PilotHarness(b).preflight(T))
    def test_restricted_passport_material_is_not_automatically_disclosed(self):
        b=fixture();w=one(b,'work_order');r=R('evidence_item','ev_private_strategy')
        w['disclosure']['included_refs'].append(r);w['disclosure']['withheld_refs']=[]
        w['disclosure']['recipient_mappings'].append({'source_ref':r,'receiving_id':'private_leak'})
        w['disclosure']['packet_digest']=packet_digest(w['disclosure'])
        self.rejected('RESTRICTED_DISCLOSURE',lambda:PilotHarness(b).preflight(T))
    def test_tampered_packet_is_rejected(self):
        b=fixture();one(b,'work_order')['disclosure']['approved_by']='actor_intruder'
        self.rejected('DISCLOSURE_DIGEST_MISMATCH',lambda:validate_bundle(b))
    def test_changed_packet_needs_new_provider_acceptance(self):
        h=PilotHarness(fixture());activation_ready(h);w,*_=h.context(T)
        d=deepcopy(w['disclosure']);d['receiver_namespace']='different_package';d['packet_digest']=packet_digest(d)
        h.append(w,T,disclosure=d)
        self.rejected('ACCEPTED_PACKET_CHANGED',lambda:h.activate(T))
    def test_removing_required_evidence_after_preflight_requires_new_preflight(self):
        h=PilotHarness(fixture());w=h.preflight(T);d=deepcopy(w['disclosure'])
        d['included_refs']=[r for r in d['included_refs'] if r['id']!='ev_invoices']
        d['recipient_mappings']=[m for m in d['recipient_mappings'] if m['source_ref']['id']!='ev_invoices']
        d['packet_digest']=packet_digest(d);h.append(w,T,disclosure=d)
        self.rejected('PREFLIGHT_PACKET_CHANGED',lambda:h.respond('ACCEPTED',T))
    def test_current_correction_invalidates_frozen_passport_for_new_effect(self):
        h=PilotHarness(fixture());old=h.latest('evidence_assertion','assertion_milestone_4',T)
        h.append(old,T)
        self.rejected('STALE_REFERENCE',lambda:h.preflight(T))
    def test_export_has_explicit_receiving_side_mapping(self):
        h=PilotHarness(fixture());self.assertEqual(2,len(h.export(T)))
        b=fixture();w=one(b,'work_order');w['disclosure']['recipient_mappings']=[];w['disclosure']['packet_digest']=packet_digest(w['disclosure'])
        self.rejected('RECEIVER_MAPPING_MISSING',lambda:PilotHarness(b).export(T))
    def test_cutover_fences_new_gre_effects_and_preserves_uncertain_inflight(self):
        h=PilotHarness(fixture());self.assertTrue(h.check_new_gre_effect(T));activation_ready(h)
        h.effects=[{'state':'QUEUED'},{'state':'IN_FLIGHT'},{'state':'RESULT_UNKNOWN'}];h.activate(T)
        self.assertEqual('CANCELLED_BEFORE_DISPATCH',h.effects[0]['state'])
        self.assertTrue(all(x['reconciliation_required'] and x['remediation_owner_id'] for x in h.effects[1:]))
        self.rejected('SERVICE_INACTIVE',lambda:h.check_new_gre_effect(T))
    def test_gre_cannot_dispatch_collection_tactics(self):
        h=PilotHarness(fixture())
        for action in ['settlement.offer','communication.send','professional.execute','funds.instruct']:
            self.rejected('GRE_COLLECTION_SCOPE_DENIED',lambda:h.check_new_gre_effect(T,action))
    def test_conflicting_mandate_blocks_activation(self):
        h=PilotHarness(fixture());activation_ready(h);w,*_=h.context(T)
        h.append(w,T,conflicting_mandate_refs=[R('authority_grant','grant_operator')])
        self.rejected('CONFLICTING_MANDATE',lambda:h.activate(T))
    def test_new_direct_mandate_prohibition_blocks_activation(self):
        h=PilotHarness(fixture());activation_ready(h);g=h.latest('authority_grant','grant_provider',T)
        changed=h.append(g,T,prohibited_actions=g['prohibited_actions']+['settlement.offer'])
        w,*_=h.context(T);h.append(w,T,direct_appointment_ref=record_ref(changed))
        self.rejected('APPOINTMENT_SCOPE_DENIED',lambda:h.activate(T))
    def test_recall_revokes_gre_access_but_external_cessation_and_copies_remain_unknown(self):
        h=PilotHarness(fixture());activation_ready(h);h.activate(T);w=h.recall(T)
        self.assertEqual(('REVOKED','UNKNOWN','REQUESTED','RETAINED_OR_UNKNOWN'),(w['disclosure']['access_state'],w['provider_work_state'],w['cessation_acknowledgment'],w['external_copy_state']))
        self.rejected('DISCLOSURE_ACCESS_ENDED',lambda:h.export(T))
    def test_correction_keeps_lineage_and_respects_recipient_access(self):
        h=PilotHarness(fixture());old=h.latest('evidence_assertion','assertion_milestone_4',T);w,*_=h.context(T)
        correction={'supersedes_ref':record_ref(old),'owner_id':'actor_reviewer','reason':'New contrary source; no erasure','recipient_work_order_refs':[record_ref(w)],'delivery_state':'PENDING'}
        new=h.append(old,T,correction=correction)
        self.assertIn(record_ref(old),[record_ref(r) for r in h.bundle['records']]);self.assertEqual([w['provider_ref']],h.correction_recipients(correction,T))
        validate_bundle(h.bundle);recalled=h.recall(T);correction['recipient_work_order_refs']=[record_ref(recalled)]
        self.rejected('DISCLOSURE_ACCESS_ENDED',lambda:h.correction_recipients(correction,T))
    def test_provider_payment_report_cannot_reduce_trusted_balance(self):
        b=fixture();p=one(b,'payment');self.assertEqual('PROVIDER_REPORT',p['observation_source'])
        h=PilotHarness(b);self.assertEqual('7800000',h.latest('financial_position','position_demo','2026-09-08T00:00:00Z')['asserted_outstanding']['units'])
        p.update(status='RECONCILED',reconciled_at='2026-09-07T12:00:00Z')
        self.rejected('REPORT_NOT_TRUSTED_PAYMENT',lambda:validate_bundle(b))
    def test_custody_and_service_billing_are_invalid_underlying_repayment_destinations(self):
        for role in ['GRE_CUSTODY','GRE_SERVICE_BILLING']:
            b=fixture();one(b,'external_binding','binding_bank')['funds_role']=role
            self.rejected('GRE_CUSTODY_DENIED',lambda:validate_bundle(b))
    def test_exact_money_and_source_tenant_are_enforced(self):
        b=fixture();one(b,'financial_position')['asserted_outstanding']['units']=7800000.0
        self.rejected('SCHEMA_INVALID',lambda:validate_bundle(b))
        b=fixture();one(b,'evidence_item')['tenant_id']='tenant_other'
        self.rejected('TENANT_MISMATCH',lambda:validate_bundle(b))
    def test_observed_zero_cannot_replace_unknown_without_basis(self):
        b=fixture();o=one(b,'outcome_observation');o['debtor_recovery']['status']='OBSERVED'
        self.rejected('SCHEMA_INVALID',lambda:validate_bundle(b))
        b=fixture();one(b,'outcome_observation')['quality_dimensions'][0]['value']='0'
        self.rejected('QUALITY_MISSINGNESS_ERASED',lambda:validate_bundle(b))
    def test_training_and_pooled_benchmarking_need_separate_rights(self):
        p=one(fixture(),'data_policy');check_data_use(p,'service_processing')
        for purpose in ['model_training','pooled_benchmarking']:self.rejected('DATA_USE_DENIED',lambda:check_data_use(p,purpose))
    def test_inactive_private_sponsor_has_no_participant_context(self):
        b=load_json(HERE/'worked-private-inactive.json');c=one(b,'case');p=c['inactive_private_context']
        self.assertEqual([],permitted_private_view(c,p['sponsor_id']))
        self.assertEqual(p['requester_private_refs'],permitted_private_view(c,p['requester_id']))
        self.assertEqual([],permitted_private_view(c,p['respondent_id']))
        self.assertTrue(p['no_further_contact']);self.assertEqual('DECLINED',p['participation'])
    def test_migration_rejects_unversioned_old_bundle_and_unknown_fields(self):
        b=fixture();b['contract_version']='0.1.0';self.rejected('SCHEMA_INVALID',lambda:validate_bundle(b))
        b=fixture();one(b,'case')['network_unlocked']=True;self.rejected('SCHEMA_INVALID',lambda:validate_bundle(b))

if __name__=='__main__':unittest.main()
