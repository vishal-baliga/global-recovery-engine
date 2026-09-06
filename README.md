# Global Recovery Engine

Recovery infrastructure helping creditors reconstruct unresolved obligations and coordinate a supported path to resolution.

**Current stage: initial environment baseline verified; backlog planning is next.**
The ARM64 development container, local PostgreSQL/Temporal/Azurite, and shared
Python/pnpm dependency environments passed their setup checks. Minimal fixtures
verify FastAPI, OpenAPI/client generation, TypeScript, a Next.js production build,
and read-only access to all three services. Customer features, domain logic,
application migrations, CI, and live integrations remain unimplemented.

Inside the development container, from the repository root with services running:

```sh
uv sync --locked
pnpm install --frozen-lockfile
uv run --locked python -m scripts.check_environment
```

See [the dependency baseline](docs/10-dependency-baseline.md) for resolved versions,
fresh-install verification, Mac service commands, and required later integrations.

## Start here

Read [Current decisions and setup checkpoint](docs/00-start-here.md) first. It explains which documents govern the current work and what remains to be verified on the developer's Mac.

| Reference | Purpose |
| --- | --- |
| [Pilot MVP brief](docs/06-pilot-mvp-brief.md) | Required outcomes for both pilot journeys |
| [Future development and business deliverables](docs/07-future-development-and-business-deliverables.md) | Deferred scope, business work, and strategic boundaries |
| [Stack and environment decision](docs/08-stack-and-environment-decision.md) | Selected architecture direction and proposed runtime targets |
| [Development environment](docs/09-development-environment.md) | Container/local-service commands and verification records |
| [Dependency baseline](docs/10-dependency-baseline.md) | Shared locks, setup fixtures, combined check, and remaining integrations |
| [Codex instructions](AGENTS.md) | Repository context and working rules for coding agents |
| [Contract reference](reference/README.md) | Earlier schemas and synthetic validation package |

## Pilot scope

- **Domestic U.S. personal/friend loans:** assist an individual lender with evidence reconstruction, assessment, borrower response, resolution, repayment tracking, specialist assistance, and explicit closure.
- **India–U.S. commercial recovery:** assist Indian businesses with unpaid commercial obligations involving U.S. businesses, including authority, evidence, provider coordination, receipts, and cross-border costs.

GRE supplies infrastructure, intelligence, coordination, controls, and records. Identified eligible creditors/providers execute the applicable recovery work. Funds follow established creditor/bank/provider arrangements.

## Delivery sequence

Pilot brief → stack/environment setup → prioritized backlog → project and delivery document updates → application development.

The working architecture is a TypeScript/Next.js web application, Python/FastAPI domain application and workers, PostgreSQL, Temporal, and managed Azure hosting. Versions and integrations must be validated during setup.

Documents `01`–`05` retain the earlier design baseline. Their B2B-only scope and MVP-unselected status are superseded by the current decisions described in [Start here](docs/00-start-here.md); their applicable domain principles remain useful. Their substantive reconciliation follows backlog creation.
