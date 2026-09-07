# Immutable 0.1.0 contract audit and bounded 0.2.0 migration crosswalk

Audit inputs: the unchanged `reference/recovery-contracts.zip` schema, validator, tests, fixture and requirements; pre-reconciliation document 05. These dispositions implement the September 7 owner decision: Foundation + Trade is the sole Pilot. They do not enable Private or Consumer operation or widen any action authority.

ZIP SHA-256: `14d24f856ade2c0b508a208d32a98c14a37723f4708b43c82f58213396bfaf72`.

The archive has exactly **29 record types**, **23 operation names**, **89 fixture records**, **4 fixture checkpoints**, and **51 `test_*` methods**. The schema describes all 23 admissions; the in-memory reference implements only `action.commit` for one `settlement.offer` / `A3` / `APPROVAL_REQUIRED` / single-payment profile. Shape availability never establishes a callable handler, authority, route release, provider eligibility, or production readiness.

## Migration policy

Retain all 29 legacy record types and all 23 legacy operation names in a separately versioned 0.2.0 contract with bounded, explicit extensions. Add `provider_acceptance_profile` as the only new record type introduced, producing 30 record types; it must describe reviewed provider scope and eligibility rather than itself grant execution authority. Retain the original ZIP and its tests unchanged and runnable separately. Change version constants and identifiers deliberately in the new contract, rather than reinterpreting 0.1.0 snapshots. Foundation supplies shared integrity/control contracts; Trade Pilot consumes only the reviewed service/action/route subset. Private and Consumer remain inactive throughout; preserving their possible representational capacity grants no admission or execution permission.

Legacy service-kind migration is semantic and reviewed:

| Legacy service kind | 0.2.0 disposition | Constraint |
|---|---|---|
| `ASSESSMENT` | `ASSESS` | Preserve assessment scope, deliverables and limitations; it does not authorize later execution. |
| `HANDOFF` | `TRANSFER` | Preserve actual accepted transfer, remaining duties and accountable owner; an offered work order does not establish transfer. |
| `MONITOR` | Reviewed split to `OBSERVE` or `CONTROL` | Select according to actual contracted monitoring/control scope and existing authority; do not infer broader control from the label. |
| `OPERATE` | Manual review required | Decompose only against documented scope and authority; never automatically map to `RESOLVE`. |

The retained `service_request.kind` is a compatibility axis; the new required `service_request.service_mode` records the reviewed mode. The new service-mode enum is distinct from execution mode even when both use `OBSERVE`. Apply the interpretation when preparing new `service_request.service_mode` values. The legacy `service_request.kind`, `PlacementCommand.payload.requested_service`, and `ServiceRequestCommand.payload.kind` shapes remain retained compatibility inputs; their broad `OPERATE` value has no implicit live mapping. The new reference helpers do not expose these commands as handlers. Legacy stored history retains its original version and meaning; unresolved conversion remains explicitly blocked for new operative use.

## All 29 legacy record types

“Reference depth” describes actual 0.1.0 Python behavior in addition to generic closed-schema, tenant, typed-reference, timestamp and version checks. It is not a claim that the 0.2.0 validator implements a domain handler.

