# Global Recovery Engine — Domain & Data Contracts

**Updated:** September 6, 2026  
**Contract version:** 0.1.0 — first reviewable engineering baseline  
**Purpose:** Canonical field shapes, references, command inputs, state transitions, consistency rules, and conformance boundaries derived from the reviewed operating model and workflows.  
**Status:** Schema and synthetic reference validation. No production API, live recovery service, corridor certification, or MVP selection is established.  
**Companion references:** [Business & Project Overview](01-business-project-overview.md) · [Product Offering & Competitive Strategy](02-product-offering-competitive-strategy.md) · [Operating Model](03-operating-model.md) · [Workflow & Interaction Specification](04-workflow-interaction-specification.md)  
**Machine-readable companion:** [recovery-contracts.zip](../reference/recovery-contracts.zip)

## 1. What this baseline settles

The operating model defines what the business records mean. The workflow specification defines what people and agents experience. This document defines how those meanings are represented, referenced, changed, and checked.

The core decisions are:

1. A **Case**, **Service Request**, **Obligation**, **Action Intent**, and **Outcome Observation** have separate identities and states.
2. A reference to a material record identifies its type, ID, and exact version. An approval also binds the exact proposed action and terms digest.
3. External requests propose or report work. They cannot directly write trusted ownership, verification, authority, cash, or completion state.
4. Human and agent callers use the same typed operations and independently enforced commit rules.
5. Financial, evidence, authority, and observation records retain their different meanings when models, interfaces, connectors, or providers change.

The record catalogue represents the full core model. It is not a requirement to implement every record type, route, screen, or service for the MVP. The next product decision selects one complete supported path through these contracts.

## 2. Deliverables and authority

| Artifact in the companion package | Purpose |
|---|---|
| `recovery-contracts.schema.json` | JSON Schema 2020-12 definitions for 29 record types, shared value types, 23 command operations, results, and the test bundle |
| `worked-case.json` | One fictional case containing 89 versioned records across all 29 record types and four checkpoints |
| `validate_contracts.py` | Schema validation, cross-record checks, financial checks, and a limited in-memory commit reference |
| `test_contracts.py` | Positive and negative contract conformance cases; separate from the workflow specification's 36 acceptance scenarios |
| `requirements.txt` | Pinned direct dependencies used for this reference validation |

The JSON Schema is authoritative for the declared field names, required/nullable fields, enum values, and closed object shapes in version 0.1.0. This document is authoritative for engineering semantics not expressible in JSON Schema. The Operating Model remains authoritative for domain meaning. Resolve a conflict explicitly across the affected references; do not silently choose whichever representation is easiest to implement.

Stored records, commands, and export bundles are different interfaces. A tenant-private test bundle is not a public API request and is never an automatic counterparty disclosure package.

## 3. Identity, ownership, and time

Every stored record carries `record_type`, `record_id`, `record_version`, `schema_version`, `tenant_id`, `created_at`, `recorded_at`, `valid_from`, `valid_until`, and `data_policy_ref`.

| Contract | Rule |
|---|---|
| Record identity | Opaque ID; no encoded amount, customer name, legal conclusion, or permission. The reference implementation permits a bounded lowercase identifier alphabet. |
| Version identity | A positive integer identifies one immutable material snapshot. Corrections create another version or a compensating record; published action bindings and agreement terms require new proposal identities when materially changed. |
| Typed reference | `{"type":"claim_passport","id":"passport_demo","version":2}`. Material decisions and receipts do not use an ambiguous “latest” reference. |
| Tenant | A security and contractual boundary, separate from legal principal, creditor, provider, or actor. A caller-supplied tenant ID must agree with authenticated scope. |
| Actor IDs | Resolve through the trusted identity service. A string naming an operator, reviewer, or agent is not proof of identity, employment, qualification, or authority. |
| Recorded time | When the system knew a record/version. The service assigns it; an imported source cannot backdate the system's knowledge. |
| Valid time | When a fact, right, or rule applied. A late correction may describe an earlier period while retaining its later recorded time. |
| Source time | Preserve reported occurrence/update time and provenance separately. Clock differences and unknown source ordering remain explicit. |
| Dates and deadlines | UTC instants use `Z`; a date-only deadline preserves local date, time zone, calendar reference, wording, and basis. An operational target does not acquire legal effect. |
| Retention | Retain required evidence and history only under the applicable policy. Disposed content is explicitly unavailable; a reference cannot promise eternal retrieval. |

