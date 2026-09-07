# GRE — Operating Model

**Updated:** September 7, 2026

**Status:** Authoritative operating design for the single Trade Pilot; live capability, provider and corridor availability remain unproved.

**Owns:** Responsibilities, shared operating invariants, service boundaries, authority, handoff, financial meaning, exceptions and surviving duties.

**Companions:** [Workflow](04-workflow-interaction-specification.md), [Contracts](05-domain-data-contracts.md), [Pilot](06-pilot-brief.md), [Architecture](08-stack-and-environment-decision.md).

## 1. One Pilot and a bounded promise

The Pilot combines GRE Foundation with **GRE Trade & Receivables**, initially testing India-creditor → U.S.-business-obligor goods/services claims. Its recurring-case creditor buyer and corridor are selected hypotheses, not established demand or permission to operate. The Trade-required Network & Control capabilities are shared horizontal capabilities in this Pilot. They are neither another matter classification nor a separately launched family.

GRE prepares source-linked claim records, assesses readiness and options, supports named-provider preflight, transports authorized disclosures and creditor instructions, records direct appointment and independent provider acceptance, and supplies contracted correction, status, cost, payment-observation and continuity services. A useful assessment, an already-paid finding, or a documented absence of a viable provider route can complete a service successfully.

An independent provider conducts post-default obligor collection through its own people, identity, systems and judgment. GRE does not collect, negotiate for the creditor as collector, supervise tactics, acquire claims, operate a borrower-facing portal, or custody/pass through repayments. Creditor control means tooling for the creditor's decisions and provider relationship. It does not give GRE authority to choose contact scripts, cadence, negotiation tactics, legal steps or provider personnel instructions.

Private Resolution, Consumer Credit and wider Trade routes retain their requirements and reopening gates in [Future Development](07-future-development-and-business-deliverables.md). Foundation reuse does not enable them. Historical descriptions of broad recovery execution are superseded for this Pilot; they remain provenance, not alternate release scope.

## 2. Shared primitives and source ownership

A claim asserts a right against identified obligated parties on a stated basis. An account balance is insufficient because it can mix contracts, currencies, rights, disputes and forums. An obligation links related claims and interests to the underlying asserted duty. A case coordinates compatible claims; a Service Request defines one bounded engagement. Completing an assessment does not authorize transfer, and completing transfer does not terminate a separate observation service.

| Canonical responsibility | Owned records and operating rule |
|---|---|
| Identity and access | Parties, representatives and scoped access; identity and membership do not establish claim ownership or action authority |
| Evidence and Passport | Originals, derived artifacts, assertions, verification and versioned views; one correction lineage |
| Obligations and financial position | Obligations, claim lines, rights interests, exact amounts, payments, allocations and reversals; no separately editable family balance |
| Authority and action control | Grants, approvals, exact bindings, current-state checks, outbox and execution receipts |
| Classification and policy | Matter facts, family/corridor profiles, effective rules, case evaluations and release conditions |
| Case and service coordination | Service scope, ownership, waiting, expiry, cutover dependencies and surviving duties |
| Provider interoperability | Provider-owned requirements, offers, validation delta, acceptance, engagement and returned events |
| Participation and agreements | Source-linked proposals, exact acceptance and conditions; Pilot records provider-led external agreements |
| Disclosure and correction | Purpose-specific exports, redaction, recipients, correction delivery and retention handling |
| Observations and assurance | Attributed events, observation horizons and quality measures derived from source records |

These are application ownership boundaries, not ten deployments. [Architecture](08-stack-and-environment-decision.md) owns implementation dependencies and transactions. Read models and compositions cannot independently change their referenced source facts.

The six named contracts compose this foundation. Claim Passport is a versioned view; Provider Acceptance Profile contains standing provider-authored requirements; Authority Envelope references grants, rights, approvals and exact limits; Corridor Pack supplies versioned directional constraints; Action Receipt composes action/attempt evidence; Resolution Quality Scorecard derives qualified measurements. None creates an alternative authority, financial or success ledger. [Contracts](05-domain-data-contracts.md) owns exact bindings and migration.

