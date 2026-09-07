# Global Recovery Engine — Prioritized pilot backlog

**Date:** September 7, 2026

**Version/status:** 0.1 — proposed delivery order for review

**Owner:** Vishal, sole developer and project lead

**Baseline:** [5511b1e](https://github.com/vishal-baliga/global-recovery-engine/commit/5511b1ef3096b7791a3c8be62a916c469c9f3a73), with the verified environment described in [document 10](10-dependency-baseline.md).

**Hierarchy:** GRE project → pilot release → 10 epics → 48 delivery stories/tasks.

## 1. Delivery decision and scope

Build a complete domestic U.S. personal/friend-loan journey first, then complete the India-origin B2B recovery journey against U.S. businesses using the same foundations. Start coverage, pricing, provider and pilot-economics decisions early. Both journeys must deliver the outcomes in [the pilot brief](06-pilot-mvp-brief.md); neither is reduced to intake, a dashboard, or a referral link.

**The local environment prerequisite is satisfied for planning.** The Mac reports and published setup code establish native ARM64 toolchains, PostgreSQL, Temporal, Azurite, shared dependency resolution, generated-client requests and the Next.js fixture build. TypeScript remains **6.0.3** with Hey API **0.99.0** until a tested upgrade resolves the observed compiler-API incompatibility. This review found no blocker to backlog planning; it did not independently rerun the developer’s Mac checks.

**Priority is the order of the stages below, then the numbered order within each stage.** Dependencies identify the minimum preceding delivery work. They are implementation dependencies, not a requirement that every customer case must pass through every route: an assessment-only case or early specialist referral remains valid. Pull the earliest unblocked item; external review delays need not stop permitted synthetic development.

All 48 items are **not started** in this draft. The local setup work is already verified and is not counted again. The order is proposed; there are no calendar commitments or invented velocity estimates. Split large items into bounded stories when picked up while retaining the parent ID, dependencies and acceptance coverage. For one developer, keep one implementation item in progress; external business/review work may progress alongside it.

The next work is **GRE-001: document reconciliation and delivery preparation**, followed by the first implementation item, GRE-006. Detailed schema, provider and infrastructure decisions are resolved within their dependent stories. Do not turn the 29 reference records or 23 reference operations into mandatory components or rewrite the whole ZIP before coding.

## 2. Epics and ownership

| Epic | Outcome | Numbered items |
| --- | --- | --- |
| E01 | Delivery foundation and planning | 001, 006, 012, 013, 048 |
| E02 | Service offer, operations and pilot economics | 002–005, 014, 019, 043–044, 046–047 |
| E03 | Identity, case foundations and audit | 007–009, 011 |
| E04 | Intake, evidence and assessment | 010, 015–016, 018 |
| E05 | Contact, borrower response and safeguards | 020–023 |
| E06 | Financial position, agreements and plan servicing | 017, 024–028 |
| E07 | Specialist execution and domestic completion | 029–032 |
| E08 | India–U.S. commercial journey | 033–037 |
| E09 | Reviewed document/AI assistance | 038–039 |
| E10 | Privacy, deployment and operating readiness | 040–042, 045 |

Every numbered item has Vishal as the accountable delivery owner. **ENG** means implementation with Codex assistance; **QA** means executable validation and observed evidence; **DOC** means a reviewed project/delivery record; **BUS** means a business decision or agreement; **OPS** means a demonstrated operating process. Qualified reviewers and execution providers own the reserved or live activities assigned under GRE-002/GRE-043; they are not assumed to be available because an item names them.

For each started item, record its specific implementer/reviewer, unresolved choices, intended evidence and any external owner. An unfilled qualified/partner role is a live-service dependency with an owner and due/review point, not a silent manual fallback.

## 3. Ordered delivery backlog

Each acceptance description is the minimum outcome to preserve when decomposing the item. Expand executable examples in the story design/acceptance note before implementation.

### 0 — Documentation and early business decisions

Complete GRE-001 before product coding. Start the business decisions early; while external answers are pending, pull the earliest implementation item whose actual dependencies are satisfied.

| Priority / item | Outcome and acceptance evidence | Depends on |
| --- | --- | --- |
| **GRE-001 · E01 · DOC** — Reconcile the project and prepare delivery documents | Update documents 01–05 in place for both pilot tracks and the agreed sequence. Prepare initial journey/role diagrams, architecture decisions, an acceptance-scenario catalog, and the first story’s design note. Identify which ZIP contracts need later story-specific revision; preserve it as a reference. Record unresolved decisions with owners and dependent stories. This documentation step precedes product coding. | — |
| **GRE-002 · E02 · BUS** — Define service responsibility and supported coverage | Record GRE’s contracting/coordination role, the creditor/provider who may execute each action, qualified review ownership, supported U.S. states and claim profiles for both tracks, purpose classification, and handling of older or already represented matters. Obtain the relevant scoped professional review before enabling affected live activities. Unknown coverage produces an explicit unsupported/review outcome. | — |
| **GRE-003 · E02 · BUS** — Define the paid offer and case economics | Specify assessment, assisted resolution, plan servicing, and specialist coordination deliverables; fees/caps, service windows, customer approvals, cancellation/refund treatment, and outside costs. Model founder/reviewer/support effort and low-value or weak-evidence cases separately for each track. A customer can understand what paid work delivers before choosing it; no price or recovery guarantee is invented. | GRE-002 |
| **GRE-004 · E02 · BUS** — Validate feasible contact, payment, acceptance, and specialist routes | Identify at least one viable route for every advertised pilot service, with actor/country/use-case admission, indicative costs, data exchange, and fallback. Compare reviewed manual and integrated routes. Define adapter contracts and sandbox access needs. A vendor’s general feature list does not establish admission for GRE’s use; actual partner commitments are completed in GRE-043. | GRE-002 |
| **GRE-005 · E02 · BUS** — Design recruitment and pilot measurement | Define separate domestic and commercial acquisition hypotheses, intended cohorts, eligibility, service targets, observation windows, and conversion/cost/outcome events. Set numerical targets before live evaluation using observed baselines. Prepare recruitment material and permission process; recruitment execution is GRE-046. Capture willingness to pay, effort, complaints, repeat/referral intent, and cases still unresolved. | GRE-003 |

### 1 — Shared delivery and control foundations

Establish the application’s identity, records, private storage and effect controls. The existing echo/build fixtures remain setup evidence and are replaced or retained deliberately as product packages develop.

| Priority / item | Outcome and acceptance evidence | Depends on |
| --- | --- | --- |
| **GRE-006 · E01 · ENG** — Establish product packages, quality tooling, and CI | Choose the minimal API/shared-domain/worker/web package structure from the verified baseline. Configure focused Python/web lint, type, unit and browser tooling, locked builds, and generated-contract drift checks in CI with disposable services. Verify a clean checkout and document safe host startup/attachment. Carry the TypeScript 6.0.3 compatibility guard into updates. Make health checks independent of expired historical Temporal probe records while preserving genuine connectivity failures; retain historical evidence separately. | GRE-001 |
| **GRE-007 · E03 · ENG** — Integrate identity and represented principals | Select/lock Clerk SDKs and integrate development sessions and organizations behind an explicit auth boundary. Support individuals, organizations, operator membership, session revocation, and represented-principal selection. Authenticate web/API requests; deny forged or missing sessions. Tests prove signing in or joining an organization does not confer case authority. Borrower access is a separate scope, completed in GRE-022. | GRE-006 |
| **GRE-008 · E03 · ENG** — Build the application shell and interaction conventions | Establish Next.js routes, error/loading/empty states, accessible forms and mobile layouts. Add Tailwind/shadcn and TanStack Query only for defined UI needs, with compatible locks. Centralize generated-client configuration, authentication transport, sensitive-data caching policy, and typed failures. Navigation or autosave never sends contact or accepts terms. Verify keyboard use and clear recovery from expired sessions. | GRE-006 |
| **GRE-009 · E03 · ENG** — Implement case, service, party, authority, and money foundations | Create PostgreSQL models and Alembic migrations for selected story needs, retaining separate cases, service requests, obligations, principals, grants, and orthogonal states. Use exact money/currency and source-aware dates, not floating-point balances or invented due dates. Enforce server-owned transitions, expected versions, least-privilege application roles, and transaction-scoped RLS. Prove cross-tenant denial and migration application against a disposable database. | GRE-007 |
| **GRE-010 · E04 · ENG** — Provide private evidence intake and storage | Implement the Blob adapter, upload/resume behavior, file-size/type limits, quarantine/scanning and safe previews. Support the pilot’s documents/images, payment records, message/email exports, and audio/transcripts through explicit formats and reviewed handling. Preserve originals, hashes, provenance, ownership, and derived versions separately. Authorization governs every upload/download; unrelated conversations are protected. Verify expired/revoked links and malformed uploads. | GRE-008, GRE-009 |
| **GRE-011 · E03 · ENG** — Record auditable changes and scoped activity history | Capture trusted actor/principal, command identity, source occurrence and recording times, relevant versions, reason, and references for material changes. Corrections append history; current snapshots are projections. Views and exports respect case/disclosure scope. A service completion cannot hide another active request, and later evidence cannot be represented as known at an earlier decision. | GRE-009 |
| **GRE-012 · E01 · ENG** — Build durable commands, outbox delivery, and provider fakes | Implement shared API/worker domain checks, transactional outbox, stable operation IDs, request-key conflicts, and aggregate commitment limits. Keep preparation, approval, dispatch, delivery, and reconciliation distinct. Add scoped provider fakes for failed/duplicate/delayed callbacks and uncertain submission. At dispatch, recheck current authority, terms, destination, balance, holds, scope, and budget. Cancellation after submission records uncertainty; it does not erase an external effect. | GRE-009, GRE-011 |
| **GRE-013 · E01 · ENG** — Instrument application operations and configuration | Add OpenTelemetry correlation, redacted structured logs, health/readiness checks, worker/queue/failure indicators, and configuration validation. Keep operational telemetry separate from the audit ledger. Assign actionable failure ownership and capture execution cost/effort fields needed by the pilot metrics. Test that credentials and private evidence do not enter routine logs. | GRE-006, GRE-012 |

### 2 — A useful domestic assessment

Demonstrate an individual creditor reaching a reviewed history, financial position, options and accountable next action, including weak or disputed evidence.

| Priority / item | Outcome and acceptance evidence | Depends on |
| --- | --- | --- |
| **GRE-014 · E02 · ENG** — Deliver two acquisition and suitability entry routes | Provide distinct personal-loan and India–U.S. commercial entry explanations, supported scope, service/fee disclosures, and inquiry conversion events. Screen purpose, parties/location, and unavailable routes without claiming nationwide execution. Unsupported submissions receive reasons and an appropriate next option. Publish/recruit only after the applicable launch conditions; synthetic previews can be built earlier. | GRE-003, GRE-008 |
| **GRE-015 · E04 · ENG** — Implement resumable personal-loan intake | Capture each advance, original repayment understanding, absent terms, recipient versus alleged borrower, prior contact/promises/extensions, partial or cash repayments, existing settlements/representatives, customer objectives and budget. Allow assessment without borrower enrollment or a written agreement. Detect potential duplicate submissions without revealing another tenant’s case. Resuming intake preserves entered evidence and attribution. | GRE-007, GRE-009, GRE-010, GRE-014 |
| **GRE-016 · E04 · ENG** — Reconstruct evidence, timeline, and missing facts | Produce source-linked advances/contact/payment chronology, assertions, contradictory accounts, and scoped reviewer findings. Separate proof of transfer from proof of a loan; preserve loan/gift/investment uncertainty. Support attributed manual transcription/translation and requests for missing evidence. Partial replies satisfy only the relevant requests. Relevant conversation context remains available without disclosing unrelated private material. | GRE-011, GRE-015 |
| **GRE-017 · E06 · ENG** — Reconcile the claimed and supportable financial positions | Handle multiple advances, supported charges, credits, releases, and alleged versus reconciled prior payments. Present asserted, disputed, and reviewed amounts with provenance. Prevent double allocation across linked obligations/cases. Import historical cash without counting it as GRE-generated recovery. Tests cover overlapping loans, cash assertions, duplicate records, and unsupported interest; missing terms remain unknown. | GRE-009, GRE-016 |
| **GRE-018 · E04 · ENG** — Deliver reviewed assessment and the Claim Passport | Present supported facts, uncertainty, evidence gaps, customer objectives, viable next routes, prerequisites, indicative effort/cost, and an exportable packet. Route deadline, identity, insolvency, rights, or eligibility issues for qualified review without inferring legal conclusions. The customer can choose assessment-only, assisted work, specialist help, or reasoned closure; weak evidence does not become a certified debt. | GRE-004, GRE-016, GRE-017 |
| **GRE-019 · E02 · ENG** — Operate the work queue and bounded service lifecycle | Give creditor and operator views a named next owner, reason, due/review time, approvals, cost/effort record, and status. Distinguish sent, delivered, accepted responsibility, partial response, and completed work. Handle owner absence, reassignment acknowledgement, silence, expiry, and handback. Import an existing plan or specialist matter at reviewed current state; do not replay historical actions or extend service indefinitely. | GRE-011, GRE-018 |
| **GRE-020 · E05 · ENG** — Implement scoped holds, complaints, and urgent review | Capture wrong-person reports, disputes, represented-party issues, hardship, threats/coercion, abuse concerns, and contact restrictions. Apply holds to affected actions and recheck them immediately before effects. Preserve permitted internal assessment and independent work. Support complaint acknowledgement, accountable review, correction, resolution, and controlled release of a hold; an internal timer cannot release it automatically. | GRE-012, GRE-019 |

### 3 — Borrower participation, agreement and repayment

Demonstrate the bilateral route with private disclosure and actual receipt/plan servicing. Implement with fakes/sandboxes until the live operating conditions are satisfied.

| Priority / item | Outcome and acceptance evidence | Depends on |
| --- | --- | --- |
| **GRE-021 · E05 · ENG** — Enable one supported contact route with accountable execution | Integrate the selected channel or record permitted external execution with approved exact content, identified actor, verified destination, scope, costs, and delivery/reply evidence. Handle failed delivery, duplicate callbacks, revocation before dispatch, and uncertain submission. Enforce contact preferences and applicable cadence. Attributed outside contact is distinguishable from a verified provider receipt; live enablement depends on GRE-043 and GRE-045. | GRE-004, GRE-012, GRE-019, GRE-020 |
| **GRE-022 · E05 · ENG** — Provide secure borrower access and disclosure | Provide expiring/revocable, appropriately verified access to the disclosed claim and approved evidence. Keep internal review and creditor negotiation limits private. Viewing or responding requires neither a debt admission, GRE payment, nor membership of the creditor organization. Test wrong-person and forwarded-link cases, credential/session expiry, field-level disclosure, and access revocation. | GRE-007, GRE-008, GRE-010, GRE-021 |
| **GRE-023 · E05 · ENG** — Handle borrower response and bilateral correction | Allow acknowledgement of all/part, gift or amount disputes, prior-payment evidence, hardship, missing terms, and alternative proposals. Preserve both accounts and reopen affected assessment/balance checks. Capture non-portal responses with source and recorder attribution. Silence or non-delivery never establishes intent, consent, or refusal. A correction updates the current view while preserving the original assertion. | GRE-017, GRE-020, GRE-022 |
| **GRE-024 · E06 · ENG** — Exchange versioned proposals and counteroffers | Support full/partial settlements, relationship-sensitive choices, concessions and installment proposals. Bind exact monetary/nonmonetary terms, private limits, expiry, and authority. Changed conditions are a counteroffer; changed facts invalidate affected approvals. Concurrent offers share commitment limits. Tests prove another party cannot see a private floor or commit using stale authority. | GRE-012, GRE-018, GRE-023 |
| **GRE-025 · E06 · ENG** — Record exact agreement acceptance and release conditions | Present the precise offered version and each party’s represented authority. Record supported portal/e-signature or reviewed external acceptance with provenance. Silence and qualified replies are not acceptance. Separate accepted terms, performance, and conditional release; preserve superseded offers and external status. Release/revival effects follow reviewed terms, never a payment-status toggle. | GRE-004, GRE-024 |
| **GRE-026 · E06 · ENG** — Provide verified creditor payment instructions | Implement an admitted hosted-link route or independently verified creditor/bank instructions, with provenance and review of changed destinations. Identify the recipient, currency, fees, and responsibility. Funds follow the creditor/bank/provider arrangement; GRE service billing is separate. Test stale or replaced instructions and unsupported provider/actor combinations using fakes or sandboxes. | GRE-004, GRE-025 |
| **GRE-027 · E06 · ENG** — Reconcile receipts, allocations, duplicates, and reversals | Record direct/off-platform and provider-reported payments as observations until source verification. Allocate once using external identity and aggregate limits; handle partial/unmatched cash, fees and corrections. A reversal appends evidence and reevaluates affected actions/obligations without automatically undoing a legal release. Prove a payment arriving before dispatch changes or stops the pending demand. | GRE-012, GRE-017, GRE-026 |
| **GRE-028 · E06 · ENG** — Service installment plans and renegotiation | Persist accepted schedules and observe actual receipts separately. Use Temporal waits for permitted reminders/reviews; check current plan, authority, balance, holds and service end before each action. Support missed installments, hardship pause, changed terms and reviewed imported plans. A signed or ongoing plan is not completed recovery. Tests include due-date/time-zone handling and restart without duplicate reminders. | GRE-012, GRE-019, GRE-025, GRE-027 |

### 4 — Complete domestic resolution and specialist fallback

Prove a complete domestic route, including accepted handoff or explicit unresolved closure, rather than counting an assessment or agreement as recovered cash.

| Priority / item | Outcome and acceptance evidence | Depends on |
| --- | --- | --- |
| **GRE-029 · E07 · ENG** — Arrange accepted specialist handoff | Match only eligible advertised routes, obtain quoted scope/cost, required creditor authorization, and explicit provider acceptance. Deliver the scoped Claim Passport securely with deadlines, outstanding issues, and ownership. Provider decline, unavailable capacity, or a changed quote returns a clear alternative/approval task. A referral sent is not a completed handoff. | GRE-004, GRE-018, GRE-020, GRE-025 |
| **GRE-030 · E07 · ENG** — Track specialist work, replacement, and return | Capture milestone/deadline/cost updates, complaints, requests, returned evidence, and responsibility changes through lightweight secure/manual exchange. Reconcile outstanding instructions before a replacement provider receives conflicting work. Missed updates and service expiry trigger a named owner and bounded disposition. Provider completion is a reported observation until required checks establish its effects. | GRE-019, GRE-029 |
| **GRE-031 · E07 · ENG** — Close service and case with an honest outcome record | Produce downloadable assertions/corrections, disputes, exact terms, observed receipts, balance, costs and closure/transfer reasons. Distinguish service completion, unpaid closure, paid obligations, release, and remaining monitoring/legal/administrative/retention duties. Assign surviving duties and allow reviewed reopening. Unknown or still-observed outcomes remain unknown/pending, not zero; closure cannot conceal another active service. | GRE-023, GRE-027, GRE-028, GRE-030 |
| **GRE-032 · E07 · QA** — Demonstrate the complete domestic journey and exceptions | Run synthetic acknowledged-loan, disputed-gift/amount, claimed-cash-payment, hardship, missing-terms/weak-evidence, third-party-recipient, and unreachable-borrower cases. Exercise self-service and attributed manual paths through assessment, response, agreement/plan, receipts, specialist fallback or reasoned closure. Verify mobile/keyboard usability, wrong-person handling, no forced admission, and honest completion evidence. | GRE-021, GRE-022, GRE-023, GRE-024, GRE-025, GRE-027, GRE-028, GRE-029, GRE-030, GRE-031 |

### 5 — Complete India–U.S. commercial recovery

Extend shared behavior for businesses, performance evidence, currencies and corridor duties. Both tracks remain required; this stage is not a future-release deferral.

| Priority / item | Outcome and acceptance evidence | Depends on |
| --- | --- | --- |
| **GRE-033 · E08 · ENG** — Implement India–U.S. commercial onboarding and claim intake | Support an Indian business directly or through an authorized operator, correct U.S. legal entity/trading name, rights/representation, invoices/contracts, performance/acceptance, currency, prior provider/settlement/proceeding, and customer objectives. Enable assisted commercial import with preview and duplicate checks. Unsupported claim/right structures are routed explicitly; the pilot does not become a cross-border personal-loan or remittance service. | GRE-007, GRE-009, GRE-010, GRE-014, GRE-018 |
| **GRE-034 · E08 · ENG** — Assess commercial obligations and choose a supported route | Extend the evidence timeline, amount reconciliation, and Passport for entity mismatch, missing performance evidence, commercial disputes, credits and partial payments. Record deadline/rights/insurance/insolvency review needs and source freshness. Present available U.S. execution routes, effort/cost and corridor prerequisites without assuming legal validity from an invoice or a registry match. | GRE-016, GRE-017, GRE-018, GRE-033 |
| **GRE-035 · E08 · ENG** — Reconcile cross-border receipts, FX, fees, and net proceeds | Preserve obligation currency, actual receipt currency, conversion source/date/rate, rounding, bank/provider fees, remittance evidence, and creditor net proceeds. Prevent mixed-currency addition and distinguish debtor payments from insurance/write-offs or other receipts. Source-reviewed manual reconciliation is supported. Test partial receipts, duplicate evidence, reversal, and a receipt differing from creditor net proceeds. | GRE-026, GRE-027, GRE-033 |
| **GRE-036 · E08 · ENG** — Coordinate commercial specialist work and residual duties | Extend agreements, plan servicing, provider handoff, cost/status returns, and closure to the commercial corridor. Assign qualified owners for applicable legal, bank/export, documentation, translation/certification, and monitoring duties. Track unsupported or pending requirements explicitly; payment or partner transfer does not erase them. Preserve existing representatives’ unresolved instructions. | GRE-028, GRE-029, GRE-030, GRE-031, GRE-034, GRE-035 |
| **GRE-037 · E08 · QA** — Demonstrate the complete commercial journey | Exercise clean commercial recovery, wrong-entity/performance dispute, prior settlement/provider involvement, partial and reversed payment, FX/fee differences, provider decline and unresolved administrative duties. Demonstrate onboarding through resolution/accepted handoff or reasoned closure with correct net proceeds. Re-run affected shared authorization and money scenarios to establish both tracks coexist. | GRE-032, GRE-033, GRE-034, GRE-035, GRE-036 |

### 6 — Assisted processing and live operating readiness

Validate bounded automation and finish privacy, deployment, partner and business operations. Start long-lead cloud/partner planning earlier when dependencies permit.

| Priority / item | Outcome and acceptance evidence | Depends on |
| --- | --- | --- |
| **GRE-038 · E09 · ENG** — Add reviewed document and AI assistance | Implement versioned task interfaces for selected OCR/extraction, summaries, issue finding and drafts using Azure Document Intelligence and the OpenAI SDK/Responses where selected. Resolve SDK/Pydantic compatibility and record model/prompt/schema/input references and cost. Outputs retain source/page links and remain proposed findings. Provide reviewed manual handling when a format or task is unsupported; live AI enablement requires GRE-039. | GRE-010, GRE-013, GRE-016, GRE-018, GRE-034 |
| **GRE-039 · E09 · QA** — Evaluate AI assistance and enforce its boundaries | Use representative synthetic/permitted examples from both tracks to assess extraction errors, contradiction handling, refusals, incomplete output, unsupported schemas, latency/cost, and reviewer effort. Test malicious instructions inside evidence: they cannot alter authority, recipients, secrets or tools. Decide data/retention settings and quality thresholds before real evidence use. Record whether each task meets them; an unready automation follows an explicit manual-route/scope record. | GRE-020, GRE-023, GRE-038 |
| **GRE-040 · E10 · ENG** — Complete privacy, retention, disclosure, and export operations | Implement versioned retention/deletion and permitted preservation holds across originals, derivatives, logs, model data and exports. Verify private borrower/creditor/partner views and download expiry. Provide customer access/correction/export and deletion-request handling with recorded disposition and owners. Account/tenant deletion cannot silently erase surviving obligations or improperly retain unrelated evidence. Define backup deletion/restore interaction for GRE-042. | GRE-007, GRE-010, GRE-011, GRE-022, GRE-031 |
| **GRE-041 · E10 · ENG** — Prepare costed staging and deployment infrastructure | Select supported regions/SKUs and production image architectures; estimate web/API/worker/database/storage/Temporal/identity/telemetry costs. Prepare Terraform, GitHub OIDC, scoped secrets/managed identities and separate staging/pilot resources. Provision under the authorization for that work. Verify staging builds, real Azure Blob identity/TLS, Clerk auth and Temporal worker connectivity/shutdown; local emulator results are not substituted. | GRE-006, GRE-007, GRE-012, GRE-013 |
| **GRE-042 · E10 · OPS** — Verify recovery, upgrades, release operations, and support | Exercise database/blob restore in isolation, migration upgrade/rollback or documented forward recovery, Temporal replay/versioning and graceful worker release. Test crash/timeout/duplicate callbacks and current-state rechecks using realistic fakes. Establish monitoring, retention-aware recovery, incident/complaint ownership, cost limits and rollback/runbooks. Document service/image upgrades and local emulator limitations, including root Azurite; prove the actual pilot deployment’s access boundaries. | GRE-009, GRE-012, GRE-013, GRE-028, GRE-040, GRE-041 |
| **GRE-043 · E02 · BUS** — Complete executable partner and service readiness | Secure the actual contracting arrangement, scoped professional review, eligible contact/payment/acceptance/specialist routes, data-use terms, provider acceptance process, response coverage and fallback. Establish named primary/backup owners and capacity for both tracks, published scope, fee/refund/support terms and update ownership. Mark each live capability enabled only for its supported configuration; missing coverage remains blocked, not a generic nationwide promise. | GRE-002, GRE-003, GRE-004, GRE-021, GRE-025, GRE-026, GRE-029, GRE-036, GRE-040 |
| **GRE-044 · E02 · ENG** — Record GRE fees, effort, and operating economics | Support the selected service billing/receipting route, including reviewed manual billing if viable, charges/refunds and outside costs. Keep GRE fees separate from creditor money and record founder/reviewer/support effort. Produce per-track conversion, revenue, cost and contribution records with defined attribution; historical receipts and open plans cannot inflate recovery or margin. | GRE-003, GRE-005, GRE-019, GRE-027, GRE-031, GRE-035 |

### 7 — Release rehearsal, real pilot and learning

Use permissioned cohorts and enabled routes only after the release conditions. Separate software correctness from observed customer value and economics.

| Priority / item | Outcome and acceptance evidence | Depends on |
| --- | --- | --- |
| **GRE-045 · E10 · QA** — Pass the two-track release and operating rehearsal | Run the critical scenario catalog against the release candidate and enabled sandbox routes with named operator/provider roles. Include tenant/private-context isolation, expired authority, changed payment before contact, duplicate/reversed cash, uncertain delivery, missed deadlines, provider replacement, restores and complaints. Verify accessible journeys, executable manual steps, pilot targets and support capacity. Record failures, restrictions and release evidence; unresolved critical failures block the affected live route. | GRE-005, GRE-032, GRE-037, GRE-039, GRE-040, GRE-042, GRE-043, GRE-044 |
| **GRE-046 · E02 · OPS** — Run invited domestic and commercial pilot cohorts | Recruit and onboard permissioned cases under the authorized outreach/service arrangements and actual capacity. Start domestic first, then commercial, while retaining both pilot commitments. Operate approved contact, review, partner and payment paths with monitoring and support. Observe actual customer/borrower participation and service effort; changes in scope/authority are recorded before dependent actions. | GRE-045 |
| **GRE-047 · E02 · BUS** — Evaluate customer value and economics separately by track | Report sample size, eligibility/conversion, time to useful assessment/action, operator/customer effort, disputes, accepted handoffs, verified receipts/net proceeds, open plans, complaints, cost and repeat intent over the defined window. Separate synthetic tests, historical cash and pilot observations. Unfinished or missing outcomes remain explicit; claim no causal lift or reliable recovery probability from this pilot alone. | GRE-046 |
| **GRE-048 · E01 · DOC** — Record the pilot decision and subsequent deliverables | Record continue/adjust/stop findings for each track, evidence supporting them, remaining duties, and the next prioritized release. Update the future register for changes with reason, customer impact, interim route/owner, dependencies and reconsideration trigger. A pilot ending does not end active customer or provider obligations. Preserve every deferred delivery/business requirement and excluded strategic boundary. | GRE-047 |

## 4. Completion conditions and documents before coding

A delivery item is complete when its stated behavior is implemented or its agreed operating deliverable exists, the focused checks have passed, the diff/record is reviewed, and the relevant guide/contract/source links are current. A package install, mocked response, provider inquiry or task assignment alone is insufficient. Claims about verification identify the environment and actual evidence.

GRE-001 prepares the following documents at the level needed for the first implementation work. Later stories extend them before their own dependent changes:

| Deliverable | Required content |
| --- | --- |
| Reconciled documents 01–05 | Both customer models and journeys, scope/current status, authority and service roles, informal evidence, money/acceptance semantics and selected-contract changes; preserve earlier useful reasoning and reference history. |
| Architecture decision records | Package and deployment boundaries, identity versus case authority, PostgreSQL transaction/RLS approach, outbox and Temporal responsibilities, Blob/provider interfaces, and the TypeScript compatibility decision. |
| Journey/interaction and acceptance catalog | Creditor, operator, borrower and specialist responsibilities; the exception matrix below; private versus disclosed data; meaningful waiting, partial-response and completion states. |
| First implementation design note | GRE-006’s file/package changes, exact commands, fixture-to-product transition, CI environment, dependencies and acceptance evidence. Subsequent items get their own bounded note before coding. |
| Operating/decision register | Unresolved actor/coverage/pricing/provider questions, owner, evidence needed, dependency and review point; scope/contract decisions remain explicit until settled. |

Technical criteria needed before live use are enforced in the relevant items, with a combined rehearsal in GRE-045. In particular: permitted data handling before real evidence; eligible actor/channel and current mandate before external contact; verified destinations and provider admission before payment activity; exact authority/terms before binding acceptance; qualified owners and accepted scope before specialist handoff. Full pilot evaluation follows both complete journeys.

Document review and integration of the Git branches precede product implementation. Setup PR #1 remains a draft. This backlog is proposed on a separate documentation branch based on the verified setup commit; it does not merge the setup branch or authorize production deployment/outreach.

## 5. Representative acceptance cases

These are synthetic design/validation examples, not claims of legal enforceability or recovered money. Each must produce a useful outcome, including supported unresolved closure where appropriate.

| Case / failure | Required result | Primary items |
| --- | --- | --- |
| Acknowledged personal loan, repeated promises, part payment | Reconstruct history, reconcile prior cash, seek exact terms and track actual remaining receipts without double counting. | GRE-015, GRE-017, GRE-025, GRE-027, GRE-028, GRE-032 |
| “It was a gift,” no written terms, cash repayment, or third-party recipient | Preserve both accounts and gaps; separate transfer from obligation; no invented date/interest/admission; scoped review or reasoned closure. | GRE-015, GRE-016, GRE-017, GRE-018, GRE-023, GRE-032 |
| Hardship, unreachable borrower, or unsupported geography | Offer permitted response/plan/alternative; distinguish failed delivery and silence; retain owner and bounded next step. | GRE-014, GRE-019, GRE-020, GRE-021, GRE-023, GRE-028, GRE-031 |
| Wrong person, shared link, revoked mandate, private negotiation floor | Deny improper access and suppress affected effects without disclosing private restrictions; preserve required history. | GRE-007, GRE-012, GRE-020, GRE-022, GRE-024, GRE-040 |
| Payment after approval but before dispatch; callback timeout or duplicate | Recheck current balance/authority; cancel or revise stale demand; reconcile uncertain submission and allocate once. | GRE-012, GRE-021, GRE-027, GRE-028, GRE-045 |
| Conditional acceptance, concurrent concessions, reversal after release | Preserve exact offered/accepted versions, enforce shared limits and evaluate release effects separately from payment reversal. | GRE-017, GRE-024, GRE-025, GRE-027, GRE-031 |
| Provider declines, changes quote, stops responding, or is replaced | No false accepted handoff; route approval/alternative and reconcile unresolved instructions with named ownership. | GRE-019, GRE-029, GRE-030, GRE-036, GRE-043 |
| Commercial entity mismatch or disputed invoice performance | Retain claim assertion, require relevant evidence/review, and limit affected contact until readiness is established. | GRE-033, GRE-034, GRE-037 |
| Cross-border partial receipt, FX/fees, prior settlement/provider | Keep source currencies, creditor net and prior history distinct; no mixed-currency addition or replay of old work. | GRE-033, GRE-035, GRE-036, GRE-037 |
| Agreement fulfilled but bank/legal/monitoring duties remain | Assign residual duties and distinguish service, cash and legal completion; unknown outcomes remain explicit. | GRE-028, GRE-031, GRE-036, GRE-047 |
| Instructions inside evidence or an unsupported AI response | Treat evidence as data; preserve source/proposed findings and require reviewed action controls. | GRE-010, GRE-012, GRE-038, GRE-039 |
| Service/process restart, deployment change, or restored data | Recover recorded work without duplicate effects; honor current authority and document limits/remaining reconciliation. | GRE-006, GRE-012, GRE-028, GRE-042, GRE-045 |

The applicable original scenarios in [workflow document 04, §13](04-workflow-interaction-specification.md#13-acceptance-scenarios-for-the-specification) remain acceptance inputs. Bulk, public API, ERP writeback and external-agent breadth are retained in the future register; their shared retry, ownership and authority principles still apply to pilot actions.

## 6. Coverage of the brief and verified-stack gaps

| Required pilot capability / business dependency | Backlog coverage |
| --- | --- |
| Acquisition and suitability | GRE-002, GRE-003, GRE-005, GRE-014, GRE-046 |
| Creditor onboarding and resumable/current-state intake | GRE-007, GRE-009, GRE-015, GRE-019, GRE-033 |
| Evidence reconstruction and exportable Claim Passport | GRE-010, GRE-016, GRE-018, GRE-034, GRE-038, GRE-039 |
| Claim and balance assessment | GRE-017, GRE-018, GRE-023, GRE-034, GRE-035 |
| Case workspace and coordination | GRE-008, GRE-011, GRE-012, GRE-019, GRE-020 |
| Supported contact and borrower response | GRE-021, GRE-022, GRE-023 |
| Negotiation and agreements | GRE-024, GRE-025, GRE-036 |
| Plans and actual payments | GRE-026, GRE-027, GRE-028, GRE-035 |
| Specialist assistance | GRE-004, GRE-029, GRE-030, GRE-036, GRE-043 |
| Completion and customer records | GRE-031, GRE-036, GRE-040, GRE-047 |
| Trust, support and operating reliability | GRE-007, GRE-010, GRE-012, GRE-013, GRE-020, GRE-040, GRE-042, GRE-045 |
| Service responsibility and coverage | GRE-002, GRE-004, GRE-020, GRE-043 |
| Deliverable commercial offer and fees | GRE-003, GRE-014, GRE-044 |
| Real execution/support capacity | GRE-004, GRE-019, GRE-029, GRE-030, GRE-042, GRE-043 |
| Pilot recruitment, value and economics | GRE-005, GRE-044, GRE-046, GRE-047, GRE-048 |

Every required-later-work row in [document 10](10-dependency-baseline.md#required-later-work) has a delivery owner through the mapping below. Installation of a library remains distinct from validation of the dependent live capability.

| Retained implementation or setup requirement | Destination and practical limit |
| --- | --- |
| Domain/API, exact money, migrations, roles/RLS and case authority | GRE-007, GRE-009, GRE-011, GRE-017, GRE-027, GRE-042 |
| Temporal domain workers, retry/replay, current-state effects and callbacks | GRE-012, GRE-021, GRE-028, GRE-042 |
| Blob adapter, OCR, real cloud identity/TLS, retention and restore | GRE-010, GRE-038, GRE-039, GRE-040, GRE-041, GRE-042 |
| Clerk packages and real web/API auth integration | GRE-007, GRE-022, GRE-041 |
| OpenAI SDK, Responses, model/data settings and task evaluations | GRE-038, GRE-039 |
| Web components, Tailwind/shadcn, query state, caching and browser checks | GRE-008 and the journey stories; GRE-032, GRE-037, GRE-045 |
| Contact/payment/e-signature/specialist fakes and executable routes | GRE-004, GRE-012, GRE-021, GRE-025, GRE-026, GRE-029, GRE-043 |
| Python/web quality tooling, CI and generated-client drift | GRE-006 and each changed behavior’s focused checks; GRE-045 |
| Costed cloud infrastructure, deployment, secrets, telemetry and incidents | GRE-003, GRE-013, GRE-041, GRE-042, GRE-044 |
| Recreated-editor attachment; version-only pins on PostgreSQL/base images | GRE-006: document/verify repeatable startup and pin policy, preserving local data. Automate attachment only after validating the correct checkout/container. |
| Retained Temporal receipt can outlive server history | GRE-006: separate historical evidence from repeatable health/CI checks; do not mistake history retention for service failure or hide genuine errors. |
| Azurite runs as root; Temporal UI bridge permits egress | GRE-042: retain local limits, assess any needed service hardening, and validate the actual hosted environment independently. |
| TypeScript 7 compiler-API failure with current Hey API | GRE-006: retain the tested 6.0.3 pin and rerun generation, live client, type and build checks for coordinated upgrades. |
| Backups/restores, upgrades and production behavior unverified | GRE-042 and GRE-045; required pilot recovery/operation work remains in this release, not merely F-P16 future scale. |

## 7. Manual delivery, future depth and scope changes

Manual handling is part of the pilot only when it has a supported scope, named accountable owner/executor, authorized inputs/disclosures, expected response window, recorded result and measured effort. A missing provider or unsupported action is not a manual implementation.

| Permitted pilot route | Record required | Items / later depth |
| --- | --- | --- |
| Reviewed transcription/translation, evidence reconstruction and assessment | Originals, recorder/reviewer, source links, uncertainty, quality/effort and explicit assessment limits | GRE-016, GRE-018, GRE-034, GRE-038; richer automation/data/languages remain F-P08/F-P12 |
| Authorized external contact and non-portal responses | Actor, exact content, destination, mandate, delivery/reply evidence and scoped follow-up | GRE-021, GRE-023; more channels/automation remain F-P07 |
| Reviewed external agreement acceptance | Exact term version, each party’s authority, acceptance evidence and conditions | GRE-025; deeper legal instruments remain F-P10 |
| Verified creditor instructions and source-reviewed receipts/FX | Destination verification, original receipt/currency/fees, allocation reviewer and reconciliation status | GRE-026, GRE-027, GRE-035; broader bank/payment automation remains F-P11 |
| Lightweight specialist packet and manual progress exchange | Quoted scope/cost, customer authorization, eligible provider acceptance, deadlines/owner and returned outcome | GRE-029, GRE-030, GRE-036; portals/network depth remain F-P06/F-P10/F-B04 |
| Defined service billing and support records | Agreed fees/refunds, service work, outside costs, support/incident responsibility and receipts | GRE-003, GRE-042, GRE-044; scaled packaging remains F-B02 |

**No pilot deliverable is deferred by this draft.** Bounded document/AI assistance is scheduled within the existing pilot/stack direction; richer automation remains future scope. If a planned capability cannot be delivered, first record the impact and the supported manual/partner replacement where allowed. If the customer promise can no longer be met, revise the pilot explicitly.

[Document 07](07-future-development-and-business-deliverables.md) remains the authoritative register for **16 product/technology candidates (F-P01–F-P16), seven business candidates (F-B01–F-B07), and five strategic boundaries (X01–X05)**. This backlog does not schedule them all or convert candidates into commitments. Broader jurisdictions/corridors, claims, connectors, public APIs, enterprise portals, channels, prediction, autonomous agents, benchmarking, policy-platform breadth, scale/assurance and expanded business models retain their recorded conditions. Necessary pilot controls, actual partner coverage and viable service economics remain in the numbered items above.

Any later scope record must include: affected item/future ID, decision/date, rationale, customer impact, interim route and named owner, dependencies, acceptance evidence, and condition for reconsideration. Preserve excluded practices and separate-business boundaries. Update both the affected pilot item and the future register so work cannot silently disappear.

## 8. Review and next action

Review the proposed order, the complete-path acceptance cases, and the live/manual responsibilities. Material changes should update dependencies and the capability coverage matrix together.

Then complete GRE-001, reconcile documents 01–05 and prepare the delivery records before GRE-006 product-foundation implementation. Business decisions GRE-002–GRE-005 can start alongside document preparation. This document creates no customer feature, migration, provider account, live contact, payment, or deployment.

**Source basis:** [pilot brief 06](06-pilot-mvp-brief.md), [future register 07](07-future-development-and-business-deliverables.md), [stack 08](08-stack-and-environment-decision.md), [environment 09](09-development-environment.md), [baseline 10](10-dependency-baseline.md), [operating model 03](03-operating-model.md), [workflow 04](04-workflow-interaction-specification.md), [domain contracts 05](05-domain-data-contracts.md), and the user’s two-track/pilot/sequence decisions. This is delivery planning from those sources; jurisdiction, pricing and vendor admission are work items for their designated review, not newly verified legal or commercial conclusions.
