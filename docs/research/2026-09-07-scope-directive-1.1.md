# Historical research source — scope directive revision1.1

**Status: historical, superseded for release scope and implementation instructions.** The owner's later decision selects one Pilot: Foundation + Trade. Private and Consumer are future development. [Current decisions](../12-scope-decisions-and-reconciliation.md), [Pilot](../06-pilot-brief.md) and [backlog](../11-prioritized-pilot-backlog.md) govern development.

The source below is retained for research and decision provenance. Its concurrent two-lane launch, old PR status and instructions to update project files are historical statements. They are not active agent instructions. External research is dated and requires the applicable current review before use.

Source SHA-256: `f3e5927a85448dd8b5154e09f33283009cb621677607e2ff024bd64acfe82923`.

The source content below is preserved with trailing whitespace normalized; the source SHA identifies the received file before that formatting change.

---

# GRE Primary Scope-Change Directive

## Product portfolio, legal perimeter, operating model, and near-term market-leadership strategy

**Prepared:** September 7, 2026

**Revision:** 1.1 — implementation-readiness review, September 7, 2026

**Status:** Reviewed scope-change direction; existing project artifacts still await coordinated reconciliation

**Applies to:** The GRE business definition, product strategy, operating model, workflows, domain/data contracts, machine-readable schemas, fixtures, tests, pilot brief, and future-development plan

**Does not do:** Amend other project files, certify legal compliance, reset the selected stack or verified environment, or claim that any designed service is commercially available

**Read first:** This revision preserves the portfolio and launch priorities in the supplied directive. It corrects the current-project baseline and a withdrawn legal citation; distinguishes commercial packaging from matter classification; retains useful private assessment when the other person never joins; repairs handoff, payment, closure, and privacy semantics; and adds a modular reuse map and document-first reconciliation plan in Sections 9.7 and 10.2–10.4. The material change record is in Section 16.

The launch posture is a substantive change from the previous pilot: Trade becomes the primary revenue lane; U.S. private-loan assistance becomes bounded preparation and voluntary resolution; institutional Consumer remains a gated expansion. The previous promise of an actively managed recovery journey is being narrowed. These tradeoffs must be stated in the revised pilot brief and tested with customers, not hidden behind new product names.

---

## 1. Instructions to the receiving GPT

Use this document as the authoritative direction for the next coordinated update of the GRE project. Do not copy it wholesale into every project file. Interpret it, inspect the complete project, and propagate each decision into the document or contract that owns that subject.

Do not reuse old offering descriptions word for word merely for continuity. Rewrite the commercial scope from the decisions in this directive while preserving validated operating/data invariants and provenance. Likewise, do not copy research prose into schemas or contracts; translate it into the correct definitions, states, controls, tests, and unresolved-review records.

The original documents 01–05 and contract reference retain a B2B/operator emphasis. The later pilot brief and backlog already add domestic U.S. personal/friend loans alongside India-origin B2B recovery. The project also has a selected stack direction and a verified development environment. This directive changes the portfolio, buyer priority, service promise, and execution boundaries; it does not erase those later decisions or require setup to start again. Section 10.2 records the inspected repository baseline.

When reviewing existing material, assign each substantive statement one disposition:

- `KEEP` — universal and still correct;
- `GENERALIZE` — useful, but written too narrowly for B2B or one corridor;
- `MOVE_TO_FAMILY_PROFILE` — valid only for a product family;
- `MOVE_TO_CORRIDOR_PACK` — valid only for a particular directional corridor or effective period;
- `REPLACE` — conflicts with this directive;
- `DEPRECATE` — exploratory language or a business model no longer in scope.

Add either or both review flags where applicable; these accompany a disposition rather than replacing it:

- `NEEDS_COUNSEL` — a legal proposition or operating permission requiring qualified review;
- `NEEDS_VALIDATION` — a market, pricing, performance, or customer assumption not yet proved.

Do not silently merge contradictions. Record the resolution and update every affected reference, including schemas, fixtures, and tests. Preserve stable filenames unless the project owner directs otherwise. If a breaking contract change is required, create a new contract version and migration note; do not reinterpret version `0.1.0` in place.

This directive has priority over older statements concerning:

- a single B2B product;
- a Trade-only pilot that omits the separately bounded domestic U.S. private-loan scenario;
- India-origin claims against U.S. businesses as a committed launch scope;
- collection agencies as the default economic buyer;
- GRE operating the complete post-placement collection lifecycle;
- Intelligence, Operations, Network, and Control as the four customer-facing product families;
- Private Resolution as an ungated copy of institutional collections or as an undefined distant backlog item;
- cross-border coverage as a general feature rather than a versioned directional corridor;
- “pre-collection” as a meaningful legal category;
- graph, agentic, blockchain, or generic AI language as the core strategic advantage.

Existing evidence, authority, service-scope, financial, event, outcome, and prepare/commit rules should be retained unless a genuine conflict is identified. They are valuable foundations, not reasons to preserve the old packaging.

Before editing, inventory the entire current project. At minimum, reconcile:

- `01-business-project-overview.md`;
- `02-product-offering-competitive-strategy.md`;
- `03-operating-model.md`;
- `04-workflow-interaction-specification.md`;
- `05-domain-data-contracts.md`;
- `recovery-contracts.zip` and its schema, fixture, validator, and tests;
- any pilot/MVP, future-development, capability-map, legal-research, or delivery-plan files that are present.

The output of the update conversation should include the updated artifacts, a cross-file change matrix, validation results, and a short register of unresolved owner, counsel, and market decisions.

For the present review, the deliverable is this revised directive and its reconciliation plan. The next coordinated pass updates project documents and reference contracts first; the backlog is then revised from that consistent baseline, before product implementation. A requirement belongs in one owning artifact and is referenced elsewhere. Older backlog IDs and completed setup evidence must remain traceable.

---

## 2. Executive decision

GRE is no longer one universal recovery product. It is one shared recovery-continuity platform supporting distinct product families with different buyers, promises, permissions, risk profiles, workflows, contracts, and economics.

The umbrella category is:

> **Recovery continuity infrastructure:** a system that turns fragmented evidence, rights, authority, and policy into a portable Claim Passport; enables a creditor to appoint independently accountable executors; and preserves creditor control, context, and trustworthy observations when a matter crosses teams, providers, systems, or borders.

A concise positioning direction is:

> **One claim record. Independent execution. Continuous creditor control.**

This is a positioning hypothesis, not a trademark decision or an established market claim.

For a buyer who does not yet know the category, use a plainer benefit statement before the category language:

> **Make a recovery case provider-ready, activate the right independent executor, and switch without starting over.**

These creditor-control messages describe the enterprise offerings. Private Resolution needs its own promise: **Understand the disagreement, choose what to share, and agree voluntarily—or leave with a clear record.** Paying for or initiating a private matter does not give one participant control over the other's record, choices, or confidential information.

Do not describe GRE as an “AI collection agency.” The company should eventually be recognizable as the **recovery continuity network** between creditor systems and independently accountable recovery providers. “Network” becomes a defensible category claim only after more than one independent provider accepts and returns the same GRE contracts in real work.

### 2.1 Portfolio architecture

GRE will have three vertical product families and one horizontal, separately sellable network family, all built on one GRE Foundation:

1. **GRE Trade & Receivables**
2. **GRE Consumer Credit Infrastructure**
3. **GRE Private Resolution**
4. **GRE Recovery Network & Control**
5. **GRE Foundation**, shared by all four

These are canonical scope names, not final trademarks. Short navigation or campaign labels may later be tested—such as **GRE Trade**, **GRE Credit Continuity**, **GRE Resolve**, and **GRE Control Network**—but branding must not hide the legal family, released corridor, or actual operator.

The commercial product is composed as:

> **GRE Foundation + Matter Family Profile + Corridor Pack + Service Mode + Executor/Authority Pattern**, made available through separately declared **commercial offering/edition entitlements**.

The matter family is Trade, Consumer Credit, or Private Resolution. Recovery Network & Control is a horizontal commercial offering that composes relevant Foundation modules; it is not a fourth legal classification or a second copy of those modules. A standalone Network customer still needs a permitted matter family, corridor, service mode, and actor. An edition purchase never enables an unreleased Consumer or Private activity.

For example:

- Foundation + Trade & Receivables + India-creditor/U.S.-business-obligor corridor + `ASSESS/PREPARE/TRANSFER` + independent U.S. agency;
- Foundation + Consumer Credit Infrastructure + U.S.-origin account/India-resident borrower corridor + `CONTROL/OBSERVE` + creditor-appointed eligible provider;
- Foundation + Private Resolution + supported domestic corridor + `ASSESS/PREPARE`, then `RESOLVE` only when parties voluntarily participate, with separately scoped qualified routes where supported.

### 2.2 Decisions, recommendations, and gates

| Status | Direction |
|---|---|
| **Adopted** | Use one shared foundation with separate family profiles. Do not force all segments through one universal customer journey or contract. |
| **Adopted** | Treat the four old layers—Intelligence, Operations, Network, and Control—as capability domains inside the platform, not as the new top-level product families. |
| **Adopted** | Use a hard operational handoff whenever an independent agency or law firm begins collection work, while maintaining a continuous creditor-side data and control experience. |
| **Adopted launch architecture** | Use one coordinated entry program with two deliberately unequal proof lanes: an enterprise Trade revenue/credibility lane and a tightly bounded U.S. domestic Private Resolution beta. They share Foundation contracts but have separate terms, safety controls, metrics, support, release gates, and public claims. Do not present this as four products launching at once. |
| **Commercial launch default** | Lead enterprise selling with Trade & Receivables plus the creditor-facing and provider-facing portions of Recovery Network & Control. Start with bring-your-own-agency or an approved creditor panel, not an open marketplace. |
| **Recommended initial buyer** | Make the creditor, rights holder, servicer, or portfolio owner the primary economic buyer. Treat agencies, law firms, and other executors as essential users and integration partners, but do not make their incentives the sole product compass. |
| **Recommended enterprise wedge** | Validate an India-to-U.S. commercial receivables corridor because it matches current project assets, but treat it as a candidate beachhead requiring buyer, provider, case-frequency, and willingness-to-pay evidence—not as established product-market fit or global availability. |
| **Controlled domestic proof lane** | Validate Private Resolution on existing, privately originated U.S. obligations through an invite-only or partner-distributed beta. It is a voluntary clarification and agreement room—not loan origination, institutional servicing, unilateral collections, public accusations, or a payment intermediary. |
| **Designed now; launch gated** | Build Consumer Credit concepts into the common model, but do not launch live consumer communications without a regulated design partner, current corridor counsel, security readiness, and clear role classification. |
| **Excluded baseline** | GRE does not buy debt, own claims, finance portfolios, securitize obligations, originate loans, provide general credit scoring, act as the principal collection agency, practice law, adjudicate disputes, operate an owned field-enforcement workforce, or hold/commingle recovered funds. |
| **Excluded baseline** | GRE does not furnish information to credit bureaus, operate as a consumer-reporting agency, or obtain/use consumer reports unless a separately reviewed product later establishes a lawful purpose, role, process, and control set. |
| **Excluded baseline** | No pay-to-rank provider placement, hidden referral bias, public shaming, contact scraping, coercive tactics, autonomous legal representation, or unsupported autonomous material actions. |
| **Reserved strategic option** | If repeated target-buyer evidence shows that a one-stop managed service is essential, separately evaluate a properly licensed, insured, staffed, and potentially ring-fenced managed-execution structure or a disclosed qualified-prime partner. This is not part of the launch, and it cannot be simulated through labels or indemnities. |
| **Interoperability strategy** | Build bilateral acceptance first. After at least two independent providers have reused the same core profile in production-like work, publish a minimal Claim Passport core and conformance kit if doing so accelerates adoption. Keep corridor packs, integrations, assurance operations, and decision/outcome products proprietary unless a later governance decision changes that. |
| **Technology restraint** | A graph-shaped domain model does not require a graph database. Do not add blockchain, tokenization, microservices, distributed event sourcing, an agent per object, or a proprietary foundation model without a measured requirement. |
| **Entity-structure gate** | Separate products contractually, operationally, and in insurance/compliance controls now. Consider separate legal entities later only if licensing, capital, insurance, tax, or counsel analysis supports it. Product naming alone does not ring-fence liability. |

### 2.3 Launch portfolio truth

The launch must be broad enough to demonstrate the umbrella and narrow enough to be credible for a founder-led company:

| Lane | Purpose | Initial scope | Commercial/public posture |
|---|---|---|---|
| **A — Enterprise proof and revenue** | Prove that GRE lowers the cost and friction of activating and governing independent recovery providers | Trade Claim Readiness + provider preflight + direct transfer + creditor control for one validated commercial profile, initially testing India-creditor/U.S.-business-obligor eligibility and demand | Paid design partnership or pilot after release; the primary sales motion |
| **B — Product visibility and trust** | Demonstrate two-sided issue clarity, exact-term agreement, and safe self-service on the same evidence/authority foundation | Existing, privately originated U.S. friend/family loans and similarly bounded obligations; voluntary verified participation; no GRE funds or collection pressure | Small closed beta through a trusted channel; a learning and brand proof, not the main revenue forecast |
| **C — Strategic enterprise expansion** | Establish the differentiated consumer-mobility design without prematurely operating regulated collections | U.S.-origin consumer account with an India-resident borrower; account/dispute/preference continuity and provider-control concepts | Design-partner discovery and shadow testing only until the institutional release gate is met |

The public story may show all three horizons, but each label must follow actual release evidence: **planned pilot/beta**, **available pilot**, **controlled beta**, or **design/shadow program**, as applicable. A visually impressive demonstration is not commercial availability. The lanes may open at different times; a combined public demonstration is not a dependency for an otherwise qualified private pilot.

---

## 3. Shared GRE Foundation

The Foundation is the common system of meaning, control, security, and interoperability. It should be implemented initially as a modular application with strict module boundaries, not as four codebases or an early distributed architecture.

Separate product development through **profiles, modules, release manifests, permissions, fixtures, evaluation suites, terms, support ownership, and release gates**. Each family can move from `DESIGNED` to `PILOT_ENABLED` independently and may depend on a declared Foundation contract version. A Foundation deployment or schema update must never make an unreleased family, corridor, or service mode operational by implication.

### 3.1 Foundation domains

| Foundation domain | Required meaning |
|---|---|
| **Party and identity** | Legal persons, natural persons, organizations, representatives, verified attributes, role assertions, and source provenance. A role label never creates authority. |
| **Obligation and financial position** | What is asserted to be owed, by whom, for what purpose, in which currency, with credits, payments, releases, reversals, and uncertainty kept distinct. |
| **Evidence and Claim Passport** | Original and derived artifacts, propositions, supporting and contrary evidence, verification scope, gaps, versioning, privilege/confidentiality treatment, corrections, and purpose-specific readiness. Integrity is not proof of truth or enforceability. |
| **Rights and authority** | Ownership, servicing, assignment, representation, mandates, settlement limits, revocation, expiry, and exact action bindings. |
| **Case and service scope** | A continuing case separated from each bounded service request, responsible actor, deliverable, fee/cap, start/end condition, and surviving duty. |
| **Classification** | Creditor type, obligated-party type, obligation purpose, account/claim type, ownership/servicing posture, locations, governing law/forum, requested acts, compensation, and executor. |
| **Corridor and policy assurance** | Effective-dated, source-linked rules and operational constraints for the exact directional scenario, with review ownership, change-impact analysis, affected-case identification, and regression tests. |
| **Decision and route economics** | Eligible alternatives, prerequisites, cost, time, uncertainty, net-value scenarios, abstention, and reasons to request more information or stop. |
| **Action control** | Prepare/commit separation, current authority, policy decision, exact content/terms, approval or bounded delegation, dispatch identity, receipt, failure, retry, and cancellation semantics. |
| **Provider interoperability** | Eligibility before ranking, credentials, conflicts, capacity, direct appointment, provider-specific acceptance profiles, scoped disclosure, handoff manifest, acceptance/rejection, exceptions, returned events, and revocation. |
| **Payment and reconciliation** | Payment instructions and observations through authorized institutions, with no implied custody, trusted source checks, allocation, reversals, and remaining balance. |
| **Events and outcomes** | Recorded-time and valid-time history, source, attribution limits, observation horizon, unknown/pending/censored states, cost, result, and closure reason. |
| **Privacy, security, and AI assurance** | Purpose limitation, tenant and participant isolation, retention, redaction, incident handling, model execution records, evaluation, human review, and data-use permissions. |

### 3.2 Claim Passport direction

