# Global Recovery Engine — coding-agent instructions

## Read before working

1. Read `docs/00-start-here.md` for current decisions, setup status, and the next task.
2. Read `docs/06-pilot-mvp-brief.md` and `docs/08-stack-and-environment-decision.md` for scope and architecture.
3. Use `docs/07-future-development-and-business-deliverables.md` when changing scope. Consult the relevant sections of documents `01`–`05` for domain detail.

Follow the user's current instructions and established authorization. The checkpoint reconciles historical document status; it does not override new user decisions.

## Current delivery stage

Vishal is the sole developer, using a MacBook Air M4 (2025), VS Code, and Codex. GitHub is connected to ChatGPT; the VS Code Codex extension is installed and signed in, as reported by the user. The local Codex inspection confirms a clean clone on native arm64 macOS 26.6.2 with 16 GiB RAM, Git, and Apple Command Line Tools. See the setup checkpoint for subsequent installation results and the next toolchain step.

Proceed incrementally: environment setup, prioritized backlog, project/delivery document reconciliation, then product implementation. Do the active setup work without inventing a product backlog or starting application features early. Routine authorized inspection and reversible setup work should continue without repeated confirmation.

The repository initially has documents and a reference ZIP only. There are no established build, lint, test, or launch commands. Inspect actual files before claiming a command exists or succeeds. Record working commands when the toolchain is established. A check run in a hosted workspace does not verify the developer's Mac.

## Architecture direction

- TypeScript/Next.js web; Python/FastAPI/Pydantic domain application; OpenAPI-generated TypeScript clients.
- PostgreSQL for business records; Temporal for durable process progress; shared Python domain checks used by API and workers.
- Azure managed hosting/storage, Clerk authentication, and provider adapters as described in the stack decision.
- Proposed majors: Node 24 LTS, CPython 3.14, Next.js 16, PostgreSQL 18. Validate compatibility and lock resolved dependencies. Record a justified fallback when needed.
- Target native Apple silicon host tooling and a reproducible Linux Dev Container. Verify container/image architecture support during setup.

The contract ZIP is an earlier schema/validator reference. It is not the application, a mandatory code generator, or a requirement to implement every record as a separate component.

## Domain principles to preserve

- Keep source evidence, assertions, model output, and reviewed findings distinct. Missing loan terms stay unknown.
- Authentication does not grant case authority. Enforce case access, disclosed borrower views, action mandates, and private negotiation context separately.
- Represent money exactly with currency and allocation records. Keep reported payments, verified receipts, reversals, agreement acceptance, and completed recovery distinct.
- Recheck current authority, balances, holds, and terms before external effects. Design retries and callbacks for deduplication and reconciliation.
- Both pilot tracks remain required. Record any deferral with its customer impact, interim route, owner, and reconsideration condition.

## Working practice

Inspect Git status and relevant instructions before editing; preserve existing user changes. Keep work bounded and reviewable, using task branches for subsequent implementation work. Do not force-push or rewrite existing history as a routine setup step.

Use synthetic data in development. Keep credentials, real case evidence, local state, and private customer material out of Git. Production actions and paid provisioning depend on authorization for the specific work; reuse authorization already granted.

Validate the consequences of the change with focused checks. Report what changed, what was actually verified, and what remains uncertain. Update the setup checkpoint when the environment state changes. Do not expand testing without a concrete remaining risk.
