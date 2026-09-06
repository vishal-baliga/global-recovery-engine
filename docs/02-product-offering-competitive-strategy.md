# Global Recovery Engine — Product Offering & Competitive Strategy

**Updated:** September 6, 2026  
**Purpose:** Authoritative detailed offering, capability map, competitive positioning, technology strategy, and expansion options.  
**Status:** Target offering for validation; MVP not selected and production availability not established.  
**External research basis:** Public sources reviewed September 5, 2026. This consolidation preserves that research; it does not represent a new market or legal review.  
**Companion references:** [Business & Project Overview](01-business-project-overview.md) · [Operating Model](03-operating-model.md) · [Workflow & Interaction Specification](04-workflow-interaction-specification.md)

## 1. Product scope

Global Recovery Engine is programmable infrastructure for resolving commercial payment obligations across organizations and borders. The product connects a claim's evidence, rights, authority, decisions, execution, and outcomes across people, agents, systems, and providers.

The full initial offering represents the complete supported recovery lifecycle in one corridor: India-origin B2B claims against U.S. businesses. The initial commercial hypothesis targets recovery operators and approximately USD 5,000–250,000 claims, 30–365 days overdue. These are targeting assumptions, not hard schema limits or validated market fit.

Coverage is declared by claim profile, requested service, route, jurisdiction, provider, and readiness status. The system can deliver a bounded assessment or handoff without requiring the customer to buy lifecycle operation. A continuing Case can contain multiple Service Requests; finishing contracted work does not establish that the debt was resolved.

The [Business & Project Overview](01-business-project-overview.md) owns buyer selection, packaging, economics, objectives, and current project status. This document owns the detailed product promise and the evidence required to make it competitive.

## 2. Product design principles

1. **Support the chosen customer's complete job.** Represent evidence preparation, decisions, execution, reconciliation, and handovers for the supported service. A capability map does not establish that every route is ready to sell.
2. **Make scope explicit.** Assessment, recovery operation, provider handoff, and monitoring have defined deliverables, responsibilities, cost limits, and completion conditions.
3. **Preserve continuity.** People, customer agents, providers, and source systems use the same case meaning, authority checks, and outcome semantics.
4. **Separate preparation from commitment.** Agents may analyze and propose within their access; consequential actions require current authority, independent checks, and an execution record.
5. **Use better technology to improve a measured outcome.** Lower total cost, fewer critical errors, faster useful decisions, reduced handoff work, and verifiable execution are comparative targets.
6. **Keep expansion conditional.** New corridors and services need demand, operating capability, expert-maintained policy, quality evidence, and workable economics.

GRE supplies the intelligence, digital workflow, controls, and customer experience within its contracted scope. Authorized customers and providers perform assigned communication, negotiation, reserved professional work, and payment execution. Actual services and conduct determine responsibility. The [Operating Model](03-operating-model.md) defines the detailed actor and authority rules.

## 3. What the market already makes table stakes

Public product materials reviewed on September 5, 2026 establish a demanding baseline:

| Competitor / archetype | What the market already offers | Implication for Global Recovery Engine |
|---|---|---|
| **InDebted** | AI-native first-party decisioning and workflows through Receive; managed third-party omnichannel collections through Collect; programmable jurisdiction-specific compliance through Comply; data-informed portfolio liquidity through Release | Decisioning, digital journeys, portals, controls, auditability, and outcome data cannot be positioned as novel by themselves. [Receive](https://www.indebted.co/solution/receive/) · [Collect](https://www.indebted.co/solution/collect/) · [Comply](https://www.indebted.co/product/comply/) · [Release](https://www.indebted.co/solution/release/) |
| **CreditNirvana** | A 20-module, closed-loop platform spanning early warning, strategy, omnichannel execution, settlement, legal enforcement, recovery/assets, operations, governance, and embedded agentic AI | “Agentic and end-to-end” is already a competitor claim. We need a superior domain model, cross-border reasoning, and evidence standard—not more agents. [CreditNirvana](https://creditnirvana.ai/) |
| **Credgenics** | Recovery prediction, segmentation, digital communications, AI voice, dialer, field operations, payment rails, legal notices, litigation tracking, compliance controls, and analytics | A full operational surface is the baseline for serious recovery software. [Credgenics](https://www.credgenics.com/) |
| **HighRadius** | Deep ERP connectivity, AI-prioritized worklists, automated dunning, email response, calling, disputes, payment links, customer portals, and enterprise analytics | Enterprise buyers expect live system integrations, work queues, measurable productivity, and configuration. [HighRadius](https://www.highradius.com/software/order-to-cash/collections-management/) |
| **Sidetrade** | Invoice-level next-best action, automated multichannel dunning, rules and action limits, customer portals, dispute routing, benchmarking, and feedback from collection outcomes | Rules-governed automation and continuous optimization are already mature in upstream AR. [Sidetrade](https://www.sidetrade.com/core-platform/o2c-apps/augmented-collection/) |
| **Delos** | B2B document extraction, claim and dispute classification, evidence/readiness evaluation, strategy routing, legal handoff, and claim acquisition | This is the closest direct product threat. Generic document AI and recovery-route classification will not be defensible. [Agency operating layer](https://www.delos.international/agencies) · [Claim-purchase thesis](https://www.delos.international/thesis) |
| **Debitura / Oddcoll** | Low-friction claim placement, APIs or bulk intake, centralized tracking, local-partner routing, standardized commercial terms, and wide international coverage | Global reach and provider routing alone are already products. [Debitura](https://www.debitura.com/) · [Debitura API documentation](https://docs.debitura.com/) · [Oddcoll](https://oddcoll.com/international-debt-collection/) |
| **Atradius / Allianz Trade / Coface** | Human expertise, debtor investigation, amicable recovery, settlements, legal escalation, insolvency support, and owned or integrated international networks | The incumbents’ trust, local knowledge, private outcome data, and execution reach are major assets even when their technology is less transparent. [Atradius](https://atradiuscollections.com/global/) · [Allianz Trade](https://www.allianz-trade.com/en_global/discover-allianz-trade/our-strategy/how-our-debt-collection-teams-work.html) · [Coface](https://www.coface.com/news-economy-and-insights/debt-collection-around-the-world-how-to-deal-with-local-specificities) |
| **Retrievables** | Simple intake and matching to commercial collection attorneys and agencies | Low-friction legal placement is useful but not sufficient as a defensible product. [Retrievables](https://retrievables.com/) |

Market context from the same research supports investigating cross-border friction, not a revenue forecast. Allianz Trade's 2026 study reports that 48% of international trade receivables in its analysis, approximately USD 1.1 trillion, are exposed to countries with very high or severe collection complexity. USTR reports USD 239.6 billion in U.S.–India goods and services trade in 2025. Neither figure is GRE's addressable paid market; reachable customers, supported cases, adoption, and price must be estimated separately. [Allianz Trade study](https://www.allianz-trade.com/en_global/news-insights/economic-insights/Commercial_debt_collection_2026_Trade_fragmented_world_Navigating_Collection_Complexity.html) · [USTR India profile](https://ustr.gov/countries-regions/south-central-asia/india)

**Research caution:** This comparison reflects marketed capabilities, not audited testing or market leadership. “Not evident” does not prove absence. We must match the chosen customer's complete job, not the union of every competitor's feature catalog. Architecture choices described as MUST BEAT are targets; none establishes measured superiority.

## 4. Full offering: one system, four product layers

### 4.1 Intelligence — understand and value the claim

The Intelligence layer converts fragmented documents and system records into an evidence-linked Claim Passport with scoped verification and an economic view of the available recovery paths.

It covers:

- multimodal intake from files, email, portals, APIs, and source systems;
- creditor, debtor, guarantor, counterparty, and related-entity resolution;
- invoice, currency, interest, credit, payment, and balance reconciliation;
- contract clause, governing-law, forum, arbitration, and authority extraction;
- chronology reconstruction;
- evidence of performance, delivery, acceptance, admission, dispute, and promise to pay;
- missing-evidence and contradiction detection;
- debtor status, insolvency, registry, litigation, and permitted asset signals;
- limitation, deadline, and urgency analysis;
- recoverability, readiness, confidence, cost, duration, and expected-net-value scenarios;
- source-connected evidence capture before default, with separate authenticity and business-performance assessments;
- obligation, rights-interest, assignment/subrogation, settlement, accounting, and cash distinctions;
- decision episodes, value of information, and portfolio budget constraints.

### 4.2 Operations — run the recovery plan

The Operations layer turns the approved strategy into governed work.

It covers:

- portfolio and case management, with separately scoped Service Requests and completion conditions;
- organization activation, late-entry handovers, and current-state verification before new actions;
- queues, assignments, tasks, SLAs, approvals, and escalation triggers;
- decision-focused work with verified standing mandates, explicit waiting owners, expiry behavior, and source-freshness checks;
- configurable strategies and next-best-action orchestration;
- communication journey design across email, messaging, letters, and voice;
- collector workbench, AI copilot, response classification, and summaries;
- dispute, promise-to-pay, settlement, and payment-plan workflows;
- debtor and creditor portals;
- payment-link and reconciliation events through authorized payment providers;
- evidence-grounded demand and legal-packet preparation;
- counsel handoff, court-stage tracking, enforcement status, and closure;
- bilateral issue resolution with isolated private strategies and a permissioned shared record;
- bounded delegated execution within a tested mandate; human review for exceptions and reserved actions;
- independent commercial, financial, legal, operational, and administrative completion.

### 4.3 Network — execute across organizational and jurisdictional boundaries

The Network layer makes a case portable and keeps it continuous when responsibility changes.

It covers:

- provider discovery, eligibility, credentials, coverage, capacity, and conflicts;
- structured provider-ready handoff through the Claim Passport;
- quotes, fees, authority, SLAs, milestones, and status normalization;
- collaboration among creditor, agency, lawyer, mediator, insurer, and other authorized specialists;
- route and provider recommendations adjusted for the actual case mix;
- cross-border translation, notarization, apostille, service, and local-procedure coordination;
- insurance notification and claim-package handoff;
- optional matching to authorized liquidity or debt-purchase providers without Global Recovery Engine purchasing the debt;
- continuous, portable case history across every handoff;
- authenticated customer-agent and partner-agent interaction through versioned service contracts;
- documented interchange formats, delivery/acceptance receipts, and evidence retrieval rights.

### 4.4 Control — govern every decision and action

The Control layer turns compliance and AI governance into active infrastructure.

It covers:

- effective-dated jurisdiction and corridor rule packs;
- programmable client policies and authority limits;
- pre-action and pre-communication validation;
- required evidence, disclosure, timing, channel, and escalation checks;
- role-based permissions and separation of duties;
- authority and execution-mode controls for material actions, including lawful bounded delegation and per-action approval where required;
- source-linked reasons, confidence, and trace IDs;
- tamper-evident action, decision, model, and override history during authorized retention, with auditable correction and disposition;
- model evaluation, drift monitoring, rollback, and exception handling;
- privacy, retention, residency, security, and separate data-use permissions;
- isolated untrusted-content processing, independently validated tool permissions, and revocation;
- applicable-rule precedence, amendment status, and unresolved legal interpretation handling.

### 4.5 Common foundation — Recovery Graph and Outcome Ledger

All four layers operate on one versioned foundation:

- **Case and Service Request:** the continuing claim record and independently contracted assessment, operation, handoff, or monitoring work;
- **Recovery Graph:** obligations, rights interests, parties, documents, assertions, clauses, evidence, disputes, jurisdictions, routes, actions, providers, and relationships;
- **Event Ledger:** every state change, communication, decision, approval, handoff, deadline, cost, and payment event;
- **Outcome Ledger:** route, provider, action sequence, elapsed time, cost, amount recovered, closure reason, expert override, and confidence calibration;
- **Policy Registry:** source-linked, effective-dated rules and client-specific controls;
- **Evaluation Registry:** test cases, model versions, prompts, policies, quality scores, and failure modes;
- **Decision Episodes and Outcome Observations:** point-in-time alternatives, selection context, attribution limits, observation windows, and known-zero/missing/censored distinctions;
- **Rights and Permission Records:** title/beneficiary history and purpose-specific permission for processing, disclosure, retention, private learning, and permitted pooled use.

## 5. Product surfaces

The system should present different interfaces over the same claim and event model:

| Surface | Primary user | Purpose |
|---|---|---|
| **Operator Workspace** | Agency intake staff, collectors, supervisors, recovery managers | Evaluate, prioritize, operate, approve, and monitor portfolios |
| **Creditor Portal** | Exporter, lender, finance or credit team | Submit cases, cure evidence gaps, authorize actions, and see economics/status |
| **Partner Workspace** | Local agency, lawyer, mediator, insolvency or enforcement specialist | Accept structured handoffs, quote, execute authorized work, and return normalized events |
| **Debtor Resolution Portal** | Business debtor and its authorized representatives | Review claim information, raise disputes, share documents, make proposals, and use integrated payment options |
| **APIs and Webhooks** | ERPs, AR systems, insurers, recovery platforms, and enterprise data teams | Create/update Claim Passports, request decisions, propose authorized actions, and receive status/outcome events |
| **Agent service interface** | Authenticated customer-owned and partner agents | Discover scoped capabilities, submit tasks, exchange approved evidence/terms, obtain execution receipts, and track outcomes |

Two delivery editions share the same domain service: **Recovery Operations** and **Embedded Resolution**. The initial commercial hypothesis is operator-first and white-label capable. Packaging, pricing principles, service economics, and their validation status are maintained in the [Business & Project Overview](01-business-project-overview.md). Surfaces express the same operating rules; they do not create independent business logic.

## 6. Capability decision framework

- **MUST MATCH:** A serious buyer expects it. Being materially weaker prevents adoption, but it is not our primary differentiation.
- **MUST BEAT:** The capability contributes to a customer outcome we intend to outperform on. This is a comparative target, not proof of superiority or an established moat.
- **INTEGRATE:** The customer needs the outcome, but the underlying capability is commodity, licensed, jurisdiction-specific, capital-intensive, or better supplied by a partner.
- **DELIBERATELY EXCLUDE:** It weakens neutrality, expands the regulatory perimeter, conflicts with the beachhead, or creates a different company.

All entries describe the target offering. Classification is a strategic decision, not proof of implementation, availability, or comparative superiority. Capability release status is recorded separately under the Operating Model.

### 6.1 Foundation and enterprise platform

| Capability | Decision | Target standard | Main comparators |
|---|---|---|---|
| Case and Service Request separation | **MUST MATCH** | Defined assessment, operation, handoff, and monitoring scope; service completion independent of claim resolution | Chosen customer job and reviewed workflow |
| Organization activation and late-entry import | **MUST MATCH** | Validate current facts, authority, commitments, and ownership without replaying historical actions | Live operating continuity |
| Decision inbox and standing mandates | **MUST MATCH** | Surface decisions and exceptions; inherit only current verified delegation; show waiting ownership and expiry | Enterprise workflow expectations |
| Secure bulk placement by portal, CSV, SFTP, and API | **MUST MATCH** | Fast ingestion for single claims and portfolios with validation and idempotency | InDebted, Delos, Debitura, Oddcoll |
| ERP, accounting, CRM, and billing connectivity | **INTEGRATE** | Stable connector framework; build only the highest-value corridor connectors directly | HighRadius, Sidetrade |
| Multi-tenant organizations and data isolation | **MUST MATCH** | Enterprise tenancy with client, portfolio, team, and provider partitions | All enterprise platforms |
| White-label configuration | **MUST MATCH** | Operator brand, domain, templates, portals, and policy configuration | InDebted Receive, Debitura |
| SSO, RBAC, permissions, and separation of duties | **MUST MATCH** | Fine-grained action and data permissions across organizations | CreditNirvana, InDebted |
| Configurable workflow builder, queues, tasks, and SLAs | **MUST MATCH** | Versioned playbooks with events, conditions, timers, approvals, and exceptions | Credgenics, CreditNirvana, Sidetrade |
| Event-derived case state | **MUST MATCH** | Reconstruct recorded claim/authority/action state from retained events and versions; preserve actual model outputs | General engineering foundation; implementation quality needs benchmarking |
| Open APIs and webhooks | **MUST MATCH** | Every important case object and event is available programmatically | Debitura, HighRadius, CreditNirvana |
| Security, encryption, retention, residency, and audit controls | **MUST MATCH** | Enterprise-grade baseline; no “startup exception” for sensitive claim data | InDebted, CreditNirvana, Credgenics |
| Broad office-of-CFO / order-to-cash suite | **DELIBERATELY EXCLUDE** | Integrate with upstream systems; do not rebuild invoicing, cash application, treasury, or credit underwriting | HighRadius, Sidetrade |

### 6.2 Claim intelligence

| Capability | Decision | Target standard | Main comparators |
|---|---|---|---|
| OCR and multimodal document intake | **MUST MATCH** | Reliable handling of scans, native files, emails, tables, and attachments | Delos, modern document AI |
| Canonical Claim Passport | **MUST BEAT** | Independent handoff acceptance with lower rework, scoped provenance, rights, and controlled disclosure | Schema adoption and comparative performance unproven |
| Field- and assertion-level provenance | **MUST BEAT** | Every material fact links to exact source evidence, extractor/model, confidence, and reviewer state | InDebted Comply is the control analogue |
| Commercial entity resolution | **MUST BEAT** | Resolve legal entities, trade names, addresses, guarantors, parents, and relevant relationships; use licensed data sources where needed | Global incumbents’ human investigation |
| Corporate, registry, court, insolvency, and asset signals | **INTEGRATE** | Normalize permitted third-party data into the Recovery Graph with freshness and source metadata | Allianz, Coface, Atradius |
| Balance, payment, credit, currency, and interest reconciliation | **MUST BEAT** | Deterministic obligation/accounting/cash/settlement allocation, rights history, and no double recovery | AR and recovery platforms require direct comparative testing |
| Case chronology reconstruction | **MUST BEAT** | Event timeline synthesized from documents and systems, with unresolved conflicts preserved | Delos adjacency |
| Evidence graph and completeness analysis | **MUST BEAT** | Connect each required proposition to supporting, conflicting, and missing evidence | Delos adjacency |
| Dispute, defense, admission, and promise classification | **MUST BEAT** | Evidence-linked taxonomy suitable for operational routing, not a generic summary | Delos, Sidetrade dispute routing |
| Governing law, forum, arbitration, authority, and clause extraction | **MUST BEAT** | Source-linked extraction with confidence and mandatory expert review where material | Cross-border legal providers |
| Multilingual document understanding and localization | **MUST BEAT** | Corridor-grade semantic consistency, not word-for-word translation | Global incumbents’ local teams |
| Human review, correction, and override capture | **MUST MATCH** | Efficient review with separately permitted evaluation/training use; corrections are not automatically ground truth | CreditNirvana, InDebted |
| Generic document summaries sold as the product | **DELIBERATELY EXCLUDE** | Summaries are supporting UX, not the value proposition | Commodity LLM capability |

### 6.3 Recovery decisioning

| Capability | Decision | Target standard | Main comparators |
|---|---|---|---|
| Account/claim segmentation and prioritization | **MUST MATCH** | Explainable work priority based on value, urgency, readiness, effort, and risk | InDebted, Credgenics, CreditNirvana, HighRadius, Sidetrade |
| Claim readiness and evidence-cure decision | **MUST BEAT** | State exactly what blocks each route and the highest-value next evidence action | Delos adjacency |
| Corridor and route eligibility | **MUST BEAT** | Evaluate permitted recovery routes, insurance/transfer options, and monitoring; separate operational closure, accounting treatment, and legal release | Global incumbents do this through experts |
| Limitation, deadline, and urgency management | **MUST BEAT** | Effective-dated rules, confidence, sources, alerts, and human approval | Cross-border legal providers |
| Debtor viability and collectability signals | **MUST BEAT** | Separate validity/readiness from practical ability to recover; show data freshness and uncertainty | Insurers and global incumbents |
| Next-best operational action | **MUST MATCH** | Recommend or trigger the next authorized action within the approved strategy | InDebted, Sidetrade, HighRadius, CreditNirvana |
| Recovery Digital Twin / ENRV simulation | **MUST BEAT** | Compare routes as distributions of recovery, cost, time, uncertainty, and execution risk | Atradius provides expert estimates; few expose a neutral multi-route model |
| Evidence-linked reasons and confidence | **MUST BEAT** | No material score without its drivers, evidence, gaps, assumptions, and applicable policy version | InDebted Comply’s traceability standard |
| Calibrated recovery probability | **MUST BEAT** | Introduce only after representative outcome data; publish calibration and confidence bands internally | Competitors claim predictive scoring |
| False precision from uncalibrated AI | **DELIBERATELY EXCLUDE** | Use ranges, scenarios, and unknowns until the data earns precision | Common AI-product risk |
| Pre-delinquency credit underwriting and broad early warning | **DELIBERATELY EXCLUDE** | Consume upstream signals; narrow evidence/readiness capture before default is included as an adjacent integration | CreditNirvana, HighRadius, Sidetrade |

### 6.4 Recovery operations and engagement

| Capability | Decision | Target standard | Main comparators |
|---|---|---|---|
| Portfolio dashboard and case workspace | **MUST MATCH** | Real-time status, balances, readiness, tasks, strategy, authority, and exceptions | All operational platforms |
| Rules-based strategies and journey orchestration | **MUST MATCH** | Configurable by segment, corridor, evidence state, response, and policy | InDebted, Sidetrade, Credgenics |
| Email, SMS, messaging, letter, and voice transport | **INTEGRATE** | Channel-neutral orchestration using authorized communications providers | Credgenics, HighRadius |
| AI-drafted communications | **MUST MATCH** | Evidence-grounded, tone-controlled, policy-checked, approval-aware generation | InDebted, CreditNirvana, Credgenics |
| Proprietary telephony stack, dialer, or foundation voice model | **DELIBERATELY EXCLUDE** | Integrate best-in-class infrastructure; own strategy, context, controls, and records | Credgenics, HighRadius |
| Recovery agents and delegated execution | **MUST MATCH** | Execute only the tested, permitted action classes within grants; include customer-owned agents and exception escalation | CreditNirvana, HighRadius, Sidetrade |
| Unbounded or unauthorized material actions | **DELIBERATELY EXCLUDE** | Automation never creates authority; a valid mandate and independently evaluated policy may permit bounded execution where lawful | Governance requirement |
| Creditor/client portal | **MUST MATCH** | Intake, evidence cure, approvals, status, economics, documents, and reporting | Debitura, Atradius, Sidetrade |
| Debtor resolution portal | **MUST MATCH** | Secure case view, dispute submission, documents, proposals, and payment integrations | InDebted, Atradius, Sidetrade |
| Dispute workflow | **MUST MATCH** | Classify, pause inappropriate action, assign, request evidence, resolve, and preserve full history | Sidetrade, HighRadius, Delos |
| Promise-to-pay, settlement, and payment-plan workflow | **MUST MATCH** | Authority-aware proposals, approvals, schedules, broken-promise events, and recalculated strategies | InDebted, CreditNirvana, Credgenics |
| Payment initiation and payment methods | **INTEGRATE** | PSP-hosted payment links and methods; Global Recovery Engine does not become the payment institution | InDebted, Credgenics, Atradius |
| Custody, escrow, or pooling of recovered funds | **DELIBERATELY EXCLUDE** | Funds move through authorized providers directly to entitled recipients | Company boundary |
| Payment and settlement reconciliation events | **MUST MATCH** | Normalize payment, reversal, fee, settlement, and allocation events without custody | Credgenics, CreditNirvana, AR platforms |
| Evidence-grounded demand and legal packet generation | **MUST BEAT** | Reusable facts, exhibits, chronology, balance, contradictions, and source citations; authorized review required | Delos, Credgenics legal notices |
| Legal advice, court representation, and filing authority | **INTEGRATE** | Qualified counsel approves, signs, files, and represents; platform prepares and tracks | Atradius, Allianz, Coface networks |
| Legal, insolvency, and enforcement stage tracking | **MUST MATCH** | Normalized milestones, deadlines, costs, documents, authority, and outcomes | Credgenics, CreditNirvana, global incumbents |
| Field collection, repossession, and physical enforcement workforce | **INTEGRATE** | Route to appropriate authorized providers when relevant; do not build a field workforce | Credgenics, CreditNirvana |
| Translation, notarization, apostille, process service, and local filing logistics | **INTEGRATE** | Orchestrate vetted specialists and preserve evidence of completion | Global legal/recovery networks |

### 6.5 Provider network and interoperability

| Capability | Decision | Target standard | Main comparators |
|---|---|---|---|
| Standalone provider directory or lead marketplace | **DELIBERATELY EXCLUDE** | Providers exist inside an intelligence and execution workflow, not as paid listings | Retrievables, generic marketplaces |
| Provider identity, licensing, coverage, capacity, and conflict checks | **MUST MATCH** | Verified, effective-dated eligibility before recommendation or handoff | Global networks |
| Claim Passport handoff | **MUST BEAT** | Transfer structured facts, evidence, authority, history, tasks, and outcome obligations without re-intake | Debitura/Oddcoll route cases but do not establish an open claim standard |
| Continuous case history across organizations | **MUST BEAT** | One canonical event history with organization-specific visibility and permissions | Incumbents often rely on handoff reports |
| Quotes, fee models, budgets, SLAs, and approvals | **MUST MATCH** | Comparable commercial terms and explicit authority before work begins | Debitura, Oddcoll, global incumbents |
| Route and provider recommendation | **MUST BEAT** | Optimize expected net recovery across route types and eligible providers, not proximity or commercial preference | Debitura, Oddcoll, Retrievables |
| Risk-adjusted provider benchmarking | **MUST BEAT** | Compare providers after controlling for claim age, value, dispute, evidence, debtor condition, corridor, and route | Debitura offers unified KPIs; deeper normalization is the wedge |
| Pay-to-rank or opaque preferred-provider bias | **DELIBERATELY EXCLUDE** | Rankings disclose factors, conflicts, commercial relationships, and uncertainty | Neutrality boundary |
| White-label partner workspace | **MUST MATCH** | Operators retain client ownership and brand while partners work in a controlled shared case | Debitura |
| One global principal collection contract under our name | **DELIBERATELY EXCLUDE** | The authorized operator/provider contracts for regulated execution; we supply infrastructure and records | Debitura/Oddcoll/global agency model |
| Insurance notification and claims submission | **INTEGRATE** | Create insurer-ready packages and exchange normalized status; insurer makes coverage decisions | Allianz, Atradius, Coface |
| Debt sale/liquidity matching | **INTEGRATE** | Eligibility, data room, valuation inputs, and authorized buyer routing without taking principal risk | InDebted Release, Delos |
| Purchasing, owning, or financing claims on our balance sheet | **DELIBERATELY EXCLUDE** | Preserve neutrality and avoid creating a capital and recovery-principal business | Delos, InDebted Release adjacency |

### 6.6 Control, compliance, and learning

| Capability | Decision | Target standard | Main comparators |
|---|---|---|---|
| Effective-dated jurisdiction and corridor packs | **MUST BEAT** | Rules, procedures, source materials, required evidence, templates, providers, costs, and deadlines versioned as deployable packs | InDebted Comply covers interaction rules; incumbents hold local knowledge |
| Policy-as-code | **MUST MATCH** | Executable rules with source status, applicability/precedence, tests, owner, dates, exceptions, and rollback | InDebted Comply |
| Pre-action compliance controls | **MUST MATCH** | Evaluate communications, route changes, evidence, authority, deadlines, and prerequisites; receipt/reconciliation covers external failure | InDebted Comply’s pre-send model |
| Explainable and traceable decisions | **MUST MATCH** | Material decisions return reasons, sources, scoped uncertainty, policy/model versions, and trace ID | InDebted Comply |
| Authority and assurance gates | **MUST MATCH** | Separate actor authority, execution mode, and assurance; support bounded delegation and necessary personal approvals | Enterprise platforms and agent authorization standards |
| Operational and AI audit trail | **MUST MATCH** | Trace actual human, rule, model, agent, and integration activity within retention/access policy; lawful disposition remains explicit | InDebted, CreditNirvana |
| Model/prompt/policy evaluation harness | **MUST MATCH** | Versioned tests, adversarial inputs, regression gates, monitoring, and rollback | Absence from marketing does not prove absence in competitors |
| Domain evaluation corpus and operating improvement | **MUST BEAT** | Demonstrate lower total effort and fewer critical errors across held-out claims, mandates, disputes, and payment failures | Comparative quality and maintenance economics require evidence |
| Model-agnostic AI orchestration | **MUST MATCH** | Replace models through evaluated adapters; preserve policy, evidence, events, and data-residency controls | Copyable infrastructure; measure cost and quality |
| Outcome Ledger | **MUST BEAT** | Verifiable, permissioned outcome observations connected to decision context; explicit missing/censored data | Competitor data coverage and causal capability are not established by marketing |
| Context-adjusted strategy and provider learning | **MUST BEAT** | Assess case mix, selection bias, overlap, and observation windows; avoid unsupported causal attribution | Conditional advantage requiring data rights and evidence |
| Experimentation and counterfactual evaluation | **MUST BEAT** | Safely compare strategies, recommendations, and human baselines within policy | Sidetrade benchmarks AI vs manual actions |
| Selling opaque outcome scores before representative data exists | **DELIBERATELY EXCLUDE** | Build trust and data first; expose uncertainty | Product-integrity boundary |

## 7. Competitor response matrix

| Competitor | We must match | We must beat | We should not copy | Primary threat path |
|---|---|---|---|---|
| **InDebted** | Decisioning, workflows, portals, AI governance, compliance controls, analytics | B2B evidence intelligence, claim portability, route economics, cross-provider neutrality | Becoming a consumer-focused collection agency or debt-liquidity principal | Expands its global data and compliance infrastructure into commercial claims |
| **CreditNirvana** | Closed-loop strategy-to-action workflow, supervisor control, legal milestones, auditability | Cross-border claim graph, arbitrary commercial documents, multi-jurisdiction route reasoning | India-lender-specific early warning, field, repossession, and asset modules as our core | Perfios distribution and data enable international expansion |
| **Credgenics** | Operational completeness, omnichannel orchestration, legal tracking, payments events, analytics | Evidence/readiness depth, global claim portability, neutral provider optimization | Building proprietary dialer, field force, or India-specific retail lending stack | Extends its full-stack platform from lenders into international commercial receivables |
| **HighRadius** | Enterprise integrations, invoice views, worklists, disputes, customer collaboration, configuration | Post-AR recovery depth, legal/provider orchestration, evidence and jurisdiction intelligence | Rebuilding the entire office-of-CFO suite | Adds late-stage recovery partners to its large enterprise distribution and data |
| **Sidetrade** | Next-best action, governed automation, customer portal, outcome measurement | Claim-level evidence graph, external recovery routes, legal readiness, corridor packs | Competing in broad order-to-cash automation | Extends its AI and data lake downstream into enforcement and provider routing |
| **Delos** | Document extraction, claim classification, evidence/readiness assessment, strategy and legal handoff | Neutrality, provenance, corridor rules, ENRV simulation, portability, provider/outcome intelligence | Purchasing claims or making the business dependent on owning enforcement rights | Combines its AI operating layer and claim ownership economics across more corridors |
| **Debitura / Oddcoll** | Easy placement, API/bulk intake, tracking, partner routing, quotes and status | Evidence understanding, route eligibility, case economics, risk-adjusted provider performance, interoperable history | Being only a referral/routing layer or hiding incentives in provider selection | Uses existing distribution and network coverage to add deeper claim intelligence |
| **Atradius / Allianz / Coface** | End-to-end route availability, credible legal escalation, client visibility, local expertise | Speed, transparency, structured evidence, configurable automation, open interoperability, explainable economics | Building an owned global human network or insurance balance sheet | Productizes decades of cases, local knowledge, and private outcomes with modern AI |
| **Retrievables** | Simple legal placement and attorney fit | Evidence quality, readiness, cross-border scope, economics, workflow, and outcomes | A lead-generation marketplace as the core business | Adds automated case analysis and performance-based matching |

## 8. Technology strategy

The architecture should let improved models lower operating cost while preserving rights and correctness. Visible features and internal schemas remain copyable; adoption, permitted data, maintained expertise, and measured performance must establish any durable advantage.

### 8.1 Evidence-linked commercial claims

The GRE domain model begins with commercial propositions that must be established, while retaining account and portfolio views:

- who contracted with whom;
- what was promised;
- what was performed;
- what became due;
- what remains unpaid;
- what was admitted or disputed;
- what rights, forums, deadlines, and routes exist;
- which actions are economically and operationally rational.

The Recovery Graph must preserve both the asserted facts and the evidence or uncertainty behind them.

The precise object meanings and invariants are maintained in the [Operating Model](03-operating-model.md). The graph describes relationships; it does not require a graph database.

### 8.2 Corridor compiler

New country support should not be a collection of prompts and documents. Each corridor pack should compile into:

- schemas and required facts;
- evidence requirements;
- route eligibility logic;
- deadline and limitation rules;
- communication and authority constraints;
- templates and localization rules;
- provider capabilities and prerequisites;
- cost/time assumptions;
- evaluation cases and expected results.

This makes geographic expansion testable and modular.

### 8.3 Recovery Digital Twin

The strategy engine should maintain a living set of alternative pathways for each claim. It updates when evidence, debtor signals, responses, costs, deadlines, provider quotes, or outcomes change.

The engine should distinguish:

- **claim validity**;
- **evidence strength**;
- **route eligibility**;
- **practical collectability**;
- **expected gross recovery**;
- **expected net recovery after cost, time, and execution risk**.

Collapsing these into one opaque score would destroy useful information.

### 8.4 Governed agent runtime

Agentic AI should run over explicit state and permissions:

1. observe a new event;
2. identify allowed goals and actions;
3. retrieve the relevant claim evidence and policy versions;
4. propose or perform actions within authority;
5. send material decisions to the required reviewer;
6. record actual inputs, decision reasons, outputs, and effects within data policy;
7. evaluate the result and update the case.

Agents consume and propose changes to the same domain service as people. The reviewed domain records and retained events remain authoritative. The number of named agent classes does not dictate the number of deployed agents or services.

### 8.5 Outcome and evaluation flywheel

Every material expert correction, recommendation disposition, provider handoff, response, cost, delay, settlement, judgment, enforcement result, and accounting/rights change should produce a structured event with applicable data-use permission.

The potential learning asset is the permitted, reliable linkage:

> **evidence state → decision → authority → action sequence → provider/corridor context → economic outcome**

That linkage is necessary but insufficient for causal analysis. Capture eligible alternatives, action selection, observation windows, customer restrictions, and unknown outcomes. Cross-tenant use requires permission and privacy controls; representative samples and defensible evaluation assumptions determine which claims can be made.

### 8.6 Interoperability standard

The Claim Passport should be both an internal domain model and an external contract:

- canonical JSON schema;
- human-readable case package;
- version and lineage rules;
- evidence manifest;
- authority and consent manifest;
- normalized event and outcome taxonomy;
- API and webhook contracts;
- visibility and redaction rules.

Independent acceptance and recurring reuse may create an advantage. Publish compatible interchange schemas, support export, and use bilateral integrations before assuming a universal standard. A closed schema alone is not defensible.

## 9. What could create a long-term lead

| Asset | Current judgment | Required proof |
|---|---|---|
| UI, prompts, generic agents, foundation-model access | Copyable | Maintain quality and speed |
| Model switching, graph schema, event history | Copyable design; important foundation | Better correctness/cost in real workflows |
| Expert-maintained corridor packs and evaluation corpus | Potential operating advantage | Coverage, update economics, error-rate and turnaround lead |
| Production integrations and verified provider execution | Potential compounding advantage | Recurring usage, low handoff rework, credible availability |
| Linked evidence/decision/action/outcome data | Potentially strong; conditional on rights and coverage | Legal/contractual use permission, representative cohorts, measurable improvement |
| Portable claim/authority/resolution records | Potential network advantage | Independent reuse and acceptance without mandatory platform lock-in |
| Lower cost per correctly resolved case | Immediate commercial wedge | Paid cohorts with support-adjusted contribution and protected quality |

Technology creates initial velocity. We should convert it into evidence of cost advantage, trusted execution, distribution, and legitimate learning. Competitors' ability to modernize is a central scenario, not a footnote.

## 10. Build, integrate, and defer

| Responsibility | Product approach |
|---|---|
| Domain meaning and continuity | Build the claim/evidence/rights model, scoped service contract, authority-aware action boundary, decision record, and outcome semantics |
| Customer and agent access | Build focused workflows and typed APIs over the same domain service; expose the minimum useful integration contracts |
| Commodity infrastructure | Adopt mature identity, storage, durable workflow, observability, communication, payment, and document-processing components where suitable |
| External specialist execution | Integrate eligible agencies, counsel, licensed data providers, payment providers, and other specialists through controlled work orders and receipts |
| Jurisdiction support | Maintain sourced, expert-reviewed, versioned corridor configuration and evaluations; activate only supported actions |
| Later options | Treat smaller claims, wider corridors, portfolio assurance, and agentic-commerce recourse as demand- and readiness-gated expansions |
| Initial exclusions | Owned debt, custody/escrow, broad underwriting/O2C, standalone general compliance SaaS, a proprietary foundation model, and autonomous legal representation |

The [Business & Project Overview](01-business-project-overview.md) defines the intended commercial perimeter. The [Operating Model](03-operating-model.md) owns action responsibility, delegation, reserved work, and the checks required before external effects. Integration does not itself remove GRE's obligations.

## 11. Comparative validation and product scorecard

The business objectives are maintained in the [Business & Project Overview](01-business-project-overview.md); metric definitions and observation rules are maintained in the [Operating Model](03-operating-model.md), Section 20. Product claims require an explicit comparison and a reproducible evaluation record.

| Question | Required comparison or evidence |
|---|---|
| Does the product understand claims better? | Authorized representative cases, critical-field/evidence error taxonomy, held-out organizations where feasible, and independent expert adjudication |
| Does the technology outperform readily available alternatives? | The same inputs, permissions, task, and service boundary evaluated against the customer's current process and a strong general model with ordinary workflow tooling |
| Is automation actually useful? | Report raw system results and final results after human correction separately; include exception rate, reviewer effort, elapsed time, and total service cost |
| Does continuity matter commercially? | Handoff acceptance, missing-information cycles, re-keying, repeated review, integration work, and time to an authorized next action |
| Are actions controlled and reliable? | Scope/authority violations, stale-source behavior, adversarial evidence, tenant isolation, revoked delegation, uncertain side effects, and reversal handling |
| Do economic recommendations help? | Explicit alternatives, available evidence, costs, observation windows, and decision uncertainty; compare like cohorts without treating selected outcomes as causal lift |
| Does the service remain viable as models change? | Substitute models/providers and measure retained correctness, speed, integration effort, and fully loaded cost |
| Is a corridor ready to sell? | Declared coverage, qualified policy review, executable provider routes, support capacity, evidence rights, and measured operating economics |

Synthetic cases support engineering checks. Customer value and production reliability need authorized real-case and service evidence. Competitor feature pages establish comparison targets; they do not demonstrate GRE's superiority. Pilot result reports must state sample size, exclusions, missing outcomes, evaluation date, and the exact capability version assessed.

## 12. Competitive monitoring priorities

These priorities reflect the September 5, 2026 research and strategic judgment. Reassess them when source evidence or customer buying behavior changes.

### Tier 1 — direct product and distribution comparisons

1. **Delos:** closest direct overlap in B2B claim intelligence and strategy; strongest reason not to confuse document AI with a moat.
2. **Debitura:** strongest cross-border routing/distribution reference; could add intelligence above its network.
3. **InDebted:** strongest integrated product and compliance architecture reference; has scale, data, and multi-market experience.

### Tier 2 — incumbents with adjacent distribution and execution assets

4. **Atradius / Allianz Trade / Coface:** trust, global reach, local expertise, and historical outcomes could become formidable if productized.
5. **HighRadius / Sidetrade:** enterprise distribution, ERP integration, invoice data, and mature AI could extend downstream.
6. **CreditNirvana / Credgenics:** sophisticated full-stack execution and India-based domain strength could expand from lender collections into trade recovery.

### Tier 3 — placement and workflow references

7. **Oddcoll:** validates centralized international placement and local-provider orchestration.
8. **Retrievables:** validates frictionless legal matching, but currently represents a narrower marketplace model.

## 13. Five-year scenario test

The following are planning scenarios for 2031, not forecasts with invented probabilities.

| Scenario | Threat to our original model | Valuable response | Leading evidence to monitor |
|---|---|---|---|
| Strong AI, limited regulated autonomy | Human review remains expensive | Superior evidence, exception selection, scoped authority, and efficient review | Customer touches per case; legal/procurement acceptance |
| Businesses delegate finance tasks broadly | Human workspaces and seat fees shrink | Embedded services, agent identity/mandates, bilateral resolution, usage contracts | Paid machine-origin cases and production partner integrations |
| ERP/payment platforms bundle recovery | Distribution captures standalone app value | Integrate where domain depth and external execution produce measurable benefit | Buyers choose build/bundle; our incremental ROI |
| Synthetic evidence and adversarial agents increase | Cheap analysis is easier to deceive | Source-connected records, independent verification, protected execution, dispute receipts | Authenticity incidents and false acceptance rates |
| Better contracting/payments reduce ordinary defaults | Raw recovery case volume falls | Recurring readiness and exception resolution if customers pay for them | Default volume, dispute mix, monitoring attach rate |
| Models commoditize rapidly, incumbents modernize | Technology lead disappears | Faster domain evaluation, trusted execution, distribution, permitted outcomes, lower cost | Competitive benchmark and replacement-model performance |

The full offering should remain useful under the first and last scenarios. The agentic-commerce scenario creates upside; the business must not require it to arrive on schedule.

## 14. Expansion options and evidence gates

| Option | Evidence required before commitment |
|---|---|
| Evidence readiness before default | Recurring source access, clear permissions, willingness to pay for prevention/readiness, and measurable reduction in later reconstruction |
| Embedded Resolution integrations | A paid buyer/integration, scoped machine authority, production support ownership, and attractive cost per fulfilled service |
| Bilateral structured resolution | Both parties' verified mandates, useful shared records without private-strategy leakage, valid exact-term acceptance, and a supported operating perimeter |
| Smaller claims | Automation and exception economics that support the price while preserving quality; low claim size is not a unique market position |
| Pooled benchmarks or learning | Separate permitted data use, sufficient representative coverage, privacy controls, and improvement beyond a viable tenant-private service |
| Portfolio assurance | A buyer with a recurring decision to support, reliable observations, and appropriate service/representation limits |
| New corridors and routes | Paid demand, qualified policy ownership, maintained source/evaluation coverage, eligible execution, and support economics |
| Agentic-commerce recourse | Actual unresolved commercial problems arising from delegated activity, customer demand, reliable identity/mandates, and a workable responsibility model |

These are options, not announced production services or an MVP backlog. Preserve architectural compatibility where inexpensive; avoid implementing speculative depth before the relevant gate is met. The current project sequence and open commercial decisions are maintained in the [Business & Project Overview](01-business-project-overview.md).

## 15. Agent access, evidence readiness, and structured resolution

| Extension | Customer value | Minimum contract | Commercial status |
|---|---|---|---|
| Embedded agent service | Operate from the customer's existing system/agent | Typed tasks, scoped authority, asynchronous status, cancellation, receipts, usage | Architecture requirement; buyer/integration validation needed |
| Evidence readiness before default | Preserve performance/acceptance proof early | Source provenance, versioned obligation, permissions, risk of missing evidence | Target offering extension; demand unvalidated |
| Bilateral structured resolution | Resolve mismatched records or negotiate permitted terms efficiently | Shared disclosed record, separate private contexts, dual mandate checks, exact-term receipts | Target offering extension with scoped autonomy |
| Rights and economic continuity | Avoid invalid demands and double recovery | Time-versioned interests; separate debt, accounting, settlement, insurance/sale proceeds, cash | Core correctness requirement |
| Decision episodes and value of information | Spend review/data/legal budget where it changes the result | Point-in-time alternatives, costs, selection context, observation windows | Core learning contract; advanced optimization follows evidence |
| Portable assurance | Let a new provider verify the handoff | Provenance/mandate/acceptance receipts and exportable schemas | Adoption hypothesis; no proprietary lock-in requirement |

Public technology signals from the September 5 research: [A2A](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents) supports agent communication; [AP2](https://ap2-protocol.org/ap2/specification/) describes payment mandates and dispute evidence but leaves detailed dispute-resolution use outside its specification. A commercial-resolution service is our inference and opportunity hypothesis, not a capability those standards grant GRE. Message interoperability and signed payment mandates do not by themselves establish valid legal delegation or resolution authority.

Autonomous negotiation also has existing adjacent providers: [Pactum](https://pactum.com/blog/understanding-autonomous-negotiations) describes autonomous procurement negotiations. This supports the direction of bounded machine negotiation, but does not establish capability or customer demand for the specific commercial-recovery service proposed here.

## 16. Scope and implementation discipline

Use one modular domain service for workspaces, APIs, and agent adapters. Prefer mature storage, workflow, identity, payment, and communication components. A graph-shaped model can use conventional storage; an audit/event contract does not require a distributed event-sourcing platform or many microservices.

Agents, models, connectors, and protocol versions are replaceable. Rights, evidence, authority, decision context, action receipts, and outcome meaning must remain stable across replacements. The [Operating Model](03-operating-model.md) specifies the domain and runtime constraints; the [Workflow & Interaction Specification](04-workflow-interaction-specification.md) defines observable interaction behavior.

Track capability status as `DESIGNED`, `SHADOW_TESTED`, `PILOT_ENABLED`, `COMMERCIALLY_SUPPORTED`, `SUSPENDED`, or `RETIRED`. Declare route/jurisdiction/provider scope and support ownership. The current document set establishes design, not production services. Operational completeness requires working services and partners.

Maintain this document in place as the authoritative detailed offering and strategy reference. Business decisions and project sequence belong in the [Business & Project Overview](01-business-project-overview.md); changing an operating rule or workflow behavior requires updating the relevant companion document. Preserve external research dates, distinguish vendor claims from observed performance, and revisit comparative conclusions when new evidence warrants it.
