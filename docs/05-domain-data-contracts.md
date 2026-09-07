# GRE — Domain and data contracts

**Updated:** September 7, 2026

**Current reference contract:** 0.2.0 — Foundation plus Trade Pilot

**Status:** Executable offline reference; no application handlers, deployed controls, provider participation or live release is established.

**Scope authority:** The latest owner decision selects Foundation plus **GRE Trade & Receivables** as the sole Pilot. The earlier directive's parallel Private beta is superseded.

**Companions:** [Operating model](03-operating-model.md), [Workflows](04-workflow-interaction-specification.md), [Architecture](08-stack-and-environment-decision.md), [Pilot release and assurance](13-pilot-release-and-assurance.md).

## 1. Authority, version and implementation boundary

The operating model owns domain meaning. This document owns contract semantics and consistency boundaries. The [v0.2 schema](../reference/v0.2/recovery-contracts.schema.json) owns its declared field names, required/nullable fields, enums and closed shapes. Resolve conflicts explicitly across those artifacts. A broad enum is representational capacity; it is never released behavior.

The [source-readable reference](../reference/v0.2/README.md) retains the 29 existing record definitions and 23 typed operation admissions under an explicit 0.2.0 contract, with bounded extensions. It introduces one record, `provider_acceptance_profile`. This is neither 30 services nor a complete backend. The modular application will implement only the shared operations used by the accepted Pilot slices.

The immutable [v0.1 ZIP](../reference/recovery-contracts.zip) remains historical and independently runnable. Its approved settlement-offer commit harness is **not** the current Pilot executor. The v0.2 `foundation_checks.py` retains its schema, reference, history, financial and selected transition invariants, while omitting that settlement dispatcher. The new `PilotHarness` demonstrates a narrow synthetic provider-review/acceptance/appointment/activation sequence. It exposes no HTTP endpoints, database migrations, external effects or production authorization API.

The [complete migration crosswalk](../reference/v0.2/migration.md) maps **all 29 legacy record types, all 23 operations, every execution-mode declaration, and the retained case/state aliases**. Closed-version consumers must negotiate supported versions. A legacy file cannot become v0.2 merely by changing its version string. The new fixtures are deliberately reauthored synthetic examples, not a production data migration or proof that all historical records can be converted automatically.

## 2. Shared identity, source ownership and time

Each record retains `record_type`, `record_id`, `record_version`, `schema_version`, `tenant_id`, `created_at`, `recorded_at`, `valid_from`, `valid_until` and `data_policy_ref`. A typed material reference remains `{"type":"claim_passport","id":"passport_demo","version":2}` and resolves within its negotiated contract and tenant. An opaque ID conveys no permission.

Material snapshots are immutable. Corrections append another version or a compensating record. The server owns recorded time; imported source occurrence time cannot backdate what GRE knew. Valid time and recorded time remain separate. Decisions use the information available at their cutoff; later facts cannot be inserted into earlier evaluation. A new effect must additionally pass current facts, authority, holds, policy and release checks.

Each fact has one canonical writer. Views and exports compose source references; they do not create another editable balance, authority ledger or success status. A Passport hash proves internal content consistency, not identity, truth, enforceability or permissible disclosure. Evidence, party assertions, contrary evidence, scoped verification and AI inference retain separate meanings. Uploaded documents and provider/model outputs remain untrusted inputs.

Cross-organization transfer requires a permitted receiving-side mapping. In the bounded fixture, `work_order.disclosure.receiver_namespace` and `recipient_mappings[]` bind each included artifact reference to a receiving ID. These are synthetic mapping examples, not shared cross-tenant IDs or access grants. Production needs authenticated recipient scope, import provenance, permissioned reference retrieval and retention-aware handling of unavailable sources.

## 3. Classification, commercial entitlement and release

`case.classification` contains `matter_family`, `profile_id`, `profile_version`, `status`, `purpose`, `claim_type`, claimant/obligated-party type, natural-person involvement, creditor/obligor countries, source references and review owner. `case.commercial_entitlements` is independent. `NETWORK_CONTROL` does not change classification or bypass a family gate.

The represented operational profile is confirmed Trade, business purpose, commercial goods/services, a business claimant and obligor, India creditor → U.S. business obligor. Any natural-person involvement, mixed/unknown purpose, guarantee requiring classification, Consumer/Private indicator or unresolved role goes to review; the harness conservatively blocks the whole proposed transfer. This conservatism is not the final action-specific policy engine. A qualified reviewed fact pattern is required before any broader exception is designed.

`corridor_pack.release_profile` binds family/profile version, permitted service modes, executor pattern, actor IDs, legal-review state, conditions, release evidence and responsible owners. Existing `corridor_pack.status` retains the separate commercial status. `source_lifecycle[]` records source, publication/retrieval/effective dates, current/withdrawn/superseded status and reviewer. Case-specific `policy_snapshot` and `capability` remain separate current evaluations and assurance records.

