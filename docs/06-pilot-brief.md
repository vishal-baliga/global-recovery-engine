# Global Recovery Engine — Pilot Brief

**Updated:** September 7, 2026

**Owner:** Vishal, project lead and sole initial developer

**Status:** Authoritative selected Pilot scope; a delivery commitment to build and validate, not a live-service declaration.

**Purpose:** Define one substantial, usable Pilot and its customer outcomes. This replaces the former two-track brief. Decision history is owned by [12](12-scope-decisions-and-reconciliation.md).

## 1. One Pilot and one complete promise

The Pilot is **GRE Foundation + GRE Trade & Receivables**, including the Trade-required Recovery Network & Control capabilities. The selected corridor hypothesis is **India-creditor → U.S.-business-obligor commercial goods/services claims**. The preferred buyer hypothesis is a creditor-side team or authorized channel with recurring files and a real preparation/provider-management problem.

The customer promise is:

> Establish a source-linked claim and current balance/rights/authority position, assess the available route, prepare it for a named independent provider, and preserve creditor continuity through acceptance, correction, observation, recall, or switching.

The Pilot must deliver a usable result even if evidence remains insufficient or no viable provider route exists. A readiness/no-route report with gaps, reasons, safe next steps, costs, unresolved duties, and an export is a complete service outcome. Provider rejection, no reply, or creditor withdrawal cannot leave a customer in an indefinite waiting state.

This is one market-facing release. Internal implementation increments are delivery sequencing, not additional products. Private Resolution, Consumer Credit, and standalone Network packaging are future work. The Pilot contains no parallel domestic personal-loan beta or live U.S.-origin consumer-account/India-resident-borrower journey.

## 2. Admission and service boundaries

Start with existing goods/services claims whose complexity makes reconstruction, evidence gaps, disputes, prior payments, authority, or provider transfer meaningful. Include appropriate late-entry imports: older or partly paid claims, prior providers, an existing agreement, or prior proceedings must enter at their verified current position. Importing history must not replay an external action.

The India-creditor/U.S.-business-obligor direction does not establish all-state support. Before live work, publish the supported creditor/obligor roles, commercial purposes, states, claim structures, activities, formats/languages, providers, review capacity, and data/payment paths. Amount/age bands remain discovery hypotheses. A business label or corporate email cannot resolve uncertain natural-person or mixed-purpose classification. Unsupported or unresolved classification receives a scoped hold, explanation, and qualified review path.

GRE provides assessment, preparation, transfer tooling, and separately scoped creditor continuity. **The creditor directly appoints the provider; the provider independently validates, accepts, and performs collection.** GRE does not conduct post-default obligor collection, negotiate as collector, supervise provider scripts/cadence/tactics, or hold/pass through repayment funds. GRE may transport exact creditor instructions and receive attributed provider reports. It retains responsibility for its own platform, disclosures, corrections, support, incident handling, and agreed continuity services.

The [Operating Model](03-operating-model.md) owns exact responsibilities and state semantics. [Workflow & Interaction Specification](04-workflow-interaction-specification.md) owns observable behavior and exception paths. [Domain & Data Contracts](05-domain-data-contracts.md) owns the represented shapes and effect checks. No manual workaround may bypass those rules.

## 3. Required customer deliverables