Aggregate claims only when creditor, obligor, legal basis, forum, rights, instructions and allocation are compatible. Link related guarantor, insurer, assignee and proceeding records without multiplying the obligation. Different legal entities or incompatible terms normally require separate coordinated cases. A suspected duplicate is reviewed; legitimate parallel specialist work is not automatically duplicate work. No cross-tenant debtor index or disclosure follows from identity matching.

## 3. Classification and availability

Record creditor and obligor types, actual obligation purpose, goods/services/account basis, ownership/servicing posture, relevant locations, governing terms/forum, requested acts, actor, compensation and data/payment paths. An incorporation label is insufficient when a natural person, guarantee, sole proprietor or mixed-purpose transaction introduces uncertainty. Preserve the assertion and hold affected disclosure/activation for classification review; do not silently route it into Consumer or Private.

Enablement requires the intersection of **family, directional corridor, service mode, actor eligibility, authority, effective policy conditions and released capability**. Commercial edition entitlements and legal-review status are separate checks. Buying an edition, deploying Foundation or passing a synthetic fixture cannot enable an unreleased service. Unknown or expired prerequisites block the affected consequential act while separately permitted intake or analysis may continue.

Pilot service modes are `ASSESS`, `PREPARE`, `TRANSFER`, `CONTROL` and `OBSERVE`. Their precise composition is versioned in [Contracts](05-domain-data-contracts.md); legacy `service_request.kind` values are not silently renamed. In particular, legacy `OPERATE` does not grant live GRE collection or resolution scope. Service mode `OBSERVE` differs from `action_intent.binding.execution_mode = OBSERVE`.

Corridor policy retains source, effective period, fact predicates, responsible reviewer, uncertainties, permitted/denied acts, conditions and review expiry. Proposed, issued and operative rules remain distinguishable. Qualified interpretations are recorded as such; AI summaries are not counsel determinations. Changes identify affected cases, profiles, queued actions and regression scenarios. Applicable external requirements cannot be overridden by a commercial policy or internal approval. Review, availability and suspension evidence belong in [Release and Assurance](13-pilot-release-and-assurance.md).

## 4. Evidence, amounts and rights

Each material assertion links to supporting and contrary sources, or explicitly records absence. Distinguish asserted, admitted, disputed, reviewed and route-eligible amounts. An obligor's admission is attributed evidence; neither admission nor a reviewed document automatically establishes legal enforceability. Verification names its subject, method, reviewer, date, purpose and limits. Presence, integrity, authenticity, performance and legal effect are different determinations.

Keep originals and derived translations/extractions separate. Corrections create a new version or annotation, preserve prior decision-time knowledge and identify affected disclosures. Record valid time and recorded time. Unknown, missing, contradicted, not applicable and verified-for-scope are not interchangeable. Preserve actual material model inputs/outputs within retention rights; a rerun is a new evaluation.

Financial position separates:

- asserted obligation and supported claim-line components;
- creditor accounting carrying amount, impairment and write-off;
- settlement or installment obligations and conditional releases;
- reported, received, reconciled, remitted, reversed and refunded cash;
- creditor/provider costs, taxes, withholding and FX;
- rights-holder entitlements, distributions, insurance proceeds and sale consideration.

Use exact decimal/currency contracts and explicit allocation, never binary floating-point balances or an unqualified sum of currencies. Every adjustment has a source and effective basis. A credit memo may correct a receivable; a proposed credit does not. Accounting write-off does not automatically release the obligor. Provider expenses cannot become debtor charges without the appropriate basis.

For a defined single-currency snapshot, outstanding asserted position reflects asserted principal and supported charges less documented effective credits/releases and reconciled allocated payments. This is a bookkeeping representation, not automated adjudication. A disputed portion stays visible rather than disappearing because readiness is weak. Draft settlement terms do not reduce the obligation; the agreement's effective conditions govern any reduction or release.

Payment observations preserve source transaction identity, payer/payee, currency, amounts, timestamps, status, evidence and allocation. Duplicate feeds represent one movement of value. Bank/rail evidence, creditor receipt and provider reports answer different questions; no whole system is universally authoritative. FX records preserve original amount, conversion source/time/rate, rounding, fees and settlement currency. Short receipt from fees or withholding remains an exception until allocated under the relevant terms. Reversals append compensating history and reassess completion; they do not erase the original receipt.