Activation requires the intersection of supported family/profile, exact directional corridor, service, actor, direct authority, policy, capability and release conditions. Commercial enablement does not establish current legal review. Current review does not establish commercial release. A frozen Passport cannot override a corrected assertion, withdrawn rule, active hold, expired grant or outdated provider requirement.

The reference represents only the countries and classification facts needed for this gate. Full origin/current/contact/processing/payment/forum/enforcement jurisdictions, regulatory role, channel/fee analysis, source hierarchy and change-impact review belong in the dependent corridor and release work. No real legal review or provider eligibility is asserted by a synthetic `COUNSEL_REVIEW_CURRENT` or `PILOT_ENABLED` value.

## 4. Service modes and legacy compatibility

Service mode, execution mode, case lifecycle and commercial edition are separate axes.

| Legacy `service_request.kind` | New `service_request.service_mode` interpretation | Required treatment |
|---|---|---|
| `ASSESSMENT` | `ASSESS` | Preserve deliverable, uncertainty and service window; no subsequent contact authority. |
| `HANDOFF` | `TRANSFER` | Preserve actual acceptance and outstanding duties; transmission alone is insufficient. |
| `MONITOR` | `OBSERVE` or `CONTROL` | Review actual contracted acts and split scopes where needed; do not widen creditor-control rights. |
| `OPERATE` | No automatic mapping | Reassess the original acts and executor; require explicit new scope. Never silently map to `RESOLVE`. |

The retained `kind` also appears in legacy placement/service command payloads. Those payloads remain compatibility admissions; v0.2 provides no transport handler that automatically activates their requested work. New stored service records require `service_mode`. The Pilot gate supports `ASSESS`, `PREPARE`, `TRANSFER`, `CONTROL`, `OBSERVE`. Represented `PREVENT` and `RESOLVE` stay unavailable.

`action_intent.binding.execution_mode` remains exactly `OBSERVE`, `PREPARE`, `APPROVAL_REQUIRED`, `DELEGATED`. The same execution vocabulary is retained in `authority_grant.execution_modes`, `capability.allowed_modes` and authority requests. `PREPARE` is not dispatch permission; `APPROVAL_REQUIRED` still requires exact approval; `DELEGATED` is never inferred from a role, edition, service label or provider response. No general delegated executor is supplied by either reference.

Legacy `case.state.*` dimensions and their stage/substate pairings remain intact. `EXECUTION` can describe an externally performed case stage; it does not designate GRE as collector. Existing `case.state.closure_state = TRANSFERRED` is preserved for historical disposition only and is not the new transfer-service completion field. `SERVICE_SCOPE_COMPLETE` may describe unpaid bounded closeout; it does not establish payment, discharge, waiver or successful collection.

## 5. The six contracts compose canonical records

[Contract composition examples](../reference/v0.2/contract-compositions.json) resolve through six closed schema view definitions. They carry source references and create no additional authoritative records.

| Contract / schema view | Canonical source ownership | Added meaning and limit |
|---|---|---|
| Claim Passport / `ClaimPassportView` | `claim_passport`, case classification, evidence/assertion/verification, obligation/financial/rights references | Existing source-linked snapshot plus profile and permitted disclosure context; no universal verified-debt flag. |
| Provider Acceptance Profile / `ProviderAcceptanceProfileView` | New `provider_acceptance_profile`, provider party/verification, `capability`, per-case `work_order` | Standing provider-authored or explicitly provider-approved requirements; not a placement response, mandate or license. |
| Authority Envelope / `AuthorityEnvelope` | `authority_grant`, `rights_interest`, `approval`, `policy_snapshot`, exact action binding | References actual principal, limits and authority provenance; the closed view cannot introduce an `allowed_actions` field or mint rights. |
| Corridor Pack / `CorridorPackView` | `corridor_pack`, `policy_snapshot`, `capability` | Direction, rule lifecycle, current applicability and release remain separately sourced. |
| Action Receipt / `ActionReceiptView` | `execution_receipt`, `action_intent`, `approval`, `event`, `model_execution` | Attempt/effect provenance and uncertainty; not a competing success ledger or provider conduct certificate. |
| Resolution Quality Scorecard / `ResolutionQualityScorecard` | `outcome_observation`, financial/payment, decision, work-order and event records | Versioned source composition; dimensions preserve denominator, horizon, missingness and attribution limits. No causal lift or provider ranking is computed. |

The standing Provider Acceptance Profile records provider identity, declaration/fee evidence, supported families/corridors/claim classes, required evidence IDs, exclusions, capacity, credentials/review due date, accepted formats, returned event kinds, freshness obligation and owner. The fixture's IDs are synthetic requirements, not a production requirement language. GRE cannot silently rewrite the provider's declaration. A material change creates a new version, identifies affected placements and requires re-preflight/reacceptance as appropriate. Historical results are retained.