| # | Exact record type | 0.2.0 Foundation / Trade Pilot disposition | Actual 0.1.0 reference depth |
|---|---|---|---|
| 1 | `party` | Retain shared identity and scoped verification meaning; Trade roles do not grant rights, mandate or access. | Shape/reference checks; principal and target equality used by commit. No identity-service implementation. |
| 2 | `data_policy` | Retain purpose, disclosure, retention and disposition controls; preserve private-context restrictions even with Private development inactive. | Policy reference checks; commit checks retained shared evidence, processing/disclosure, retention/legal hold. No storage enforcement. |
| 3 | `case` | Retain independent state vector, service links and owned remaining duties; add only explicit bounded profile/service context. | Closed-case invariants, event-linked transition helper, live current-case/hold checks in commit. No case handler. |
| 4 | `service_request` | Retain bounded principal/scope/window/caps/deliverables; use the reviewed service-kind mapping above. | Fulfillment/transfer/closure checks and current active service/scope/window/cap checks in commit. No request or fulfillment handler. |
| 5 | `obligation` | Retain underlying duty, invoice/charge/credit lines and linked-case identity. Trade is the active claim purpose. | Financial-position line totals/currency and cross-case allocations; commit reserves obligations. No obligation admission handler. |
| 6 | `rights_interest` | Retain asserted/verified/disputed/ended interests; new profile never converts an assertion into ownership or servicing rights. | Shape/references/time only; no dedicated rights-verification handler or complete rights waterfall check. |
| 7 | `claim_passport` | Retain versioned assertions, evidence, gaps and scope-specific readiness; reviews remain separate from source intake. | Current passport must be a bound material dependency at commit; no assessment generator. |
| 8 | `evidence_item` | Retain original/derived/attested/observed/AI distinctions, untrusted-content flag, custody and disposition. | Generic provenance references; commit checks current retained/disclosable evidence. No external authenticity check. |
| 9 | `evidence_assertion` | Retain supporting/contrary evidence and source-class distinction; missing terms stay unknown. | Shape/references/time only; no inference or finding handler. |
| 10 | `verification_record` | Retain who/method/scope/evidence/limitations; only trusted reviewed admission can publish verification. | Result consulted for mandates, provider eligibility and capability assurance; no verifier implementation. |
| 11 | `authority_grant` | Retain action/mode/party/route/corridor/channel/budget/term bounds and revocation. Provider acceptance/profile cannot mint a grant. | Extensive current grant checks in commit; acceptance and selected case-transition authority checks. No grant issuance/revocation handler. |
| 12 | `policy_snapshot` | Retain exact material-input and action/case binding, expiry and unresolved issues; Foundation/Trade checks may only narrow eligibility. | Commit checks current ALLOW, no conditions/issues, scope, expiry/material versions and corridor. No full policy compiler. |
| 13 | `capability` | Retain explicit release status, owner, evidence, limits and reassessment. Trade release requires the existing operational gates; Private/Consumer inactive. | Commit checks enabled status, action/mode/route/corridor, current assurance and reassessment. No release manager. |
| 14 | `corridor_pack` | Generalize purpose vocabulary to preserve inactive Consumer/Private/mixed/unknown representations; add directional release profile and source lifecycle. Trade-only current gates still reject all other families. | Schema fixes claim purpose to `B2B_COMMERCIAL`; commit checks enabled matching corridor, applicability and review due. No jurisdiction compiler. |
| 15 | `strategy_plan` | Retain authorized primary/fallback/parallel routes within actual service scope; unsupported routes remain inactive. | Shape/references/time only; no strategy selection or execution handler. |
| 16 | `decision_episode` | Retain contemporaneous information, alternatives, eligibility, uncertainty and selection basis. | Cutoff, selected-eligible alternative, ranges and non-invented propensity/probability checks. No causal estimator. |
| 17 | `action_intent` | Retain immutable exact binding, digest, supersession, status and stable operation identity; profile extension cannot bypass commit. | Immutable binding/digest checks; single-profile commit, stale-reference rejection and duplicate prevention. |
| 18 | `approval` | Retain exact action/version/digest/principal/expiry and trusted approver scope; unchanged execution-mode semantics. | Commit validates approval binding, current approval and approver grant. No approval-recording handler. |
| 19 | `execution_receipt` | Retain each attempt and independently observed/unknown result; provider acceptance is not delivery or success. | Action digest, success evidence/time, unknown-result remediation owner; retry-disposition helper. No adapter dispatch/reconciliation. |
| 20 | `work_order` | Retain bounded offer, acceptance conditions, eligibility, cost, evidence access and return duties; new acceptance profile may inform eligibility but cannot replace work-order acceptance. | Accepted/active/completed orders require response, resolved conditions and scoped eligibility verification. No provider handler. |
| 21 | `waiting_requirement` | Retain owner, recipient, delivery, responsibility acceptance, due basis, partial satisfaction, expiry and escalation. | Satisfied response/outstanding checks; legal deadline basis checks. No timer or escalation runtime. |
| 22 | `agreement` | Retain immutable exact terms and independent acceptance; preserve release/fulfillment distinctions and unsupported-instrument gating. | Terms digest/immutability, party and authority acceptance, conditional release checks; commit only bounded single-payment terms. |
| 23 | `payment` | Retain report/receipt/reconciliation/reversal/refund distinctions and source class; no custody or funds instruction implied. | External transaction deduplication; reconciled debtor-payment and confirmed reversal checks through allocations/positions. No bank/PSP adapter. |
| 24 | `allocation` | Retain explicit apply/reverse direction and obligation/payment linkage; reconcile across all linked cases. | Cross-case payment limits, original reversal basis, aggregate reversal limits, currency/temporal checks. No transactional ledger. |
| 25 | `financial_position` | Retain exact currency/minor-unit position and separate release/receipts; accounting or service closeout cannot zero a claim. | Full supported single-currency bookkeeping equation, release trigger and allocations. No general legal-validity or FX engine. |
| 26 | `outcome_observation` | Retain scope/horizon/source and observed/unknown/censored amounts; service result is not cash recovery. | Window, assessment-not-recovery, financial-position observation match and attribution-limit checks. No causal proof. |
| 27 | `event` | Retain versioned subject/source/cause/reason/payload integrity and retention meaning. | Payload-reference digest, direct self-causation guard, event-linked case transition validation. No authenticated producer/audit store. |
| 28 | `model_execution` | Retain model/workflow identity, actual retained input/output refs, cost and reviewer disposition; never elevate AI output to reviewed facts. | Shape/references/time only; no model runner or full evaluation/retention engine. |
| 29 | `external_binding` | Retain verified recipient/destination/endpoint identity, source and recheck; inactive binding cannot authorize a send or movement of funds. | Commit checks current active target/party/recheck; payment destination system contributes to deduplication. No endpoint verification adapter. |