Assignments, participation and insurance may change pursuit authority and proceeds entitlement. Insurance payments and sale price are not debtor recovery. Identify notice, consent, cooperation, subrogation and distribution duties from the relevant instruments and qualified review. A rights transfer can invalidate a prior mandate; linked services must not recover or allocate more than the permitted aggregate obligation.

## 5. Qualified state axes and accountable actors

One status cannot express a case that is disputed, under an accepted provider mandate, partly paid and still awaiting GRE observation. Preserve independent axes and refer to qualified record paths where implemented.

| Axis | Meaning and owner |
|---|---|
| `case.state.lifecycle_stage` / `case.state.stage_state` | Case coordination view; an execution stage does not say GRE performs collection |
| `case.state.readiness_state`, `case.state.authority_state`, `case.state.engagement_state`, `case.state.dispute_state`, `case.state.legal_state`, `case.state.payment_state` | Independent domain views; specific grants, issues and receipts remain authoritative; engagement may describe external provider work |
| `case.state.holds[]` | Scoped blocks with basis, owner, review time and release authority |
| `case.state.closure_state` and completion dimensions | Operational disposition plus distinct financial, commercial, legal, export-administrative, operational and retention duties |
| `service_request.status` | State of that contracted service; `TRANSFERRED` is distinct from `case.state.closure_state = SERVICE_SCOPE_COMPLETE` |
| `work_order.acceptance_state`, `execution_conditions[]`, `direct_appointment_ref`, `provider_work_state` | Commercial response, independent validation, direct mandate and active external work remain separate |
| `work_order.activation_at` / `work_order.cutover_at` | Execution prerequisites, fencing, external uncertainty and responsibility transition |
| Disclosure/access and external cessation | GRE access changes, provider acknowledgment, retained copies and unresolved external actions |
| Observations and freshness | What each source reported, when observed and what remains unknown |

These qualified paths refer to the v0.2 design in [Contracts](05-domain-data-contracts.md), not added fields in the immutable v0.1 reference. Disclosure/access and external cessation remain distinct operating facts even where represented through receipts and evidence rather than dedicated fields. Legacy `work_order.status = ACCEPTED` retains its compatibility meaning of acceptance with resolved conditions; `work_order.acceptance_state` records the separate commercial response. No acceptance or dashboard state substitutes for current authority and activation checks.

Every active service has an accountable organization/role, next decision or review time, backup and escalation path. A case coordination owner prevents forgotten dependencies; it does not assume the provider's professional responsibility. The creditor owns claim instructions, provider appointment, budget and commercial decisions. GRE owns its contracted assessment, disclosure, platform controls and continuity duties. The provider owns independent validation and execution. Qualified advisers own their opinions and reserved acts; banks/payment institutions supply authorized financial services. GRE support accesses only the permitted case scope.

Holds attach to affected acts, actors, lines or disclosures. Identity, authority, evidence, policy, conflict, security, payment and legal-review holds need reasons and release ownership. Sanctions/watchlist signals require supported sources, exact-party review and an accountable compliance disposition; a name match is not a final finding. A precautionary insolvency signal blocks affected GRE transmission/activation and alerts the responsible creditor/provider; qualified review determines external legal effects. Permitted preservation, correction, support or protective specialist work can remain available. Queues are derived views, never unowned substitutes for these duties.

## 6. Authority and prepare/commit control

Keep action classes A0–A5 as categories: read, prepare, routine operational effect, commercial commitment, reserved professional act, and funds/title act. They are not autonomy levels. Execution modes `OBSERVE`, `PREPARE`, `APPROVAL_REQUIRED` and `DELEGATED` remain separate from service modes, commercial entitlements and assurance. A broad grant cannot enable a capability outside Pilot scope.

A grant identifies principal, verified grantor and grantee, evidence, permissible/prohibited acts, case/party/recipient/purpose scope, financial and nonfinancial limits, subdelegation, expiry, revocation and review basis. A verified standing mandate can cover recurring permitted administrative work without repeated approval. New terms, disclosure purposes or insufficient corporate authority require the correct decision owner. Signed integrity evidence does not prove corporate power.

