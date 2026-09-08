# Architecture and stack decision

**Status:** Selected direction, reconciled September 7, 2026. Local setup is verified; product implementation and production provisioning are pending.

**Owner:** Vishal, with coding-agent implementation and review support.

**Owns:** Module boundaries, technology choices, source-of-truth rules, integration boundaries and architecture change decisions.

**Scope:** [Foundation + Trade Pilot](06-pilot-brief.md). Exact installed versions and observed checks belong to [10](10-dependency-baseline.md); host commands belong to [09](09-development-environment.md).

## 1. Selected application structure

Use one GitHub repository containing a modular Python domain application and a TypeScript web application. Run the backend as an API process and workers as needed. Family workflows compose shared operations. Deployment processes are not separate business ownership boundaries.

The selected stack remains Next.js/React/TypeScript; FastAPI/Pydantic/Python; PostgreSQL with SQLAlchemy, Psycopg and Alembic; Temporal; and Azure Blob. The verified container, dependency locks and setup fixtures remain useful. Their presence does not establish a customer product or production readiness.

This fits the founder's data/application background and the Pilot's document reconstruction, exact financial records, long waits and independently executed provider work. Upgradeability comes from explicit contracts, owned data and adapters, compatibility checks and disciplined migrations. Replacing a provider or workflow engine still has a cost.

## 2. Component decisions and remaining integration work

| Concern | Direction | Current boundary and next proof |
|---|---|---|
| Web | Next.js App Router, React, TypeScript; Tailwind/shadcn and TanStack Query when the first UI needs them | Creditor/reviewer and provider-review surfaces; a direct obligor collection portal is outside this Pilot. Explicit sensitive-data caching and browser checks. The existing web is a build fixture. |
| API/domain | FastAPI/Pydantic, Python modules, REST/OpenAPI, generated Hey API TypeScript client | One authoritative operation implementation; web types do not replace server-side validation or authority. |
| Records | PostgreSQL, SQLAlchemy, Psycopg, Alembic | Exact monetary values, constraints, transaction-scoped authorization and migrations. Runtime role must be non-owner/non-bypass with tested tenant isolation. |
| Durable progress | Temporal Python SDK; local development server, hosted Temporal service when justified | Workflow/activity histories, retry and wait semantics; workers invoke current domain checks. GRE hosts the workers even when the service is managed. |
| Evidence | Azure Blob adapter; Azurite locally | Quarantine, permitted disclosure, expiry/retention and restore behavior must be implemented. Emulator SharedKey/HTTP success does not validate Azure identity/TLS or production storage. |
| Identity | Clerk remains selected integration direction | Validate SDK, token/session lifecycle and organizational roles; map identities to GRE-owned actors. Case and action authority remain GRE responsibilities. No live account integration is claimed. |
| AI | Official OpenAI Python SDK and Responses/structured outputs behind bounded task interfaces | Add when implementing extraction/review assistance; evaluate missingness, contradictions, refusal, harmful errors, latency, human effort and cost. |
| OCR/layout | Azure Document Intelligence where supported; permitted manual review fallback | Validate exact API/model, formats and page/source references. An extraction is not proof of authenticity, debt or enforceability. |
| External providers | Secure assisted packet/reply first; CSV/SFTP/API adapters when a named provider needs them | Provider-owned requirements and acceptance; contractually defined event return and exception ownership. Integrate actual declared interfaces, not a speculative universal connector catalog. |
| Payments | Verified creditor/provider instructions and source-reviewed observations; supported PSP adapter if needed | GRE service billing is separate. No repayment custody/pass-through; provider admission, destination verification and reversal handling are required before a live route. |
| Hosting | Azure Container Apps, ACR, managed PostgreSQL and Blob | Cost, region, customer requirements, worker deployment, identity, network, backup/restore and incident readiness must be proved before live deployment. |
| Delivery | Terraform, GitHub Actions, OIDC, Key Vault and managed identities | Scoped deployment authority and exact artifact versions; no paid resources are provisioned by this documentation change. |
| Observability | OpenTelemetry with Azure Monitor/Application Insights as selected backend | Sensitive content is redacted. Operational telemetry is separate from attributable domain audit records. |
| Quality | pytest/Hypothesis/Ruff/Pyright and suitable web lint/Vitest/Playwright | Install when the relevant product package is introduced; use risk-driven assertions, migrations, isolation, replay and end-to-end checks. |
| Development | Existing ARM64 VS Code Dev Container, uv and pnpm | Preserve locked versions and documented TypeScript compatibility fallback. Use [10](10-dependency-baseline.md) for commands. |

