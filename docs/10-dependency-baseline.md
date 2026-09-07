# Initial application dependency baseline

**Verified:** September 6, 2026, in the GRE ARM64 development container.

**Scope:** shared dependency resolution and setup fixtures; no customer-facing
features, domain implementation, application migrations, or cloud provisioning.

## Manifests and fixture layout

- `pyproject.toml` / `uv.lock`: one shared Python environment for FastAPI,
  Pydantic, SQLAlchemy, Psycopg, Alembic, Temporal, and Azure Blob. Uvicorn is
  included to exercise a real HTTP server; HTTPX is in the default development
  dependency group. `.python-version` matches container Python 3.14.7.
  `tool.uv.package=false` avoids inventing application package boundaries during
  setup. The older isolated service probes/locks and their records are preserved.
- `package.json` / `pnpm-workspace.yaml` / `pnpm-lock.yaml`: one pnpm workspace
  with shared compiler/codegen tools, `fixtures/web`, and `packages/api-client`.
  Every direct external version is exact, peer checking is strict, and only
  esbuild/sharp dependency builds are allowed. pnpm remains 11.10.0 on Node 24.
- `fixtures/api/app.py`: a synthetic POST `/setup/echo` with Pydantic request and
  response models. `fixtures/api/openapi.json` is its generated contract.
- `openapi-ts.config.ts` / `packages/api-client/src`: Hey API's generated types,
  Fetch client, and SDK. Generated artifacts are committed and regenerated from
  the local schema; no hosted Hey API registry is needed. Do not edit them manually.
- `fixtures/web`: minimal Next.js App Router build fixture consuming a generated
  response type. It has no external fonts/assets, authentication, database calls,
  or customer journey. `next-env.d.ts` and `.next/` are generated/ignored;
  `next typegen` prepares types before `tsc` on a fresh checkout.
- `scripts/`: setup verification commands, including a live generated-client
  request and read-only shared-service probes. They do not establish the product's
  future module structure or executable acceptance suite.

## Install and check

Inside the **development container**, from `/workspaces/global-recovery-engine`:

```sh
uv sync --locked
pnpm install --frozen-lockfile
uv run --locked python -m scripts.check_environment
```

The last command is the **combined environment check**. It concurrently checks
all three services from the shared Python environment, checks FastAPI/Pydantic
request/response behavior, exports OpenAPI, regenerates the TypeScript client,
type-checks both workspace packages, calls a temporary loopback Uvicorn server
with the generated client, and runs `next build`. Next telemetry is disabled for
this command. A failure returns nonzero; there is no service-skip mode.

Expected final line: `GRE combined dependency/environment check: PASS`.
The temporary API process uses an ephemeral port inside the editor container and
is terminated on success or failure; no Mac port is published.

Focused commands, also in the **development container**:

```sh
uv run --locked python -m scripts.check_services
uv run --locked python -m scripts.export_openapi
pnpm generate:client
pnpm typecheck
pnpm build
uv run --locked python -m scripts.check_fresh_installs
```

The fresh-install check creates an empty temporary workspace, copies only the
manifests/lockfiles, runs exactly `uv sync --locked` and
`pnpm install --frozen-lockfile`, and checks that manifests/locks remain unchanged.
It reuses package download caches but starts with no virtual environment or
`node_modules`. It removes only its own temporary directory. The working
installation, service volumes, credentials, and verification records are untouched.

The three existing services must be running and this editor must be attached.
If they need starting/attachment, run in **Mac Terminal**, replacing
`GRE_CONTAINER_ID` with the current editor container ID:

```sh
cd "/Users/diztort/GRE Development/global-recovery-engine"
docker ps --format 'table {{.ID}}\t{{.Names}}\t{{.Image}}'
bash .devcontainer/postgres-host.sh up GRE_CONTAINER_ID
bash .devcontainer/temporal-host.sh up GRE_CONTAINER_ID
bash .devcontainer/azurite-host.sh up GRE_CONTAINER_ID
```

See [the environment guide](09-development-environment.md) for individual
stop/restart commands and retained persistence-verification records. The baseline
check itself neither starts nor restarts Docker services.

## Resolved versions

Full transitive versions, platform wheels, and hashes are in the lockfiles.
These are observed pins, not claims of compatibility with every future plugin.

| Python component | Resolved version |
| --- | --- |
| Python / uv | 3.14.7 / 0.12.10 |
| FastAPI / Pydantic | 0.141.1 / 2.13.5 |
| Starlette / pydantic-core | 1.6.0 / 2.46.5 |
| SQLAlchemy / Psycopg binary | 2.0.52 / 3.3.5 |
| Alembic | 1.19.2 |
| Temporal SDK | 1.32.0 |
| Azure Blob SDK / azure-core | 12.30.1 / 1.41.0 |
| Uvicorn / HTTPX | 0.52.4 / 0.28.1 |

| Node/workspace component | Resolved version |
| --- | --- |
| Node / pnpm | 24.20.0 / 11.10.0 |
| Next.js | 16.3.4 |
| React / React DOM | 19.2.8 / 19.2.8 |
| TypeScript | 6.0.3 |
| Hey API OpenAPI generator | 0.99.0 |
| tsx (setup client runner) | 4.23.13 |
| Node / React / React DOM types | 24.13.3 / 19.2.18 / 19.2.7 |

## Compatibility decisions and observed results