## 6. Review, acceptance, direct appointment and activation

`work_order` remains the canonical placement aggregate. These are its new qualified paths:

| Path | Values / meaning |
|---|---|
| `provider_acceptance_profile_ref` | Exact standing profile version for this offer. |
| `preflight_profile_ref`, `preflight_packet_digest`, `preflight_state` | Exact evaluated profile and packet; `NOT_RUN`, `READY`, `DELTA`, `STALE`. `READY` means ready for that review profile. |
| `acceptance_state` | `PENDING`, `CONDITIONAL`, `REJECTED`, `ACCEPTED`, `EXPIRED`; provider commercial response. |
| `validation_delta[]` | Requirement ID, reason, open/satisfied state and supporting sources. |
| `accepted_packet_digest` | Exact reviewed disclosure digest associated with the response; changing the packet requires new acceptance. |
| `direct_appointment_ref` | Creditor-to-provider `authority_grant`, independently verified for the actual scope. |
| `execution_conditions[]`, `independent_validation_ref` | Separately sourced prerequisites and provider's scoped validation. |
| `provider_work_state` | `NOT_STARTED`, `ACTIVE`, `PAUSED`, `CEASED`, `UNKNOWN`; separate from response and GRE service state. |
| `activation_at`, `cutover_at` | Recorded activation/cutover, only after the guards. A timestamp cannot supply missing authority. |
| `offer_expires_at`, `owner_id` | Expiry and accountable owner for response, rejection, silence or exception. |

First disclose only the minimized, independently permitted inputs needed for conflicts, eligibility and review. `work_order.disclosure` binds purpose, recipient, included/withheld/redacted artifacts, data-policy basis, reviewer, expiry, access state, receiving mapping and JCS/SHA-256 packet digest. Review access is not an execution mandate. Privileged, restricted, legally held and trade-secret artifacts conservatively fail the reference disclosure check; a released product needs qualified rules for legitimate exceptions and approved derivative redactions.

The provider may return a delta or rejection without reconstructing the whole file. Conditional acceptance never enables execution. Commercial acceptance can be recorded while conditions remain open; legacy `work_order.status = ACCEPTED` retains its stronger resolved-condition meaning. The helper therefore keeps legacy `status = OFFERED` at early commercial acceptance, progressing to `ACTIVE` only after activation. Legacy response payload `ACCEPTED_WITH_CONDITIONS` maps to new `acceptance_state = CONDITIONAL`; `DECLINED` maps to `REJECTED`. An unverified old `ACCEPTED` value cannot be upgraded into current activation.

The creditor directly appoints the provider. Activation requires exact accepted packet/profile, current mandate, principal/provider/actor and act scope, budget, rights, independent validation, fulfilled conditions, non-conflicting mandates and current gates. The provider executes externally through its own identity and judgment. GRE transports permitted creditor decisions and supplies its contracted preparation, correction and continuity services; it does not select collection tactics or negotiate as collector.

At cutover, fence new effects under the ended GRE service and cancel queued work that remains cancelable. Sent/in-flight/unknown effects retain reconciliation and an owner. Then `service_request.status = TRANSFERRED` records completion of that bounded GRE transfer. It does not change the underlying obligation, agreement, payment, case closure or other services. Separate `CONTROL/OBSERVE` requests and preservation/complaint/support duties keep their own owner, scope and window.

Recall distinguishes `disclosure.access_state = REVOKED`, `cessation_acknowledgment = REQUESTED/CONFIRMED/UNKNOWN`, external work state and `external_copy_state = RETAINED_OR_UNKNOWN`. GRE access revocation cannot remotely erase exported documents, undo an in-flight action or prove the provider ceased work. Replacement activation requires reviewed, non-conflicting authority; a complete second-provider switch transaction is still product/integration work.

## 7. Exact effects, receipts and financial meaning

An action binds exact case/service/principal/executor/target, content/terms, material versions, authority, policy, capability, money, expiry and execution mode. `binding_digest = SHA-256(JCS(binding))`; terms use their own exact digest. Changing material content requires a new proposal and approval, not mutation of an offered action. Actor strings, hashes and approvals in a supplied bundle do not authenticate anyone.

Production prepare/commit must authenticate separately, resolve current versions and permissions, enforce holds and limits, bind exact content and destinations, deduplicate request/action identity, reserve shared commitments and atomically create a durable outbox record. Dispatch and reconciliation remain separate. The v0.2 helper's gate checks and list of queued/in-flight effects demonstrate only expected decisions; they implement no durable outbox, idempotent dispatcher or concurrency controls. The unchanged legacy 51 tests remain separate evidence for the earlier in-memory settlement example.