These are architecture selections and integration tasks, not claims that every listed SDK or account is installed. Selected primary references: [FastAPI client generation](https://fastapi.tiangolo.com/advanced/generate-clients/), [PostgreSQL RLS](https://www.postgresql.org/docs/current/ddl-rowsecurity.html), [Temporal Python](https://docs.temporal.io/develop/python), [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/overview), [GitHub Azure OIDC](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-azure).

## 3. Module ownership

These are internal responsibilities. Start with only the packages needed by a complete slice; do not create a service or a generic framework for each row.

| Module | Owns | Must not independently own |
|---|---|---|
| Identity/access | External identity mapping, memberships, sessions and scoped case access | Rights to collect, settlement mandate or another party's private record |
| Case/service | Continuing cases, bounded services, responsible owner, waits and surviving duties | Whether an obligation is paid or a provider accepted work |
| Evidence/Passport | Source artifacts, assertions, verification records and versioned portable views | A competing financial balance or an automatic truth label |
| Obligations/finance | Obligations, rights interests, exact currency amounts, reported/verified payments, allocation and reversal | New legal rights inferred from a transfer or model output |
| Agreements | Exact externally agreed terms, acceptance evidence, schedules and conditional releases | A payment or provider status that automatically creates acceptance or discharge |
| Authority/actions | Grants, approvals, exact action binding, current commit checks, outbox and receipts | A permission granted by a UI role or a stale workflow snapshot |
| Classification/policy | Matter profile, corridor rules, evaluations and release conditions | An entitlement to act merely because a feature is purchased |
| Provider exchange | Provider profiles, review requests, placement/deltas, direct appointment references and returns | Provider tactical supervision or a guarantee of external cessation |
| Disclosure/corrections | Purpose-specific views, manifests, scoped export and correction delivery | Universal permission to disclose every Passport source |
| Observations/quality | Attributed events, freshness, costs, outcome measurements and evaluation evidence | Payment, agreement, authority or legal truth from a provider report alone |

Network & Control packages selected modules commercially; it is not another copy of them. A future family may add its own participation or account-history workflow while reusing shared operations. Private participant isolation and Consumer data roles require deliberate future designs, not a Trade workflow with renamed labels.

## 4. Data and effect boundaries

PostgreSQL owns authoritative business state. Temporal owns durable process progress. Blob owns stored object bytes while database records define provenance and access. Derived read models, model outputs, incoming events and exported Passports reference canonical records without becoming independent editable truth.

Write the domain state change and its outbox intent in one database transaction. A worker claims work with a stable operation/attempt identity and rechecks applicable authority, holds, amount, service scope, disclosure, provider eligibility and current release conditions before an external effect. Design callback delivery and retries for duplication and reconciliation. Exactly-once external execution is not assumed.

Example: a placement offer is prepared against a specific provider profile and disclosed packet. If the profile, mandate or material claim facts change before activation, the worker cannot treat the earlier response as unconditional authority. It records the delta and obtains the required current decision. A timeout after an external send remains uncertain until the relevant receipt or reconciliation resolves it.

An Action Receipt composes attempt-level evidence; an Authority Envelope composes grants and exact bindings; a Quality Scorecard derives measurements. [05](05-domain-data-contracts.md) owns the schema and [03](03-operating-model.md) owns business semantics. An external system identifier is provenance, not a credential or cross-tenant read right.

Enforce authorization at every entry point: web, API, worker, import, callback, support operation and future protocol adapter. Use a non-owner database runtime role, transaction-local tenant/actor context and negative access tests. Credentialed provider review access can precede appointment when independently permitted, but cannot authorize collection. Retention, legal holds and corrections are not defeated by labeling an export immutable.

## 5. Runtime and deployment

The web calls the API. API and workers call shared domain operations. Workers poll Temporal task queues; no inbound connection from Temporal to a worker is implied. The outbox relay may run in a worker process. Models and transport adapters receive the minimum permitted inputs and return attributed results.

Keep sensitive Temporal payloads minimal, preferring opaque references. Address payload encryption, region, retention, graceful shutdown and replay-compatible upgrades before live use. A polling worker needs an appropriate availability/scaling configuration; managed workflow hosting does not run application workers for GRE.

| Environment | Use | Required separation |
|---|---|---|
| Local | Synthetic product work and existing service probes | Git-ignored credentials and persistent developer volumes; no real evidence by default |
| CI | Disposable build, reference, migration and behavioral checks | Independent databases/storage; no access to local records or paid models by default |
| Staging | Real cloud identity/network and supported sandbox integration | Separate resources, credentials and permitted datasets |
| Pilot production | Released Trade scope and named providers | Audited access, monitored operations, restore evidence, support and incident ownership |

A U.S. primary region remains the working deployment hypothesis, subject to buyer requirements, lawful transfers, service availability and cost. Azure hosting alone does not establish end-to-end residency: identity, AI, telemetry, workflow and partner services need explicit data-flow review. Future India Consumer data restrictions may require different storage topology; they do not force a speculative replatform of this Trade Pilot.

## 6. Incremental reuse and delivery practice

Build the first complete Trade slice through authenticated intake, reviewed evidence/balance and a useful assessment or no-route result. Add named-provider preflight, an attributed response, reliable direct activation and provider continuity in subsequent dependent slices. Privacy, correction, service completion and operational controls needed for assessment are delivered with that service; later provider extensions reuse them. Shared controls used by a slice must be real; optional modules can remain absent. No slice can advertise a live service before its [release gate](13-pilot-release-and-assurance.md).

Work on one bounded implementation item at a time, with independent business/provider discovery in parallel. Agents may work concurrently on separate owned files, but coordinate shared schema/migration boundaries and ports/data. Generated clients are regenerated from the canonical API, never manually maintained as another contract definition.

An architecture change record must identify the failed requirement or measured problem, options, migration/operating cost, decision, owner and validation. Keep the selected stack unless this evidence justifies changing it. Redis, Kafka, Kubernetes, specialized graph/vector stores, public protocol adapters and richer agent frameworks are [future candidates](07-future-development-and-business-deliverables.md), not default Foundation requirements.

The existing dependency setup check includes retained historical workflow evidence; a completed workflow may eventually age out of Temporal retention. The first delivery item separates historical persistence proof from repeatable service health without masking genuine failures. Do not claim the issue is already fixed.

### P-001 package and CI decisions

The [P-001 implementation plan](implementation/P-001-development-foundation.md), dated September 8, fixes the initial source layout and delivery choices: one installable `gre-platform` Python distribution under `src/gre`; `apps/web` for the product shell; separate generated product/setup clients; repeatable health independent of historical workflow retention; and a native ARM64 disposable CI gate using the existing toolchain. These are planned implementation decisions, not claims that the packages or CI already exist. Exact task boundaries and compatibility evidence belong to that plan and its verification record.

## 7. Accountabilities

Vishal owns product decisions, priorities and release accountability. Coding agents inspect actual repository state, implement authorized bounded changes, run available checks, preserve unrelated work, and report exact outcomes and limitations. They cannot claim a Mac check from a hosted run, legal approval from a source search, or product readiness from a fixture build.

GRE's runtime AI is separate from the development agent. Runtime AI may propose or extract through restricted application operations; it cannot bypass authority or current-state gates. Vendor data settings, permitted purpose, logging and retention must be decided before real evidence is sent to models. A no-training setting does not imply zero retention.

The current task completed documentation/reference design. Product development follows [11](11-prioritized-pilot-backlog.md); actual installed versions and setup commands remain in [10](10-dependency-baseline.md).
