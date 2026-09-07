# Current decisions and setup checkpoint

**Checkpoint date:** September 7, 2026

**Project:** Global Recovery Engine (working name)

**Owner/developer:** Vishal

**Repository:** `vishal-baliga/global-recovery-engine` — private

## Current direction

The user has proceeded from the two-track pilot brief to stack selection and incremental environment setup. Use the pilot brief and stack document as the working baselines for this stage. Their original proposal/version labels are preserved; component compatibility and service configuration remain to be verified during implementation.

The pilot includes domestic U.S. personal/friend loan assistance and India-origin B2B recovery against U.S. businesses. Domestic personal loans are an initial acquisition priority; both journeys remain pilot commitments. Cross-border personal loans and general remittance are future or separate scope, as recorded in the future register.

The agreed sequence is **brief → stack/environment → prioritized backlog → project/delivery document updates → development**. Preparing this repository is environment and context setup. The setup fixtures do not establish a product application. A proposed prioritized backlog is now recorded in document 11.

## How to read the documents

| Files | Current use |
| --- | --- |
| [06 — Pilot MVP brief](06-pilot-mvp-brief.md) | Required pilot outcomes, real-case readiness, and operating/business dependencies |
| [07 — Future register](07-future-development-and-business-deliverables.md) | Preserved future deliverables and scope-change rules |
| [08 — Stack and environment](08-stack-and-environment-decision.md) | Working architecture and proposed runtime targets |
| [09 — Development environment](09-development-environment.md) | Container/local-service configuration and actual Mac verification records |
| [10 — Dependency baseline](10-dependency-baseline.md) | Shared manifests/locks, combined setup check, resolved versions, and retained integration requirements |
| [11 — Prioritized pilot backlog](11-prioritized-pilot-backlog.md) | Proposed order, 10 epics/48 items, dependencies, acceptance evidence, manual routes, and retained requirements |
| [01 — Business overview](01-business-project-overview.md), [02 — Product strategy](02-product-offering-competitive-strategy.md) | Earlier business/product baseline; B2B-only and MVP-unselected passages await reconciliation |
| [03 — Operating model](03-operating-model.md), [04 — Workflow](04-workflow-interaction-specification.md), [05 — Domain contracts](05-domain-data-contracts.md) | Domain/reference detail to apply and extend for selected pilot stories |
| [Contract package](../reference/README.md) | Preserved offline schemas, synthetic example, and validator |

This checkpoint resolves historical scope/status conflicts during setup. The two-track pilot and chosen architecture take precedence over older scope/status passages. Preserve applicable evidence, authority, financial, privacy, and outcome principles. Reconcile the original documents substantively at the agreed documentation stage; this import only converts their companion links into repository-relative links.

## Environment status

The initial findings come from the read-only local Codex inspection pasted by Vishal after cloning. That inspection made no file changes or installations. Later user-reported installation results are recorded below. Each observation describes the Mac at the time of its report; repository updates are tracked in Git.

| Item | Evidence/status |
| --- | --- |
| Development machine | MacBook Air M4 (2025), native `arm64`, 16 GiB RAM, macOS 26.6.2 |
| VS Code and Codex | VS Code 1.136.1; Vishal supplied the local Codex report confirming execution inside the GRE container, with the Docker marker and VS Code container server present. |
| ChatGPT GitHub connection | Account and private repository access verified |
| Repository baseline | Project references and Codex guidance committed in `e6dcf64`; later setup findings are incremental documentation updates |
| Clone on the Mac | Fetched origin successfully; clean working tree safely switched to `setup/devcontainer`, tracking `origin/setup/devcontainer` at `445db9a` before local setup fixes. Correct remote `vishal-baliga/global-recovery-engine`. |
| Git | Host Git 2.50.1; authenticated fetch succeeded on the Mac. Azurite setup commit `5bd4c1b` is present on GitHub branch `setup/devcontainer`; the dependency baseline began from this clean, up-to-date baseline. PR #1 remains a draft. |
| Apple Command Line Tools | Installed and selected; package version 26.6.0.0.1781586589 |
| Homebrew | Installed and verified by user-provided terminal output: 6.0.22, prefix `/opt/homebrew`, `brew doctor` reports “Your system is ready to brew.” |
| Docker | User output verifies Desktop 4.89.0 (238018), client/engine 29.7.2, client `darwin/arm64`, server `linux/arm64`, context `desktop-linux`; Compose 5.5.0. ARM64 `hello-world` image download and container execution succeeded; user supplied the complete “Hello from Docker!” output. |
| Dev Containers | Microsoft `ms-vscode-remote.remote-containers` 0.466.0 confirmed installed through the VS Code CLI. GRE image build, offline ARM64 check, and actual editor/Codex container session passed. |
| Node/pnpm | Absent from the host PATH at the initial inspection. Container Node 24.20.0 and pnpm 11.10.0 built and verified on ARM64. |
| Python/uv | Apple Python 3.9.6 remains on the host. Container Python 3.14.7 and uv 0.12.10 built and verified on ARM64. |
| Other CLIs | GitHub, PostgreSQL, Temporal, Azure, Terraform, and Dev Container CLIs not found on PATH; install only when their setup stage requires them |
| Local PostgreSQL | PostgreSQL 18.6 Bookworm verified on native ARM64. Mac host startup/health and editor-container TCP connectivity passed. A committed synthetic row survived a normal PostgreSQL restart; probe cleanup passed. Private internal network and persistent named volume configured; lifecycle commands and resolved digest recorded in the environment guide. |
| Local Temporal | Official CLI development-server image 1.8.3 pinned by digest; embedded Server 1.31.2 / UI 2.50.1 verified native ARM64 and non-root. Persistent SQLite volume, private SDK network, localhost-only UI (HTTP 200), and locked Python 3.14 SDK 1.32.0 probe passed. The same workflow/run completed after normal server and worker restarts. |
| Local Azurite | Blob-only Azurite 3.36.0 verified native ARM64, pinned by digest, with internal network/no host ports and persistent named storage. Locked SDK 12.30.1 ran on Python 3.14.7/API 2025-11-05. Authenticated bytes/metadata, anonymous HTTP 403, same-blob restart persistence, and scoped cleanup all passed. |
| Provider fakes | Not yet established |
| Cloud and service accounts | Azure, Temporal Cloud, Clerk, runtime AI, and integration provisioning not verified; architecture selection alone does not provision them |
| Dependency baseline/setup fixtures | Shared Python and pnpm manifests/locks verified with fresh locked installs. FastAPI/Pydantic, generated TypeScript client, strict TypeScript checks, and Next 16 production fixture build passed; read-only checks reached all three services from the shared Python environment. See document 10. |
| Product/CI | No customer/domain implementation, application migrations, CI pipeline, or executable product acceptance suite yet. Later integration requirements remain tracked in document 10. |