A complete conformance bundle resolves all of its typed references within the same tenant. Production services may use scoped reference retrieval rather than transmitting every referenced object. Cross-organization exchange must create a permissioned package and receiving-side references with provenance; knowing another tenant's identifier grants no access.

JSON Schema checks the declared shapes. Trusted identity resolution, residency, retention enforcement, time-zone/calendar applicability, and legal authority require service controls.

## 4. Core records and responsibility

| Record | Main responsibility and relationships |
|---|---|
| `party` | Legal identity, asserted roles, and scoped identity verification; roles do not themselves grant authority |
| `data_policy` | Purpose-specific processing, disclosure, evaluation, learning, retention, and disposition permissions |
| `case` | Compatible claims/obligations, coordination owner, scoped services, state vector, and remaining duties |
| `service_request` | Contracting party, represented principal, bounded work, allowed acts, window, caps, deliverable, and fulfillment |
| `obligation` | Underlying payment duty, compatible invoice/charge/credit lines, obligated parties, and linked cases |
| `rights_interest` | Documented ownership, assignment, subrogation, security, participation, or servicing interest |
| `claim_passport` | Versioned assertion, evidence, rights, action-specific readiness, gaps, and financial-position reference |
| `evidence_item` | Source artifact metadata, integrity hash, custody, derivation, observation time, and retrieval/disposition |
| `evidence_assertion` | A proposition with supporting and contrary evidence; distinguishes party assertions, attestations, observations, and AI inference |
| `verification_record` | Who verified what, by which method and evidence, for which scope, with which limitations |
| `authority_grant` | Verified principal/delegate relationship, permitted/prohibited actions, scope, bounds, dates, and revocation |
| `policy_snapshot` | Exact policy evaluation and material inputs for a particular case/action |
| `capability` | Declared availability, supported actions/modes/routes, assurance evidence, owner, limits, and reassessment |
| `corridor_pack` | Sourced and reviewed jurisdiction configuration, applicability, supported routes, and maintenance ownership |
| `strategy_plan` | Authorized coordination across primary, fallback, and parallel routes, with costs and exit triggers |
| `decision_episode` | Information available at the time, eligible alternatives, uncertainty, selection rule, and observation horizon |
| `action_intent` | Exact proposed action, immutable binding, status, approvals, and operation identity |
| `approval` | An authorized decision tied to one action/version, binding digest, principal, and expiry |
| `execution_receipt` | A particular dispatch attempt and observed result, including uncertainty and remediation responsibility |
| `work_order` | Provider scope, evidence access, authority, eligibility, acceptance, budget, and return obligations |
| `waiting_requirement` | Required response, owner, recipient, delivery/acceptance status, due basis, expiry, and escalation |
| `agreement` | Exact proposed/shared terms, independent party acceptances, validity review, and subsequent fulfillment/release observation |
| `payment` | Source-classified reported or reconciled transaction; debtor payment differs from insurer or sale proceeds |
| `allocation` | Application or reversal of reconciled debtor payment against an underlying obligation |
| `financial_position` | A reconcilable position across asserted duty, accounting view, effective releases, allocated cash, and outstanding amount |
| `outcome_observation` | Scoped service result and independently observed financial/business results, source, horizon, and attribution limits |
| `event` | Versioned subject/source references, occurrence and recorded time, actor, causal linkage, reasons, and payload integrity |
| `model_execution` | Actual retained input/output references, replaceable model/workflow identity, cost, disposition, and limitations |
| `external_binding` | A verified recipient, communication identity, payment destination, provider endpoint, or source-write target |