Retain **Claim Passport** as the canonical portable artifact, with a stable core and family-specific profiles. Do not rename it merely because a consumer obligation may be account-based or a private dispute may be informal. User-facing labels may vary, but the interoperable core should remain consistent.

The Claim Passport should become GRE's most important external contract:

- canonical machine-readable schema;
- human-readable evidence and limitation summary;
- version, authorship, and provenance rules;
- obligation, rights, authority, and consent manifests;
- disclosed disputes, contradictions, and missing items;
- corrections and superseded assertions without erasing the prior record;
- privilege, confidentiality, trade-secret, and sensitive-data labels that affect review and disclosure;
- purpose-specific readiness rather than one universal “verified” status;
- disclosure/redaction manifest;
- provider acceptance conditions and validation delta;
- normalized event, cost, and outcome return contract;
- exportability without mandatory platform lock-in.

Start through bilateral integrations and conformance tooling. Do not claim an industry standard until independent parties repeatedly accept and reuse it.

A Passport is a versioned, purpose-scoped view of canonical records, not another editable ledger or a universal database of alleged debtors. A common format does not require GRE to store every source document: customer-controlled storage and scoped references remain options when the applicable role or data rules require them. No cross-tenant identity matching, duplicate-case discovery, or shared debtor index is implied. Corrections propagate only to identified permitted recipients; an exported copy cannot be remotely erased merely by revoking GRE access.

Preserve correction lineage and audit meaning under the applicable retention and legal-hold policy. Do not turn “immutable” into indefinite retention of personal data. Disclosure snapshots and audit records need explicit expiry, deletion/redaction handling, and a limited record of what changed where lawful. Revocation, deletion, correction, and recipient retention obligations are separate operations.

### 3.3 Core terminology

Use neutral core terms and family-specific display language:

| Core concept | Trade display | Consumer display | Private display |
|---|---|---|---|
| `obligated_party` | Business debtor / customer | Borrower / consumer | Responding participant / alleged borrower |
| `claimant_or_rights_holder` | Creditor / supplier / exporter | Lender / owner / servicer | Requesting participant / alleged creditor |
| `obligation` | Invoice or commercial receivable | Account or consumer debt | Alleged private obligation |
| `issue` | Commercial dispute | Dispute, hardship, complaint, or servicing issue | Point of agreement or disagreement |

Do not use “borrower” for every claim, and do not let a B2B/B2C label substitute for the underlying classification.

### 3.4 The six compounding platform contracts

These are the product objects that should make GRE harder to replace over time. They are more important than any single user interface or model:

These are external or domain contracts with different owners and lifecycles, not an instruction to create six new databases, services, or independent sources of truth. Section 9.7 maps them to the existing reference records.

| Contract | What it does | Why it compounds |
|---|---|---|
| **Claim Passport** | Carries the source-linked obligation, evidence, uncertainty, rights, authority, disputes, corrections, and disclosure manifest | Each accepted profile reduces reconstruction across creditors and providers |
| **Provider Acceptance Profile** | States a provider's supported case classes, jurisdictions, evidence/data requirements, exclusions, fees, capacity, credentials, validation steps, input formats, and returned events | Converts vague “network coverage” into testable readiness and makes provider preflight useful to both sides |
| **Authority Envelope** | Binds the principal, executor, permitted acts, settlement/budget limits, expiry, revocation, and exact decision provenance | Makes direct appointment and bounded machine assistance safer and portable |
| **Corridor Pack** | Binds a family, direction, actors, activities, data/payment paths, effective rules, counsel conditions, release status, and regression cases | Turns legal and operational change into a maintained product rather than a memo |
| **Action Receipt** | Records who proposed, reviewed, approved, transmitted, performed, observed, failed, canceled, or corrected a material action | Gives creditors and providers an evidence trail without pretending GRE performed the provider's work |
| **Resolution Quality Scorecard** | Preserves net economics, elapsed time, rework/errors, disputes/complaints, reversals, durable agreements, data coverage, and continuity/switch performance as separate dimensions | Enables context-correct learning without reducing quality to gross dollars or an opaque rank |

The Provider Acceptance Profile is a first-class contract, not a checklist buried in an integration. A transfer is “provider-ready” only for a named profile version. A provider remains responsible for its independent validation and may return a structured delta. “No re-intake” is an aspirational service level that GRE may claim only after data shows a provider normally needs no information beyond the declared delta.

### 3.5 Staged openness and standard leadership

Do not confuse publishing a schema with establishing a standard. Use this sequence:

1. **Bilateral proof:** maintain GRE-owned Passport/core profiles and integration mappings, alongside provider-authored or explicitly provider-approved Acceptance Profiles; obtain real acceptance from selected providers. GRE technical maintenance must not silently change a provider's declared requirements.
2. **Portable core:** after at least two independent providers reuse the same core, publish a small, privacy-conscious Claim Passport core plus examples, versioning rules, and a conformance harness if the adoption benefit exceeds the copying risk.
3. **Ecosystem extensions:** allow family, corridor, and provider extensions without corrupting the core; publish compatibility and deprecation rules.
4. **Neutral governance option:** consider an external working group only when multiple creditors and providers will contribute implementation effort and governance. Do not surrender differentiation merely to call GRE an open standard.

The likely open layer is shared syntax and conformance. GRE's likely proprietary advantage remains the maintained mappings, corridor assurance, provider integrations, workflow, permissioned observations, evaluation data, and operational trust.

---

## 4. Product families

| Family | Economic buyer/user | Core job | Who performs recovery/resolution acts | Initial maturity target | Baseline exposure posture |
|---|---|---|---|---|---|
| **Trade & Receivables** | Creditor, insurer, factor, servicer, or embedded trade/AR channel | Make complex commercial claims ready, routable, accepted, and portable | Creditor first-party team or directly appointed agency/law firm | Paid enterprise pilot | Moderate but corridor/activity dependent; commercial status is not a universal exemption |
| **Consumer Credit Infrastructure** | Regulated lender, servicer, or debt owner | Preserve account, policy, dispute, preference, and provider continuity as a borrower/account moves | Creditor or directly appointed qualified provider | Design/shadow program | Highest regulatory, conduct, data, security, and oversight burden |
| **Private Resolution** | Participants or trusted sponsor/channel | Clarify a private obligation and support exact voluntary agreement or safe exit | Participants themselves; qualified neutral/professional only when separately engaged | Capped closed beta | Material collection-characterization, UPL/mediation, privacy, electronic-agreement, and safety risk |
| **Recovery Network & Control** | Creditor/servicer primarily; providers and embedded platforms secondarily | Preflight, appoint, transfer, observe, correct, recall, and switch across independent executors | The directly accountable executor; GRE supplies the control/interoperability layer | Trade pilot component; later standalone | Role, referral/ranking, vendor oversight, data, competition, and licensing analysis depends on actual conduct |

Every family must have its own buyer promise, release manifest, legal review, terms, support model, failure states, fixtures, metrics, and economics. Sharing the Foundation is not permission to share every workflow or dataset.

Family-level “buyer” and “user” labels also do not assign data ownership. In Private Resolution, each participant controls their permitted disclosures; shared facts require explicit shared visibility. A sponsor, employer, member program, or paying participant receives only the scoped service information it is entitled to, never automatic access to the other person's strategy, hardship, evidence, or safety reports.

### 4.1 GRE Trade & Receivables

**Category promise:** Convert fragmented, disputed, or cross-border commercial receivables into decision-ready and execution-ready claims, then preserve continuity through independently accountable recovery routes.

**Primary buyers:** Creditor-side CFO, treasury, credit, AR, export-finance, legal-operations, or recovery leaders with recurring commercial files; credit insurers and authorized servicers where their role is explicit; embedded AR/ERP or trade platforms with committed distribution.

**Best initial cases:** Commercial goods or services receivables with enough value and complexity that evidence reconstruction, route choice, cross-border requirements, provider intake, or switching materially affects economics.

**Poor initial fit:** Clean low-value domestic invoices needing ordinary dunning; one-off small creditors who want a single contingency agency to “just collect”; consumer or mixed-purpose obligations; cases whose only need is litigation representation.

Prioritize buyers in this order:

1. **Anchor/channel buyer:** a trade-credit insurer, factor, export-finance/receivables platform, authorized servicer, or enterprise creditor with recurring files and an existing provider panel. One integration can expose GRE to repeated cases and more than one executor.
2. **Lighthouse creditor:** a mid-market exporter or supplier with recurring cross-border exceptions, an accountable finance/legal owner, and enough annual cases to measure rework and switching.
3. **Deprioritized direct buyer:** a one-off small business with one invoice and no panel. The hard-handoff model adds visible friction for this segment and is unlikely to beat a contingency agency's convenience.

#### Initial capability packages

| Package | Customer job | Initial service modes |
|---|---|---|
| **Claim Readiness** | Reconcile parties, obligations, evidence, balance, rights, disputes, dates, and missing facts into a purpose-scoped Claim Passport | `ASSESS`, `PREPARE` |
| **Route & Economics** | Compare lawful, available routes using prerequisites, external cost, elapsed time, uncertainty, relationship impact, and expected net value | `ASSESS` |
| **Provider Preflight & Recovery Transfer** | Test the case against a named Provider Acceptance Profile; produce a minimized packet; support direct appointment, validation delta, and explicit acceptance or rejection | `PREPARE`, `TRANSFER` |
| **Creditor Continuity** | Show creditor-owned status, costs, returned observations, recall/switch readiness, and unresolved duties without GRE directing the provider's collection conduct | `CONTROL`, `OBSERVE` |
| **Continuity Readiness** | Preserve contract, invoice, performance, acceptance, change, credit, and payment evidence before default for selected high-risk receivables | `PREVENT` — launch-adjacent experiment, not broad O2C |

#### Intended edge

- evidence-to-execution fidelity rather than generic OCR;
- corridor-aware route economics rather than a generic recovery score;
- portable authority and evidence rather than repeated provider intake;
- provider-specific preflight rather than an ambiguous “complete file” score;
- direct creditor control without requiring GRE to become the collector;
- case-level impact analysis when a corridor rule or provider requirement changes;
- context-adjusted provider and route learning rather than simplistic recovery-rate rankings.

#### Required proof

- lower creditor and provider labor per accepted placement;
- fewer missing-document and balance-correction cycles;
- faster time to an accepted or correctly rejected placement;
- high first-pass reuse of the Claim Passport;
- at least two independent providers able to reuse the same core profile, even where their extension requirements differ;
- faster recall or provider switching without lost context;
- credible improvement in total net outcome after fees, delay, internal effort, disputes, and reversals;
- willingness to pay independent of gross recovered dollars.

### 4.2 GRE Consumer Credit Infrastructure

**Category promise:** Preserve accurate, lawful, and humane continuity when a consumer account, borrower, creditor policy, or recovery provider moves across systems, organizations, or countries.

**Primary buyers:** Banks, credit unions, fintech lenders, card issuers, NBFCs, regulated servicers, and debt owners with multi-provider, multi-system, or borrower-mobility problems.

**Signature market hypothesis:** **Borrower mobility continuity**—for example, an account originated in the United States where the borrower now resides in India. The market thesis is not that GRE can “collect globally”; it is that origin facts, ownership, balance, prior notices, disputes, hardship, preferences, authority, applicable policy, eligible executors, and outcomes can remain coherent across the move.

This is the highest-regulation family. It must not inherit Trade workflows merely by changing labels.

An India-resident borrower does not by itself make a U.S.-origin account subject to RBI's Digital Lending Directions. Establish the lender/regulated-entity perimeter, activity, territorial connections, and GRE role before selecting the policy or storage design. Where those Directions apply, LSP storage restrictions and India/overseas-processing requirements can materially constrain a GRE-hosted Consumer Passport. A creditor-held record with limited access is one candidate design, not a regulatory conclusion. See Section 6.8.

#### Initial capability packages

| Package | Customer job | Baseline posture |
|---|---|---|
| **Account Integrity** | Reconcile account, ownership/servicing, balance, identity, prior communications, dispute, hardship, complaint, and consent/preference history | Intelligence and control only |
| **Correction Relay** | Preserve a consumer's dispute or correction, identify its accountable owner, propagate the permitted update to affected systems/providers, and record response/receipt status | `CONTROL`, `OBSERVE`; future/gated |
| **Mobility Assessment** | Determine what changed when the borrower moved, what facts and permissions are missing, and which routes require specialist review | `ASSESS`, `PREPARE` |
| **Direct Provider Activation** | Let the creditor appoint an eligible agency or counsel directly using a minimized, versioned packet and current mandate | `TRANSFER` |
| **Panel Continuity** | Give the creditor one view of provider acceptance, exceptions, costs, complaints, incidents, returned events, and recall/switch status | Creditor-side `CONTROL`, `OBSERVE` |
| **Creditor-First Tools** | Support creditor-owned workflows and communications under the creditor's identity and policies | Future/gated; only after role, law, assurance, and design-partner review |

#### Intended edge

- mobility-aware consumer recovery control plane;
- continuity of dispute, vulnerability, consent, and communication context across handoffs;
- a visible correction and complaint chain so changing providers does not reset the consumer's history;
- machine-readable creditor policy and exact authority without GRE becoming the provider's supervisor;
- independent-provider portability and a reliable validation delta;
- evidence-linked, reviewable AI rather than autonomous borrower pressure.

#### Non-negotiable baseline

- no GRE-branded borrower collection communications;
- no assumption that “first party,” “pre-collection,” “software,” or “AI assistant” determines legal classification;
- no autonomous settlement, waiver, admission, threat, litigation decision, or material contact strategy;
- no consumer fees charged by GRE for institutional recovery activity;
- no payment pass-through through GRE;
- no credit-bureau furnishing, consumer-reporting, or consumer-report access by GRE in the baseline product;
- complaints, hardship, representation, bankruptcy/insolvency, deceased-person, identity mismatch, fraud, and safety signals route to an accountable qualified human under current policy.

The long-term competitive promise is **full-lifecycle continuity without full-lifecycle operation**. GRE may eventually power creditor-controlled, creditor-branded first-party workflows under a separate service mode and assurance gate, because enterprise competitors already provide these capabilities. That option must not be mistaken for permission to launch GRE-branded collection or to direct an independent agency's tactics.

#### Required proof before launch

- a regulated creditor design partner with a named compliance and operations owner;
- current legal review for each exact corridor, actor, communication, data flow, fee model, and provider relationship;
- enterprise security and incident controls acceptable to the buyer;
- a complete borrower complaint and correction path;
- successful shadow testing and adversarial evaluation;
- comparative reduction in errors, duplicate/conflicting communications, activation delay, and provider rework;
- evidence that the creditor values the product despite retaining its own oversight duties.

### 4.3 GRE Private Resolution

**Category promise:** Give individuals a safe, proportionate, evidence-backed route from a private financial disagreement to documented clarification or voluntary resolution.

**Users:** Individuals involved in friend/family loans, shared expenses, informal advances, or other supported private obligations. Distribution may ultimately be direct, embedded, employer/member-benefit, insurer, legal-aid, or financial-wellness based; this is not yet decided.

Do not market this as “AI debt collection for friends.” That framing encourages coercion, weakens trust, and collapses facilitation into collection.

#### Initial capability concept

- guided claim and issue preparation;
- verified, voluntary participation with clear role disclosure;
- separate private workspaces for each participant;
- a controlled shared record showing agreed, disputed, unsupported, and unknown points;
- proposals, counters, exact-term acceptances, and performance tracking;
- a supported PSP payment link directly to the entitled recipient, or independently verified recipient payment instructions with reviewed off-platform receipt reconciliation; provider acceptance of the exact activity is a release dependency, not an assumption;
- route-out to a qualified mediator, lawyer, agency, court information resource, or safety process when appropriate;
- later, constrained two-sided AI assistance that cannot create admissions, waivers, threats, or acceptance.

The first beta should be narrower than the eventual family:

- existing, privately originated U.S. obligations between verified adults;
- evidence appropriate to the requested service, including messages, transfer records, or clearly labeled recollection; weak evidence permits a limited preparation/gap report where supported, but never a verified-debt label or automatic invitation eligibility;
- no assignment, debt purchase, institutional creditor, professional lender, collection agency, or repeated-use lender;
- no rent/eviction, wages, child or spousal support, taxes/fines, medical debt, secured repossession, active insolvency/bankruptcy, deceased/incapacitated participant, criminal allegation, or case with a detected abuse/safety concern;
- at most one reviewed invitation and, only if the released profile permits, one reminder; non-participation ends the bilateral invitation/resolution attempt, with no escalation or inference of admission. These are product limits, not a legal safe harbor; even the first invitation requires approved activity and channel treatment;
- no promise that an electronically recorded outcome is legally enforceable in every state.

