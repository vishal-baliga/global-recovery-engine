# Pilot release and assurance

**Status:** Required release design; no live release approved. September 7, 2026.

**Owner:** Vishal. Qualified reviewers and operational partners must be named for the actual activity.

**Owns:** Conditions and evidence for operating the Trade Pilot, incident/support responsibility and stop behavior. Product scope is in [06](06-pilot-brief.md); operational rules are in [03](03-operating-model.md).

## 1. What a release authorizes

A release identifies a matter-family/profile version, directional corridor, creditor actor pattern, service modes, permitted data flows, deployment, volume/support ceiling and validity period, plus the provider actor/profile when provider work is in scope. Release is explicit and scoped. Purchasing an edition, deploying a shared module or passing the reference validator does not release a service.

Only Trade & Receivables is selected for the Pilot. Private Resolution and Consumer Credit remain unavailable. The first directional commercial profile tests an India creditor and U.S. business obligor; precise states, claim subtype, any admission bands and actor roles must be resolved for the sold service before accepting a live case. Actual provider coverage additionally gates provider-specific work; it is not a prerequisite for creditor-only assessment. Unknown or mixed-purpose natural-person cases require review and cannot pass as ordinary Trade by default.

Vishal approves the business release after required legal, security, provider and support evidence exists. A counsel review is an input with scope, sources, conditions and review date; it is not a blanket regulator approval. The launch default excludes GRE obligor collection, principal collection/law practice, recovery-funds custody and consumer-report access/furnishing.

## 2. Evidence levels

| Level | Permitted purpose | Evidence before proceeding |
|---|---|---|
| Synthetic development | Implement and test modeled behavior | Synthetic data, controlled credentials, explicit authorization model, source attribution, local or disposable test resources |
| Historical diagnostic | Paid or consented assessment of permitted historical Trade files | Named customer/owner, actual data rights and minimized flow, terms/deliverable/fees, qualified activity review, access/security/support suitable for the data; no collection or active placement implied |
| Current-claim assessment | Assess a live unresolved Trade matter, including insufficient evidence or no viable route | Same applicable real-data/activity protections as the diagnostic; current authority, source-based urgency/holds, qualified review path and bounded service/support. No provider is required unless provider-specific work is sold; no disclosure/placement authority follows from assessment |
| First prospective placement | Assess, preflight, directly appoint and activate one qualified provider | Exact released profile; current required legal review; provider terms/eligibility/profile; security and recovery evidence; owner for every wait/exception; direct appointment and acceptance conditions; supported repayment observation and no-custody flow |
| Recurring Pilot | Repeated files and continuing observation/correction | Service capacity, event-return commitments, freshness and escalation, cost/support evidence, renewed access/credentials/review coverage and incident response |
| Portability demonstration | Make a bounded two-provider reuse/switch claim | Two independent accepting providers, measured additional intake, authorized export/correction, recall/cessation evidence and scoped replacement mandate; public permission for any identified example |

These levels are evidence states within one Pilot, not separate MVP and Pilot releases. One provider can support first-placement proof. Two providers are required before claiming demonstrated portability. A synthetic demonstration is not evidence of actual provider acceptance or market demand.

## 3. Required review records