Specialist proceedings, richer dispute taxonomies, complex rights waterfalls, and route-specific legal/financial instruments need their own reviewed extensions before implementation. The core identifiers and references preserve room for them; this baseline does not supply every specialized payload.

## 5. Consistency and transaction boundaries

A graph-shaped domain does not require a graph database, a distributed service for every record, or an agent per object. A modular application can own these consistency boundaries.

| Boundary | Required atomic or conditional work |
|---|---|
| Case coordination | Check the expected version; apply a permitted transition; record the owner/reason; publish the corresponding event |
| Service fulfillment | Verify contracted deliverables and remaining duties; complete only that request; do not close unrelated active work |
| Obligation and cash | Deduplicate source transactions; reconcile; reserve/allocate without double recovery across linked cases; append corrections/reversals |
| Action commitment | Recheck live facts and permissions; compare versions; reserve shared limits; record authorization/operation identity; insert the durable outbox item |
| Provider engagement | Bind the accepted scope and cost; activate only after acceptance and conditions/eligibility checks |
| Agreement | Preserve each exact offered term set and acceptance evidence; record performance and release effects separately |

Record snapshots are server-owned projections of accepted domain changes. A client cannot mark a case closed by uploading a new `case.state`, mark a payment reconciled by changing its status, or create authority by submitting an `authority_grant` record.

Use transactional constraints for obligation allocations and competing commercial commitments. The reference harness serializes requests in memory to demonstrate expected results. It does not prove database isolation, distributed locking, crash recovery, or concurrent-worker correctness.

## 6. State and transition contract

The formal case fields are `state.lifecycle_stage`, `stage_state`, `readiness_state`, `authority_state`, `engagement_state`, `dispute_state`, `legal_state`, `payment_state`, `holds`, `closure_state`, and `completion`.

The Operating Model's enum values are retained. JSON Schema rejects an invalid stage/substate combination, such as `ASSESSMENT + ENFORCEMENT_ACTIVE`. Independent dimensions remain independent.

| Transition family | Preconditions and result |
|---|---|
| Placement → construction/assessment | Valid supported scope, parties, minimum authority, and sufficient current material; reviewed late entry can use a documented checkpoint |
| Construction ↔ assessment | Evidence cure, contradictions, or reconciliation change action-specific readiness |
| Assessment → decision | Recorded alternatives, limitations, economics, and applicable authority |
| Decision → execution/escalation | Supported service/capability, authorized strategy, eligible executor, and required provider acceptance |
| Execution/escalation ↔ assessment | Material dispute, evidence, rights, authority, policy, or economic change |
| Execution/escalation → resolution | A supported resolution process has begun; this does not itself establish accepted terms or verified cash |
| Resolution → closure → closed | Reconcile each required completion dimension; settle or explicitly assign remaining duties; no active service may be hidden |
| Closed → assessment/placement | Explicit reason and authority; preserve history and determine what new or surviving service scope permits |

Same-stage updates still need their expected version and applicable guards. A reviewed handover permits late entry into a justified stage; it never replays historical communications or treats imported claims of authority/payment as verified.

`SERVICE_SCOPE_COMPLETE` can close operations with an unpaid claim after bounded work ends. It is not an observed zero recovery, waiver, or paid-in-full state. Monitoring does not continue indefinitely without contracted scope.

The transition helper checks identity, next version, the allowed stage graph, reason, and the explicit authority requirement for selected boundaries. Production handlers must enforce the full preconditions in the Operating Model, including separation of duties and case-specific policy.

## 7. Command admission and result semantics

The package defines 23 operation names:

| Group | Typed operations | Main admission boundary |
|---|---|---|
| Placement and service | `case.place`, `service.request`, `case.import_handover` | Proposed work/current-state handover; no automatic verification or execution authority |
| Evidence and assessment | `evidence.attach`, `verification.record`, `assessment.request`, `strategy.propose` | Registered sources and scoped findings; reviewer/agent eligibility is checked independently |
| Authority and approval | `authority.request`, `authority.revoke`, `approval.record` | Requests do not mint grants; recorded verification/approval requires the corresponding trusted actor and instrument |
| Actions | `action.prepare`, `action.commit`, `action.cancel`, `action.reconcile` | Exact binding and live checks; cancellation/uncertain effects remain distinct |
| Provider work | `work_order.offer`, `work_order.respond` | Actual accepted scope, conditions, cost, and executor |
| Resolution | `agreement.propose`, `agreement.observe_acceptance` | An observation of acceptance requires exact-term and authority review; external legal effects cannot be overwritten by a UI status |
| Financial | `payment.observe`, `payment.reconcile` | Reported transaction, authoritative evidence, allocation, and reconciliation are separate |
| Completion and observations | `service.fulfill`, `case.propose_close`, `outcome.observe` | Fulfilled scope and supported observations; no direct declaration that every obligation ended |

Command envelopes identify request/operation identity, intended tenant, actor, represented principal, referenced versions, and a closed typed payload. The service obtains trusted identity, policy, time, and live state independently. Caller assertions are inputs to validation.

The three `ActionCommand` operations additionally bind the target Action Intent and its digest. General commands use `expected_refs` plus typed payload references. Material handlers must require all relevant current versions; a caller cannot choose to omit a necessary consistency check.

A `CommandResult` separates request acceptance, task status, domain status, result references, waiting requirements, reasons, and permitted next operations. Service completion and financial/business observations are read from their own referenced records. Completion of a job never implies that a debt was recovered.

These are transport-independent contracts. Future HTTP endpoints, webhooks, and agent adapters must preserve them. An HTTP response or message acknowledgement describes transport/request handling, not the final commercial result. [HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110.html)

## 8. Exact action, approval, and commit contract

An Action Intent contains an immutable `binding` with case/service/principal/executor, target party and verified destination, action class and execution mode, route/corridor/channel, exact terms reference and digest, evidence references, authority/policy/capability versions, material record versions, cost, and expiry.