#### Complete service outcomes, including non-participation

Private Resolution has two bounded stages. `ASSESS/PREPARE` may start with one requesting adult and produces their source-linked timeline, asserted balance, missing terms, contradictions, uncertainty, and permitted export. `RESOLVE` opens a shared room only after independent, voluntary participation. The service explains that distinction and what a fee covers before purchase. A refusal, unanswered invitation, or inability to locate a person never converts the preparation record into an admitted debt.

Non-participation still yields a useful limited deliverable: the requesting person's permitted record, a reasoned service closure, and general information or a participant-initiated request for separately eligible professional help. GRE neither automatically refers the respondent to a collector nor discloses their private information because they declined. No new contact or data transfer inherits permission from the failed invitation. Measure preparation-only value and willingness to pay separately from bilateral participation.

For participating cases, preserve partial agreement, disputed gifts, alleged cash repayments, multiple advances, hardship, amended terms, external payments, reversals, missed installments, and disagreement after acceptance. Each party accepts the exact same agreement version; agreement acceptance, performance, verified receipts, discharge/release, and service closure remain independent. A missed payment creates a reported exception and a permitted review path, not new collection authority or automatic penalties. Do not invent due dates, interest, limitation effects, or consent to recurring debits.

Identity checks establish the attributes needed for the activity and protect private access; they do not prove a loan or require collecting full identity documents for every preparation task. The recipient must be able to inspect a minimal, reviewed explanation and decline without admitting a debt. Sensitive case details require the appropriate access verification.

#### Intended edge

The possible advantage is a **two-sided, abuse-resistant resolution protocol**—not creditor automation. It should preserve both accounts of events, make evidentiary uncertainty visible, prevent one participant from seeing the other's private strategy, and prefer proportional agreement over pressure.

Private Resolution must differentiate from friend/family lending products that already structure new loans, schedule repayments, and automate reminders, and from general online dispute-resolution systems that already support negotiation and mediation. GRE's wedge is the **post-friction Resolution Room**: reconstruct what each person says happened, expose agreement and uncertainty without declaring a winner, support exact voluntary proposals, and preserve a safe route out. Zirtue currently markets structured friend/family bill-pay loans and automatic repayment; AAA/ODR.com markets structured online negotiation, mediation, and arbitration workflows. Those adjacent offerings validate the jobs, but also mean “digital agreement + reminders” and “online mediation” are not sufficient differentiation. [Zirtue](https://www.zirtue.com/) · [AAA Online Dispute Resolution](https://www.adr.org/odr/) · [ODR.com](https://odr.com/)

#### Safety and trust requirements

- voluntary participation and easy exit;
- strict limits on repeated invitations or contact attempts;
- no address-book scraping, public exposure, social pressure, employer/family contact, or deceptive identity;
- route-out for threats, stalking, coercion, domestic abuse, criminal allegations, incapacity, unsupported claims, or serious power imbalance;
- no claim that GRE is neutral counsel, a mediator, or an adjudicator unless the service is actually delivered by a qualified actor under an appropriate structure;
- family-specific retention, privacy, support, and complaint controls;
- transparent fixed pricing is the baseline hypothesis; avoid percentage-of-debt and aggressive success-fee incentives.

#### Launch gate

Run this as a separately governed, small closed beta only after U.S. activity/state legal characterization, invitation language, safety routing, privacy/retention, participant support, electronic-agreement treatment, and complaint handling are reviewed. Cap beta volume and monitor every case. Expansion requires evidence of voluntary participation, comprehension, safe exits, support-adjusted economics, and no pattern of harassment or misuse. A shared technical foundation does not justify an ungated public launch.

### 4.4 GRE Recovery Network & Control

**Category promise:** Integrate once, transfer without rebuilding the claim, keep executors directly accountable, and preserve one creditor-controlled history across provider changes.

This is a horizontal product family used by the three vertical families and sellable independently to creditors, servicers, agencies, law firms, insurers, and embedded platforms.

#### Editions

| Edition | Primary user | Value |
|---|---|---|
| **Creditor Control** | Creditor, owner, or servicer | Approved panels and bring-your-own-agency; direct appointment; authority, budgets and settlement limits; acceptance/exceptions; unified status; complaints/incidents; cost visibility; recall and switching; contextual comparison |
| **Provider Connect** | Agency, law firm, mediator, or other qualified executor | Standardized intake; evidence mapping; conditional acceptance; exception requests; credential/capacity profile; direct system integration; structured return of status, cost, payment observations, and outcomes |
| **Corridor Assurance** | Creditor compliance, legal operations, risk, and vendor-management teams | Effective-dated policy packs; source/reviewer status; change alerts; affected-case analysis; control evidence; regression results; review expiry and release gates |
| **Passport Conformance** | Providers, integrators, and enterprise technical teams | Profile validation; mapping tests; sample fixtures; compatibility reports; signed/versioned acceptance declarations; no implication of legal or regulatory endorsement |

Corridor Assurance is operationalized, source-linked change management—not automated legal advice. Legal interpretations, release conditions, and review currency must identify the qualified reviewer; GRE may show an unresolved issue or expired review rather than fabricate an answer.

#### Intended edge

Build a practical recovery interoperability layer comprising:

- a portable Claim Passport;
- a machine-readable direct mandate and authority envelope;
- a provider-owned, versioned Acceptance Profile and testable preflight;
- family/corridor-specific provider eligibility;
- standardized acceptance, rejection, exception, event, and outcome semantics;
- action receipts and a correction relay across permitted system boundaries;
- creditor-attributed instructions transported by GRE;
- rapid recall and switching;
- context-adjusted performance evidence with uncertainty and data-coverage warnings.

#### Provider adoption design

Providers will resist or bypass GRE if it only adds creditor oversight and data demands. Provider Connect must reduce their work through cleaner files, fewer repeated document requests, explicit authority, faster exception handling, API integration, reusable credentialing, and better client reporting.

Early provider participation should be free or priced only where GRE delivers a separately valuable provider workflow. Support low-friction CSV/SFTP/secure-portal adapters before requiring API work, and let a provider export its mappings and event history. The first network effect is **acceptance coverage**, not pooled recovery data: each additional provider profile gives creditors another executable route and gives providers faster access to prepared work.

Begin with creditor-selected providers and bilateral integrations. Do not begin with a broad open marketplace, universal provider league table, or claim that the network is neutral merely because GRE does not collect. Eligibility must precede ranking; commercial relationships and data coverage must be disclosed; payment cannot improve eligibility or hidden rank.

---

## 5. Classification, corridors, and service availability

### 5.1 Replace B2B/B2C shortcuts

Every matter must be classified using facts that can change the applicable rules and product behavior:

1. creditor/claimant legal type and regulatory status;
2. obligated party type, including whether a natural person is involved;
3. purpose at origination—business, personal/family/household, mixed, guarantee, or unknown;
4. obligation and instrument type;
5. current owner, servicer, insurer/subrogee, representative, and authority chain;
6. creditor, debtor, contact-recipient, data-processing, payment, and executor locations;
7. origin jurisdiction, current residence/place of business, governing law, forum, and enforcement venue;
8. requested service and actual acts—analysis, location verification, communication, negotiation, settlement, reporting, payment, filing, or enforcement;
9. communication identity and degree of discretion/control;
10. compensation, referral, contingency, and payment-flow structure;
11. intended data uses and disclosures;
12. selected executor and direct contractual relationships.

If purpose or role classification is uncertain, place the matter on hold or route it to qualified review. Do not default an ambiguous natural-person obligation into Trade.

### 5.2 Corridor packs are directional operating products

A corridor is not merely “U.S.–India.” It is a versioned configuration for a defined direction, family, parties, acts, dates, data flows, payment path, and executor model.

Each corridor pack must contain:

- exact supported profiles and exclusions;
- required facts and evidence;
- current primary legal/regulatory sources and their hierarchy;
- effective and transition dates;
- communication, channel, identity, cadence, language, disclosure, and consent constraints;
- data collection, sharing, transfer, retention, deletion, and residency constraints;
- provider licensing, qualification, insurance, venue, and authority prerequisites;
- limitation/deadline and preservation logic with qualified-review triggers;
- payment, foreign-exchange, sanctions, tax, and reconciliation constraints;
- complaint, dispute, vulnerability, and incident paths;
- operational owners, counsel-review owner, review-by date, and regression tests;
- change-impact behavior identifying affected cases, controls, provider profiles, and communications when a source or interpretation changes;
- commercially enabled service modes and executor patterns.

Candidate corridor sequence:

1. **India creditor → U.S. business obligor, Trade & Receivables:** first validation candidate because project knowledge already exists. Begin with assessment, preparation, direct transfer, and observation—not GRE collection activity.
2. **U.S. domestic privately originated obligation, Private Resolution:** a parallel controlled-beta profile limited to voluntary two-sided clarification and exact-term agreement. “Domestic” does not remove state-by-state activity, communication, privacy, electronic-agreement, or safety review.
3. **U.S.-origin consumer account → India-resident borrower, Consumer Credit:** differentiated mobility hypothesis, but launch only with a regulated design partner and corridor-specific counsel.
4. **Additional U.S. domestic, India domestic, or international enterprise profiles:** add only where a committed buyer or distribution partner, qualified executor coverage, case frequency, and economics justify them.
5. Additional corridors only after operational and legal release gates are met.

Do not describe GRE as globally available because the data model can represent many countries.

Keep U.S. domestic and India domestic Trade/Consumer opportunities, U.S.–India reverse Trade corridors, and later private/cross-border profiles in the scope register with their own buyer hypotheses and reconsideration conditions. Their architectural representability is not live coverage. Track each promised future development or business deliverable explicitly; distinguish a future candidate from an excluded business model.

### 5.3 Service modes

| Mode | Meaning | Important boundary |
|---|---|---|
| `PREVENT` | Pre-default evidence readiness and exception preservation | Does not become general underwriting, O2C, or loan origination |
| `ASSESS` | Construct a scoped Claim Passport and analyze gaps/options | Delivery does not authorize contact or guarantee collectability |
| `RESOLVE` | Support an authorized first-party or voluntary bilateral resolution workflow | Family-, actor-, identity-, and corridor-specific; not a universal GRE permission |
| `PREPARE` | Cure evidence, authority, data, and provider-readiness gaps | No external collection effect by itself |
| `TRANSFER` | Freeze and disclose a minimized handoff packet for direct provider acceptance | The bounded transfer service completes only when its acceptance conditions are met; separately scoped GRE duties continue |
| `CONTROL` | Provide creditor-side policy, appointment, budget, recall, switching, and oversight tooling | The creditor controls its provider; GRE does not supervise individual collection tactics |
| `OBSERVE` | Receive and normalize permitted external events and outcomes | External reports remain observations until independently verified where required |

Service-mode names are also separate from action execution modes. In the existing reference, `service_request.kind` uses `ASSESSMENT/OPERATE/HANDOFF/MONITOR`, while `action_intent.binding.execution_mode` uses `OBSERVE/PREPARE/APPROVAL_REQUIRED/DELEGATED`. The new commercial `service_mode` vocabulary must have an explicit versioned mapping; identical words do not mean identical authority. Legacy `OPERATE` cannot be converted automatically into a permitted live `RESOLVE` service.

Commercial availability and legal review are separate dimensions. Retain a product status such as `DESIGNED`, `SHADOW_TESTED`, `PILOT_ENABLED`, `COMMERCIALLY_SUPPORTED`, `SUSPENDED`, or `RETIRED`, and add a separate legal-review record such as `UNREVIEWED`, `ISSUES_IDENTIFIED`, `COUNSEL_REVIEW_CURRENT`, `APPROVED_WITH_CONDITIONS`, `REVIEW_EXPIRED`, or `REVIEW_REQUIRED`. Do not let a commercial status imply legal approval.

---

## 6. Legal-exposure and operating framework

### 6.1 Governing principle

The legal perimeter follows GRE's actual conduct, communications, discretion, compensation, representations, data practices, payment flow, and relationship to the creditor and provider. Product labels and contract wording are relevant but not dispositive.

Therefore:

> **“Pre-collection,” “software,” “marketplace,” “AI assistant,” and “independent contractor” are not safe harbors.**

This document is a product and control framework, not a legal opinion. Before enabling any live family/corridor/service/executor combination, obtain current advice from qualified counsel in the relevant jurisdictions and translate that advice into versioned controls and tests.

### 6.2 Default operating postures

| Posture | GRE may do | GRE must not infer |
|---|---|---|
| **Intelligence** | Ingest permitted data, reconcile, classify, identify gaps, generate a scoped assessment, and recommend eligible alternatives with uncertainty | That analysis proves the debt, legal entitlement, limitation status, enforceability, location, or permissible action |
| **Creditor tooling** | Let an authorized creditor user configure policies, review drafts, approve actions, and use its own identity and channels when legally supported | That creditor branding alone removes GRE or vendor obligations |
| **Preparation and transfer** | Produce a minimized Claim Passport, facilitate direct appointment, transmit permitted data, and record provider acceptance/rejection | That successful transmission means the provider validated or accepted the debt |
| **Creditor-side control** | Transport creditor-attributed instructions, show returned events, compare context, and support recall/switching | That GRE may choose the agency's next contact, negotiation tactic, or legal step |
| **Observation** | Receive structured reports and preserve source/verification status | That provider-reported payment, settlement, or closure is authoritative without the required source |
| **Reserved work** | Integrate qualified agencies, counsel, mediators, investigators, payment institutions, or other licensed actors | That GRE may itself collect, practice law, mediate, investigate, transmit funds, or enforce merely because a partner could |

For the initial Trade bundle, identity/location work means permitted entity resolution and verification from approved sources. It does not include contact scraping, covert surveillance, field investigation, or a general skip-tracing service. Any broader location activity requires source-specific permissible-purpose, privacy, licensing, and disclosure review.

### 6.3 Hard operational handoff

The preferred post-preparation relationship is:

| Relationship | Responsibility |
|---|---|
| **Creditor ↔ GRE** | Assessment, permitted identity/location work, evidence and authority preparation, route decision support, transfer tooling, and separately scoped non-operational observation/control services |
| **Creditor ↔ agency** | Direct appointment, collection mandate, settlement authority, fees, complaints, supervision, and responsibility for collection conduct |
| **GRE ↔ agency** | Minimum necessary technical/data exchange, security, data-use restrictions, integration, and event-return terms—not a hidden collection subcontract |
| **Borrower/obligor ↔ agency** | Agency-operated collection communications, negotiation, arrangements, and payment experience within its mandate. Complaint/dispute responsibilities follow applicable law and agreements; creditor grievance/oversight duties and GRE's own support, correction, and incident duties survive. GRE routes received issues to the accountable owner and records receipt/escalation without conducting collection negotiations. |

At handoff, distinguish review access from authority to execute:

1. Identify the principal, intended provider, exact service scope, current authority, deadlines, and Provider Acceptance Profile version. Give preflight reviewers only the minimum separately permitted data needed for conflicts, eligibility, and validation; transmission does not authorize collection.
2. Issue a versioned transfer offer and disclosure snapshot. The provider returns acceptance, conditional acceptance with a structured delta, rejection, or an unanswered/expired offer. A revised packet is a new version, never a silent alteration of an already reviewed one.
3. The creditor directly appoints the provider. The provider records independent validation and satisfies any conditions required to begin the specified acts. Bind execution to the exact accepted packet and current mandate; conditional acceptance alone does not unlock incompatible work.
4. At the agreed cutover, end GRE operational authority for the transferred service, fence new action commits, and cancel queued work that remains cancelable. Preserve sent/in-flight/uncertain effects for reconciliation; neither a handoff nor a cancellation request proves a message was recalled.
5. Record provider activation and transfer-service completion separately. Use the qualified state defined in the new contract (for example, `service_request.status = TRANSFERRED`); do not reuse `case.state.closure_state = SERVICE_SCOPE_COMPLETE` as though it were the same state. A declined or unanswered placement does not count as an accepted transfer.
6. The provider performs collection through its own identity, personnel, channels, systems, and professional judgment within the direct mandate. Repayment goes to the entitled creditor or an authorized financial arrangement, never through GRE's baseline accounts.
7. Continue separately scoped `CONTROL/OBSERVE` work, corrections, complaints about GRE, required preservation, and other surviving duties with a named owner and service window. Closing the transfer service does not remove these responsibilities or resolve the obligation.