| Review | Questions to resolve for the actual Trade release | Accountable evidence |
|---|---|---|
| Legal activity and actors | Creditor/rights-holder and service-provider roles; applicable solicitation/referral/collection licensing or exemptions; identity/data sources; GRE's exact acts and compensation | Qualified jurisdiction/activity work product, responsible reviewer, limitations, effective/review dates and permitted acts |
| Claim/corridor | Commercial purpose, actual parties, ownership/assignment/insurance rights, governing law/forum, relevant limitation and preservation duties | Reviewed profile and case exceptions; source-linked decisions; no automatic legal conclusion from country labels |
| Provider | Credentials, authority, conflicts, capacity, coverage, direct engagement, acceptance requirements and required event return | Provider-authored/approved profile, independent checks, current dates, direct terms and data/interface agreement |
| Data and disclosure | Lawful collection/use, controller/processor roles, minimization, sensitive/privileged material, transfers, retention/deletion and recipient obligations | Data-flow map, agreements and disclosure policy; actual service-specific access and deletion evidence |
| Money and billing | Entitled repayment recipient, destination change verification, fees/FX, receipts/reversals, GRE fee billing and applicable payment-provider support | Supported route, verified instructions, reconciliations and separate GRE billing records; no repayment pass-through |
| Security and operations | Tenant/provider isolation, MFA, least privilege, file quarantine, secrets, monitored services, support and recovery | Implemented controls, focused tests, independent security review appropriate to the buyer/data and operating exercises |
| AI/OCR | Permitted inputs/use, source attribution, model/provider retention and region, failure/refusal, prompt injection and material error | Task inventory, representative evaluation, reviewer workload, approved configuration and rollback/manual path |
| Commercial/public proof | Scope/price/customer expectations, outcome attribution, sample selection, use of names/case details | Customer terms, pre-registered measures and approved bounded claims in [14](14-market-validation-and-proof.md) |