## All 23 legacy operation names

Every row has a typed closed admission schema. Retain the names in 0.2.0 with versioned payload changes only when specified. “No handler” means the original package does not implement the operation; validating its payload is not accepting its proposed domain effect. The 0.2.0 contract validator must not claim otherwise.

| # | Exact operation | 0.2.0 Foundation / Trade Pilot disposition | Actual reference-handler depth |
|---|---|---|---|
| 1 | `case.place` | Retain proposed scoped intake; restrict active profile/purpose to reviewed Trade scope, with explicit service-kind migration. | Typed `PlacementCommand`; no handler. |
| 2 | `service.request` | Retain bounded service request; migrate service kind by reviewed mapping, preserving authority/window/caps. | Typed `ServiceRequestCommand`; positive/negative admission tests; no activation handler. |
| 3 | `case.import_handover` | Retain reviewed current-state import with provenance and permission; no replay or inherited trusted authority/cash. | Typed `HandoverCommand`; no import handler. |
| 4 | `evidence.attach` | Retain untrusted source intake and provenance; no automatic verification. | Typed `EvidenceAttachCommand`; no attachment handler. |
| 5 | `verification.record` | Retain scoped reviewed findings; trusted reviewer resolution remains independent. | Typed `VerificationCommand`; stored verification results used elsewhere; no recording handler. |
| 6 | `assessment.request` | Retain supported-route assessment within `ASSESS` scope; output is bounded analysis. | Typed `AssessmentCommand`; no assessment handler. |
| 7 | `strategy.propose` | Retain proposed route coordination and limitations; route proposal does not authorize execution. | Typed `StrategyCommand`; no proposal handler. |
| 8 | `authority.request` | Retain instrument-backed request with unchanged mode meaning; cannot create a grant or activate inactive profiles. | Typed `AuthorityRequestCommand`; no request/issuance handler. |
| 9 | `authority.revoke` | Retain revocation control and reason/current references; live effects must be rechecked before commitment. | Typed `AuthorityRevokeCommand`; commit tests mutated revoked state, not a revoke handler. |
| 10 | `approval.record` | Retain exact proposed binding decision and scope; never treat UI or transport acknowledgement as approval. | Typed `ApprovalCommand`; approval checks in commit, no recording handler. |
| 11 | `action.prepare` | Retain proposed immutable binding for supported action/profile; no external effect from preparation. | Typed `PrepareActionCommand`, reusing `ActionBinding`; no prepare handler. |
| 12 | `action.commit` | Retain the exact live authorization boundary; any new Trade profile needs explicit implementation/tests beyond the legacy profile. | Only implemented command: in-memory single approved A3 settlement-offer profile; reserves and returns `SCHEDULED`, with `external_effect_committed: false`. |
| 13 | `action.cancel` | Retain cancellation request semantics before/after dispatch and uncertain reservation ownership. | Typed member of `ActionCommand`; commit method rejects this operation; no cancellation handler. |
| 14 | `action.reconcile` | Retain reconciliation of the existing durable operation before any safe retry. | Typed member of `ActionCommand`; retry-disposition helper only; no reconcile handler. |
| 15 | `work_order.offer` | Retain scoped provider offer; evaluate reviewed acceptance profile plus case-specific eligibility/authority. | Typed `WorkOrderOfferCommand`; no provider offer handler. |
| 16 | `work_order.respond` | Retain actual accepted/conditional/declined response and conditions; profile match is not response. | Typed `WorkOrderResponseCommand`; stored work-order checks only; no response handler. |
| 17 | `agreement.propose` | Retain immutable exact-term proposal for reviewed supported instrument only. | Typed `TermsProposeCommand`; stored terms/limited commit checks, no proposal handler. |
| 18 | `agreement.observe_acceptance` | Retain exact-term acceptance evidence and independent authority review for each party. | Typed `AcceptanceObserveCommand`; stored acceptance checks, no observation handler. |
| 19 | `payment.observe` | Retain source-classified reported/observed transaction; no reconciled cash change on report. | Typed `PaymentObserveCommand`; financial checks only, no intake handler. |
| 20 | `payment.reconcile` | Retain trusted-source reconciliation and allocation boundary, exact money and reversal semantics. | Typed `PaymentReconcileCommand`; offline financial invariants, no reconciliation handler. |
| 21 | `service.fulfill` | Retain contracted deliverable/conditions and assigned remaining duties; no automatic claim recovery or case closure. | Typed `FulfillServiceCommand`; stored service/closeout checks, no handler. |
| 22 | `case.propose_close` | Retain proposed disposition with evidence/remaining duties; scope-complete unpaid closure remains valid. | Typed `CloseCaseCommand`; stored closure and transition checks, no close handler. |
| 23 | `outcome.observe` | Retain scoped independently sourced outcomes and unknown/censored amounts; no invented zero or lift. | Typed `OutcomeObserveCommand`; stored observation checks, no handler. |