| Deliverable | What the Pilot must actually provide |
|---|---|
| **Suitability and a clear offer** | One Trade entry journey; supported-scope screening; role, fee/cap, outside-cost, service-window, cancellation and support disclosures; a useful result for unsupported inquiries. No provider or legal availability is implied. |
| **Creditor onboarding and current-case intake** | Organization/representative identity and case authority appropriate to the service; secure resumable uploads; duplicate review; objectives and budget; existing representatives, assignments, agreements, proceedings, and deadlines. Login alone grants no case authority. |
| **Source-linked claim reconstruction** | Retain originals, source excerpts, translations/extracts, assertions, and reviewed findings distinctly. Reconstruct parties, contract/invoice, delivery/performance, acceptance, dispute, and chronology; show contrary evidence and gaps. Produce an exportable purpose-scoped Claim Passport. |
| **Exact financial, rights, and authority assessment** | Reconcile invoices, credits, claimed/verified payments, supported charges, prior settlements, rights interests and mandates. Preserve original currency, disputed amounts, unknowns, allocation and reversal lineage. An accounting adjustment or insurance/sale proceeds must not silently extinguish the obligation. |
| **Route and economics decision** | Explain prerequisites, available eligible routes, external cost/time assumptions, uncertainty, specialist needs, and next owner. Support evidence cure, review, prepare/transfer, defer/monitor when scoped, or stop/no viable route. Do not invent terms, enforceability findings, or recovery probabilities. |
| **Named-provider preflight** | A provider-authored or explicitly approved Acceptance Profile version; current scope/credentials/conflicts/capacity checks; packet-to-profile comparison; minimum permitted review disclosure; quoted scope/fees and a precise validation delta. Readiness is relative to that named profile. |
| **Direct appointment and hard handoff** | Exact transfer offer/version and disclosure manifest; provider rejection, conditional acceptance, acceptance, or expiry; direct creditor appointment; independent provider validation and fulfilled execution conditions; current mandate; explicit activation/cutover. A transmitted packet is not an accepted or active placement. |
| **Creditor workspace and scoped observation** | Tasks, approvals, deadlines/review dates, named owners, service expiry, cost commitments, source-attributed provider updates, external agreements/plan observations and payment reports. Track gaps and overdue reports. Provider operations remain outside GRE control. |
| **Correction, recall, and switch continuity** | Propagate permitted corrections to identified recipients; export the usable record with limitations; record recall request, access revocation, provider cessation acknowledgment, in-flight exceptions, retained-copy duties and replacement acceptance. Prevent conflicting overlapping execution scopes. |
| **Completion, support, and dependable operation** | Deliver an outcome record showing assertion/corrections, current balance, observed receipts, costs, external status and uncertainty, service result, and surviving obligations. Provide wrong-party, complaint, urgent-review, privacy, security, retention, incident and reopening paths with accountable owners. |

Supported uploads and reviewed manual extraction/import are acceptable initially. Every required manual or provider step needs an identified role, capacity, recorded result, service window, and measured effort. A packet emailed to an unnamed future partner does not fulfill the handoff promise. Critical access, money, authority, disclosure, and current-state effect controls require application enforcement when the associated functionality is implemented.

## 4. Handoff and continuity experience

The creditor sees the named provider, profile version, shared material, service scope, fees, mandate, and what remains unresolved before authorizing exchange. Review disclosure permits conflicts/eligibility/intake review only. Provider responses can request a precise delta, reject with reasons, or remain unanswered until expiry; each branch retains a responsible owner and next decision.

Direct appointment and provider acceptance do not by themselves permit every act. Activation requires the current mandate, independent validation, satisfied conditions, supported scope and release/policy checks. Conditional acceptance cannot unlock the conditioned work. Changed material facts, terms, authority, profile or packet version require the affected review to be revisited. At cutover, fence incompatible queued GRE effects within the transferred scope, cancel what remains cancelable, and reconcile sent/in-flight/unknown effects rather than declaring them recalled.

After activation, the provider runs collection in its own identity and systems. GRE shows what that provider reports, with source, event time, receipt time, verification scope and missing information. A provider label such as “paid” is not a verified receipt or creditor net proceeds. Record payment evidence and allocation, actual fees/FX where relevant, duplicates and reversals without moving money. Imported settlement and installment information remain external observations with their source and exact terms; GRE is not offering plan-servicing collection reminders or negotiation.

Recall is a process, not a button that proves external cessation. GRE can revoke its access and suspend its integration while preserving necessary support/correction duties. It cannot remotely erase an exported document or guarantee the provider stopped work. Escalate nonresponse, account for prior effects and retained-copy obligations, and activate a replacement only after the relevant conflicts and conditions are resolved. The original case persists across distinct services and provider engagements.