`execution_receipt.attribution` identifies proposer, principal, reviewer, approver, transmitter, performer and observer, plus source status. `RESULT_UNKNOWN` needs accountable reconciliation. Provider performance is attributed to that provider; GRE transmission is attributed to GRE's actor. Transport acknowledgement, provider acceptance and successful collection are different facts. An uncertain receipt never authorizes blind resend.

Money remains exact nonnegative integer strings in minor units: `{"currency":"USD","exponent":2,"units":"7800000"}`. The supported equation is:

`outstanding = asserted principal + supported charges − valid credits − effective releases − reconciled debtor payments`

This is bookkeeping over supported records, not a legal validity finding. Credits, release, insurance proceeds, debt sale, accounting write-off, payment and reversal stay distinct. Allocation requires reconciled debtor payment and must prevent duplicate/over-allocation across linked cases. A reversal appends compensating allocation; revival of an earlier release needs its actual terms and qualified determination.

`payment.observation_source = PROVIDER_REPORT` must remain `REPORTED`, with no reconciliation timestamp. `INDEPENDENT_FINANCIAL_SOURCE` is a source classification that still requires trusted evidence and matching in a real adapter. A provider's reported payment does not reduce the reconciled balance. `external_binding.funds_role` rejects `GRE_CUSTODY` and `GRE_SERVICE_BILLING` as destinations for repayment of the underlying obligation. GRE's own ordinary service billing is a separate Pilot service-billing workflow, with defined manual invoicing permitted, not a repayment ledger or custody workaround.

Agreements retain exact immutable terms, independent party acceptances, performance, effective release and payment observations. A promise or accepted agreement cannot mark an obligation paid. The new Trade fixture intentionally stops short of an agreement/reconciled-payment execution path; the retained legacy suite separately exercises its bounded settlement, conditional release and reversal semantics.

## 8. Correction, privacy, outcome and future representation

`evidence_assertion.correction` references the superseded assertion, reason, accountable owner, intended work-order recipients and delivery state. The old assertion remains resolvable. The helper checks recipient access and refuses revoked routes; it does not transmit a correction or authorize every new source artifact. Actual correction content needs its own reviewed minimized disclosure, receipt/error handling and recipient retention treatment.

Service processing, tenant evaluation, pooled benchmarking and model training are independent `data_policy` permissions. Permission for service delivery or returned outcomes does not imply training rights. Retention, deletion, legal hold, correction and recipient access are separate controls; immutable history does not mean indefinite retention of personal content. The reference checks selected metadata, not storage deletion or content-level privacy enforcement.

The scorecard's optional `outcome_observation.quality_dimensions[]` preserves net economics, readiness/accuracy, time/effort, treatment/safety, agreement durability and continuity separately. Its parent provides the observation horizon and attribution basis. Unknown/pending/censored values remain null; observed zero requires evidence. Fixture dimensions are explicitly unknown and establish no performance measurement.

Consumer and Private are inactive future examples. The Consumer fixture represents an institutional U.S.-origin/India-resident classification and fails the Trade operational gate. The Private fixture represents a requesting adult, responding adult, declined participation, no-further-contact and private/shared reference separation. `case.inactive_private_context` is deliberately a limited fixture shape; sponsor/payer status grants no participant data. It does not implement invitation admission, duplicate suppression, a shared room, agreement formation, safety support, consumer protections or a released service. Those needs and reopening gates remain in [Future development](07-future-development-and-business-deliverables.md).

## 9. Validation evidence and remaining work

Run the [reference commands](../reference/v0.2/README.md) in an isolated Python environment. The September 7 reconciliation run used Python 3.12.13 with `jsonschema[format]==4.26.0` and `rfc8785==0.1.4`. The immutable legacy validator passed **89 records / four checkpoints** and **51 tests**. The new suite passed **42 tests**, separately from the workflow document's product acceptance scenarios; details are in the reference README.

The new suite exercises a complete synthetic Trade review → accepted placement → direct appointment → conditions → activation/cutover path, together with classification, release, source/policy/authority expiry, conditional/rejected/expired outcomes, changed requirements/packet, safe disclosure/export, exact money, report/custody denial, correction/access, uncertain receipts and inactive profile boundaries. Schema metaschema/format checking is enabled.

This baseline does **not** establish production authentication, authorization, authentic mandates/sources, legal applicability, full rights waterfalls, complete command handlers, durable/idempotent/concurrent effects, provider integration, actual payment reconciliation, malware/prompt-injection defense, deployment isolation, privacy/retention enforcement, incident response, procurement readiness or recovery improvement. Its broad schema support must not be advertised as those controls. [Release assurance](13-pilot-release-and-assurance.md) and the prioritized backlog own the remaining product, operational and expert-review evidence before any activation.