Treat PATH checks as observations of the inspected environment, not proof that a tool cannot exist elsewhere. Update this table with actual results as setup progresses. Use a project-managed Python later; leave the Apple-provided Python in place.

## Completed editor and agent verification

On September 6, 2026, Vishal supplied a local Codex report confirming the actual VS Code container session:

- Workspace: `/workspaces/global-recovery-engine`.
- Operating system: Debian GNU/Linux 12 (bookworm), Linux `7.0.12-linuxkit`.
- Architecture: `aarch64` / ARM64.
- User: `vscode`, UID/GID `1000`, non-root.
- Docker marker and VS Code container server present.
- `python .devcontainer/check_environment.py --expect-arch arm64` exited 0 with `GRE development toolchain: PASS (linux/arm64)`.
- All pinned versions, Python virtual environment/SSL/SQLite, pnpm execution, and workspace write checks passed.

The next session inspected a clean working tree on `setup/devcontainer`, fetched origin, and safely fast-forwarded `c937128` to `2c80392` before PostgreSQL setup edits. No local changes needed stashing or removal. The earlier pnpm stdout/preflight fix and build-resolved image digests are recorded in [the development-environment guide](09-development-environment.md).

This completes the language-toolchain and editor/agent setup. Subsequent PostgreSQL, Temporal, Azurite, and initial shared dependency verification are recorded below; application integrations and product behavior remain pending.

## Completed PostgreSQL increment

On September 6, 2026, Vishal ran the Mac host helper to start `postgres:18.6-bookworm`
on `linux/arm64` and attach this development container. The agent connected using
the locked Psycopg 3.3.5 probe from Python 3.14 ARM64, checked the server version,
architecture, and persistent data path, and committed one synthetic record.
After Vishal's normal database restart, the agent verified the same record and a
changed server start time, then cleaned up the probe. All steps passed.