## Every execution-mode declaration and use

There are **four concrete enum declarations**, all containing exactly `OBSERVE`, `PREPARE`, `APPROVAL_REQUIRED`, `DELEGATED`:

| Schema path | Migration |
|---|---|
| `$defs.ActionBinding.properties.execution_mode` | Preserve unchanged; consumed by both `action_intent.binding` and `PrepareActionCommand.payload.proposed_binding`. |
| `$defs.authority_grant.properties.execution_modes.items` | Preserve unchanged; permitted mode list is bounded by the actual verified grant. |
| `$defs.capability.properties.allowed_modes.items` | Preserve unchanged; capability availability does not grant case authority. |
| `$defs.AuthorityRequestCommand.properties.payload.properties.requested_modes.items` | Preserve unchanged; requested mode does not become granted mode. |

| Exact legacy mode | 0.2.0 meaning and disposition |
|---|---|
| `OBSERVE` | Preserve observation scope; it grants no new external-action authority. Distinguish from the `OBSERVE` service label. |
| `PREPARE` | Preserve preparation scope; preparing an action or draft grants no authority to dispatch it. |
| `APPROVAL_REQUIRED` | Preserve exact approval requirement and live rechecks; approval binds the exact action/version/digest/principal and expiry. |
| `DELEGATED` | Preserve bounded delegated authority semantics only. Do not infer delegation from `OPERATE`, an enabled profile, provider acceptance or a role. The legacy commit harness explicitly rejects this mode. |

The validator checks the single profile at `CommitHarness.commit`, then membership in grant execution modes and capability allowed modes. Neither the `PREAUTHORIZED` action status nor the `AUTHORIZED` case/strategy status overrides execution mode, exact approval, mandate, holds or current-state checks.

## Every case-state enum and its duplicated uses

Retain all existing state values and meanings in the new contract; inactive route representations can be preserved for history/import while operational admission/transition gates reject unsupported use. No enum value or migration label grants operational authority. New service context must not replace the independent state vector.