Use primary laws, regulations and official guidance with their hierarchy and amendment/withdrawal status. For example, federal consumer-debt definitions do not establish a comprehensive B2B exemption; state actor/activity coverage needs its own review. [CFPB scope overview](https://www.consumerfinance.gov/ask-cfpb/what-laws-limit-what-debt-collectors-can-say-or-do-en-329/). Archived CFPB Bulletin 2013-07 was withdrawn in 2025 and must not be cited as current guidance. [Official withdrawal](https://www.federalregister.gov/documents/2025/05/12/2025-08286/interpretive-rules-policy-statements-and-advisory-opinions-withdrawal).

Current source review and engineering integration of a rule are different evidence. A retrieved page may be amended, withdrawn, not yet effective, or irrelevant to the particular actor. Record publication, retrieval and effective dates independently. A source change identifies possibly affected cases and reviews; it does not rewrite historical facts or automatically authorize new acts.

## 4. Control evidence needed before real data and operations

For any historical diagnostic or current-claim assessment, implement protection appropriate to the actual data and service: scoped identity/access, tenant separation, encryption in transit and at rest, authorized sources, safe file handling, retention/deletion/export, model/subprocessor settings and reachable incident/support owners. Preserve current authority, source-based urgency/holds, exact supported money/rights, source-linked review and an honest service result. Synthetic success alone does not satisfy real-data readiness.

Before operating the deployed assessment service, demonstrate the shared controls it uses:

- A non-owner/non-bypass database role and negative tenant/case access checks, including imports, workers and privileged support operations.
- A quarantined upload path with size/type limits, malware handling, safe extraction and no instruction-following from evidence content.
- Idempotent commands, attributable requests/receipts, current-authority checks, revocation fencing, retry reconciliation and timeouts that preserve uncertainty for the service's actual effects.
- Exact currencies, supported balances, sourced existing receipts, allocations and reversals. An imported status label cannot directly mark an obligation paid.
- Creditor/reviewer correction and complaint handling, permitted recipient/export records, revoked-link behavior and owned unresolved requests. An exported copy cannot be remotely erased.
- Consistent database/evidence restore in isolation, measured recovery targets, retention interaction and integrity checks, without a destructive exercise on live data.
- Monitoring, replay/versioning for used workers, graceful release/rollback, backup failure detection, audit access and a rehearsed incident path.
- An honest security/vendor package and independent penetration testing or buyer-accepted equivalent proportional to the actual data/activity. Do not claim certification or bank-grade readiness without exact evidence.
- Defined billing/refund records, no-route/insufficient-evidence completion, residual-duty and reopening behavior, named support/absence coverage and measured service capacity.

The assessment `.A` slices in [11](11-prioritized-pilot-backlog.md) deliver this minimum without provider-placement or switching implementation. A documented manual-only assessment can satisfy the scoped AI decision without enabling OCR/model processing; any later AI task requires its own implementation, evaluation and permitted data settings. No manual route waives evidence, authority, privacy, financial or support controls.

**Provider services add controls according to the acts enabled.** Provider preflight/disclosure requires actual named-profile requirements, permitted minimized review access, provider isolation, current eligibility and attributable review responses; it does not grant execution authority. Placement/activation additionally requires the staged packet/profile, acceptance/delta, current direct appointment, satisfied execution conditions and explicit activation/cutover. Before activating provider work, demonstrate fencing of incompatible commits/dispatch, reconciliation of sent/unknown effects, scoped recall and blocked conflicting replacement activation while cessation is unresolved. Synthetic replacement scenarios may prove modeled controls without claiming two-provider commercial adoption.

Continuing provider work requires source-aware returns, verified recipient instructions and actual receipt/reversal reconciliation for its supported financial route, correction/complaint delivery and escalation that survive handoff, and tested provider-effect/recovery scenarios. The `.B` slices extend the same modules and deployment. These provider requirements do not gate a service that only assesses and returns a record to the creditor; that service must neither disclose to nor activate a provider under its assessment authority.

Record applicable controls and any justified not-applicable entries in the actual release record. A provider-specific control may be omitted only while its corresponding act remains unavailable. Certifications and stronger enterprise requirements follow the customer/data/activity; they are neither automatically waived because this is a Pilot nor required for every synthetic task. Future institutional Consumer procurement remains separately gated.

## 5. Operational ownership and service capacity

Vishal is accountable for establishing GRE support and incident coverage, including a backup/absence arrangement before a live service promise depends on it. A named provider remains responsible for its recovery work; a named creditor owner remains responsible for creditor decisions and direct oversight. Human roles can be combined only where competence, authority and conflict boundaries permit it.

Each service records the deliverable, fee/cap, start/end conditions, expected response window, next actor, escalation deadline and surviving duties. No case can be left indefinitely “awaiting provider” without an owner. Manual actions use the same source/authority records and cost capture; they are not invisible exceptions to the control model.

Set a real active-case/support ceiling from the founder's capacity and agreed response windows. Expand cohorts only after measuring workload and incidents. Customer communication must reflect the current supported service and outside responsibilities; a dormant service or stale provider report cannot be presented as active management.

## 6. Suspension and incident behavior

Suspend the affected act or service when classification is unresolved, a required review expires, authority changes, provider eligibility lapses, an identity/destination mismatch appears, a complaint/protected-treatment signal requires a hold, or a security/financial incident makes continued action unreliable.

Suspension fences new GRE effect commits and cancels work still cancelable. It does not prove that an external provider stopped, a message was recalled or an exported file was erased. Record notification, acknowledgment, uncertain in-flight effects and reconciliation. Preserve permitted complaint, correction, evidence access and legal-preservation paths while affected collection-enabling acts are held.

Incident records identify scope, containment, sources, affected recipients/cases, accountable decisions, notifications required by the actual agreement/law, recovery and reopening evidence. Provider independence does not remove GRE's responsibility for its own access, disclosures, representations or integration failures.

## 7. Release record and renewal

Before enabling a real-data service, record the exact software/schema/matter-profile versions and provider versions where applicable, the actual service scope, controls/tests, resolved decisions, outstanding nonblocking limitations, support ceiling, monitoring, rollback/suspension owner and sign-off references. An assessment-only record identifies provider engagement/placement as not applicable and keeps those acts disabled; it still needs all required assessment review, protection and support evidence. Do not mark a missing required reviewer or a provider commitment needed for the sold provider service as a nonblocking limitation.

Re-evaluate when the activity, creditor, provider, corridor, fees, data flow, model, support capacity or material software behavior changes. New acts pass current applicable gates; historical reproductions retain the policy and facts valid at the relevant time. The [backlog](11-prioritized-pilot-backlog.md) tracks implementation; this artifact defines the release evidence it must produce.