## 5. Required difficult outcomes

| Scenario | Useful and honest result |
|---|---|
| Entity mismatch, uncertain purpose, ownership or mandate | Hold affected work, identify missing proof and review owner, retain the customer's supported preparation work. |
| Disputed performance, conflicting records, insufficient evidence or an already-paid invoice | Preserve both accounts, correct the supported position, show remaining uncertainty, and avoid unsupported placement. |
| Provider declines, cannot act, asks for changes, or never replies | Return a structured delta/disposition with owner, expiry/review date and alternatives; do not count it as accepted transfer. |
| Authority revoked, payment arrives, or material evidence changes during handoff | Re-evaluate pending work against current state; stop incompatible new effects and reconcile earlier effects. |
| Duplicate, reported-only, partial or reversed payment | Preserve source and uncertainty, reconcile allocation and remaining balance exactly, and revise affected observations and pending instructions. |
| Correction needed after export or provider change | Identify permitted recipients, request/record acknowledgment and exceptions, retain correction lineage and recipient obligations without promising remote erasure. |
| No economically or operationally viable route | Deliver the assessment, reasons, evidence gaps, safe next steps, export, fees and surviving duties; complete only the scoped service. |
| Transfer/observation window expires with an unresolved claim | Show the continuing obligation, external engagement, unknown outcome and explicit renewal/exit owner; do not label it recovered or legally released. |

Targeted behavioral conformance must cover these paths and meaningful negative examples. A reference snapshot or synthetic test demonstrates represented semantics, not live runtime enforcement, partner acceptance, legal readiness, or customer value.

## 6. Business and release work included

A usable Pilot includes the operating and commercial work necessary to deliver the promise: actual contracting/role structure, applicable qualified review, named support and specialist ownership, provider eligibility and exchange arrangements, privacy/security handling, incident and correction processes, fees/caps and service terms, and a cohort within service capacity. These are release dependencies, not optional future enhancements.

The first diagnostic does not depend on two providers. One qualified provider may support the first accepted-placement proof once its affected release conditions are satisfied. **Two independent providers must accept/reuse the core before a bounded portability claim is made.** Build and exercise the correction/export/recall/switch behavior required by the Pilot even while commercial proof develops; simulations must stay labeled simulations.

[13](13-pilot-release-and-assurance.md) owns release manifests, gates, review ownership and blocking evidence. [14](14-market-validation-and-proof.md) owns recruitment hypotheses, baselines, sample definitions, numerical targets and permitted claims. Set thresholds before judging a live cohort. Measure total creditor/provider/GRE effort, time to assessment and explicit placement disposition, critical errors, correction/switch success, paid use, support-adjusted contribution, and truthful outcome coverage. Synthetic examples cannot establish demand or recovery improvement.

## 7. Delivery discipline and changes

Use the existing verified Next/TypeScript and Python/FastAPI/Pydantic direction with PostgreSQL, Temporal and Azure Blob, as owned by [08](08-stack-and-environment-decision.md). One developer builds a modular application, reusing shared contracts and tested adapters. Preserve environment files, locks, SDK/codegen versions, fixtures and factual setup history. The legacy contract ZIP stays historical; [05](05-domain-data-contracts.md) owns the versioned reference transition.

The immediate order is current-document reconciliation, contract/conformance reconciliation, then [prioritized backlog](11-prioritized-pilot-backlog.md), before application development. This sequence does not reopen completed environment selection or add application/cloud work to the documentation task.

[07](07-future-development-and-business-deliverables.md) preserves all deferred product/business items and strategic boundaries. Reducing an included outcome requires a dated decision, reason, customer impact, interim route/owner, dependencies and reconsideration condition in [12](12-scope-decisions-and-reconciliation.md), plus corresponding updates to the offer and backlog. An unresolved implementation choice does not make an essential Pilot outcome future work.