| Field | Exact 0.1.0 values / migration |
|---|---|
| `CaseState.lifecycle_stage` | `PLACEMENT`, `CONSTRUCTION`, `ASSESSMENT`, `DECISION`, `EXECUTION`, `ESCALATION`, `RESOLUTION`, `CLOSURE`, `CLOSED`; retain. `ASSESSMENT` lifecycle is not renamed merely because service kind becomes `ASSESS`. |
| `CaseState.stage_state` | `ACTIVE`, `AGREEMENT_PENDING`, `APPROVAL_PENDING`, `ASSEMBLING`, `ASSESSED`, `AUTHORIZED`, `CLOSURE_REVIEW`, `CURE_REQUIRED`, `DRAFT`, `ENFORCEMENT_ACTIVE`, `EXHAUSTED`, `FINAL`, `HANDOFF_PENDING`, `INSOLVENCY_ACTIVE`, `IN_REVIEW`, `OUTCOME_PENDING`, `PAUSED`, `PAYMENT_PENDING`, `PLACED`, `PROCEEDING_ACTIVE`, `READY`, `RECONCILING`, `REVIEW_READY`, `ROUTE_PROPOSED`, `SUBMITTED`, `VALIDATING`; retain exact stage pairing below. `HANDOFF_PENDING` is not a service-kind alias. |
| `CaseState.readiness_state` and `claim_passport.readiness` | `UNCHECKED`, `INSUFFICIENT`, `CURE_IN_PROGRESS`, `REVIEW_READY`, `VERIFIED_FOR_SCOPE`, `DEGRADED`; retain both uses and scope-specific meaning. |
| `CaseState.authority_state` | `NONE`, `PENDING`, `LIMITED`, `ACTIVE`, `EXPIRED`, `REVOKED`; retain as state summary, never as substitute for verified action-specific grant. |
| `CaseState.engagement_state` | `NOT_STARTED`, `READY`, `ACTIVE`, `PAUSED`, `UNREACHABLE`, `EXHAUSTED`; retain separately from service and provider acceptance. |
| `CaseState.dispute_state` | `NONE`, `ASSERTED`, `TRIAGE`, `EVIDENCE_PENDING`, `PARTIALLY_RESOLVED`, `RESOLVED`, `DEADLOCKED`; retain. |
| `CaseState.legal_state` | `NOT_REFERRED`, `COUNSEL_REVIEW`, `PRE_ACTION`, `FILED`, `JUDGMENT`, `ENFORCEMENT`, `INSOLVENCY`, `COMPLETE`; retain representation, while unsupported specialist execution remains gated. |
| `CaseState.payment_state` | `NONE`, `PROMISED`, `PLAN_ACTIVE`, `PARTIALLY_PAID`, `REPORTED_PAID`, `RECONCILED_PAID`, `FAILED`, `REVERSED`; retain distinctions; unsupported installment operation is not enabled by `PLAN_ACTIVE`. |
| `CaseState.closure_state` | `OPEN`, `RESOLVED_FULL`, `RESOLVED_PARTIAL`, `UNRECOVERED`, `WITHDRAWN`, `INELIGIBLE`, `DUPLICATE`, `TRANSFERRED`, `SERVICE_SCOPE_COMPLETE`; retain. |
| `CloseCaseCommand.payload.proposed_disposition` | Same closure values except `OPEN`; retain admission subset and proposed-only meaning. |
| `CompletionDimension.status` | `NOT_APPLICABLE`, `PENDING`, `SATISFIED`, `EXCEPTED`, `REOPENED`; retain for all six `Completion` dimensions: `financial`, `commercial`, `legal`, `export_administrative`, `operational`, `retention`. |
| `Hold.status` | `ACTIVE`, `RELEASED`; retain authorized release and scoped blocked actions/parties/routes. |
| `Hold.code` | `AUTHORITY_HOLD`, `IDENTITY_HOLD`, `EVIDENCE_HOLD`, `COMPLIANCE_HOLD`, `SANCTIONS_HOLD`, `BANKRUPTCY_STAY_HOLD`, `CONFLICT_HOLD`, `SECURITY_HOLD`, `PAYMENT_RECONCILIATION_HOLD`, `LEGAL_REVIEW_HOLD`; retain protective representation even when related action routes are inactive. |

All `CaseState` fields, `holds` and `completion` are required; `case.state` references this closed shared shape.