The database uses named volume `gre-postgres18-data`, internal network
`gre-database`, verified empty host port bindings (`{}`), and a generated Git-ignored
development password. See [the environment guide](09-development-environment.md#local-postgresql-18)
for exact Mac start/stop/restart/attach commands, the observed image digest, and
verification details. Recreated editor containers need host network attachment.
Docker orchestration remains on the Mac; no CLI/socket was added to the editor.

## Completed Temporal increment

On September 6, 2026, Vishal started the official Temporal CLI development server
from the Mac. CLI 1.8.3 (Server 1.31.2, UI 2.50.1) ran natively on ARM64 as UID
1000. The image is pinned by version and resolved digest in Compose. SQLite state
persists in named volume `gre-temporal-dev-data`. The SDK network is internal;
the dedicated UI bridge enables only a `127.0.0.1:8233` host binding, verified
with HTTP 200. gRPC remains unpublished.

The locked SDK 1.32.0 probe ran on Python 3.14.7 in the editor container. It
started a synthetic workflow, queried it as waiting for a signal, and shut down
its worker. After a normal Mac-hosted server restart, a new worker queried,
signaled, and completed the **same workflow/run ID**. History contained exactly
one start, signal, and completion (nine events). Both worker processes exited
cleanly. The completed synthetic history and ignored receipt remain available.
See [the environment guide](09-development-environment.md#local-temporal-development-server)
for exact host lifecycle/attachment and probe commands, the image digest,
workflow/run IDs, timestamps, and observed results.

This establishes normal development-server and worker restart recovery, not
backup/restore, upgrade safety, production availability/authentication, or
application workflow behavior. Recreated editor containers require host network
attachment. The UI bridge allows server egress. Docker orchestration remains on
the Mac, with no Docker CLI/socket added to the editor.

## Completed Azurite Blob increment

On September 6, 2026, Vishal ran Microsoft's official Azurite 3.36.0 image from
the Mac, pinned by version and resolved digest. Native ARM64 execution, named
volume `gre-azurite-blob-data`, internal network `gre-azurite`, and empty host port
bindings were verified. Only Blob service runs. The official image uses root;
the editor remains non-root. Emulator-only credentials are generated locally and
ignored by Git.

The locked Azure Blob SDK 12.30.1 probe ran in Python 3.14.7 with explicit API
2025-11-05. It uploaded/downloaded a private synthetic blob with exact bytes and
metadata and confirmed an unauthenticated GET returned HTTP 403. Following a
normal Mac service restart, the same blob, metadata, ETag, and modified time
survived; anonymous access was still rejected. Cleanup removed only the
ownership-checked probe container and local payload/receipt, confirmed container
removal, and found other container names/metadata unchanged. The emulator remains
running. See [the environment guide](09-development-environment.md#local-azurite-blob-storage)
for the digest, resource ID/hash, actual timestamps, and exact Mac lifecycle and
editor attachment commands.

This verifies local Blob behavior and normal-restart persistence, not Azure
RBAC/managed identity/TLS, backup recovery, upgrades, production durability, or
application storage adapters. Recreated editor containers require host attachment.
The emulator's default root user remains a development-service limitation.

## Completed initial dependency baseline

On September 6, 2026, the shared root Python environment resolved FastAPI,
Pydantic, SQLAlchemy/Psycopg/Alembic, Temporal, and Azure Blob together. The pnpm
workspace resolved Next.js 16.3.4, React 19.2.8, TypeScript 6.0.3, and Hey API
0.99.0. TypeScript 7.0.2 initially resolved but failed Hey API compiler-API use;
6.0.3 passed generation, checking, and building. Full pins and remaining
requirements are in [the dependency baseline](10-dependency-baseline.md).

Both `uv sync --locked` and `pnpm install --frozen-lockfile` passed in fresh
empty environments with unchanged manifests/locks. The combined check passed
FastAPI request/response and validation, OpenAPI export, generated-client live
HTTP requests, strict TypeScript checking, and a Next.js production fixture build.
SQLAlchemy accessed PostgreSQL in a read-only transaction; Alembic read no current
migration heads without creating a version table. Temporal and authenticated
Azurite checks passed concurrently. The retained Temporal workflow/run was still
completed, and all existing service verification receipts were unchanged.

Run from the editor repository root after locked installation:

```sh
uv run --locked python -m scripts.check_environment
```

All fixtures are setup-only. The earlier individual service probes, data volumes,
credentials, and completed restart records are preserved. Docker orchestration
remains on the Mac; no host commands or service restarts were needed this increment.

## Backlog planning checkpoint — September 7, 2026

GitHub confirms the completed initial setup baseline at `5511b1ef3096b7791a3c8be62a916c469c9f3a73` on `setup/devcontainer`. The custom setup code, dependency manifests, and documented TypeScript fallback were reviewed without finding a blocker to backlog planning. Runtime evidence remains the local Mac/Codex reports above; no new hosted runtime check is represented as a Mac verification.

[Document 11](11-prioritized-pilot-backlog.md) proposes 48 delivery items across 10 epics and eight stages: documentation/business decisions; shared foundations; domestic assessment; borrower resolution/payment; complete domestic outcomes; India–U.S. commercial completion; assisted processing/live readiness; and pilot evaluation. Both tracks remain required. The draft maps all pilot capabilities and document 10’s remaining integration/quality/operations requirements, including the combined check’s dependence on retained Temporal history, to delivery items. No pilot deliverable was deferred and document 07’s candidates/boundaries are unchanged.

The backlog is on a separate documentation branch based on the verified setup commit. Setup PR #1 remains a draft; neither branch is merged by this planning work. The source environment, service data and local Mac working tree were not changed.

## Next action

Review the proposed backlog order and acceptance coverage, then complete GRE-001: reconcile documents 01–05 and prepare the initial architecture, journey/acceptance, operating-decision and first-story delivery records. Detailed contracts extend with their dependent stories; the reference ZIP is not an application scaffold.

GRE-002–GRE-005 business decisions can proceed alongside documentation. Product coding begins with GRE-006 after the documentation step. Inspect local Git status, preserve changes, and synchronize the appropriate reviewed branch before editing. Do not rerun completed service-restart probes merely to begin planning; use the documented combined check when a concrete environment change needs verification.