Every material GRE effect starts with an Action Intent: exact content/terms, actor/principal, recipient and communication identity, pinned source/Passport references, policy and authority binding, limits, expiry and stable operation identity. Preparation cannot send a packet, commit spend or change a financial record.

At commit and immediately before dispatch, authoritative operations recheck current scope/release, authority/revocation, policy/holds, recipient/disclosure, relevant evidence and freshness, rights/payments/disputes/agreements, current versions, shared limits, competing commitments and continued necessity. Material changes require fresh preparation or approval. Concurrent work reserves shared limits transactionally; two users cannot independently spend the same remaining authority.

Persist authorization, reservations and durable outbox work consistently. Dispatch workers use the same controls and honor cutover/revocation fences; workflow retries are not new business authority. Preserve operation keys across retries, reject key reuse with a changed payload, and retain attempt digests/external references. Delivery, acknowledgment, observed effect, failure, partial effect and unknown result remain distinct. A timeout after possible transmission enters reconciliation, not automatic resend with a new key. A dispatched effect may require a separately authorized correction or withdrawal; compensation cannot promise external reversal.

These are implementation requirements. Reference snapshots and negative examples demonstrate represented semantics only; they do not establish transactional enforcement, reliable adapters or live safety.

## 7. Provider preflight, acceptance and cutover

Eligibility precedes comparison: check the exact matter/acts, geography, credentials and review dates, conflicts, capacity, data constraints, commercial terms and supported returned observations. A creditor's own panel is explicitly labeled. No pay-to-rank influence or invented provider availability is permitted.

A **Provider Acceptance Profile** belongs to the provider: supported/excluded cases, evidence requirements, validation stages, fees/caps, conflicts, capacity, required appointment, input formats and event/exception return terms. Provider-ready means readiness against a named profile version, not universal validation. Reusable evidence can reduce intake, but independent review may still identify a legitimate delta.

1. **Preflight disclosure:** Verify principal, named provider, purpose, scope and permission. Disclose only necessary data for conflict/eligibility/review. Review access conveys no collection mandate.
2. **Versioned offer:** Freeze the offered Passport and disclosure manifest. Record received, rejected, conditional, accepted, unanswered or expired response under the contract. Changed scope/price/requirements form an explicit delta and may require creditor approval.
3. **Direct appointment:** Creditor and provider establish their engagement, fees, mandate and obligations directly. GRE's technical/data terms do not create a hidden collection subcontract.
4. **Independent execution validation:** Record fulfillment of the provider's conditions for the specified acts, current eligibility, mandate and approved packet version. Conditional acceptance does not activate unresolved work. Different validation stages cannot be collapsed into one “accepted” badge.
5. **Activation/cutover:** Recheck current prerequisites, fence conflicting GRE commits, cancel cancelable queued effects and inventory sent/in-flight/unknown work. Record provider activation and the transfer service's result separately. The Pilot does not acquire GRE collection authority before cutover.
6. **Residual services:** Continue only separately scoped control/observation and surviving correction, incident, support and preservation duties, each with owner, window and return conditions.

Decline, expiry, conflict, failed delivery or silence leaves a named owner to cure, extend, seek another eligible provider or conclude no viable route. An urgent source-based deadline needs escalation before a routine offer timeout. One provider can establish first accepted placement; a bounded portability claim needs two independent providers reusing the core profile. Neither requirement asserts partners exist.

## 8. Control, observation, recall and switching

Provider execution remains external after activation. GRE can transport the creditor's exact authorized budget/mandate decision and display returned exceptions; it cannot decide the provider's next collection act. GRE may enforce its security, access, interface and data-use conditions and suspend its own functionality or eligibility representations after incidents. Preserve permitted correction, complaints and evidence access during a scoped suspension.

Each return contract states event types, source identity, cadence/freshness expectations, costs, status exceptions and closeout requirements. Display source occurrence time, receipt time and last successful synchronization. Missing events are unknown, not evidence of inactivity or zero recovery. A stale payment source blocks or narrows affected balance-sensitive actions. Provider silence escalates through the creditor's relationship and GRE's contracted support path; no unresponsive provider silently loses responsibility in the record.