Before acceptance, rejection, failed delivery, deadline proximity, or provider silence leaves the service with an explicit responsible owner and next decision. Do not place urgent work in an ownerless “awaiting provider” state. On recall or switching, distinguish requested revocation, effective GRE access revocation, provider acknowledgment of cessation, in-flight exceptions, retained copies, and replacement activation. Prevent overlapping conflicting mandates for the same acts; permit specialist roles only where scopes are explicit. GRE can revoke its access and escalate an unresponsive provider, but cannot technically guarantee an external actor stopped or deleted exported records.

The handoff produces an Action Receipt for GRE's preparation/transmission and the provider's acceptance response. It does not certify the truth, enforceability, legal sufficiency, or permissibility of the provider's next act. Provider acceptance is a commercial/operational state; the provider's legal and factual validation remains independently recorded.

GRE may enforce security and access requirements, data-use restrictions, credential/insurance eligibility, incident notification, interface conformance, and protection against misuse of GRE's identity. GRE should not control:

- scripts or exact message wording used by the agency;
- contact timing or frequency;
- daily targets or work queues;
- individual negotiation tactics;
- settlement decisions except by transporting the creditor's exact authority or decision;
- threats, litigation strategy, filings, or enforcement choices;
- agency personnel supervision or compensation;
- selection of the next collection action.

An exception returned by the provider may ask the creditor for a new decision. GRE may transport that decision and update the record; GRE must not silently become the decision maker.

Executor independence does not require GRE to ignore misuse of its platform or known incidents. GRE may suspend its own access, integration, eligibility representation, or dispatch functionality and route urgent issues under the applicable agreement. These protective controls are distinct from directing a provider's collection tactics. A suspension must preserve permitted complaints, corrections, evidence access, and incident handling rather than disabling every service indiscriminately.

### 6.4 State semantics after handoff

`TRANSFERRED` is a service state, not the end of the case or the creditor relationship. The revised model must distinguish:

- GRE transfer-service completion;
- direct provider engagement state;
- provider acceptance and active-work state;
- creditor instruction/authority state;
- external observations and their verification state;
- any separate GRE `CONTROL` or `OBSERVE` service;
- underlying obligation, payment, dispute, agreement, legal, and closure states.

This is the mechanism behind the intended **hard operational handoff; continuous creditor experience** design. It reduces role ambiguity but does not create a legal safe harbor.

### 6.5 What the creditor should be sold

Do not lead with “GRE reduces our liability” or “GRE transfers your liability.” That is incomplete and unattractive to sophisticated creditors, especially regulated ones that retain oversight responsibilities.

Lead with:

- one implementation across the creditor's chosen providers;
- no hidden subcontracting and a directly accountable executor;
- an accepted, versioned claim packet instead of repeated re-intake;
- faster activation and fewer evidence loops;
- preservation of disputes, preferences, prior actions, and authority;
- transparent fees, exceptions, and total economics;
- creditor-controlled recall and provider switching;
- unified, source-aware observations without surrendering the provider relationship;
- less vendor lock-in and lower operational concentration risk.

The hard handoff is the enabling legal/operating architecture. The product value is continuity, control, portability, and measurable reduction in friction.

The offer will not be equally attractive to every creditor. Make the target truth explicit:

| Creditor situation | Expected attractiveness | Why |
|---|---|---|
| Existing agency/law-firm panel, recurring complex files, fragmented portals, vendor-risk obligations, or a real need to recall/switch | **High if GRE proves workflow savings** | The creditor already bears contracting and oversight cost; GRE can reduce duplicate intake, concentration risk, and evidence loss |
| One incumbent provider but recurring disputed/cross-border matters and expensive internal preparation | **Medium; lead with Claim Readiness and preflight** | The packet and economics may create value, but portability is initially an option rather than a daily need |
| One-off or low-value creditor seeking a single contingency service and no internal recovery owner | **Low** | Another platform and direct provider relationship feel like work; a full-service agency is simpler |
| Regulated consumer creditor with multi-provider operations | **Potentially high, but procurement- and assurance-heavy** | Continuity, complaints, corrections, and oversight matter, but the buyer will expect mature security, integration, governance, and regulatory support |

Accordingly, do not sell the hard handoff as a universal convenience feature. Sell first to buyers for whom provider independence, oversight, and switchability are already valuable. For the low-fit segment, GRE would need an embedded channel or a clearly disclosed managed front door that preserves direct executor responsibility; it should not distort the baseline model to imitate a traditional one-stop agency.

### 6.6 Responsibility that remains

Indemnification, defense obligations, limitations, and insurance can allocate losses between contracting parties, but they cannot stop a consumer, counterparty, or regulator from naming GRE. GRE remains accountable for its own:

- inaccurate or misleading assessment/handoff;
- unlawful collection, enrichment, use, or disclosure of data;
- misleading representations about role, authority, provider neutrality, results, or compliance;
- security, access-control, retention, model, or system failures;
- unauthorized actions or communications;
- pre-handoff conduct;
- negligent provider eligibility or credential representations within GRE's assumed scope;
- failure to honor contractual incident, correction, deletion, or support duties.

### 6.7 Family-specific legal posture

| Family | Baseline risk posture | Required response |
|---|---|---|
| **Trade & Receivables** | Commercial debt is generally outside the U.S. federal FDCPA's consumer-debt scope, but state collection licensing, unfair-practice, contract, privacy, professional, data-source, sanctions, payment, and cross-border rules may still apply. | Limit launch to defined commercial-purpose profiles; run state/activity and corridor review; do not advertise a B2B exemption as comprehensive. |
| **Consumer Credit Infrastructure** | Debt collection, servicing, UDAAP, state licensing, creditor oversight, privacy, complaints, communications, hardship, and regulated-outsourcing rules can attach to GRE, the creditor, and providers depending on actual roles. | Highest assurance; regulated design partner; no GRE-branded collection; current source-linked corridor pack; human escalation; creditor retains oversight. |
| **Private Resolution** | Legal characterization may turn on the obligation, GRE's fee and conduct, who GRE represents, communication behavior, electronic-agreement and mediation/UPL rules, privacy, safety, and local collection statutes that may be broader than federal law. | Voluntary two-sided design; role disclosure; abuse controls; fixed-fee hypothesis; qualified route-out; state/activity-specific legal and safety review. |
| **Recovery Network & Control** | Soliciting or arranging claims, ranking/referring providers, setting tactics, sharing provider/creditor performance or pricing data, handling data, or touching funds may alter licensing, agency, antitrust, service-provider, and conflict analysis. | BYO panel first; direct contracts; transparent economics; eligibility before ranking; no funds; aggregation and access controls; no hidden operational supervision. |

### 6.8 Current primary-source implications

The project update should use these as control-design inputs, rechecking them at the time of implementation:

- The U.S. CFPB states that the FDCPA principally covers personal, family, and household debts rather than business debts, while state laws may add protections. Regulation F governs entities that meet its debt-collector definition. This supports separate Trade and Consumer profiles, not a blanket commercial safe harbor. [CFPB overview](https://www.consumerfinance.gov/ask-cfpb/what-laws-limit-what-debt-collectors-can-say-or-do-en-329/) · [Regulation F](https://www.consumerfinance.gov/rules-policy/regulations/1006/)
- State activity definitions can be broad. Arizona, for example, uses a broad collection-agency definition covering direct or indirect solicitation of claims, subject to applicable statutory exemptions. A state-by-state actor/activity matrix is therefore required before U.S. launch. [Arizona DIFI](https://difi.az.gov/collection-agencies-nmls) · [ARS 32-1001](https://www.azleg.gov/ars/32/01001.htm) · [ARS 32-1004 exemptions](https://www.azleg.gov/ars/32/01004.htm)
- The Consumer Financial Protection Act prohibits covered persons and service providers from engaging in unfair, deceptive, or abusive practices. GRE's role depends on the applicable statutory definitions and actual conduct; a direct creditor–agency contract does not settle that classification. CFPB Bulletin 2013-07, previously cited here, was withdrawn on May 12, 2025 and is not current guidance. [12 USC 5536](https://www.govinfo.gov/content/pkg/USCODE-2024-title12/html/USCODE-2024-title12-chap53-subchapV-partC-sec5536.htm) · [Statutory definitions, 12 USC 5481](https://www.govinfo.gov/content/pkg/USCODE-2024-title12/html/USCODE-2024-title12-chap53.htm) · [CFPB withdrawal notice](https://www.federalregister.gov/documents/2025/05/12/2025-08286/interpretive-rules-policy-statements-and-advisory-opinions-withdrawal)
- U.S. banking agencies' third-party guidance says the use of third parties does not diminish a bank's responsibility for safe, sound, and lawful activity. Design the Consumer family to make creditor oversight easier, not to promise its elimination. [Interagency guidance](https://www.federalregister.gov/documents/2023/06/09/2023-12340/interagency-guidance-on-third-party-relationships-risk-management)
- Where India's 2025 Digital Lending Directions apply, the regulated entity remains responsible for an LSP's acts and omissions, must review and guide recovery-agent conduct, must tell the borrower which recovery agent is authorized before contact, retains grievance responsibility, restricts data collection/sharing, and generally requires repayment directly to the regulated entity rather than through an LSP pass-through account. [RBI Digital Lending Directions, 2025](https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=12848&Mode=0)

- The same Directions apply to specified RBI-regulated entities and digital lending activities, not automatically to every foreign-origin account involving an India-resident borrower. Where applicable, paragraph 13 limits LSP storage to specified minimal operational borrower data, requires India-based storage, and requires data processed abroad to return to India and be deleted abroad within 24 hours. Establish the exact applicability and permitted data topology before implementing a Consumer Passport store; customer-held records and scoped access are design candidates subject to that review. [RBI Directions, paragraphs 3–5 and 13](https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=12848&Mode=0)
- India's final Digital Personal Data Protection Rules, 2025 use phased commencement: some rules began on publication, rule 4 begins one year later, and most substantive listed rules begin eighteen months later. Build purpose, notice, consent/other lawful basis, rights, retention, processor, breach, and transfer controls for the applicable current and future phases; do not mark the whole regime simply “active” or “inactive.” [MeitY final Rules](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

- Track commencement of the DPDP Act separately from the Rules. G.S.R. 843(E) phases the Act itself, including delayed commencement of substantive processing provisions and section 44(2), which changes the existing IT Act framework. Preserve applicable existing obligations during transition; evaluate territorial scope and exemptions separately. [Act commencement notification](https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf) · [DPDP Act](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf)
- U.S. financial institutions subject to the FTC Safeguards Rule must maintain information-security programs and oversee service providers through selection, contracts, monitoring, and reassessment. Whether or not GRE is directly covered in a particular role, Consumer Credit Infrastructure must be capable of meeting financial-institution vendor requirements. [FTC Safeguards Rule guidance](https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know)
- The U.S. Fair Credit Reporting Act restricts access to consumer-report information to specified permissible purposes and gives furnishers accuracy/dispute obligations. GRE therefore excludes consumer-report access and bureau furnishing from its baseline rather than assuming recovery activity makes every data use permissible. [FTC FCRA overview](https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act)
- U.S. calls and texts can trigger rules beyond the FDCPA. FCC materials explain that the TCPA restricts specified autodialed, artificial/prerecorded-voice calls and robotexts absent consent or an exemption and protects revocation. Any future communications mode needs channel-specific analysis and consent/revocation state; a generic “permission to contact” field is insufficient. [FCC order](https://docs.fcc.gov/public/attachments/FCC-24-24A1.pdf)
- Servicemember status can change the lawful financial and civil treatment of an account. Consumer profiles need an effective protection/hold and qualified-review path, not merely a vulnerability label. [CFPB SCRA overview](https://www.consumerfinance.gov/consumer-tools/military-financial-lifecycle/the-servicemembers-civil-relief-act-scra/)
- Under current U.S. federal definitions, accepting funds from one person and transmitting them to another can constitute money transmission depending on facts and circumstances. GRE should integrate authorized payment institutions and receive reconciliation events rather than possess or control funds. [31 CFR 1010.100](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-A/section-1010.100)
- Cross-border activity requires risk-based sanctions controls proportionate to products, counterparties, and geography. Screening is one control, not a complete legal determination. [OFAC compliance framework](https://ofac.treasury.gov/media/16331/download?inline=)
- Network analytics require competition review. Recent U.S. enforcement over a third-party algorithm using competitors' nonpublic information illustrates that an intermediary does not make competitively sensitive data sharing harmless. GRE must separate tenant data, restrict granular cross-provider pricing/strategy visibility, and review any benchmark or recommendation design. This is an issue-spotting inference, not a conclusion that ordinary provider scorecards are unlawful. [U.S. DOJ RealPage resolution](https://www.justice.gov/opa/pr/justice-department-requires-realpage-end-sharing-competitively-sensitive-information-and)
- Legal sources need valid-time treatment. As of this directive's date, RBI's new Export and Import of Goods and Services Regulations, 2026 had been published but were scheduled to take effect October 1, 2026. The project must preserve the rule that applied to the actual event, not whichever page was retrieved most recently. [RBI 2026 Regulations](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=13277&Mode=0) · [effective-date circular](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=13278&Mode=0)

### 6.9 Legal review matrix required before activation

For every enabled combination, counsel and accountable operators must resolve and document at least:

- debt/claim and purpose classification;
- collection-agency, debt-buyer, servicing, LSP, marketplace/referral, investigator/data-broker, and other licensing characterization;
- permissible identity/location data sources and permissible purpose;
- communication identity, channel, content, timing, frequency, recording, consent, opt-out, language, and accessibility;
- validation, dispute, complaint, hardship, representation, bankruptcy/insolvency, deceased-person, and fraud handling;
- servicemember/military, protected-benefit, vulnerability, accessibility, language, and other protected-treatment requirements;
- settlement, interest, fees, limitation/deadline, waiver, admission, release, and authority rules;
- consumer-report access, furnishing, adverse-action, fair-lending/fair-treatment, and automated/consequential-decision implications where applicable;
- law practice, mediation, arbitration, filing, and enforcement boundaries;
- electronic signature/record, consent evidence, agreement formation, cooling-off, mediation confidentiality, and enforceability treatment;
- privacy roles, lawful processing basis, notice, minimization, data subject rights, processor terms, retention, deletion, localization, and cross-border transfer;
- security standard, incident notice, audit, subcontractor, and regulator/customer access;
- payment instructions, money transmission, FX/remittance, sanctions, AML/KYC responsibilities, tax, and reconciliation;
- referral fees, contingency compensation, provider ranking, conflicts, and disclosures;
- antitrust/competition limits for shared provider, creditor, pricing, strategy, capacity, and outcome data;
- insurance, indemnification, complaint ownership, record retention, audit rights, and termination/transition assistance.

No language model may infer final legal answers for these fields from a generic jurisdiction label. Store the source, reviewer, conditions, effective date, review date, and abstention/escalation path.

---

## 7. Market assessment and leadership thesis

### 7.1 What is already table stakes

Current vendor claims show that GRE cannot lead merely by offering AI, omnichannel workflows, portals, compliance rules, APIs, provider routing, or end-to-end dashboards:

- InDebted markets AI-native first-party decisioning, digital journeys, enterprise governance, auditability, and a fully managed third-party alternative; its Comply product markets programmable jurisdiction-specific rules, pre-send checks, source-linked traces, and vulnerability detection. [Receive](https://www.indebted.co/solution/receive/) · [Comply](https://www.indebted.co/product/comply/)
- InDebted's acquisition of Receeve/Receive combined first-party collections decisioning with a third-party service, illustrating active market convergence toward bundled end-to-end platforms. GRE should assume well-capitalized competitors will keep filling feature gaps. [InDebted acquisition announcement](https://www.indebted.co/blog/newsroom/indebted-acquires-receive/)
- January markets AI-driven consumer conversations across voice, SMS, and chat, including authentication, payment, and settlement, with creditor-set guardrails. [January](https://www.january.com/)
- HighRadius markets agentic collections orchestration, automated work, dispute handling, calling, and broad ERP integration for B2B receivables. [HighRadius](https://www.highradius.com/software/order-to-cash/collections-management/)
- Credgenics markets an end-to-end institutional recovery platform across digital, calling, field, legal, payment, and analytics workflows. [Credgenics](https://www.credgenics.com/)
- Delos markets document extraction, claim classification, evidence/legal readiness, strategy routing, and legal handoff for collection teams. [Delos](https://www.delos.international/agencies)
- Debitura markets APIs for creditors, embedded referral partners, and collection providers, with placement, real-time status, documents, payments, and wide international reach. [Debitura API](https://www.debitura.com/integration/debt-collection-api)
- C&R Software markets automated, analytics-based agency placement and centralized monitoring. Agency routing and performance dashboards therefore cannot be treated as whitespace. [C&R Placement Plus](https://blog.crsoftware.com/the-benefits-of-performance-based-debt-collection-agency-placements)
- Atradius, Coface, and TCM already offer international B2B recovery reach and local-provider expertise; TCM describes an alliance of agencies and law firms across more than 167 countries. [Atradius](https://atradiuscollections.com/global/services/online-debt-collection) · [Coface](https://www.coface.com/news-economy-and-insights/debt-collection-around-the-world-how-to-deal-with-local-specificities) · [TCM](https://www.tcmgroup.com/)
- Zirtue already structures friend/family bill-pay loans, repayment, and reminders, while AAA/ODR.com provides structured online negotiation and qualified dispute-resolution workflows. Private Resolution cannot win merely by digitizing an IOU or adding a chat room. [Zirtue](https://www.zirtue.com/) · [AAA ODR](https://www.adr.org/odr/)
- Enterprise security is a competitive prerequisite. InDebted markets ISO 27001/9001, SOC 2 and PCI coverage, and HighRadius exposes a trust center with ISO, SOC, PCI, SSO/MFA, audit, penetration-testing, and continuity controls. GRE cannot defer procurement readiness until after product-market fit with banks. [InDebted security](https://www.indebted.co/solution/information-security/) · [HighRadius trust center](https://trust.highradius.com/)

These are vendor representations, not independently verified performance. They are sufficient to show that the feature labels themselves are not novel.

### 7.2 Competitive conclusion and chosen battlefield

| Market archetype | What buyers already get | Why GRE should not attack head-on | GRE's selected opening |
|---|---|---|---|
| Full-service or digital collection agency | One vendor, outreach, negotiation, payment experience, contingency or managed execution | GRE's hard handoff will not beat this on one-off convenience | Independent executor accountability plus creditor-owned continuity and switchability |
| AR/O2C platform | ERP integration, dunning, disputes, cash application, forecasting, pre-default automation | Building a broad AR suite would dilute the wedge and overwhelm founder capacity | Evidence/authority readiness for complex claims that may cross into external recovery |
| Collections system or vendor-management tool | Workflows, decisioning, agency allocation, dashboards, compliance controls | Dashboards and AI routing are already mature categories | Portable contracts that survive system and provider change, plus acceptance preflight |
| Global agency network or marketplace | Country reach, local agents, placement, portal status | A country count is easy to copy and says little about case quality or control | Directional corridor assurance and independently testable Provider Acceptance Profiles |
| Claim-preparation/legal-tech tool | Extraction, case assessment, document assembly, legal handoff | Readiness alone may become a feature inside an incumbent | Closed-loop acceptance, correction, event return, recall, and re-transfer |
| Private-loan or ODR product | New-loan terms, reminders, payments, negotiation, mediation/arbitration workflows | Generic IOUs and online negotiation are not novel | A post-friction, evidence-aware, two-sided Resolution Room with strict abuse controls |

GRE is choosing a **cross-provider control and continuity** battlefield. It should interoperate with agencies, law firms, AR platforms, ODR providers, and payment institutions rather than attempting to replace all of them. The product must be meaningfully better at the seams between those systems.

### 7.3 The category-level opening

GRE's defensible hypothesis is the combination of:

1. **Acceptance continuity** — readiness is tested against a named provider profile, and the provider's independent acceptance or validation delta is structured.
2. **Evidence continuity** — claims remain source-linked, contradictory evidence remains visible, and readiness is purpose-specific.
3. **Authority continuity** — the exact principal, rights, mandate, limits, revocation, and provider appointment travel with the matter.
4. **Policy continuity** — effective-dated corridor and creditor policy is evaluated against the actual actor and action, and rule changes identify affected cases.
5. **Correction continuity** — disputes, corrections, complaints, preferences, and superseded assertions do not disappear when a file or provider changes.
6. **Executor independence** — agencies and counsel accept responsibility directly rather than operating as an opaque GRE subcontractor.
7. **Provider portability** — a creditor can transfer, recall, and switch without rebuilding the case or surrendering its data relationship.
8. **Outcome continuity** — costs, delays, disputes, payments, reversals, and closure reasons return in normalized but source-honest form.
9. **Mobility continuity** — origin facts and current-location constraints remain coherent when a person, account, or claim crosses borders.

The available competitor materials do not prove that this exact open, cross-provider, cross-border continuity layer is an established category. That is an inference and a market hypothesis, not proof of whitespace. Test it directly with creditors and providers.

### 7.4 Why the hard handoff can win commercially

A hard handoff alone is a weaker offer than a full-service agency: it gives the creditor another contract and can appear to end GRE's usefulness at the moment execution begins.

It becomes attractive when Network & Control makes the handoff materially better than current servicing:

- direct accountability without losing a unified interface;
- provider choice without re-intake;
- faster activation and lower internal labor;
- less dependence on any agency's proprietary portal or data model;
- comparable costs and outcomes across the creditor's own case mix;
- continuity when a provider declines, loses eligibility, underperforms, or must be replaced;
- one evidence and authority standard across internal, first-party, agency, legal, and payment systems.

The product must absorb the contracting friction through reusable direct panel agreements, appointment workflows, authority envelopes, and integrations. It should provide unified cost reporting, not blur who invoices for or is responsible for collection work.

The commercial contrast is:

> A traditional provider gives the creditor one outsourced execution path. GRE should give the creditor one control plane across independently accountable paths.

That is compelling only when GRE makes the seams nearly invisible. The sales demonstration must show a messy case becoming provider-ready, a provider returning a precise delta, and the creditor switching to a second eligible provider without reconstructing the claim. If GRE cannot show that sequence, “hard handoff” will sound like a limitation rather than an advantage.

### 7.5 Durable advantage

Do not describe an LLM, prompts, “agentic AI,” a graph schema, or an event ledger as the moat. The potential compounding assets are:

- independently accepted Claim Passport profiles and conformance tests;
- expert-maintained, effective-dated corridor packs and evaluation cases;
- provider integrations that actually reduce intake and reporting work;
- permissioned, context-correct decision/action/outcome observations;
- comparative evidence of lower total effort and fewer critical errors;
- enterprise trust, security, incident, and governance capability;
- distribution through creditor systems and provider networks;
- credible exit and portability rather than artificial lock-in.

Learning must respect the difference between service delivery, tenant-private evaluation, pooled benchmarking, and model training. Outcome return does not automatically grant a right to train or resell. GRE must remain valuable in a tenant-private deployment.

Build the moat in this order:

1. **Workflow proof:** reliably reconstruct and preflight difficult cases.
2. **Acceptance proof:** two or more independent providers reuse the core contract.
3. **Integration proof:** returned events, corrections, recall, and switching work without parallel manual portals.
4. **Assurance proof:** corridor changes produce reviewable case-impact and regression evidence.
5. **Learning proof:** permissioned, context-adjusted observations improve decisions without creating hidden bias or data-rights problems.
6. **Category proof:** creditors and providers use GRE terminology and conformance outside a single bespoke pilot.

An open core can strengthen stages 2 and 6; opening the entire product too early can erase stages 3–5. The standardization decision must follow adoption evidence.

### 7.6 Market-leadership standard

“Market leader” is a goal, not copy for the next website. GRE earns the claim when it can demonstrate, on comparable cohorts:

- multiple independent providers accepting the same Claim Passport profile;
- materially less time and labor from case intake to accepted placement;
- materially fewer critical evidence, identity, balance, authority, and data errors;
- successful provider recall/switch without loss of context;
- current counsel-reviewed corridor behavior with regression evidence;
- normalized observations covering a meaningful share of cases without disguising missing or censored outcomes;
- repeat paid use and retention from creditor-side buyers;
- provider adoption because GRE reduces their cost, not only because a creditor requires it;
- no deterioration in complaint, dispute, vulnerability, privacy, or incident outcomes;
- support-adjusted unit economics that work without success-fee pressure or possession of funds.

Report a **Resolution Quality Scorecard**, not one gamable recovery score. Keep at least these dimensions visible:

| Dimension | Examples | Guardrail |
|---|---|---|
| Net economic outcome | Collected/settled value, fees, internal effort, delay cost, reversals | Do not attribute external recovery uplift to GRE without a defensible comparison |
| Readiness and accuracy | Critical-field completeness, correction rate, evidence/authority exceptions | A signed or hashed artifact does not prove its contents are true |
| Time and effort | Preparation, provider review, acceptance, recall/switch time | Separate automation speed from human-review time |
| Treatment and safety | Disputes, complaints, repeated contact, hardship/safety escalations, safe exits | Never optimize money by hiding or penalizing protective outcomes |
| Agreement durability | Kept arrangements, modifications, reversals, reopened disputes | Use a defined observation horizon and show censored/unknown outcomes |
| Continuity | Event coverage, correction propagation, export completeness, provider-switch success | Missing provider data remains missing; do not impute certainty |

Pre-register pilot baselines and success thresholds with design partners. Do not retrofit metrics after seeing the result or claim causal recovery uplift from selected cases.

Cross-border complexity supports investigation, not a revenue forecast. Allianz Trade estimates that 48% of international trade receivables in its analysis are exposed to very-high or severe collection-complexity countries, and USTR reports $239.6 billion of U.S.–India goods and services trade in 2025. Neither figure is GRE's addressable market. Size the business from reachable buyers, eligible annual cases, adoption, price, and support cost. [Allianz Trade 2026](https://www.allianz-trade.com/en_global/news-insights/news/collection-complexity-score-2026.html) · [USTR India profile](https://ustr.gov/countries-regions/south-central-asia/india)

### 7.7 Marketing claim ladder

Leadership positioning must be ambitious without outrunning evidence:

| Evidence state | Claims GRE may make | Claims GRE must not make |
|---|---|---|
| Designed/demo only | “Source-linked, versioned recovery preparation”; “built for independent provider handoff” | “Accepted by agencies,” “compliant,” “global,” “faster,” or “market-leading” |
| Shadow-tested | State the exact corpus, date, profile, measured extraction/review results, and limitations | Real-world recovery, live safety, or provider-acceptance claims |
| One live provider/pilot | Name only authorized partners; report exact pilot cohort and workflow results | “Network,” universal portability, or causal recovery lift |
| Two-plus independent accepting providers | “Portable across these named/qualified providers for this profile”; “switch demonstrated under these conditions” | Universal “no re-intake” or global coverage |
| Repeated comparable paid cohorts | Quantified time/rework/quality improvements with methodology and observation window | Unqualified superlatives or results outside the measured population |

“Market leader” should remain an internal objective until adoption and comparative evidence support a bounded external claim.

---

## 8. Go-to-market and development sequence

### 8.1 One launch program, two proof lanes, one incubated expansion

GRE should not announce four mature products. Enter with one coherent platform story and evidence at three different maturity levels:

| Lane | Offer | Buyer/user | Role in the launch |
|---|---|---|---|
| **Enterprise commercial lane** | **Trade Claim Readiness + Provider Preflight + Direct Recovery Transfer + Creditor Control** using the creditor's existing agency or approved panel | Anchor/channel creditor, insurer, factor, servicer, or recurring exporter | Paid proof of operational value and the primary revenue motion |
| **Controlled private lane** | **Private Resolution Room** for supported existing domestic personal obligations | Two voluntarily participating adults, preferably reached through a trusted sponsor/channel | Visible product proof and structured safety/behavior learning; not the primary revenue claim |
| **Institutional consumer lane** | **Consumer Mobility Continuity** design and shadow evaluation | Regulated lender/servicer and its compliance/operations teams | Strategic design-partner program; no live GRE-branded collections |

This resolves the requirement that the initial product demonstrate both a domestic U.S. personal-loan scenario and India-to-U.S. recovery without treating them as one legal service or launching an institutional consumer collector by accident.

The enterprise land-and-expand motion should be: **historical Readiness Diagnostic → one-provider preflight/transfer → recurring portfolio workflow → second-provider portability → Corridor Assurance → upstream Continuity Readiness**. Each expansion must earn a new budget or measurable job; do not give away the entire roadmap in a bespoke pilot.

### 8.2 Enterprise pilot design

The enterprise pilot should involve:

- one to three creditor-side design partners with recurring eligible commercial files, preferably including an anchor/channel with repeat distribution;
- an accountable finance/recovery buyer, an operations owner, a legal/compliance owner, and an information-security contact on the customer side;
- at least one incumbent agency per buyer and at least two independent providers across the overall pilot so portability can be tested;
- a signed/versioned Provider Acceptance Profile for every participating provider;
- 30–50 permissioned historical files spanning paid, disputed, rejected, unsuccessful, and unresolved outcomes for error taxonomy and shadow reconstruction;
- a small prospective cohort only after classification, data, security, hard-handoff, and provider-acceptance controls are ready;
- comparable files prepared through current practice and GRE where feasible, with selection rules documented before outcomes are observed;
- direct creditor-provider contracts already in place or executed through a reusable direct appointment flow;
- a planned recall/re-transfer simulation, including access revocation and data export, even if no live case needs switching;
- no live GRE obligor collection communications and no GRE funds flow.

The first paid entry offer may be a fixed-scope **Recovery Readiness Diagnostic**: reconstruct a historical cohort, quantify missing evidence/rework, map it to one or two provider profiles, and produce a business case. Credit some or all of that fee against a pilot only if the diagnostic demonstrates a viable cohort. This is a sales tool, not a substitute for a platform proof.

### 8.3 Private Resolution closed-beta design

Do not acquire a broad direct-to-consumer audience before safety and support costs are known. Prefer one trusted distribution partner such as a credit-union member program, employer financial-wellness benefit, community mediation/legal-aid partner, or other institution able to recruit both good-faith participants without coercion.

Before live cases, test synthetic and consented usability scenarios covering disagreement, non-participation, exact-term acceptance, withdrawal, identity mismatch, abuse indicators, and route-out. Then set a numerical cap with the counsel/safety reviewer and support owner. The earlier 20–40 figure is a provisional recruitment ambition, not evidence of safe capacity. Define the cap in admitted matters, count matters even if the other person never joins, and set a separate active-case/concurrency ceiling. Start in small tranches with human review and an incident/support owner for every admitted matter.

The beta must not create a collection funnel. It should measure whether GRE can help people clarify, agree, safely decline, or reach an appropriate qualified route. A repayment is one possible outcome, not the only success state.

Pre-register the Private funnel and decision thresholds separately: eligible requests, invitation attempts/delivery, independent enrollment, clarification, proposal/agreement or decline, and observed performance. Keep unreachable, excluded, declined, and withdrawn matters in their appropriate denominators. Measure comprehension, preparation-only usefulness, support minutes, privacy/safety events, and sponsor/user willingness to pay. Testing only already-cooperative pairs cannot establish usefulness for people whose earlier requests went unanswered. Honor refusal as a legitimate participant outcome even when low participation invalidates the business hypothesis.

### 8.4 Proof framework and provisional ambitions

Measure the complete job, not just model extraction:

| Proof area | Enterprise measures | Private Resolution measures |
|---|---|---|
| Readiness | Creditor preparation time; critical data/evidence/authority exceptions; corrections | Issue comprehension; ability to distinguish agreed, disputed, unsupported, and unknown points |
| Acceptance | Provider review time; first-pass/conditional acceptance; delta size; rejection reason | Invitation comprehension; verified voluntary participation; withdrawal/non-participation honored |
| Continuity | Event coverage/latency; correction propagation; recall, export, and switch time | Separate/private context integrity; exact proposal/version history; safe exit and route-out completion |
| Economics | Internal/external cost; support, compute/data, integration, and incident cost; willingness to pay | Support minutes; sponsor/user acquisition cost; fixed-fee or sponsor willingness to pay |
| Outcomes | Net proceeds, delay, dispute, complaint, reversal, closure, and censored outcomes over a defined horizon | Clarification, mutual agreement, durable performance where observable, documented disagreement, safety/complaint outcomes |
| AI quality | Raw model accuracy, final reviewed accuracy, abstention/exception rate, human effort, harmful-error tests | Symmetry/fairness tests, unsafe persuasion, false certainty, privacy leakage, human escalation |

The first enterprise cohort should pre-register commercially meaningful thresholds. A reasonable ambition to negotiate—not a public promise—is at least a one-third reduction in manual preparation/re-intake effort, a material reduction in clarification cycles, and a successful same-core transfer or switch across two providers. If buyers do not consider the agreed thresholds sufficient to change budget or workflow, meeting them is not product-market proof.

### 8.5 Commercial model defaults

- **Trade & Network:** paid diagnostic or implementation plus a platform/portfolio commitment and defined assessment, preflight, transfer, control, and observation units. External agency/counsel fees are contracted and paid directly.
- **Consumer Credit:** later enterprise platform, implementation, assurance, and volume-based service units; no borrower charge by GRE; pricing must not reward harmful contact volume or prolonged delinquency.
- **Private Resolution:** test transparent fixed, sponsor-paid, or membership pricing. Do not use percentage-of-claim pricing in the beta, and do not make one participant pay for more pressure on the other.
- **Provider Connect:** make early participation low-friction and normally free unless GRE supplies a separately valuable provider product. Never sell eligibility or rank. Disclose commercial relationships.
- **Corridor Assurance:** may become a subscription/enterprise add-on once GRE can prove maintained reviews, change-impact behavior, and support—not merely link to public legal sources.
- Defer outcome-contingent fees until attribution, reversals, licensing characterization, and incentive effects have been reviewed. Do not rely on them for launch economics.

GRE may receive payment for its own contracted platform or preparation service under the released pricing terms. Its service-fee invoice, taxes/refund obligations, and billing events must remain separate from money owed to a creditor or other participant. The no-custody boundary concerns third-party repayment/recovered funds, not ordinary payment for GRE's own services.

### 8.6 Sequence by evidence, not by ambition

| Sequence | Product work | Gate to proceed |
|---|---|---|
| **1** | Reconcile project documents, module ownership, and versioned reference-contract semantics; validate representative fixtures; then revise the backlog as described in Section 10.3 | Consistent document/contract baseline and a backlog traced to it; product implementation has not begun |
| **2** | Build one shared “case-to-accepted-handoff” demonstrator plus the separate Private Resolution Room path; use synthetic data | Security baseline, role clarity, reliable state semantics, red-team results |
| **3** | Run the Trade historical Readiness Diagnostic and Private synthetic/usability/safety program in parallel, reusing only safe Foundation modules | Named enterprise buyer/provider and private distribution/safety owners; counsel-scoped activities |
| **4** | Start the prospective Trade pilot and capped Private closed beta | Data permissions, direct appointments, support coverage, corridor/profile release records, stop controls |
| **5** | Activate the second accepting provider, demonstrate recall/re-transfer, publish a bounded benchmark/case study, and decide whether to publish the Passport core/conformance kit | Repeat use, provider value, measured workflow gain, authorized public evidence; the second provider may be recruited earlier without blocking the first diagnostic |
| **6** | Run Consumer Credit mobility discovery, data mapping, and shadow evaluation with a regulated institution | Named compliance/operations sponsor, enterprise trust readiness, current legal matrix, clear economics |
| **7** | Pilot a narrowly bounded Consumer capability without GRE-branded collection | Formal institutional release, monitored complaint/correction path, human operations, adversarial evaluation |
| **8** | Expand `PREVENT`, corridors, qualified routes, protocol adapters, or autonomy | Specific paid demand, data rights, calibrated assurance, provider capacity, and support economics |

Discussion priority is not implementation order. A founder may use managed/manual operations behind a coherent interface during validation, but the labor and limitations must be measured. Do not engineer every family, connector, or jurisdiction in parallel.

Consumer buyer discovery may run earlier alongside Trade/Private work; its listing here does not require waiting to ask useful commercial questions. Sensitive-data shadow work and any live capability still require their own release conditions. A sample-size ambition, two-provider public demonstration, advisory council, or certification target must not become an unexamined prerequisite for every synthetic slice or initial paid diagnostic.

### 8.7 The “enter with a bang” launch package

The launch moment should be proof-dense, not adjective-dense. Aim to have:

1. **A live case-to-handoff demonstration:** messy documents and ledger data become source-linked propositions, contradictions, gaps, a Claim Passport, route economics, and a provider-specific preflight.
2. **A visible acceptance moment:** a real participating provider accepts, conditionally accepts, or rejects through its declared profile and returns a precise validation delta.
3. **A switch demonstration:** access is revoked, the same core Passport is minimized for a second provider, authority is reissued, and history remains intact.
4. **A corridor assurance demonstration:** one effective-dated rule or provider-requirement change identifies affected cases and re-runs the relevant tests.
5. **A separate Resolution Room demonstration:** two parties see different private workspaces, a controlled shared fact map, exact proposal versions, and a safe decline/route-out.
6. **A public proof pack:** an authorized lighthouse case study or benchmark methodology, redacted sample Passport, profile/conformance example, security and data-use overview, corridor change log, and honest capability-status page.
7. **Named ecosystem credibility:** at least one creditor/channel design partner, two provider participants across the enterprise pilot, current corridor counsel, and an independent consumer/safety voice. Use names publicly only with express permission.

Do not coordinate the public launch around a feature-complete platform date. Coordinate it around a verified proof threshold.

### 8.8 Stop, narrow, or pivot triggers

- If reachable India-to-U.S. buyers do not have enough recurring eligible files, move the wedge to an embedded insurer/factor/servicer channel or another evidence-dense corridor; do not use trade-volume statistics as a substitute.
- If providers will not declare acceptance requirements or cannot consume a common core without full duplicate intake, determine whether GRE should sell preparation to providers instead. Do not claim a network effect that does not exist.
- If the Trade workflow does not materially reduce total labor, critical errors, or activation delay, narrow to the highest-friction claim subtype or stop the transfer/control expansion.
- If creditors overwhelmingly value one-stop execution over portability, retain Claim Readiness as a product and reassess whether a licensed/managed structure is strategically justified; do not quietly blur the hard-handoff boundary.
- If Private Resolution produces weak voluntary participation, disproportionate support cost, unsafe use, repeated-contact behavior, or poor sponsor economics, keep it as research or an embedded qualified-partner tool rather than a public growth product.
- If counsel determines a planned activity requires licensing or a materially different regulated role, either obtain the authority and operating capacity deliberately, place it with a qualified partner, or remove the activity. Contract wording is not a workaround.

---

## 9. AI, data, and technical strategy

### 9.1 AI role

AI may extract, reconcile, classify, summarize, translate, identify contradictions, draft, simulate scenarios, recommend, and perform bounded low-risk operations under explicit policy. It must not create legal rights, authority, verified facts, payment truth, final legal conclusions, or permission to contact.

Every consequential use needs:

- exact input and output references;
- model/workflow/version identity;
- family, corridor, purpose, and policy context;
- confidence, uncertainty, and known limitations;
- human review or an independently enforced bounded delegation where permitted;
- exact action binding and current-state recheck before dispatch;
- outcome and correction capture under applicable data rights;
- adversarial, bias/harm, privacy, and model-substitution evaluation.

Treat every uploaded document, email, message, webpage, provider response, and model-generated artifact as untrusted input. The ingestion path needs file-type validation, malware scanning, isolation, hidden-content and prompt-injection defenses, source preservation, structured extraction boundaries, and human review for consequential propositions. A document's instructions must never override GRE policy, authority, or system instructions.

AI assistance must be role-aware. In Private Resolution, one participant's assistant cannot reveal or optimize against the other's private strategy. In Consumer, AI cannot suppress a dispute, complaint, hardship, representation, or protected-treatment signal because a model predicts lower recovery. Translation and summarization are derived artifacts and do not replace the source.

Customer and participant data must be excluded from provider-model training by default unless a separately documented right, purpose, notice/consent or other lawful basis, customer configuration, and retention process permits the exact use. A model vendor's “no training” setting does not eliminate GRE's own minimization, transfer, logging, and deletion duties.

Use NIST's voluntary AI Risk Management Framework concepts—govern, map, measure, and manage—as an assurance reference, not as a compliance certificate. [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/)

### 9.2 Architecture direction

- Begin with a modular monolith and explicit module/data ownership.
- Use shared Python domain modules with explicit owners and family/corridor policies; API handlers and Temporal workers call the same domain operations. A canonical meaning does not require one giant service class or one universal workflow.
- Keep models, document processing, communication transports, payments, workflow engines, and external protocols replaceable.

- Preserve the selected Next.js/TypeScript, FastAPI/Pydantic/Python, PostgreSQL, Temporal, Azure Blob, and generated OpenAPI-client direction and verified lockfiles unless a concrete revised requirement justifies an ADR. “Replaceable” means explicit interfaces and known migration costs, not a promise of costless portability. Production regions, provisioning, real identity/payment/OCR/model integrations, and customer-specific data topology still need implementation decisions.
- Keep authoritative records distinct from suggestions, imports, and provider observations.
- Preserve bitemporal/effective-date behavior for law, rights, authority, evidence, and policy.
- Make every cross-family data access purpose-bound; shared code does not imply shared tenant, participant, or training access.
- Use APIs and events because they improve real interoperability, not to perform architectural theater.
- Keep an internal relationship model that can answer graph-shaped questions without committing to a graph database.
- Do not use blockchain or tokenization for ordinary provenance; signed/versioned records and access controls are the baseline.
- Do not create a multi-agent swarm as a product architecture. Logical agents/capabilities may run through ordinary services and queues.

### 9.3 Data model additions or generalizations

The next contract version should consider explicit support for:

- `matter_family_profile` and profile version, separate from commercial offering/edition entitlements;
- Claim Passport core/profile version and conformance result;
- obligation purpose and classification confidence/source;
- creditor/rights-holder regulatory type;
- natural-person involvement and mixed-purpose hold;
- origin, current, contact, processing, payment, forum, and executor jurisdictions;
- `service_mode` and executor/authority pattern;
- communication identity and accountable principal;
- direct provider appointment and contract reference;
- Provider Acceptance Profile version, declared requirements, provider-authored status, and effective period;
- immutable handoff snapshot and disclosure manifest;
- provider validation delta, conditional acceptance, rejection, and reasons;
- Authority Envelope and Action Receipt lineage;
- GRE operational-role termination time;
- separate external engagement, GRE service, and case states;
- post-handoff observation/control scope;
- complaint, hardship/vulnerability, communication preference, representation, and dispute continuity for Consumer;
- correction request, accountable owner, downstream propagation, response, and receipt state;
- protected-treatment/hold indicators and qualified-review ownership without exposing unnecessary sensitive details;
- separate participant contexts, shared facts, participation consent, safety state, and route-out for Private;
- invitation source, attempt count, withdrawal/non-participation, and no-further-contact state for Private;

- privacy-reviewed repeat-invitation/misuse controls across reopened or duplicate submissions, without exposing another user's records or creating a general cross-tenant debtor index;
- provider credential, license, insurance, jurisdiction, capacity, conflict, and review validity;
- corridor source/reviewer status, review expiry, rule change, affected-case set, and regression result;
- privilege, confidentiality, trade-secret, legal-hold, and disclosure-review treatment;
- Resolution Quality Scorecard dimensions, observation horizon, missingness, comparison cohort, and attribution limitations;
- data-purpose permissions for service, evaluation, benchmarking, and training;
- legal-source/review status independent from commercial capability status.

Do not add every possible field to one giant universal record. Use a stable core plus validated family/corridor extensions with explicit compatibility rules.

### 9.4 Enterprise trust and procurement readiness

Trust is part of the product, not a later compliance project. Current competitors publicly market ISO, SOC, PCI, SSO/MFA, penetration testing, audit, and continuity controls. GRE must sequence honestly:

| Release level | Minimum evidence |
|---|---|
| **Synthetic demonstrator** | Secure development baseline; secrets and dependency management; test-data policy; authorization model; audit events; backup/restore test; no production claims |
| **Sensitive-data enterprise pilot** | Data inventory/flow map; DPA and subprocessor register; least privilege, MFA and tenant isolation; encryption in transit/at rest; retention/deletion/export; secure file ingestion; vulnerability management; logging/monitoring; incident response; business continuity/disaster recovery; access review; independent penetration test or buyer-accepted equivalent; named security owner |
| **Regulated institutional pilot** | Enterprise SSO/SAML and role lifecycle where required; stronger environment and data-residency controls; formal vendor-risk package; model inventory/evaluation/change control; complaint/correction operations; evidence of recovery and incident exercises; customer audit/regulator-access terms; appropriate insurance |
| **Scaled enterprise availability** | Buyer-validated availability/support; repeatable implementation and offboarding; continuous control monitoring; and SOC 2 Type II, ISO 27001, PCI, or other independent assurance where the product and buyer actually require it |

Do not claim a certification, “bank grade,” regulatory approval, or full compliance before the precise scope is independently established. A trust center may publish current policies, subprocessors, architecture summaries, status, and completed evidence while clearly marking unavailable reports.

### 9.5 Future-facing interoperability without protocol theater

GRE should be compatible with the coming agent-to-agent ecosystem, but its domain contracts must remain independent of any one protocol:

- W3C Verifiable Credentials 2.0 may eventually help represent provider credentials, organization roles, or bounded authority in a tamper-evident and selectively disclosable form. The W3C specification is explicit that cryptographic verification does not prove the truth of the encoded claim; GRE must retain issuer trust, validation, revocation, purpose, and privacy rules. [W3C Verifiable Credentials 2.0](https://www.w3.org/TR/vc-data-model-2.0/)
- A2A or successor agent protocols may transport discovery, tasks, status, and artifacts between creditor and provider agents. They do not supply GRE's classification, legal authority, acceptance, or action-control semantics. [Linux Foundation A2A](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents)
- AP2 mandate patterns may inform exact user intent, authorization, and tamper-evident receipts for future payment links. AP2 does not authorize GRE to transmit money or decide a settlement, and payments should still occur through qualified institutions. [Google AP2](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol)
- MCP or successor tool protocols may expose narrowly scoped retrieval and operations to enterprise assistants. Use explicit scopes, human-visible authorization, output filtering, rate limits, and audit; never expose a broad “act on case” tool.

Implement ordinary APIs/events and the internal permission model first. Add protocol adapters only when a named customer/provider integration or distribution channel requires them.

### 9.6 Data-learning strategy

The data moat should begin with tenant-private value. Later pooled products may use aggregation thresholds, de-identification, clean-room/federated computation, differential privacy, or confidential-computing patterns where proportionate, but none removes the need for rights, purpose, security, competition, re-identification, and fairness review.

The safest compounding data initially are structural and operational: which declared requirement caused a provider delta, which fields caused rework, how long a transition took, which events were missing, and whether a correction propagated. GRE does not need the most intimate consumer data to learn how to make recovery infrastructure work better.

---

### 9.7 Modular reuse and implementation depth

Use one repository and a modular application, with an API process and worker processes where needed. Family packages compose shared domain operations; they do not copy models, money rules, access checks, or effect logic. A module boundary is ownership inside the application, not a reason to create another deployment. The existing Python/TypeScript split and generated client remain useful.

| Module boundary | Canonical responsibility | Reuse and protection |
|---|---|---|
| Identity and access | Actor mapping, membership, participant access | Shared checks; identity never grants case authority or proof of debt |
| Evidence and Passport | Sources, assertions, reviewed findings, versioned Passport views | Same evidence machinery; family-specific readiness and permitted views |
| Obligations and financial position | Asserted obligations, exact money/currencies, receipts, allocations and reversals | One authoritative financial history for permitted related services; no separate editable family balance |
| Authority and action control | Grants, approvals, exact bindings, commit checks, outbox and effect receipts | Every API, worker and adapter invokes the same controls |
| Classification and policy | Matter profiles, corridor versions, evaluations and release conditions | Separate from billing entitlements; unknown classification fails closed for affected actions |
| Case and service coordination | Service boundaries, responsible owner, waiting, expiry and surviving duties | Shared primitives; Trade transfer and Private participation use different state machines |
| Provider interoperability | Provider profiles, preflight, placement, acceptance delta and returned events | Shared by Trade and later eligible Consumer services; private decline never activates it automatically |
| Participation and agreements | Exact proposals/acceptances and performance references | Shared agreement semantics; family-specific participation, representation and privacy policies |
| Disclosure and correction | Scoped exports, redaction, recipient access and correction delivery | One disclosure check; sharing a Passport does not share all source material |
| Observations and assurance | Attributed events, quality measurements, evaluation and public-claim evidence | Read models derive from source facts; they cannot overwrite payment or authority truth |

These responsibilities can begin in a small number of packages. Name their owner, public operations, permitted dependencies and transaction boundaries in the architecture record; avoid generic plug-in frameworks or dozens of empty modules before a real slice needs them. PostgreSQL holds business truth. Temporal holds durable progress and invokes domain operations. Transport adapters translate external formats and return observations; they do not independently approve business actions. The web consumes generated contracts and does not reimplement authoritative rules.

Map the six strategic contracts onto the reference before adding records:

| Strategic contract | Existing reference basis | Required treatment |
|---|---|---|
| Claim Passport | `claim_passport`, evidence/assertion/verification and financial/rights references | Extend the existing snapshot and profile semantics; preserve canonical source lineage |
| Provider Acceptance Profile | Provider party/verification, `capability`, per-case `work_order` | Add standing provider-authored requirements; keep them separate from each placement and its response |
| Authority Envelope | `authority_grant`, `rights_interest`, `approval`, `policy_snapshot`, `ActionBinding` | Compose authoritative references and exact limits; an exported envelope cannot mint a new grant |
| Corridor Pack | `corridor_pack`, `policy_snapshot`, `capability` | Extend directional scope and review metadata; separate source rules, case evaluation and commercial release |
| Action Receipt | `execution_receipt`, `action_intent`, `approval`, `event`, `model_execution` | Extend or compose per-attempt evidence, including uncertain effects; do not invent a competing success ledger |
| Resolution Quality Scorecard | `outcome_observation`, financial/payment, decision, work-order and event records | Derive versioned metrics with denominator, observation horizon and source references |

Each fact has one canonical owner/writer; compositions may snapshot references without becoming independently editable truth. Existing tenant-contained references need an explicit receiving-side mapping for provider profiles, exported Passports and shared policy definitions. Reused source IDs never grant cross-organization read access. Preserve unknown or unmappable legacy fields for review; do not infer authority during migration.

| Area | Define in the document/reference pass | Minimum implementation when its pilot lane is built | Later depth to retain in the future register |
|---|---|---|---|
| Shared Foundation | Ownership, invariants, versions, disclosure and action contracts | The shared operations exercised by a complete Trade slice and a complete Private slice | Specialized stores, distributed services and broad framework machinery only for measured needs |
| Six platform contracts | Minimal meanings, source mappings and compatibility | Only the fields/operations needed for scoped readiness, acceptance, authority, receipts, release and basic quality reporting | Public standard/conformance ecosystem and advanced assurance products after adoption proof |
| Trade + Network | Named profile, actors, responsibility cutover and exceptions | Reviewed preparation; provider preflight and explicit direct acceptance; permitted corrections, observations, export and recall. Secure assisted import/export may be the first adapter | Many providers, rich portals, automated source connectors and portfolio optimization |
| Private | Preparation-only, invitation, bilateral room, safe exit, agreement and payment-state semantics | Useful preparation even without participation; independent access; controlled sharing; exact acceptance; bounded performance/reconciliation and support | Wider obligations/states, channels, qualified routes and advanced two-sided AI after evidence |
| Consumer | Classification, data/topology assumptions, representative inactive fixtures and activation gates | No live Consumer operations implied; only agreed design/shadow work under its own data permissions | A separately released institutional capability with its partner, procurement and legal conditions |
| Analytics and interoperability | Source-honest measures and ordinary API/event contracts | Tenant-private basic metrics and one real needed provider adapter | Pooled learning, advanced rankings, public APIs/protocol adapters and published standards |

Implementation proceeds through complete vertical slices. For each slice, build only the shared capabilities it uses, then exercise reuse in the second family rather than copying code. The two lane workflows may share a timeline component, for example, while retaining different disclosure, invitation, and handoff rules. Optional modules stay unavailable until explicitly released. Every manual pilot step still needs an owner, evidence, failure path and measured cost.

---

## 10. Required changes to current project artifacts

| Artifact | Required scope update |
|---|---|
| **Business & Project Overview** | Replace the one-product/B2B/operator-first summary with the umbrella category, four-family portfolio, creditor-first economic buyer, two-lane entry program, gated institutional Consumer expansion, hard-handoff value proposition, six platform contracts, and updated commercial boundaries. Preserve honest project status and unvalidated assumptions. |
| **Product Offering & Competitive Strategy** | Recast Intelligence/Operations/Network/Control as capability domains. Define all four product families, ICP/anti-ICP, jobs, packages, risk postures, proof requirements, chosen competitive battlefield, Provider Acceptance Profile, Corridor Assurance, provider-adoption strategy, staged openness, claim ladder, and evidence-gated roadmap. Remove any implication that AI outreach, a country count, routing, a graph, or agentic terminology alone is differentiation. |
| **Operating Model** | Generalize universal records and gates beyond B2B. Add the full classification model, family-specific operating profiles, executor/authority patterns, direct appointment, hard-handoff sequence, creditor-versus-GRE control attribution, Provider Acceptance Profile, validation delta, Action Receipt, correction relay, corridor change impact, separate post-handoff states, and family-specific exclusions. Retain case/service separation, authority, prepare/commit, financial, event, and observation invariants. |
| **Workflow & Interaction Specification** | Replace the single B2B default with a shared core journey plus family profiles. Keep a Trade case-to-accepted-handoff and recall/switch journey; add the bounded Private Resolution Room path; represent Consumer mobility as a design/shadow variant until released. Make transfer completion, post-handoff observation, corrections, complaints/safety, and direct creditor decision ownership visible. |
| **Domain & Data Contracts** | Define core-versus-profile ownership; version the contract; generalize B2B enums and required fields; add classification, Provider Acceptance Profile, handoff, direct appointment, role termination, validation delta, Authority Envelope, Action Receipt, correction propagation, privilege/disclosure treatment, scorecard dimensions, family extensions, and legal-review status. Do not break old records silently. |
| **Schema package and validator** | Preserve the existing B2B fixture as a Trade legacy/reference fixture where useful. Add or revise fixtures and negative tests for hard handoff, consumer controls, private contexts, and profile compatibility. Update validation code and contract version together. |
| **Pilot/MVP brief** | Define the enterprise Trade pilot and capped Private Resolution beta as separate lanes with shared-foundation dependencies. State exact included/excluded actions, cohorts, comparison method, participants, support owners, metrics, legal/security gates, stop conditions, and public-claim permissions. |
| **Security, assurance, and legal-release plan** | If no artifact owns these topics, create one. Map the trust release levels in Section 9.4, family/corridor/activity legal reviews, source/reviewer/effective dates, control evidence, model-risk records, incidents, change impact, and review expiry. Do not bury this only in product prose. |
| **Market-validation and launch-proof plan** | If absent, create a lean artifact for ICP interviews, buyer/provider commitments, Readiness Diagnostic, benchmark methodology, claim ladder, public proof pack, launch threshold, and stop/pivot triggers. |
| **Future-development plan** | Align horizons with the evidence sequence in Section 8.6. Keep debt purchase, principal collection, owned enforcement, custody, broad underwriting/O2C, consumer reporting, and autonomous legal action outside the promised roadmap unless the owner explicitly reopens them. |

### 10.1 Required workflow/contract tests

At minimum, add acceptance or conformance tests proving that:

1. A consumer or mixed-purpose indicator cannot pass through a Trade-only scope gate.
2. Completing `ASSESS` or `TRANSFER` does not mark the obligation paid, resolved, released, or closed.
3. Transfer cutover fences new commits under the ended GRE service and cancels queued work that remains cancelable; in-flight, already-sent, and uncertain effects retain receipts and reconciliation paths.
4. GRE cannot represent a placement as active or enable provider execution through its interfaces without a current direct appointment, explicit acceptance, satisfied execution conditions, and current applicable gates. Permitted preflight review access is separate.
5. The agency may conditionally accept or reject without forcing full duplicate intake; the validation delta remains visible.
6. The disclosure package contains only permitted data and preserves a manifest of included, withheld, and redacted material.
7. The agency uses its own communication identity after handoff.
8. A provider report is an observation and does not directly write trusted payment, agreement, rights, or closure state.
9. A separate `CONTROL` or `OBSERVE` request can continue after `TRANSFER` without giving GRE authority over tactics.
10. Creditor-attributed instructions cannot be mistaken for GRE decisions.
11. Recall or provider loss of eligibility revokes GRE-controlled access, cancels what can still be canceled, tracks external cessation acknowledgment and uncertain effects, and gates replacement activation against conflicting mandates. It never claims to erase previously exported provider records.
12. No repayment or recovered-funds destination resolves to a GRE custody/pass-through account in baseline profiles. GRE billing for its own separately disclosed service is distinct and cannot be mistaken for repayment of the underlying obligation.
13. Consumer hardship, complaint, representation, opt-out/preference, identity mismatch, and insolvency/bankruptcy signals suppress incompatible automation and route to the accountable owner.
14. Private Resolution keeps each participant's private strategy separate from the shared record and requires independent exact-term acceptance.
15. Private safety route-outs prevent repeated engagement and inappropriate automated pressure.
16. Historical evaluation reproduces the applicable effective records; a newly proposed action also passes current applicable law, authority, holds, and release conditions. Neither the newest retrieved page nor an old frozen Passport alone authorizes a new act.
17. Training or pooled benchmarking is rejected unless the specific data policy permits it.
18. Product availability and legal-review status are checked independently.
19. Preflight is evaluated against an exact Provider Acceptance Profile version; an effective requirement change expires or re-runs affected readiness results rather than silently preserving them.
20. Provider acceptance is distinct from GRE transmission, legal approval, factual verification, and execution start.
21. Action Receipts preserve proposer, principal, reviewer/approver, transmitter, external performer, observer, version, time, and uncertainty without misattributing a provider act to GRE.
22. A corridor-rule change identifies potentially affected cases and tests but does not retroactively rewrite historical facts or automatically authorize a new action.
23. A correction preserves the superseded assertion and source, routes to the accountable owner, and propagates only to permitted downstream recipients with receipt/error state.
24. Privileged, confidential, trade-secret, legally held, and restricted data cannot enter a provider disclosure merely because it exists in the Passport.
25. A Private invitation limit, decline, withdrawal, or no-further-contact state prevents additional automated invitations and cannot trigger an agency transfer.
26. Private Resolution cannot accept an institutional creditor, assigned/purchased debt, excluded obligation type, unsafe case, or unverified repeated-use lender into the beta profile.
27. A new Private agreement cannot become accepted without all required parties independently accepting the same exact version. Agreement acceptance, performance, verified repayment, release/discharge, documented disagreement, and service completion remain separate; an installment promise does not mark the obligation paid.
28. Consumer-report retrieval, credit-bureau furnishing, and adverse-action generation fail closed in baseline profiles. GRE charges to consumers for institutional recovery activity are prohibited; Private service pricing follows its separately released transparent terms and cannot purchase additional pressure.
29. Family/participant isolation prevents Trade or creditor data, one private participant's strategy, or one tenant's observations from appearing in another context or training corpus without an explicit permitted policy.
30. Export/recall/re-transfer produces a complete allowed core plus a manifest of withheld/redacted data, revokes obsolete access, and does not carry expired authority to the next provider.
31. An MCP, A2A, AP2, or other external-protocol adapter cannot bypass the same identity, authority, policy, prepare/commit, payment, and audit controls as the ordinary interface.
32. Public capability and performance claims resolve to current evidence, profile/corridor scope, date, and approval; expired or broader claims fail the publishing gate.

33. A Network & Control entitlement cannot bypass the underlying Trade, Consumer, or Private profile and release conditions.
34. Declined or unanswered Private participation still permits the scoped preparation deliverable and safe service closure, without an admission, new contact, or automatic professional referral.
35. Partial/external payments, duplicates, reversals, amendments, and missed performance preserve the correct financial and agreement states without invented penalties or collection authority.
36. Sponsor or payer status never grants another participant's private data; permitted correction/export/withdrawal behavior remains explicit.
37. Reopened or duplicate submissions cannot reset applicable invitation suppression; the control itself does not reveal other tenants' cases.
38. A frozen Passport or receipt cannot override data retention/deletion policy, a current hold, revoked authority, or a corrected fact.
39. Provider silence, rejection, failed event return, or stale data produces a visible exception, freshness timestamp, and responsible owner; it is not reported as successful placement, recovery, or confirmed cessation.

These are behavioral acceptance requirements. During reference reconciliation, implement conformance tests only for the represented semantics and mark other items as future product/integration checks. For unreleased profiles, test fail-closed activation plus representative contract examples; do not build an entire live Consumer application merely to satisfy this list. A passing reference validator does not establish runtime authorization, safe external execution, or production readiness.

---

### 10.2 Inspected baseline and preservation rules

The following GitHub state was inspected on September 7, 2026. These are repository observations and previously recorded Mac verification results, not a new run on the developer's laptop:

| Baseline | Observed state | Reconciliation treatment |
|---|---|---|
| `main` | `3fca8a93ac86852fbc44b0b3265143045bc5eecd` | Historical default branch; it does not yet contain all setup work |
| `setup/devcontainer` / PR #1 | `5511b1ef3096b7791a3c8be62a916c469c9f3a73`; open draft | Preserve the verified environment, locks and setup fixtures; review integration separately |
| `docs/pilot-backlog` / PR #2 | `2f8721b928e0faa728bb7697226b272a6d9693e4`; open, no longer draft; based on `setup/devcontainer` | Historical planning baseline, not authority to build the old scope; neither PR was changed by this review |
| Documents and reference | Docs 00–11, README, AGENTS, stack/environment/dependency guides, original contract ZIP | Inventory exact paths, versions and source hashes; reconcile stale prose without deleting historical evidence |
| Runtime state | Verified ARM64 toolchain, PostgreSQL, Temporal, Azurite and FastAPI/Next/generated-client fixtures | Useful reusable setup; no implemented customer product, migrations, product CI or live integrations asserted |

[PR #1](https://github.com/vishal-baliga/global-recovery-engine/pull/1) · [PR #2](https://github.com/vishal-baliga/global-recovery-engine/pull/2) · [Dependency baseline at the verified commit](https://github.com/vishal-baliga/global-recovery-engine/blob/5511b1ef3096b7791a3c8be62a916c469c9f3a73/docs/10-dependency-baseline.md)

Retain TypeScript 6.0.3's documented compatibility fallback and the existing locked versions; this scope review is not an upgrade task. Existing operational limitations—host attachment after editor recreation, remaining digest pins, backup/restore and upgrade validation, and historical workflow-retention versus health-check behavior—remain engineering work with honest prior status. Do not repeat completed setup or claim these limitations were fixed here.

The revised directive is the scope authority for the next pass. For reconciled project documents, use one reviewed Git revision as the canonical content and update the corresponding attached/shared document identities from it. Keep a manifest of repository path, commit/content hash, document identity/version and sync status. Do not maintain independently edited “ChatGPT” and “GitHub” versions of the same specification. The attachment reviewed here was edited as the same document; other attachments remain unchanged until reconciliation.

### 10.3 Ordered reconciliation plan

This is a document and contract migration plan, not the replacement implementation backlog.

| Pass | Work and owning artifacts | Completion evidence |
|---|---|---|
| **R0 — Baseline and change authority** | Refresh actual branch/PR state, current files and document identities. Record this directive, source precedence, retained setup and all material scope changes. Choose an isolated reconciliation branch containing the verified setup and historical planning baseline; preserve unrelated work. | Inventory and decision log; no assumed merge or destructive overwrite |
| **R1 — Product promise and scope** | Update 01 business, 02 offering/strategy, 06 pilot and 07 future register together. Specify matter profiles versus commercial editions, buyer priority, both proof lanes, exact service outcomes, excluded acts, release status and commercial hypotheses. | Every old pilot deliverable has a disposition, customer impact and owner; every future candidate or strategic exclusion remains recorded |
| **R2 — Operating and module design** | Update 03 operating model, 04 workflow and 08 architecture. Define module ownership, qualified state axes, staged disclosure/acceptance/cutover, Private non-participation and performance paths, manual responsibilities, classification/release gates and data topology. Give legal/security release evidence and market-proof work an owning artifact; create a lean plan only where none exists. | Representative Trade and Private journeys plus failure paths trace to one owner per fact/decision; inactive Consumer remains explicit |
| **R3 — Versioned reference contracts** | Reconcile 05 and the schema/fixture/validator/test package as one change. Map all 29 records and 23 operations and the six proposed strategic contracts. Preserve v0.1.0 as historical; introduce a new version for breaking changes with a migration/compatibility note. | Executed reference checks for represented semantics, legacy compatibility or explicit rejection, representative new fixtures, schema/reference consistency and no silent permission widening |
| **R4 — Publish a consistent document baseline** | Reconcile 00 checkpoint, README and AGENTS; refresh scope/sequence references in 09 environment and 10 dependency baseline while preserving observed results. Complete the cross-file matrix, source/review register and unresolved decisions. Publish reviewable document changes and synchronize corresponding shared documents from the exact reviewed revision. | Content/hash/version manifest, internal-link checks, consistent terminology and status; actual test results identified by environment; PRs remain reviewable without an assumed merge |
| **R5 — Revise the backlog** | Only after R1–R4 agree, reconcile 11 and every GRE-001–048 item with the new scope, module ownership, implementation depth, dependencies and acceptance evidence. Preserve IDs/history and map replacements/splits. Carry forward F-P/F-B/X references and unresolved external dependencies. | A prioritized backlog with complete scope coverage, no duplicated foundational stories, and explicit pilot/manual/future/excluded dispositions |
| **R6 — Begin product development** | Build a bounded synthetic vertical slice on the retained stack, reuse its domain operations in the second lane, then expand through the appropriate real-data/provider release gates. | Reviewable changes and focused behavioral evidence for each slice; no family activation merely because code was deployed |

Detailed product migrations, specialized inactive-family extensions and integrations can be designed in their dependent stories. The pre-backlog reference pass establishes the shared meanings and breaking contract semantics; it does not require implementing every reference record or all later capabilities. Preserve the original ZIP in version history and record its hash before producing a replacement version; do not regenerate it as if the original had always represented the new portfolio.

The current PR #2's old scope must not be merged or treated as the new accepted build plan merely because its GitHub review status changed. Reconcile PR bases and content explicitly when publishing the new document/backlog baseline. The user's prior request to keep setup PR #1 in draft remains in force unless changed. Publishing or merging status is not evidence of product availability.

### 10.4 Traceability and missed-opportunity checks

The change matrix should use one row per substantive requirement, with: old artifact/section or backlog/future ID; `KEEP/GENERALIZE/MOVE_TO_FAMILY_PROFILE/MOVE_TO_CORRIDOR_PACK/REPLACE/DEPRECATE` disposition; new owning section/module/profile; rationale and customer impact; required software, manual or partner route; implementation/release depth; dependencies; acceptance evidence; accountable owner; unresolved decision and reconsideration trigger. `NEEDS_COUNSEL` and `NEEDS_VALIDATION` are review flags that can accompany a disposition, not excuses to lose the requirement.

In particular, preserve and resolve:

- The two original real-world scenarios as representative acceptance paths. A one-off creditor may be a useful case-design example without being the recurring enterprise sales ICP. No real case is admitted merely because it appears in a synthetic example.
- Standalone paid preparation/readiness and permitted safe export when a provider declines or a private respondent never joins. Validate whether that outcome is worth buying; do not imply collection success.
- Import of existing agreements, representatives, prior payments and external work at their verified current position, so customers are not forced to restart at origination.
- Low-friction assisted import/export before a broad integration catalog; provider acceptance and return-data obligations are part of the paid pilot contract, with freshness and missing-data reporting.
- Trade performance disputes, credits, insurer/factor/servicer rights and relevant preservation duties. A provider transfer must not silently drop export, insurance, limitation, tax/FX or other outstanding responsibilities; identify the qualified owner and source of each applicable duty.
- The commercial choice to prioritize recurring creditors and bounded Private assistance. Record the old end-to-end coordination/contact/servicing promises that are replaced, which actor now performs each action, and the lost convenience/market segment to test.
- Every retained future development and business candidate, including domestic India and U.S. enterprise profiles, reverse corridors, Consumer mobility, richer provider integrations, stronger assurance and protocol/data products. Excluded models remain exclusions rather than promised upgrades.

---

## 11. Contract and organizational structure

### 11.1 Baseline agreements

The project should anticipate, without drafting final legal language:

1. **Creditor–GRE master agreement and product schedule** defining the exact family, corridor, service modes, deliverables, boundaries, support, fees, data roles, security, incidents, correction, and exit assistance.
2. **Creditor–provider direct collection/professional agreement** defining mandate, communications, settlements, payment, fees, complaints, supervision, insurance, indemnity, and provider conduct.
3. **GRE–provider technical/data exchange agreement and profile schedule** defining access, permitted use, security, disclosure limits, Provider Acceptance Profile authorship/change control, acceptance/events, incident reporting, interface conformance, export, and protection of identities; it must not quietly make the provider GRE's collection subcontractor.
4. **Data-processing and cross-border transfer terms** appropriate to each party's actual role and jurisdiction.
5. **Private Resolution participant terms, privacy notice, invitation rules, and safety policy** separate from enterprise creditor terms, plus a distribution/sponsor agreement where a partner recruits or pays for users.
6. **Evaluation, benchmark, and public-evidence terms** defining which data may be used for service, tenant-private evaluation, pooled benchmarking, model training, case studies, or public claims. Do not infer one use from another.

Tripartite onboarding, reusable direct panel terms, and click-to-appoint mechanics may reduce friction, but the creditor's direct appointment and the provider's independent acceptance must remain substantively real.

### 11.2 Insurance and diligence

Define evidence and review requirements for GRE and providers, including appropriate cyber, technology E&O/professional, collection-agency, legal-professional, crime/fidelity, and other relevant coverage. Insurance supports loss allocation; it does not certify permission or erase responsibility.

Keep provider credentials effective-dated and independently reviewable. A badge in GRE is not a regulatory endorsement.

### 11.3 Governance that supports category leadership

Before scale, create a small external challenge structure rather than a decorative advisory board:

- **Creditor Design Council:** finance/recovery, legal/compliance, vendor-risk, and operations users who review buyer value, controls, and benchmark relevance.
- **Provider Implementation Council:** at least two independent agencies/law firms or other executors who review intake burden, acceptance semantics, event return, recall, and commercial fairness.
- **Participant and Safety Voice:** an independent consumer advocate, mediator/ODR expert, legal-aid professional, or safety specialist with authority to challenge Private and Consumer designs.
- **Corridor Counsel:** qualified U.S. and India counsel or coordinated counsel work product for the precise released corridor and activities.
- **Security/AI reviewer:** independent review proportionate to the data and automation risk, especially before regulated Consumer work.

Record conflicts, compensation, recommendations, management decisions, and unresolved objections. Councils advise and test; they do not create legal approval or transfer accountable operating decisions away from GRE and its customers.

### 11.4 Umbrella and entity structure

Use one GRE brand and Foundation, with separate product schedules, ledgers, access policies, support queues, risk registers, insurance mapping, release manifests, and data-use policies from the start. Do not create multiple companies merely to make the portfolio diagram look sophisticated.

Trigger a formal entity-structure review if a family would require a collection/servicing/LSP/payment/mediation or other regulated license; become principal or fund holder; create incompatible duties to opposing participants; require materially different insurance or capital; expose regulated customer data to a different workforce; or justify independent investment/tax treatment. If separate entities are later used, preserve real contracts, governance, operations, data access, capitalization, and representations between them. Corporate separation can allocate and contain some risk; it does not erase GRE's own acts or prevent claims across entities.

---

## 12. Owner decisions and explicit change controls

The following defaults govern until the project owner explicitly changes them after evidence and, where applicable, counsel review:

- creditor-side primary buyer;
- Trade + BYO-agency Network/Control as the first commercial bundle;
- a coordinated two-lane entry program: enterprise Trade as the revenue/credibility lane and a separately gated U.S. domestic Private Resolution closed beta as the product-visibility/learning lane;
- the initial “domestic U.S. personal-loan” requirement means an existing privately originated obligation in the bounded Private Resolution profile, not institutional consumer debt; changing that interpretation requires an explicit owner decision and the Consumer release gates;
- India-creditor/U.S.-business-obligor as a validation candidate, not a committed launch fact;
- no GRE-branded post-default collection communications;
- no GRE custody, commingling or pass-through control of participant repayment or recovered funds;
- no GRE debt ownership or principal collection role;
- no consumer-report access, credit-bureau furnishing, or general credit scoring;
- no outcome-contingent fee at initial launch;
- no open provider marketplace or pay-to-rank;
- no pooled training/benchmarking without separate rights;
- no Consumer live launch without a regulated design partner;
- no Private live beta without activity/state legal review, independent safety input, strict case exclusions, invitation limits, monitored support, and a volume cap;
- Provider Acceptance Profile, Authority Envelope, Corridor Pack, Action Receipt, and Resolution Quality Scorecard as first-class contracts alongside Claim Passport;
- staged openness: prove bilateral acceptance before publishing a minimal Passport core or conformance kit;
- one modular technical foundation with profiles, not separate codebases;
- no blockchain, tokenization, graph-database mandate, proprietary model, or agent swarm.

The following remain genuine decisions—not facts to invent during documentation updates:

- GRE's legal entity domicile and eventual subsidiary structure;
- the final first buyer, claim subtype, amount/age band, pricing, and SLA;
- whether the first corridor has sufficient reachable paid volume;
- the exact anchor/channel strategy and which partner owns distribution for each launch lane;
- exact activities GRE will ever perform before transfer, including any location verification or creditor-branded communications;
- which agencies/providers will integrate and under what commercial terms;
- the precise Consumer mobility pilot and institutional partner;
- the final Private Resolution beta states, permitted obligation types, distribution, pricing, support, and volume cap after counsel/safety review;
- the pre-registered pilot thresholds and authorized public benchmark/case-study methodology;
- whether and when any Claim Passport specification is publicly licensed;
- whether a later licensed or managed execution structure is commercially and legally justified if target creditors demand a one-stop service;
- production regions, provisioning, live-provider admission, residency/data topology, first connectors, and detailed module implementation. The selected stack direction and verified development baseline are retained; replatforming requires a concrete requirement and an explicit ADR.

Do not convert an unresolved decision into polished certainty.

---

## 13. Acceptance criteria for the scope-update conversation

The coordinated project update is complete only when:

- all current files use the same portfolio, family, corridor, service-mode, and executor terminology;
- no universal section assumes every obligation is B2B, every debtor is a business, or every buyer is an agency;
- the old four layers are clearly capabilities, while the new four families are commercial/product boundaries;
- the two launch lanes share only appropriate Foundation contracts and remain separate in users, terms, data, permissions, support, legal reviews, metrics, and public status;
- universal invariants are separated from family and corridor rules;
- hard handoff and continuous creditor-side control coexist without making GRE the agency's operational supervisor;
- direct provider appointment, acceptance, and independent validation are represented in workflows and contracts;
- Provider Acceptance Profile, Authority Envelope, Corridor Pack, Action Receipt, and Resolution Quality Scorecard have clear ownership, versions, and state semantics alongside Claim Passport;
- transfer-service completion is distinct from case, claim, payment, agreement, and external provider states;
- Consumer and Private risks are not handled by cosmetic renaming of Trade workflows;
- legal assertions are current, source-linked, effective-dated, appropriately qualified, and marked for counsel where needed;
- capability availability is not confused with legal approval or production readiness;
- enterprise trust requirements and evidence are mapped to demonstrator, sensitive-data pilot, regulated pilot, and scaled availability rather than expressed as unsupported “bank-grade” claims;
- the schema/fixture/test package is version-consistent and its validation is actually run;
- all broken internal links and stale cross-references are corrected;
- marketing language distinguishes current capability, pilot target, strategic hypothesis, and future option;
- competitive differentiation is expressed in measurable customer outcomes rather than feature adjectives;
- the Trade pilot and Private beta are each narrow enough for a founder-led build, have separate stop controls, and do not make GRE a live collection agency by implication;
- the initial domestic personal-loan scenario is represented through the bounded Private Resolution profile, while institutional Consumer collection remains gated;
- public claims follow the evidence ladder, and the launch proof pack can demonstrate acceptance, switchability, corridor change impact, and two-sided safety without exaggerating availability;
- unresolved owner, legal, data-rights, security, integration, and commercial questions are listed rather than concealed.

---

## 14. Final strategic interpretation

The scope change should make GRE broader in architecture but narrower in each released promise.

The winning company is not “an AI collection agency for every debt.” It is the infrastructure that lets a creditor understand a claim, prove what can responsibly be proved, test it against an executor's real requirements, choose an economically sensible and legally available route, appoint the right independent executor, and retain a coherent record when the matter moves.

That positioning gives the hard handoff commercial meaning:

- GRE does not disappear at transfer;
- GRE does not need to control the collector to remain valuable;
- the creditor receives continuity and optionality that a closed full-service provider cannot easily offer;
- providers receive cleaner work and lower administrative cost;
- rule, requirement, dispute, and correction changes remain visible instead of disappearing between portals;
- the platform can expand into institutional consumer mobility and private resolution without pretending their laws, safeguards, and user relationships are the same.

The hard handoff is legally and commercially useful only when the surrounding product is exceptional. GRE must make direct appointment, provider acceptance, status return, correction, recall, and switching feel like one coherent experience while preserving who actually decided and acted.

The near-term leadership opportunity is therefore not maximum feature breadth. It is to become the most trusted and reusable **evidence-authority-acceptance-handoff** layer in one valuable enterprise corridor, prove that independent creditors and providers work better through it, and show the same foundation supporting a safe, two-sided domestic Resolution Room. Institutional Consumer Credit then becomes a credible expansion, not an unsupported launch claim.

Entering “with a bang” should mean that the market sees something difficult and verifiable in one sitting: a dirty case becomes decision-ready; a real provider states exactly what it will accept; the creditor can change executors without losing the record; a rule change identifies affected work; and a private participant can disagree or leave without being pressured. That proof is more defensible than announcing dozens of AI agents, hundreds of countries, or an unearned compliance claim.

---

## 15. Research-use note

The supplied directive records a September 7, 2026 research date. This revision selectively rechecked the material legal points in Section 6.8, the USTR/Allianz figures, and the InDebted, Zirtue, AAA and ODR positioning used in the review. It corrected the withdrawn CFPB bulletin and clarified RBI/DPDP applicability. Other linked vendor claims are retained from the supplied research and were not independently re-audited in full during this pass.

Competitor pages are vendor representations, not independent performance. Neither feature overlap nor the absence of a matching public description proves market whitespace. Regulatory sources are issue-spotting and control-design inputs, not a legal opinion or an operating authorization. Future source records must distinguish publication, retrieval, effective/transition dates, jurisdiction/actor applicability, amendment/withdrawal status, and qualified-review currency. Reverify before activation and do not treat a still-accessible withdrawn guidance page as current authority.


---

## 16. Revision 1.1 change record and remaining decisions

This review retains the incoming directive's four commercial families, shared Foundation, creditor-first enterprise buyer, Trade-led revenue strategy, controlled U.S. Private beta, gated Consumer expansion, independent execution and no-custody/no-principal-collection boundaries.

| Material correction | Why it matters | Revised location |
|---|---|---|
| Corrected the historical scope and retained selected stack/verified setup | Prevents duplicate setup and an accidental return to B2B-only planning | 1, 9.2, 10.2, 12 |
| Distinguished matter classification from Network commercial entitlements | A horizontal offering cannot bypass Consumer or Private gates or duplicate Foundation modules | 2.1, 9.3, 9.7 |
| Scoped creditor-control language and sponsor access | Paying for a private matter does not grant control over the other party's information | 2, 3.2, 4, 4.3 |
| Added preparation-only, weak-evidence, refusal and unreachable-person outcomes | Keeps the original informal-loan problem useful even when bilateral participation fails | 4.3, 8.3, 10.4 |
| Separated exact agreement, payment, performance and closure | Avoids reporting a promise, silence or workflow completion as recovered money | 4.3, 10.1 |
| Reordered provider review and handoff; added explicit exceptions and cutover | Providers need permitted inputs before validation; conditional acceptance is not authority to execute | 6.3–6.4, 10.1 |
| Qualified cancellation, switching, stale reports and surviving complaints | Revocation cannot undo in-flight actions or delete external copies; service duties do not all end at transfer | 6.3–6.6, 10.1 |
| Corrected the withdrawn CFPB source; clarified RBI storage/applicability and DPDP commencement | Prevents stale guidance and an inapplicable or unlawful storage assumption from becoming design truth | 4.2, 6.8 |
| Defined reuse of existing records and separate state/mode axes | Six named contracts do not require six competing ledgers or a rewrite of 29 records | 3.4, 5.3, 9.7 |
| Added scoped retention, correction/export and repeat-invitation behavior | Portability and immutable history need privacy semantics, including after withdrawal | 3.2, 9.3, 10.1 |
| Separated design, pilot implementation and later depth; made lane release independent | Prevents all families, proof assets and integrations from becoming one blocking launch project | 2.3, 8.3–8.6, 9.7 |
| Added explicit document/contract → backlog → development sequence and cross-copy provenance | Makes the next update reviewable while preserving existing work and future deliverables | 10.2–10.4 |

The important unresolved decisions remain commercial and operational: the reachable anchor buyer and recurring claim profile; actual provider participation and return-data commitments; the supported Private states, invitation channel, service price and safe operating capacity; Consumer design-partner and data-role applicability; production topology and live-provider admission; and numerical proof/stop thresholds. This review does not manufacture buyers, coverage, legal opinions or product-market fit.

Review evidence: full directive read; current repository branches, PR state, tree and setup/architecture records inspected; original pilot/future records and contract mappings compared; material legal and selected market claims checked against the cited sources. No Mac runtime or product tests were rerun, and no other project document, GitHub branch, PR or backlog was changed in this review.