The baseline began from clean `setup/devcontainer` at `5bd4c1b`. Fetch confirmed
origin was up to date. There was no root `.venv`, `node_modules`, or application
manifest. Initial and final fresh installs passed; the final isolated check
installed 36 Python distributions and 82 pnpm packages on Linux ARM64 with no
manifest/lock changes. Package caches were reused in the final fresh check.

- **TypeScript fallback:** 7.0.2 resolved within Hey API 0.99.0's declared peer
  range but generation crashed accessing `ts.SyntaxKind.AnyKeyword`. Pinning
  **6.0.3** restored generation, strict type checking, and the Next production
  build. Do not upgrade TypeScript alone without rerunning this complete path.
  Explicit Node types are configured for the compiler. Hey API recommends exact
  version pins during its initial development. [Hey API setup](https://heyapi.dev/docs/openapi/typescript/get-started)
- **Python request fixture:** Starlette's TestClient emitted a deprecation warning
  for HTTPX. The fixture uses HTTPX's ASGI transport directly and additionally
  exercises real Uvicorn HTTP through the generated TypeScript client. No extra
  HTTP client family was added just to satisfy the TestClient warning.
- **API version:** Azure Blob uses explicit Azurite-compatible `2025-11-05`, with
  API validation enabled. Its newer SDK default is not assumed emulator-compatible.
- **Workspace build:** an explicit Turbopack root covers both the fixture and
  generated workspace package. `next typegen` runs before standalone type checking.
  Next 16's build is separate from linting; no linter pass is claimed.
  [Next TypeScript configuration](https://nextjs.org/docs/app/api-reference/config/typescript)
- **Combined check passed:** valid FastAPI response and invalid-request HTTP 422;
  OpenAPI export and local client generation; strict `tsc` for both packages;
  real generated-client HTTP 200 response and typed HTTP 422 error; Next 16.3.4
  Turbopack production build with static `/` and `/_not-found` routes. The build
  used the pinned Node runtime and generated client type, with no service writes.
- **Shared service checks passed concurrently:** SQLAlchemy/Psycopg connected to
  PostgreSQL 18.6 in an explicitly read-only transaction; Alembic read no current
  migration heads without creating its version table. Temporal health passed and
  the previously recorded workflow/run remained completed. Authenticated Azurite
  properties/listing passed (zero containers after the previous scoped cleanup).
  Service-start and Temporal workflow receipts were byte-for-byte unchanged.

The production build is a fixture compilation result, not a deployed or
production-ready GRE application. No service restart test was repeated in this
increment, and the earlier completed verification records remain authoritative
for those observed restarts.

## Required later work

These are retained integration/validation areas from the selected stack. The current
Foundation + Trade Pilot and future-family dispositions are authoritative in
[06](06-pilot-brief.md), [07](07-future-development-and-business-deliverables.md)
and [11](11-prioritized-pilot-backlog.md). Vishal owns their scoped implementation
and any permitted manual/provider route. Installation alone completes no product requirement.

| Required integration/work | Remaining validation before the dependent capability |
| --- | --- |
| Domain/API and database | Application package boundaries, real schemas/migrations and upgrade tests, exact money/currency handling, transaction behavior, application roles/RLS, and tenant/case authorization. Alembic was read-only here. |
| Temporal workers | Domain checks shared with the API, workflow/activity implementation, retries/idempotency, replay/versioning, changed authority before effects, callbacks/reconciliation, and deployment/shutdown behavior. |
| Blob and document processing | Application storage adapter, permissions/retention, real Azure identity/TLS/networking, upload limits/formats, backup/restore; add and validate the selected Document Intelligence SDK when implementing extraction. |
| Authentication | Clerk SDK selection/locks and web/API integration; verify sessions/organizations separately from case access, provider disclosure, and action mandates. No Clerk package or account integration is established here. |
| Runtime AI | OpenAI SDK/Responses/Pydantic compatibility, model/data settings, refusal handling, evaluations, source attribution, and provider adapter; not installed or runtime-tested by this baseline. |
| Web runtime/client | Application routes/components, actual base URL/auth configuration, errors/cache behavior, accessibility, and browser/end-to-end checks. Add Tailwind/shadcn and TanStack Query when their planned use is defined. |
| Provider exchange, payments, external acceptance | Provider fakes and sandbox/assisted adapters, exact actor/service admission, direct appointment/acceptance, callbacks/deduplication and reconciliation. GRE obligor contact, bilateral resolution and plan-operation interfaces are outside this Pilot; future depth and families remain in 07. |
| Quality and delivery | Appropriate Ruff/type-check/pytest/Hypothesis and web test/lint tooling, CI, generated-contract drift checks, security/dependency-update checks, realistic failure fixtures, and product acceptance checks. Current scripts are setup checks only. |
| Cloud and operations | Costed/authorized Azure and Temporal Cloud provisioning, managed PostgreSQL/Blob, Clerk/provider accounts, deployment images, Terraform/CI delivery, secrets, OpenTelemetry, backup/restore, and incident handling. |

See [the Pilot brief](06-pilot-brief.md), [architecture](08-stack-and-environment-decision.md),
and [future register](07-future-development-and-business-deliverables.md) for
current outcomes and scope boundaries. Documents and reference contracts are now
reconciled; implementation follows [11](11-prioritized-pilot-backlog.md).
This historical dependency verification implements no customer-facing feature.