`binding_digest = SHA-256(JCS(binding))`. The digest is prefixed `sha256:`. Terms use the same convention on their closed `terms` object. The reference uses RFC 8785 canonical JSON so serialization order does not change the digest. A digest establishes internal content consistency; trusted provenance, signatures, storage integrity, and real authority require independent controls. [RFC 8785](https://www.rfc-editor.org/info/rfc8785/)

An approval binds the exact Action Intent version and binding digest. Changing money, terms, recipient, executor, scope, or a material dependency invalidates the prior binding. Terms are not silently edited after offer/approval; a new proposal preserves supersession and the status of any earlier externally delivered offer.

At commit:

1. Authenticate the caller and represented principal; resolve current access.
2. Resolve the request key and exact binding; return a prior result for a legitimate retry or reject conflicting reuse.
3. Check current case/service scope, versioned material facts, holds, and action necessity.
4. Revalidate grants, approvals, revocation, dates, recipient/destination, rights, policy, corridor, and capability assurance.
5. Enforce amount, nonfinancial terms, disclosure, cadence, budget, and aggregate-obligation constraints.
6. Atomically reserve shared limits and record an outbox item with the durable operation identity.
7. Dispatch through the eligible adapter; retain attempts, acknowledgement, observation, and reconciliation separately.

The included harness implements a single approved, single-payment settlement-offer profile. It deliberately rejects other actions, delegated execution, installment variations, and unsupported nonfinancial terms. That bounded reference is a contract demonstration, not a selected MVP.

## 9. Retry, event, cancellation, and waiting contract

Use a request key scoped to tenant, authenticated actor/service identity, represented principal, and operation. Reuse with a different semantic request is a conflict. Transport attempt IDs or timestamps may change without creating another business operation.

An Action Intent also has stable operation identity. A fresh request key cannot force the same action to run again. Separate action IDs affecting the same obligation still encounter shared commitment and budget reservations.

A dispatch timeout produces `RESULT_UNKNOWN` and accountable reconciliation. Query the existing external operation before deciding whether another attempt is safe. “Exactly once” is not a general guarantee across independent providers; adapter-specific idempotency and observed effects determine safe behavior.

Cancellation before dispatch can suppress work and release eligible reservations transactionally. After dispatch, a cancellation request is a new control event; it does not prove that the recipient failed to receive an offer or that an external commitment disappeared. Uncertain reservations remain under reconciliation rather than expiring into a duplicate effect.

Events retain source occurrence, server recording time, subject/version, known causal references, reason, material payload references, and integrity metadata. Correct facts with new records/events. Payload digests do not authenticate the producer; a production service needs authenticated admission, trusted integrity anchors, retention-aware audit storage, and adapter conformance.

Waiting requirements distinguish transport delivery, acceptance of responsibility, partial response, completion, expiry, and reassignment. An expired internal timer cannot supply consent or release a protected hold. Date-only legal or contractual deadlines retain their source and applicability basis.

## 10. Financial and acceptance contract

Money is represented as an exact nonnegative integer string in minor units, with explicit currency and exponent. USD 78,000 is:

```json
{"currency":"USD","exponent":2,"units":"7800000"}
```

Do not use binary floating point for stored cash or obligation arithmetic. Reversal direction is an explicit record kind, not an unexplained negative value. The currency catalogue, permitted precision, FX conversion/rounding, tax, distributions, and jurisdiction-specific treatment need supported service configuration.

For the supported single-currency position:

`outstanding = principal + supported charges - valid credits - effective releases - reconciled debtor payments`

This is a bookkeeping invariant over supported records. It does not determine legal validity. An accounting write-off, insurance receipt, sale price, and debtor payment remain separate facts.

A reported payment does not reduce the reconciled position. Allocation requires the authoritative source and supported matching/review. Deduplicate by external transaction identity and enforce aggregate allocation limits across linked cases.

Agreements preserve immutable exact terms and independent party acceptances. Fulfillment and `release_effective_at` are later observations outside the terms digest. The fixture's USD 8,000 release occurs only after the documented USD 70,000 payment condition is established.

A later payment reversal appends a reversal allocation. It does not automatically reverse a prior legal release: whether an obligation revives needs the actual terms, evidence, and qualified determination. The reference tests a reversal that restores USD 70,000 outstanding while leaving the earlier USD 8,000 release effective. Other release/revival instruments require reviewed extensions and applicable controls.

## 11. Evidence, private contexts, and learning

Keep original artifacts, derived artifacts, party assertions, model inferences, and verification records separate. A content hash is not proof of performance or enforceability. Scope every verification and keep contradictory evidence visible.

A decision's input references must have been recorded by its information cutoff. Later evidence cannot be inserted into the earlier knowledge state. Model execution records retain the actual relevant inputs/outputs under policy; a model rerun is a new execution and need not reproduce the same text.

Data permissions distinguish delivering the service, tenant-private evaluation, pooled benchmarking, and model training. Tenant-private operation must remain viable. A shared proposal may reference only approved shared evidence; private negotiation strategy does not become shareable because it is linked to the same case.

Outcome amounts distinguish `OBSERVED`, `PENDING`, `UNKNOWN`, `RIGHT_CENSORED`, and `NOT_APPLICABLE`. Only an observed monetary field contains a value; an observed zero needs a source and observation horizon. A case can have observed interim cash while time-to-resolution remains censored; report those as different observations.

Decision Episodes retain eligibility, missing information, selection rules, and uncertainty. Do not invent selection probabilities for human or deterministic choices. Linked activity and outcomes provide traceability; they do not by themselves establish causal lift.

## 12. Worked case

All parties, artifacts, mandates, provider eligibility, rule packs, enabled statuses, and dates in the fixture are fictional. They express assumed prerequisites of a test scenario. No actual provider, regulatory rule, payment, or service availability is certified.

| Checkpoint | Service and case meaning | Financial meaning |
|---|---|---|
| Intake | Four USD 19,500 invoices; identity/evidence defects remain | USD 78,000 assertion; no recovery established |
| Assessment delivered | Assessment request fulfilled; further operation has its own request and authority | USD 78,000 remains asserted; recovery observation is unknown |
| Provider reports payment | Approved exact-term offer has been delivered and accepted; bank reconciliation is pending | A provider report does not reduce the last reconciled USD 78,000 position |
| Closeout | USD 70,000 receipt reconciled; conditional release recorded; operating scope fulfilled | USD 70,000 debtor recovery + USD 8,000 effective release = USD 0 outstanding |

The final case can show partial recovery against the original assertion and full performance of the settlement simultaneously. Export-administrative and retention duties retain named owners after operational closure.

The test suite also constructs an assessment-only exit with an unpaid claim, and a later payment-reversal branch. Neither branch silently creates another service or equates bookkeeping with legal effect.

## 13. Validation and practical limits

The first completed validation run passed **51 conformance checks**. The package validates the schema against its metaschema, checks all 89 records in the worked example, and exercises positive and negative domain cases. Date/time format validation is explicitly enabled; format annotations alone are insufficient. [JSON Schema 2020-12](https://json-schema.org/draft/2020-12) · [Python jsonschema validation](https://python-jsonschema.readthedocs.io/en/stable/validate/)

| Tested area | Evidence from the reference checks |
|---|---|
| Data contracts | Required/closed fields, typed references, tenant separation, exact money, dates, stage/substate pairs, and typed service requests |
| Authority and content | Expired/revoked grants, stale approval, changed material state, exact action/terms binding, and bounded terms |
| Controlled execution | Retry identity, fresh-key duplicate prevention, shared commitment reservation, caps, holds, policy, capability, and disclosure |
| Financial meaning | Unreconciled reports, other proceeds, duplicate transactions, over-allocation, release conditions, and payment reversal |
| Scope and observation | Assessment completion, unpaid scope closure, unknown versus zero, active work at closure, and retained duties |
| Historical correctness | Later information excluded from earlier decisions, exact acceptance evidence, and absent invented propensities |

The tests do **not** prove production authentication, genuine signatures/authority, source authenticity, legal applicability, deployed tenant isolation, durable transactions/outboxes, true concurrent workers, provider delivery, PSP reconciliation, performance at scale, or recovery uplift.

The broad command schemas define admission shapes. Most command handlers, the complete policy/corridor compiler, rich financial instruments, and full runtime transitions remain unimplemented. Passing this suite is not passing all 36 workflow acceptance scenarios. Capability release still needs its applicable workflow, integration, operating, and expert-review gates.

## 14. Running and maintaining the package

Extract the companion archive into a working folder with Python 3.10 or later. From that folder:

```bash
python -m venv .venv
```

Activate the environment using the command for your operating system, then run:

```bash
python -m pip install -r requirements.txt
python validate_contracts.py
python -m unittest -q test_contracts
```

The validator reads local files and produces no external effect. Its default input is `worked-case.json`; an alternate compatible bundle can be supplied as a path. The reference Python code is a conformance tool and does not select the application's implementation stack.

Keep this specification and `recovery-contracts.zip` as the current pair. The archive contains the schema, fixture, validator, tests, and dependency file; it does not duplicate the business or operating documents.

Version schema and command contracts deliberately. With closed objects and enums, adding an optional property or enum value can still break an older consumer. Negotiate supported contract versions and test adapters; never reinterpret a stored version in place. Unsupported route-specific payloads fail explicitly until a compatible reviewed extension is introduced.

**Next project step:** map capabilities and dependencies to these contracts, compare complete candidate MVP paths, and select one using customer value, development effort, operating responsibility, and validation evidence. Implementation architecture and the build plan follow that selection.
