# Global Recovery Engine

Recovery preparation and continuity infrastructure for independently accountable execution.

**Current release scope: one Pilot — GRE Foundation + Trade & Receivables.** The first profile targets India creditors with unpaid commercial goods/services claims against U.S. businesses. GRE prepares source-linked claims, tests readiness against a named provider's requirements, supports direct appointment and acceptance, and preserves corrections, observations and portability. Buyer demand, precise coverage and live release remain to be established.

**Current stage:** Authoritative project documents and versioned reference contracts reconciled. P-001 has a published implementation plan and seven ordered tasks; the next step is Mac checkout/environment confirmation, followed by implementation of that plan. Existing setup verification is historical evidence.

## Start and develop

- [Start here](docs/00-start-here.md): current decisions, observed setup and next work.
- [Pilot brief](docs/06-pilot-brief.md): included outcomes, operating boundaries and real service requirements.
- [Prioritized Pilot backlog](docs/11-prioritized-pilot-backlog.md): Foundation/Trade delivery and the disposition of every old backlog item.
- [P-001 implementation plan](docs/implementation/P-001-development-foundation.md) and [verification record](docs/implementation/P-001-verification-record.md): selected design, task sequence and pending local evidence.
- [Architecture](docs/08-stack-and-environment-decision.md): shared modules, stack and source/effect ownership.
- [Development environment](docs/09-development-environment.md) and [dependency baseline](docs/10-dependency-baseline.md): exact commands, pins and observed verification.
- [Agent instructions](AGENTS.md): working and validation rules.

## Specification owners

| Document | Purpose |
|---|---|
| [01 — Business overview](docs/01-business-project-overview.md) | Buyer, value and business boundaries |
| [02 — Product and strategy](docs/02-product-offering-competitive-strategy.md) | Portfolio, packages and competitive hypothesis |
| [03 — Operating model](docs/03-operating-model.md) | Responsibilities and domain invariants |
| [04 — Workflow](docs/04-workflow-interaction-specification.md) | Complete Trade interactions and exceptions |
| [05 — Contracts](docs/05-domain-data-contracts.md), [reference](reference/README.md) | Versioned schemas, fixtures, validators and migration limits |
| [07 — Future development](docs/07-future-development-and-business-deliverables.md) | Other families, deferred depth and excluded models |
| [12 — Scope decisions](docs/12-scope-decisions-and-reconciliation.md) | Authority, decisions and cross-file reconciliation |
| [13 — Release and assurance](docs/13-pilot-release-and-assurance.md) | Conditions before real-data/live operation |
| [14 — Market proof](docs/14-market-validation-and-proof.md) | Discovery, economics, measurement and public claims |

Private Resolution, Consumer Credit and standalone Network commercialization remain future development. Trade includes the shared Network & Control capabilities it needs. GRE does not own debt, perform the provider's collection work or custody recovered funds. Its own platform, data, support and agreed continuity duties remain explicit.

GitHub documents at the reviewed commit govern development. Historical research and original contractZIP0.1 preserve provenance; they do not override the current single-family scope. Current source-readable reference contracts are planning/conformance artifacts, not a deployed application.

In the editor container, with local services running and attached:

```sh
uv sync --locked
pnpm install --frozen-lockfile
uv run --locked python -m scripts.check_environment
```

See the environment guide for safe host lifecycle/attachment commands and the reference README for contract checks. Use synthetic data and keep credentials/customer evidence out of Git.
