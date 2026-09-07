# Start here — current GRE baseline

**Updated:** September 7, 2026. **Owner/developer:** Vishal.

**Current scope:** One market-facing **Pilot: GRE Foundation + Trade & Receivables**, with the Network & Control capabilities needed by Trade.

**Stage:** Project documentation and reference contracts reconciled; product implementation follows the current backlog.

## Current decision and next work

Build a source-linked commercial claim readiness, named-provider preflight, direct appointment/acceptance and continuing correction/status/financial-observation service. The initial profile targets India creditors and U.S. business obligors. Buyer demand, exact released states/activities, provider coverage and live permission remain evidence to establish.

Private Resolution, institutional Consumer Credit and standalone Network commercialization are [future development](07-future-development-and-business-deliverables.md). There is no concurrent personal-loan Pilot commitment. GRE does not perform the provider's collection tactics or custody recovered funds. Its own disclosure, support and agreed continuity responsibilities survive handoff.

The next implementation item is **P-001 in [11](11-prioritized-pilot-backlog.md)**: introduce the minimal product package/quality structure on the verified setup. Business discovery/provider work can proceed alongside permitted synthetic development. Read the item's actual dependencies and prepare its bounded design before editing product code.

## Read by purpose

| Need | Owning document |
|---|---|
| Current authority, changes and unresolved decisions | [12 — Scope and reconciliation](12-scope-decisions-and-reconciliation.md) |
| Customer promise and exact Pilot inclusions | [06 — Pilot brief](06-pilot-brief.md) |
| Business and competitive portfolio | [01](01-business-project-overview.md), [02](02-product-offering-competitive-strategy.md) |
| Responsibilities and user/provider paths | [03 — Operating model](03-operating-model.md), [04 — Workflow](04-workflow-interaction-specification.md) |
| Domain semantics and executable reference | [05](05-domain-data-contracts.md), [reference README](../reference/README.md) |
| Modules and technology | [08 — Architecture](08-stack-and-environment-decision.md) |
| Mac/container commands and actual pins | [09 — Environment](09-development-environment.md), [10 — Dependencies](10-dependency-baseline.md) |
| Ordered delivery and old-item disposition | [11 — Backlog](11-prioritized-pilot-backlog.md) |
| Real-data/live-service conditions | [13 — Release and assurance](13-pilot-release-and-assurance.md) |
| Buyer discovery, proof and public claims | [14 — Market validation](14-market-validation-and-proof.md) |
| Deferred families, depth and business options | [07 — Future register](07-future-development-and-business-deliverables.md) |

Current checked-out Git documents govern development. Historical research, older attachments and superseded backlog revisions explain prior decisions; they do not override this scope. New owner decisions must be propagated to all affected owning artifacts.

## Verified setup and honest limits

These are previously recorded Mac/local-Codex observations, preserved from setup commit `5511b1ef3096b7791a3c8be62a916c469c9f3a73`. The documentation pass did not rerun the Mac toolchain or restart its services.

| Area | Recorded evidence |
|---|---|
| Mac | MacBook Air M4 (2025), native ARM64,16GiB RAM, macOS26.6.2 |
| Editor | VS Code 1.136.1, Dev Containers 0.466.0, signed-in Codex executing as non-root `vscode` in Debian 12 ARM64 |
| Host tooling | Git 2.50.1; Apple CLT; Homebrew 6.0.22 at `/opt/homebrew`; Docker Desktop 4.89.0/Engine 29.7.2/Compose 5.5.0; ARM64 hello-world passed |
| Language tools | Python 3.14.7, Node 24.20.0, pnpm 11.10.0, uv 0.12.10; offline and editor environment checks passed |
| PostgreSQL |18.6 Bookworm ARM64; private network, persistent named volume; authenticated connectivity and synthetic normal-restart persistence passed |
| Temporal |CLI1.8.3, embedded Server1.31.2/UI2.50.1, SDK1.32.0; same workflow/run survived server/worker restart; localhost UI worked |
| Azurite |3.36.0 ARM64; private Blob emulator; authenticated bytes/metadata and HTTP403 anonymous rejection; restart persistence and scoped cleanup passed |
| Shared dependencies |Fresh locked installs, FastAPI validation, generated client live requests, TypeScript check and Next fixture production build passed; TypeScript 6.0.3 fallback retained |
| Still pending |Customer product, application migrations/CI, live identity/AI/OCR/provider integrations, production deployment and runtime acceptance evidence |

Exact historical commands, digests and test observations remain in 09/10. Recreated editor containers need host attachment; some image pins, backup/restore and upgrade validation remain work. Azurite's default root process and Temporal UI bridge egress are documented development limits. Historical workflow receipts can outlive server history; P-001 separates this evidence from repeatable health checks.

## Working locations and checks

Mac checkout: `/Users/diztort/GRE Development/global-recovery-engine`.
Editor container: `/workspaces/global-recovery-engine`.
This hosted ChatGPT workspace is neither of those environments.

From the editor repository root, with the three local services running and attached:

```sh
uv sync --locked
pnpm install --frozen-lockfile
uv run --locked python -m scripts.check_environment
```

These are setup/dependency checks. Use [reference README](../reference/README.md) for contract conformance commands. Do not substitute either for product behavior, production readiness or legal/commercial evidence.

Keep credentials, customer evidence, local state and private material out of Git. Preserve local data and unrelated changes; inspect branch and working-tree status before work. The repository update does not mean the Mac checkout automatically changed branches or commits.
