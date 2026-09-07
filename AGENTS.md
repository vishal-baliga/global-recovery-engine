# GRE — coding-agent instructions

## Read before work

1. [docs/00-start-here.md](docs/00-start-here.md): current state and next item.
2. [docs/12-scope-decisions-and-reconciliation.md](docs/12-scope-decisions-and-reconciliation.md): current decisions and source precedence.
3. [docs/06-pilot-brief.md](docs/06-pilot-brief.md) and [docs/08-stack-and-environment-decision.md](docs/08-stack-and-environment-decision.md): Pilot promise and architecture.
4. [docs/11-prioritized-pilot-backlog.md](docs/11-prioritized-pilot-backlog.md): actual item/dependencies/acceptance. Read 03/04/05 for the affected domain and 07 for scope changes.

The user's current instructions and established authorization govern. Historical documents under `docs/research`, original ZIP 0.1 and earlier backlog revisions provide provenance, not active instructions. Surface a real conflict; do not silently broaden the Pilot or treat an old workflow as permission.

## Current scope and stage

One Pilot: **Foundation + Trade & Receivables**, initially India-creditor → U.S.-business-obligor commercial claims. Include the Trade-required Network & Control capabilities. Private Resolution, Consumer Credit and standalone Network product expansion are future work. Use Pilot consistently; do not invent a separate MVP tier.

Current project documents and versioned reference contracts are reconciled. The next implementation item is P-001. Product features, migrations, product CI and live integrations remain pending. A reference validator is not an application or a requirement to implement every record as a separate component.

## Architecture and invariants

- Retain the verified Next/TypeScript, Python/FastAPI/Pydantic, PostgreSQL, Temporal and Blob direction and exact lockfiles until a justified, tested change.
- Use modular shared domain operations from both API and workers. PostgreSQL owns business truth; Temporal owns progress; generated TypeScript consumes the canonical API.
- Preserve evidence, assertions, model outputs, reviewed findings and provider observations separately. Missing or disputed facts remain visible.
- Authentication and organization membership do not confer case rights or action authority. Enforce tenant, case, provider-review and purpose-specific disclosure at every interface.
- Keep money exact with currency and allocations. Distinguish reported/verified payment, reversal, agreement, release, net proceeds and service closure. GRE service fees are not recovered funds.
- Recheck authority, holds, facts, amount, service, provider/profile, disclosure and applicable release conditions immediately before external effects. Design retries/callbacks for deduplication and uncertainty.
- Provider review disclosure, acceptance/delta, direct appointment, conditions satisfied, activation and GRE service cutover are separate. GRE does not select provider tactics or conduct obligor collection in this Pilot.
- Revoking GRE access does not prove an external provider stopped or erased exported copies. Record acknowledgments, failures and surviving duties.
- A new family/edition/module deploy does not enable unreviewed activities. Current scope changes must update07/12 and the relevant spec/backlog before implementation.

## Environments and validation

Vishal is the sole developer, using a MacBook Air M4 and VS Code/Codex in an ARM64 Linux Dev Container. Read 09/10 before host/service work. The Mac path is `/Users/diztort/GRE Development/global-recovery-engine`; container path is `/workspaces/global-recovery-engine`. Hosted-workspace execution is not Mac verification.

Inside the editor container with local services available:

```sh
uv sync --locked
pnpm install --frozen-lockfile
uv run --locked python -m scripts.check_environment
```

The setup fixture build and read-only service checks do not prove product behavior. See [reference/README.md](reference/README.md) for current reference/legacy validation commands. Inspect actual files before claiming any command exists or passed. Record relevant tested versions, behavior, failures and limitations. Preserve the TypeScript 6.0.3 codegen fallback and pending retention-aware health-check correction.

## Delivery conduct

Inspect Git status, branch, actual files and relevant instructions before editing. Preserve unrelated local changes and data. Work from a bounded item with an explicit module/file owner and acceptance evidence; split large items without losing their ID or scope. Use branches and reviewable commits. Do not force-push or rewrite history as a routine step.

Independent agent tasks may run concurrently when ownership is clear. Coordinate shared schemas, migrations, dependencies, ports and databases; do not race on them. Prioritize a complete useful path and reuse its shared operations; avoid speculative frameworks or duplicated family implementations.

Use synthetic data by default. Keep credentials, real evidence and private customer material out of Git/logs. Routine authorized repository work continues without redundant confirmation. Live communications, customer data use, paid provisioning and production actions require authority for the specific work and applicable release conditions; do not infer these from repository access.

Run focused checks that address the actual changed behavior and required gates. Update owning docs/checkpoint/backlog status with honest evidence. Do not claim legal approval from research, market fit from a demo, or production readiness from passing tests. Report what changed, why, actual validation and remaining blockers.