Recall and switching distinguish requested revocation, effective GRE access removal, instruction delivery, provider acknowledgment of cessation, outstanding commitments/proceedings, retained copies, export/return obligations and replacement activation. Fence new conflicting commits promptly. Do not represent access revocation as remote deletion or proof that external work stopped. If cessation remains uncertain, record that uncertainty and hold conflicting replacement work pending a documented creditor/qualified disposition. Separately scoped nonconflicting specialist work requires explicit boundaries.

A continuity packet includes permitted source/Passport versions, rights/authority, issues, exact live terms, historical actions and receipts, cash/costs, freshness gaps, deadlines, unresolved work and retained duties. A replacement performs its own preflight and acceptance. A switch is not successful merely because an export downloaded.

## 9. Privacy, correction and AI boundaries

Access is tenant-, actor-, object-, field-, purpose- and service-scoped. Provider review gets a minimized packet, not a whole portfolio. Privileged advice, private strategy, commercial limits, unrelated evidence and provider-confidential information require separate treatment. Evidence access for service delivery does not authorize pooled learning, resale, benchmarking or training.

Record each recipient, purpose, artifact/version, redaction and permitted onward use. Corrections identify affected recipients and authorized follow-up; previously delivered content is not silently overwritten. Retention, legal hold, erasure, return, access revocation and recipient duties are separate operations. Preserve lawful audit meaning without promising immutable personal data forever.

Documents, emails, provider events and agent messages are untrusted data. Embedded instructions cannot choose privileged tools, redirect recipients/funds, reveal secrets or widen scope. Models may extract, classify, compare scenarios, prepare packets and suggest corrections; independent controls validate authoritative effects. Log actual material outputs, source/prompt/model versions, human disposition and uncertainty within permission. Models cannot grant authority, cure missing proof through assertion, adjudicate legal issues or direct external collection.

## 10. Waiting, service completion and economics

Evidence requests, approvals, offers, financial investigations and returned exceptions retain requesting owner, recipient, delivery status, due/review time, escalation and expiry. Partial responses satisfy only matched requirements. Silence never constitutes acceptance. Distinguish contractual/legal dates, authority expiry, provider commitments, source freshness, service windows and internal review targets; preserve time zone and source wording. Do not invent legal deadlines or service guarantees.

Operational closure requires an authorized disposition, canceled/reconciled pending effects, completed or transferred active services, honest observations and assigned residual duties. Financial receipt, installment satisfaction, settlement satisfaction, legal release, creditor accounting, export-administrative reporting and retention can differ. Reversal, new evidence or correction may reopen affected dimensions under current authority. Ending an observation window does not authorize indefinite paid monitoring.

GRE billing is separate from debtor balances, provider fees and repayment instructions. A service contract defines its billable unit, included revisions/retries, caps, outside costs, window, cancellation/reopening and hand-back. Display costs before commitment; changing a provider quote cannot silently expand approved spend. GRE-defect correction is not new billable work. Prices, support coverage and SLAs remain validation items, not assertions in this design.

Quality records preserve readiness improvement, customer/provider rework, acceptance and activation latency, rejection/delta reasons, continuity defects, observations, cash and reversals, costs, complaints and actual human effort. Known-zero, pending, unknown and right-censored outcomes differ. Historical cash is not newly recovered through GRE; linking a provider or model to a payment does not establish causal credit. Provider comparisons disclose case mix, selection effects, source coverage and observation horizon. Use scenario ranges and abstention when route probabilities lack evidence. Decisions preserve considered alternatives and constraints, while future pooled learning and public standards stay gated in [Future Development](07-future-development-and-business-deliverables.md).

## 11. Verification and maintenance

[Workflow](04-workflow-interaction-specification.md) owns the complete Trade path and failure interactions. [Contracts](05-domain-data-contracts.md) owns exact records, transitions, fixtures and limited conformance evidence; [Release and Assurance](13-pilot-release-and-assurance.md) owns runtime and live-operation gates. Preservation of the historical reference never permits stale semantics to activate new work. Operating changes must update those owners together, with their scope and unresolved decisions recorded in [Reconciliation](12-scope-decisions-and-reconciliation.md).