| Lifecycle stage | Only permitted `stage_state` values (the schema's nine conditional branches) |
|---|---|
| `PLACEMENT` | `DRAFT`, `SUBMITTED`, `VALIDATING` |
| `CONSTRUCTION` | `ASSEMBLING`, `CURE_REQUIRED`, `RECONCILING`, `REVIEW_READY` |
| `ASSESSMENT` | `IN_REVIEW`, `ASSESSED` |
| `DECISION` | `ROUTE_PROPOSED`, `APPROVAL_PENDING`, `AUTHORIZED` |
| `EXECUTION` | `READY`, `ACTIVE`, `PAUSED`, `EXHAUSTED` |
| `ESCALATION` | `HANDOFF_PENDING`, `PLACED`, `PROCEEDING_ACTIVE`, `ENFORCEMENT_ACTIVE`, `INSOLVENCY_ACTIVE` |
| `RESOLUTION` | `AGREEMENT_PENDING`, `PAYMENT_PENDING`, `RECONCILING` |
| `CLOSURE` | `CLOSURE_REVIEW`, `OUTCOME_PENDING` |
| `CLOSED` | `FINAL` |

The reference transition graph (same-stage updates also permitted with guards) is: `PLACEMENT` → `CONSTRUCTION|ASSESSMENT|CLOSURE`; `CONSTRUCTION` → `ASSESSMENT|CLOSURE`; `ASSESSMENT` → `CONSTRUCTION|DECISION|CLOSURE`; `DECISION` → `ASSESSMENT|EXECUTION|ESCALATION|CLOSURE`; `EXECUTION` → `ASSESSMENT|ESCALATION|RESOLUTION|CLOSURE`; `ESCALATION` → `ASSESSMENT|EXECUTION|RESOLUTION|CLOSURE`; `RESOLUTION` → `ASSESSMENT|EXECUTION|CLOSURE`; `CLOSURE` → `ASSESSMENT|RESOLUTION|CLOSED`; `CLOSED` → `ASSESSMENT|PLACEMENT`. The helper permits an explicit `late_entry_verified` override of the graph, not automatic historical replay; production must establish that trusted review independently. It requires authority when leaving `CLOSED` or entering `EXECUTION`, `ESCALATION`, or `CLOSED`. This does not implement all operating preconditions or all state-dimension transition handlers.

## Other state/status/result enums and mirrored admission/output uses

All following values retain their 0.1.0 meaning. Their retention is shape/history compatibility, not a release of unsupported action capabilities.

| Field(s) | Exact values |
|---|---|
| `party.identity_status` | `ASSERTED`, `VERIFIED_FOR_SCOPE`, `DISPUTED` |
| `data_policy.disposition` | `ACTIVE`, `RESTRICTED`, `DISPOSED` |
| `service_request.status` | `REQUESTED`, `VALIDATING`, `ACTIVE`, `WAITING`, `FULFILLED`, `PARTIALLY_FULFILLED`, `WITHDRAWN`, `TRANSFERRED`, `FAILED` |
| `outcome_observation.service_result`; `Checkpoint.expected_service_result` | `ACTIVE`, `FULFILLED`, `PARTIALLY_FULFILLED`, `WITHDRAWN`, `TRANSFERRED`, `FAILED` |
| `rights_interest.status` | `ASSERTED`, `VERIFIED_FOR_SCOPE`, `DISPUTED`, `ENDED` |
| `evidence_item.authenticity_status` | `NOT_ASSESSED`, `VERIFIED_FOR_SCOPE`, `CONTESTED`, `UNVERIFIABLE` |
| `evidence_item.disposition`; `event.retention_disposition` | `RETAINED`, `REDACTED`, `DISPOSED` |
| `evidence_assertion.status` | `UNKNOWN`, `ABSENT`, `NOT_APPLICABLE`, `ASSERTED`, `SUPPORTED`, `CONTRADICTED`, `VERIFIED_FOR_SCOPE` |
| `verification_record.result`; `VerificationCommand.payload.result` | `VERIFIED_FOR_SCOPE`, `NOT_VERIFIED`, `CONTRADICTED`, `INCONCLUSIVE` |
| `authority_grant.status` | `PENDING`, `ACTIVE`, `LIMITED`, `EXPIRED`, `REVOKED` |
| `policy_snapshot.decision` | `ALLOW`, `ALLOW_WITH_CONDITIONS`, `DENY`, `REVIEW_REQUIRED` |
| `capability.status`; `corridor_pack.status` | `DESIGNED`, `SHADOW_TESTED`, `PILOT_ENABLED`, `COMMERCIALLY_SUPPORTED`, `SUSPENDED`, `RETIRED` |
| `strategy_plan.status` | `PROPOSED`, `APPROVAL_PENDING`, `AUTHORIZED`, `ACTIVE`, `EXHAUSTED`, `SUPERSEDED` |
| `decision_episode.alternatives[].probability_status` | `CALIBRATED`, `SCENARIO_ASSUMPTION`, `ABSTAINED` |
| `decision_episode.selection_rule` | `HUMAN_JUDGMENT`, `DETERMINISTIC_POLICY`, `STOCHASTIC_POLICY`, `ABSTAINED` |
| `action_intent.status` | `PROPOSED`, `VALIDATED`, `APPROVAL_PENDING`, `PREAUTHORIZED`, `AUTHORIZED`, `SCHEDULED`, `DISPATCHED`, `CANCELLED`, `EXPIRED` |
| `approval.decision`; `ApprovalCommand.payload.decision` | `APPROVED`, `REJECTED`, `REVOKED` |
| `execution_receipt.result` | `ACKNOWLEDGED`, `SUCCEEDED`, `FAILED`, `RESULT_UNKNOWN`, `PARTIALLY_COMPLETED` |
| `work_order.status` | `DRAFT`, `OFFERED`, `ACCEPTED_WITH_CONDITIONS`, `ACCEPTED`, `ACTIVE`, `RETURN_PENDING`, `RETURNED`, `DECLINED`, `CANCELLED`, `COMPLETED` |
| `WorkOrderResponseCommand.payload.response` | `ACCEPTED`, `ACCEPTED_WITH_CONDITIONS`, `DECLINED` |
| `waiting_requirement.status` | `OPEN`, `PARTIALLY_SATISFIED`, `SATISFIED`, `EXPIRED`, `CANCELLED`, `SUPERSEDED` |
| `waiting_requirement.delivery_status` | `NOT_SENT`, `SENT`, `DELIVERED`, `ACKNOWLEDGED`, `FAILED`, `UNKNOWN` |
| `waiting_requirement.acceptance_status` | `NOT_REQUESTED`, `PENDING`, `ACCEPTED`, `DECLINED` |
| `waiting_requirement.expiry_effect` | `REVIEW_AND_REASSIGN`, `BLOCK_STALE_COMMIT`, `CLOSE_SCOPED_MONITORING` |
| `agreement.status` | `DRAFT`, `OFFERED`, `COUNTERED`, `ACCEPTED`, `EXPIRED`, `WITHDRAWN`, `PERFORMING`, `FULFILLED`, `DEFAULTED`, `DISPUTED` |
| `payment.status` | `REPORTED`, `RECEIVED`, `RECONCILED`, `FAILED`, `REVERSED`, `REFUNDED` |
| `ObservationAmount.status` | `OBSERVED`, `PENDING`, `UNKNOWN`, `RIGHT_CENSORED`, `NOT_APPLICABLE`; its conditional `OBSERVED` branch requires value/source/horizon semantics. |
| `outcome_observation.reconciliation_status` | `NOT_APPLICABLE`, `PROVISIONAL`, `RECONCILED`, `PARTIAL`, `UNKNOWN` |
| `outcome_observation.resolution_kind` | `ASSESSMENT_DELIVERED`, `PAYMENT`, `SETTLEMENT`, `PLAN`, `DISPUTE_DETERMINATION`, `FORMAL_RESULT`, `INSURANCE`, `TRANSFER`, `WITHDRAWAL`, `INELIGIBLE`, `DUPLICATE`, `KNOWN_UNRECOVERED`, `UNOBSERVED` |
| `model_execution.human_disposition` | `NOT_REVIEWED`, `ACCEPTED`, `EDITED`, `REJECTED`, `IGNORED`, `EXPIRED` |
| `external_binding.status` | `ACTIVE`, `UNVERIFIED`, `REVOKED` |
| `CommandResult.request_status` | `ACCEPTED`, `REJECTED` |
| `CommandResult.task_status` | `QUEUED`, `RUNNING`, `WAITING_FOR_INPUT`, `WAITING_FOR_APPROVAL`, `COMPLETED`, `FAILED`, `CANCELLED` |
| `CommandResult.domain_status` | `PREPARED`, `AUTHORIZED`, `SCHEDULED`, `DISPATCHED`, `ACKNOWLEDGED`, `SUCCEEDED`, `FAILED`, `RESULT_UNKNOWN`, `PARTIALLY_COMPLETED`, `CANCELLED` |

`ObservationAmount` is reused by all five outcome monetary fields: `debtor_recovery`, `other_proceeds`, `creditor_cash_received`, `recovery_cost`, and `remaining_obligation`. Its `OBSERVED` shape needs a non-null Money value and nonempty basis references; other statuses require a null value. An observed zero must have its own source/horizon. The horizon is carried by the parent outcome's window, not by a new state label.

## Runnable legacy commands and actual audit outcome

Extract the ZIP into its own scratch directory; run with Python 3.10+ as document 05 specifies:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python validate_contracts.py
.venv/bin/python -m unittest -q test_contracts
```

The immutable `requirements.txt` pins `jsonschema[format]==4.26.0` and `rfc8785==0.1.4`. `validate_contracts.py` defaults to its sibling `worked-case.json`; an alternate compatible bundle may be supplied as a positional path. It calls JSON Schema Draft 2020-12 metaschema validation and explicitly enables `FormatChecker`. No extra schema CLI argument is exposed, although `validate_bundle(bundle, schema_path=...)` supports an alternate schema programmatically. The in-memory `CommitHarness` loads its own sibling legacy schema directly, so merely supplying a 0.2.0 schema to `validate_bundle` does not migrate that harness.

The completed reconciliation run used Python 3.12.13 in an isolated environment with those exact direct requirements. The unchanged legacy validator passed 89 records/four checkpoints and all 51 legacy tests passed. These results are separate from the v0.2 suite and do not establish runtime enforcement. See README for current v0.2 results.

## Bounded-extension pitfalls to resolve explicitly

1. **Closed versioned shapes.** Legacy `$id` is `urn:gre:contracts:0.1.0`; bundle `contract_version` and record/command `schema_version` are constants. Optional additions and enum additions can break old consumers. Build a distinct 0.2.0 artifact and explicit conversion path, preserving original ZIP/hash and history; do not edit old fixture versions in place.
2. **Action identity and digest.** `ActionBinding` is closed, includes execution mode, and requires a present `terms_ref` and `terms_digest`; both may be null for applicable non-terms actions. Adding profile/provider context to a binding changes its digest and requires a new exact proposal/binding and approval. The legacy commit profile itself requires actual agreement terms. Do not globally string-replace service labels inside lifecycle/action/terms states.
3. **No inferred authority.** Service, profile, capability, route, provider eligibility/acceptance, caller identity, case authority summary, and actual action mandate remain separate. Adding `provider_acceptance_profile` must not promote the work order to accepted/active, mint a grant, satisfy approval, release holds, change execution mode or turn an unsupported route into an enabled route.
4. **No silent `OPERATE` conversion.** `ASSESSMENT→ASSESS` and `HANDOFF→TRANSFER` are constrained semantic mappings. `MONITOR` requires reviewed OBSERVE/CONTROL selection; `OPERATE` requires manual bounded decomposition. Unresolved migration cannot execute through a default to RESOLVE or DELEGATED.
5. **Schema reach versus runtime reach.** Adding/reusing action enums does not implement handlers. `action.cancel` and `action.reconcile` are shaped but explicitly rejected by `CommitHarness.commit`; the retry helper is not reconciliation. v0.2 must retain that explicit boundary or independently implement and test a newly stated profile.
6. **Observed state versus authority.** Retaining legal, escalation, installment, transfer, insurance and rights representations allows truthful history without enabling those operations. Inactive Private/Consumer purpose/profile must be rejected at operative admission/commit, including nested proposed binding/context, and not silently narrowed into Trade.
7. **Negative controls survive migration.** Preserve failed/unknown dispatch reconciliation, duplicate request and fresh-key action deduplication, shared obligation reservation, revoked/stale mandates, invalid approvals/digests, private-evidence denial, unresolved provider conditions, reported-versus-reconciled payments, cash/release distinction, nonzero unpaid scope closeout, and unknown-versus-zero outcomes.
8. **Reference limits are material.** The package is in-memory and single-profile. It does not demonstrate durable outbox/locking, authenticated identity, true signatures/source validity, provider dispatch, production access isolation, actual legal/corridor applicability, concurrent workers, or general rights/financial instruments. New schema acceptance must not imply these controls now exist.
