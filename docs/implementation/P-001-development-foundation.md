# P-001 — Development foundation implementation plan

**Date:** September 8, 2026. **Revision:** 1.1 — sprint readiness review. **Owner:** Vishal. **Status:** Planned; implementation has not started.

**Parent:** [P-001 in the Pilot backlog](../11-prioritized-pilot-backlog.md). **Evidence:** [Verification record](P-001-verification-record.md).

**Inspected source:** Initial design used `72a4c1dabd795e97f74f00cca329da6e98edc40a`; this review checked published `main` at `5f027b20ce33d996cbbb8672804680ae0f44aa62`, its actual runtime files and issues #4–#11. This plan was prepared here with Vishal and published before Mac checkout/environment confirmation. It describes files and commands to implement; it does not claim they already exist.

## 1. Outcome and execution boundary

P-001 turns the verified dependency fixtures into a maintainable development foundation for the Foundation + Trade Pilot. At completion, the real web and Python packages have clear ownership, deterministic API/client generation, focused automated checks, repeatable service health and a working CI gate. A fresh ARM64 environment can install and run them from the committed locks without modifying existing developer data.

This implements package/quality infrastructure, a minimal process-liveness API, a development web shell and worker configuration scaffolding. Claim handling, authentication, tenant database roles/migrations, recovery workflows, outbox/provider effects, customer uploads, runtime AI and cloud deployment remain in their owning later backlog items. A green P-001 gate proves this foundation, not the released Pilot.

Vishal defines the plan and task scope here. Local Codex implements the selected task after the local readiness checkpoint and a subsequent instruction to begin. It may make routine implementation choices within the decisions below, explain findings and propose corrections. It must not replace this plan, generate a competing backlog or expand scope. A material discovery updates this canonical plan and the affected issue before dependent work proceeds; unrelated authorized work need not stop.

## 2. Source inventory and concrete changes

| Existing source | Finding | Planned treatment |
|---|---|---|
| `pyproject.toml`, `uv.lock` | Shared dependencies; `tool.uv.package=false`; no installable product | Convert the root Python project into one installable distribution with `src/gre`; retain resolved runtime versions and add only needed build/check dependencies |
| `fixtures/api/app.py`, `fixtures/api/openapi.json` | Synthetic `/setup/echo`, valid response and invalid-request checks | Preserve as setup regression evidence; never expose it from the product API |
| `packages/api-client`, `openapi-ts.config.ts` | The apparent API client currently represents only the setup fixture | Reserve `@gre/api-client` for product OpenAPI; relocate fixture generation to a clearly named setup client |
| `fixtures/web`, pnpm workspace | Verified Next build fixture only | Preserve it; add `apps/web` for the actual application shell on the same dependency versions |
| `scripts/check_services.py` | Read-only Postgres/Azurite checks; Temporal health also describes an old recorded workflow | Separate live health from historical workflow-receipt inspection; keep failure and uncertainty explicit |
| `scripts/check_environment.py` | Setup checks regenerate tracked schema/client files | Retain its setup purpose, but make check-mode verification compare temporary generation without rewriting tracked files |
| `scripts/check_fresh_installs.py` | Copies only manifests/locks into a temporary directory | Update for an installable package and new workspace members; add wheel installation outside the source checkout |
| `.devcontainer/Dockerfile`, Compose files and host helpers | Verified ARM64 tools/services; some version-only image references; persistent developer resources | Preserve architecture, versions and volumes; verify immutable image references and idempotent current-container attachment |
| `.devcontainer/devcontainer.json` | VS Code points to system Python; only toolchain check runs after creation | Select the project `.venv` interpreter when installed; keep service startup/attachment a host operation |
| `reference/` | Immutable legacy ZIP plus readable v0.2 contract suite | Run both in separate processes/import contexts; no reference code imported into `src/gre` |
| `.github/workflows/` | No CI exists | Add one stable ARM64 check gate using disposable resources and the shared command implementations |

## 3. Selected implementation design

### 3.1 Python ownership and packaging

Use **one Python distribution**, `gre-platform`, with import root `gre`, and one existing `uv.lock`. It has the following initial layout; do not scaffold every future domain record or service.

| Target path | Responsibility |
|---|---|
| `src/gre/__init__.py` | Package identity without startup side effects |
| `src/gre/config.py` | Typed, explicitly loaded configuration; no secret-bearing representations |
| `src/gre/domain/__init__.py` | Future shared business rules; no FastAPI, SQLAlchemy, Temporal, Azure, subprocess or network imports |
| `src/gre/api/app.py` | FastAPI application factory and minimal liveness route; transport boundary |
| `src/gre/worker/__main__.py` | Worker configuration check/bootstrap boundary; no collection workflow or pretend live worker |
| `tests/unit/`, `tests/architecture/`, `tests/integration/` | Focused behavior, import-boundary and isolated integration checks |

Use `uv_build==0.12.10` as the declared build backend, with explicit module name `gre` and source root `src`. Verify that exact backend with the installed uv/Python before using it; an unavailable/incompatible backend requires a documented change, not a toolchain-wide upgrade. Keep `requires-python = ">=3.14,<3.15"`. Include only product source and intended package metadata in the wheel; exclude fixtures, references, credentials, local data and development artifacts.

Keep FastAPI 0.141.1, Pydantic 2.13.5, SQLAlchemy 2.0.52, Psycopg 3.3.5, Alembic 1.19.2, Temporal SDK 1.32.0, Azure Blob 12.30.1 and Uvicorn 0.52.4 unless an observed incompatibility requires a separately justified change. Package-name/build changes necessarily alter the root lock entry; preserve existing unrelated dependency resolutions and inspect any transitive churn.

Use Pydantic already installed for configuration validation. The P-001 worker configuration is deliberately small:

| Environment key | Local default | Validation |
|---|---|---|
| `GRE_TEMPORAL_ADDRESS` | `gre-temporal:7233` | Host and port; reject an empty value, embedded credentials, URL scheme or invalid port |
| `GRE_TEMPORAL_NAMESPACE` | `default` | Nonempty identifier |
| `GRE_TEMPORAL_TASK_QUEUE` | `gre-development` | Nonempty identifier; a valid value does not mean a worker is polling |

An explicitly supplied environment mapping overrides defaults; the startup caller may pass the process environment. Empty/malformed supplied values fail rather than use defaults. The validator accepts an injected mapping for tests. No automatic `.env` discovery or product file loader is introduced in P-001; explicit files used by service probes follow section 3.3. Importing modules and constructing/exporting the liveness API must not load application configuration/secret files, read process configuration or contact services. Reading Python source during import is naturally permitted. Keep config loading at the worker entry point; do not add a second settings framework.

Validation failures identify a field/reason without echoing supplied values, including exception chains and structured errors. Prove this with an invalid synthetic secret value captured from stdout/stderr; a masked field representation alone is insufficient. Domain import tests cover relative imports and GRE API/worker/configuration dependencies as well as the listed third-party/I/O modules.

The API exposes `GET /health/live` with stable operation ID `get_liveness` and typed JSON `{"status":"ok"}`. It reports process liveness only. It reveals no credentials, dependency details or machine inventory and does not claim database/provider readiness. Default development binding is loopback; no authentication-free claim endpoints are introduced. The worker supports `--check-config`, rejects invalid configuration, redacts secrets and performs no external work. Actual worker polling/workflow registration belongs to the dependent workflow work; starting an empty registry must not look like a functioning worker.

### 3.2 Web and two deliberately separate API contracts

Use `apps/web` / `@gre/web` for the Next.js application, retaining Next 16.3.4, React 19.2.8, TypeScript 6.0.3, pnpm 11.10.0 and Hey API 0.99.0. Keep `fixtures/web` / `@gre/web-fixture` as a small setup regression. Add `apps/*` to the existing pnpm workspace; preserve exact direct dependencies, strict peers and the existing dependency-build allowlist.

| Surface | Product | Setup regression |
|---|---|---|
| Python application | `gre.api.app:create_app` | Existing `fixtures.api.app:app` |
| Canonical generated schema | `contracts/openapi.json` | Existing `fixtures/api/openapi.json` |
| Generator configuration | `openapi-ts.config.ts` | New `openapi-ts.setup.config.ts` |
| Generated client | Existing `packages/api-client`, `@gre/api-client` | New `packages/setup-api-client`, `@gre/setup-api-client` |
| Consumer | `apps/web` and product client probe | `fixtures/web` and existing setup client probe |

Move/regenerate the current fixture client into the setup package and update its imports atomically. The two outputs describe different APIs; neither is an independently maintained schema or a source of business truth. Shared generator settings may be factored once if useful. Do not hand-edit generated code, copy `/setup/echo` into the product, or make product code import fixtures/references.

Make `scripts.export_openapi` take an explicit `--target product|setup`, export sorted deterministic JSON and support `--check`. Keep all call sites explicit. `scripts.check_codegen` exports and generates both contracts into owned temporary directories, compares file sets and bytes with tracked artifacts, and fails on additions, removals or differences. It must not repair drift while reporting success. Use the generator's supported configuration/CLI interface, verified against the pinned version. New product schemas must not depend on running databases or environment-specific URLs/timestamps.

The initial web page is a clearly labeled development shell with a stable page title and basic accessible layout. It collects no customer information and advertises no recovery capability. Its build may consume a generated product type, while a separate live TypeScript probe checks the actual liveness response. Retain the setup probe's HTTP 200 and 422 coverage. No Clerk, Tailwind/shadcn, TanStack Query, analytics or model account is needed for this shell; introduce them in the item that uses them.

### 3.3 Repeatable health versus historical persistence evidence

`scripts.check_services` remains read-only for developer data. Keep authenticated Postgres/Azurite checks and bounded client calls. Add `--config PATH` for a strict JSON object with exactly three service sections:

| Section | Required fields |
|---|---|
| `postgres` | `host`, `port`, `database`, `user`, `password_file` |
| `azurite` | `endpoint`, `account_name`, `account_key_file` |
| `temporal` | `address`, `namespace` |

Without the option, retain current local DNS/account/password-file defaults. With the option, require all fields, reject unknown/empty/malformed values, resolve relative secret paths against the config file, and fail on missing/unreadable files. Do not partly fall back to local defaults. CI supplies a job-owned config and secret files mounted read-only; no secret values are stored in the JSON or command arguments. Validate the configured database/account/namespace, retaining the expected server/API versions. The aggregate accepts and forwards the same `--config PATH`. Logs/errors never print keys, passwords, full credentialed URLs or secret-file contents; verify failures using synthetic secret values.

The service-check phase, whether invoked standalone or by the aggregate, must exit within a configured wall-clock deadline plus a bounded cleanup allowance; the aggregate separately bounds its other phases. Use an owned process supervisor or an equivalent demonstrated hard boundary. Cancelling `asyncio.wait_for` around `to_thread` does not terminate the underlying work; do not call that a command deadline. Cover a deliberately stuck check, kill/reap only owned subprocesses, and check receipt preservation in failure/timeout paths too. The existing aggregate must invoke the same bounded boundary in .01.

Normal Temporal health checks current gRPC service/namespace accessibility. They do **not** require a historical completed workflow to remain queryable. Add an explicit `--inspect-historical-temporal` diagnostic mode for the retained receipt:

- No receipt: report that no historical comparison was performed; current health can pass.
- Valid receipt and matching completed run: report a separately verified historical match.
- Valid receipt but exact workflow/run returns `NOT_FOUND`: report historical evidence unavailable, potentially retention/deletion; do not assert retention as the proven cause or mark persistence verified. Current health can still pass if independently healthy.
- Malformed receipt, different status/run, denied access, timeout or another RPC error during an explicitly requested inspection: fail the requested diagnostic with a redacted reason. Do not swallow all failures as retention.
- Current service/namespace failure: always fail the normal health gate regardless of any historical receipt.

Hash existing verification receipts before/after checks; neither mode may overwrite, delete or recreate them. The old seed/restart/resume probe stays a separate deliberate persistence test. P-001 does not repeat destructive or live-volume restart/restore exercises.

### 3.4 Quality tools and required commands

Add exact compatible check-tool versions when the relevant task is implemented and record their resolutions in document 10. Current runtime pins are not to be raised simply to satisfy a linter. Selected tools: Ruff for Python lint/format, Pyright for Python types, pytest for focused tests, ESLint with the pinned Next config for web/TypeScript, and Playwright for one Chromium shell smoke. Use the existing `tsx` and Node assertions for live generated-client checks. Hypothesis and Vitest remain available when actual domain properties or isolated UI logic warrant them; empty suites or trivial tests do not add evidence. The .04 pytest scope explicitly includes .01 health/timeout tests, configuration, packaging/import boundaries and check-runner/codegen behavior. Keep reference test discovery in its separate processes. A declared required suite that collects no tests fails.

Use explicit lint/type scopes for handwritten source/check scripts and actual consumers. Exclude generated clients from style rewriting, but type-check them. Preserve archived reference code without mass reformatting. Start strict checking on new product code; use narrow documented exceptions where a third-party type boundary needs them, never blanket disabling to turn CI green. Next 16 uses the ESLint CLI; `next build` is a separate check.

Provision the pinned Playwright Chromium binary and compatible Debian ARM64 system libraries in .04, before its browser acceptance. Add the required image libraries through the Dockerfile and document the host rebuild/reconnect step; install the browser into a writable user cache using the locked Playwright tool. CI reuses this path in .06. Keep the check process non-root. Smoke-test the already-built product shell with the intended title, heading/landmark and no uncaught page error; do not rebuild it for the smoke. Do not reuse an unrelated server on an occupied port. Use a bounded owned server and cleanup. Run the two Next builds and the single Chromium worker sequentially; record resource/time failures before changing versions or weakening checks.

These are **target commands to implement**, not current execution claims:

| Command from repository root | Required behavior |
|---|---|
| `uv sync --locked` and `pnpm install --frozen-lockfile` | Install the selected development workspace without changing manifests/locks |
| `uv run --locked python -m scripts.check_services` | Bounded, read-only current connectivity, independent of historical workflow retention |
| `uv run --locked python -m scripts.check_environment` | Preserve setup API/client/type/build coverage; no tracked-file regeneration in check mode |
| `uv run --locked python -m scripts.check_codegen` | Read-only product + setup schema/client drift check |
| `uv run --locked python -m scripts.check_product` | Ruff lint/format check, Pyright, relevant pytest, ESLint, workspace TypeScript, product client HTTP probe, Next build and Chromium shell smoke; named failures return nonzero |
| `uv run --locked --group reference python -m scripts.check_reference` | Both reference validators/suites in separate processes and temporary legacy extraction; original ZIP unchanged |
| `uv run --locked python -m scripts.check_fresh_installs` | Empty working installs plus built-wheel import from outside the repo; no mutation of the normal environment or locks |
| `uv run --locked uvicorn gre.api.app:create_app --factory --host 127.0.0.1 --port 8000` | Local product liveness API; occupied port fails without killing another process |
| `pnpm --filter @gre/web dev --hostname 127.0.0.1` | Local development shell |
| `uv run --locked python -m gre.worker --check-config` | Validate worker configuration without registering a business workflow |

The `reference` dependency group uses the existing reference direct pins (`jsonschema[format]==4.26.0`, `rfc8785==0.1.4`) with resolved transitive versions in the root lock. Test modules from legacy and v0.2 must not share one Python import context. Runtime packages do not depend on this group.

Each aggregate calls reusable focused checks. The product aggregate owns product web/client checks and the explicitly listed infrastructure unit tests; the existing environment aggregate owns fixture web/client checks. Keep root `pnpm build`, `typecheck` and `check:client` as documented setup aliases during transition; introduce explicit product/setup scripts, and make every caller select its scope. A public codegen check validates both contracts once. The aggregate functions reuse its per-target implementation without silently omitting either target or running both again. CI composes the same focused functions so each service, generation, type, build and suite check runs once; fresh-install repetition is intentional independent-install evidence. Service-requiring checks are explicit; unit/API-shape checks run without services. Fresh-install compatibility must be updated in the task that changes packaging/workspace membership: .02 includes Python source and build metadata; .03 includes every new pnpm member and generated source. Do not leave the existing command broken until .05, which owns the stronger reproducibility proof. For the independent wheel check, install locked runtime dependencies into a fresh environment without an editable project, then install the built wheel without re-resolving dependencies. Remove inherited `PYTHONPATH`/`PYTHONHOME` and project/virtual-environment overrides; import the package/API factory from a directory outside the checkout and its ancestors. Assert `gre.__file__` resolves within that environment's installed package, and inspect the wheel file list for excluded material. .02 proves this minimally; .05 automates the full fresh-install path. Cache reuse is allowed; describe a fresh environment accurately instead of claiming a cold download.

### 3.5 Images, developer lifecycle and CI

Keep local ARM64 service topology, host helpers, named volumes and secrets. Complete immutable `tag@digest` references for Dockerfile source stages and PostgreSQL after verifying the official registry artifact, architecture and existing version; preserve already verified Temporal/Azurite digests. Record index versus platform-manifest digests explicitly. Pin the complete image reference used by helpers too, avoiding the current hard-coded PostgreSQL tag inspection. Do not infer that apt packages or a mutable GitHub runner OS are byte-for-byte reproducible merely because base images are pinned.

All three helpers already support `attach CURRENT_CONTAINER_ID`; use that for running services when reconnecting a recreated editor. Use `up CURRENT_CONTAINER_ID` only when startup is needed. Discover the actual ID; do not retain `9b0a594f1f29` as configuration. Temporal/Azurite `up` and `status` refresh `local-data/*/server.json`: these are mutable lifecycle observations, unlike the historical workflow probe. Record an intentional lifecycle refresh separately, then snapshot receipts for subsequent read-only checks. Never claim a refresh was an unchanged-file check or overwrite historical persistence proof to hide a failure. Ordinary application/worker containers do not get the host Docker socket. Adjust VS Code's Python interpreter to `${workspaceFolder}/.venv/bin/python` after project installation and document the first-sync requirement; do not turn editor creation into an unbounded build or automatic service/data reset.

CI uses `ubuntu-24.04-arm` and the **same ARM64 toolchain Dockerfile/pins**. Current GitHub documentation lists this runner for private repositories; repository policy/access, available minutes and any existing spending limit are checked read-only in G0, then actual runner execution is verified in .06. Do not silently switch to AMD64/QEMU or a paid/self-hosted runner if unavailable. Native AMD64 parity is future portability evidence unless a later deployment requires it.

Create `.github/workflows/ci.yml`, `ci/compose.yaml` and a host-side `scripts/run_ci.sh`. Reuse the existing version/digest settings through one checked source or an explicit equality check; do not leave independent drifting service versions. CI Compose is a disposable topology, not a copy of the developer lifecycle policy:

- Run the toolchain/check container as non-root with an owned writable disposable checkout. UID/workspace permissions are handled explicitly, not by making the test process root.
- Three synthetic services use unique project/run/attempt names and job-only credentials/storage. No fixed `gre-*` developer volume/network names, no host ports/UI and no developer `local-data` mounts. Build/package downloads may use normal CI egress; no production/provider credentials are supplied.
- Host orchestration creates and labels only these resources, installs locked dependencies, runs the gates and captures redacted failures. Use bounded cleanup traps for normal exit, partial-start failure and handled interruption; preserve the original failure exit. CI also attempts owned cleanup in an always-run final step. Forced process/runner termination may prevent traps; record ephemeral runner disposal as the fallback rather than promise cleanup code always executes. Test partial startup and a handled cancellation. Never call global Docker prune or delete a volume without verifying ownership.
- The same run checks toolchain/architecture, setup compatibility, current service connectivity, product quality, codegen drift, reference conformance and fresh installation. Explicitly create Chromium/system dependencies compatible with the chosen container; browser installation is a prerequisite, not a test pass.
- Trigger on `pull_request`, `push` to `main`, and manual dispatch. Keep the required gate scheduled for documentation-only changes too. Use stable job/check name `GRE / foundation`, a 30-minute job timeout and cancellation of an older run for the same PR. Capture actual runtime before changing this bound. No `pull_request_target` execution, automatic commits, releases, package publishing or deployment.
- Use minimal `contents: read` permissions and full verified commit-SHA pins for Actions. Do not retain checkout credentials in the test container or pass the Docker socket into it. Capture only bounded redacted logs/results; never upload whole workspace, secrets or service volumes as artifacts.
- A nonzero child command fails CI. Do not use `continue-on-error` for a required gate. Failed startup must fail, not skip all service tests and report success.

For a pull request, test GitHub's proposed merge revision and record the event, PR head, base and actual checkout SHA separately. GitHub's default PR checkout is not the source head. Rerun after head/base changes that invalidate the tested merge; check the displayed status belongs to the current candidate. A `push` run tests the actual merged `main` commit. No green result for an earlier revision is completion evidence for changed code.

P-001 requires an actual successful push-to-main CI run and final Mac checks at the same final merged revision; section 4's closeout protocol avoids a self-referential evidence commit. Record check name/run URL and whether branch protection enforces it. If required-check administration is unavailable, record that limitation and manually enforce the same current-candidate passing-check requirement; do not claim protection is configured or bypass an existing repository rule. GitHub billing/runner access is an actual external dependency, not a completed planning assumption.

## 4. Ordered child tasks

**Tracking:** [Parent issue #4](https://github.com/vishal-baliga/global-recovery-engine/issues/4). GitHub issues track task state; this document owns task scope and acceptance. The verification record owns observed evidence. No task is complete because this plan or its issue exists.

| Task | GitHub issue | Depends on |
|---|---|---|
| P-001.01 — Separate repeatable service health from historical evidence | [#5](https://github.com/vishal-baliga/global-recovery-engine/issues/5) | G0 local confirmation |
| P-001.02 — Establish the installable Python package and transport boundaries | [#6](https://github.com/vishal-baliga/global-recovery-engine/issues/6) | P-001.01 |
| P-001.03 — Add the web shell and separate product/setup client generation | [#7](https://github.com/vishal-baliga/global-recovery-engine/issues/7) | P-001.02 |
| P-001.04 — Make quality and contract checks executable | [#8](https://github.com/vishal-baliga/global-recovery-engine/issues/8) | P-001.03 |
| P-001.05 — Verify fresh installs, image references and editor reproducibility | [#9](https://github.com/vishal-baliga/global-recovery-engine/issues/9) | P-001.04 |
| P-001.06 — Add disposable ARM64 CI and the merge gate | [#10](https://github.com/vishal-baliga/global-recovery-engine/issues/10) | P-001.05 |
| P-001.07 — Reconcile evidence and close the foundation item | [#11](https://github.com/vishal-baliga/global-recovery-engine/issues/11) | P-001.06 |

Work on one task branch/PR at a time, branching from updated `main` after its predecessor merges. Suggested branches: `p001/01-service-health` through `p001/07-verification`. Do not batch all seven into one unreviewable implementation PR.

**Task completion and sprint control:** Each issue contains the execution checklist below; the plan owns its meaning. Vishal is accountable and local Codex implements the selected task. Before .06 provides CI, record focused task acceptance, affected existing commands and diff review before merging. From .06 onward require the actual configured gate as well. Update commands, file ownership, resolved dependencies and evidence in the PR that changes them; .07 consolidates them. Do not merge a known broken baseline on the promise that a later task will fix it.

The sprint goal is all seven evidenced outcomes and the P-004 handoff. No duration or capacity has been agreed. Record Vishal's available implementation/review time and any deadline at G0; use observed .01/.02 effort to revisit the forecast. .04 and .06 contain the largest compatibility/integration uncertainty. Keep work in progress to one task, surface a blocker with its owner/next action, and bring a material split or deferral here rather than quietly removing acceptance. Unfinished P-001 work stays open if the calendar window ends. Missing customers/providers do not block these synthetic checks.

### P-001.01 — Separate repeatable service health from historical evidence

**Depends on:** G0 local readiness below. **Files:** `scripts/check_services.py`, `scripts/check_environment.py` for the common bounded caller/config forwarding, focused tests, documents 09/10 only for changed commands/behavior. Existing isolated persistence probes remain intact.

Implement section 3.3 and explicit CI configuration overrides. Use the existing libraries; a focused standard-library `unittest` file can cover this before pytest is introduced. Acceptance: current service failure, historical absent/valid/not-found/malformed/denied/mismatched cases have the stated outcomes; exact typed `NOT_FOUND` is distinguished from other RPC failures; all waits bounded; credentials redacted; verification receipts unchanged. Check actual read-only local connectivity once authorized. No synthetic historical receipt is fabricated to make the check pass.

**Execution checklist:**

- [ ] Implement and test strict local/explicit service configuration and redacted failure output.
- [ ] Separate live namespace health from optional historical inspection, covering all stated receipt/RPC outcomes.
- [ ] Share the hard deadline/cleanup boundary across standalone and aggregate commands; prove a stuck check exits and receipt preservation runs on failures.
- [ ] Run focused unit checks and one read-only local connectivity check; preserve existing persistence probes and update behavior/evidence docs.

### P-001.02 — Establish the installable Python package and transport boundaries

**Depends on:** P-001.01. **Files:** `pyproject.toml`, `uv.lock`, `src/gre/`, `scripts/check_fresh_installs.py` for immediate compatibility, focused Python tests, `.gitignore` and command docs only as needed.

Implement section 3.1, backend pin, config loader, liveness factory and worker config check. Acceptance: build/install/import succeeds outside repo CWD; imports/export do not open services or read application configuration/secret files; API returns the exact minimal contract; wrong configuration fails without secret leakage; domain cannot import framework/I/O layers; no fixture/reference imports enter the distribution. Worker configuration check is distinguished from an operational worker. Test one invalid config and the package/transport failures; avoid fake claims/ORM tables merely to populate packages.

**Execution checklist:**

- [ ] Convert the Python project/lock to the selected distribution/backend and add only the minimal owned package boundaries.
- [ ] Implement the specified worker settings and liveness contract with invalid-input, secret-output and import-boundary checks.
- [ ] Adapt the existing fresh-install command now; build and independently install/import a wheel with clean import paths.
- [ ] Verify prior setup commands still work, inspect lock churn/wheel contents and record actual pins/commands/evidence.

### P-001.03 — Add the web shell and separate product/setup client generation

**Depends on:** P-001.02. **Files:** `apps/web/`, workspace/package manifests and lock, `contracts/openapi.json`, both generator configs, `packages/api-client/`, `packages/setup-api-client/`, export/client scripts, existing aggregate callers, fresh-install copier, affected fixture imports and command docs.

Implement section 3.2 atomically. Acceptance: product schema has liveness and excludes `/setup/echo`; fixture retains its independent schema and HTTP 200/422 behavior; both clients generate and type-check at TypeScript 6.0.3; product live client receives the specified response; new web shell builds without external assets/accounts. Client/schema generation is deterministic, and a second generation has no differences. Preserve the existing echo fixture as evidence, with its imports updated to the setup client.

**Execution checklist:**

- [ ] Create the development shell and relocate setup generation/consumers while reserving the existing client package for product.
- [ ] Add explicit target export/generation and update every aggregate, root script alias and fresh-install workspace member atomically.
- [ ] Verify deterministic product/setup schemas, independent live clients, setup 200/422 behavior, type checks and both builds.
- [ ] Verify the product imports no setup/reference source; document generation/check commands and record evidence.

### P-001.04 — Make quality and contract checks executable

**Depends on:** P-001.03. **Files:** quality-tool manifests/locks/config, relevant tests, `scripts/check_product.py`, `scripts/check_codegen.py`, `scripts/check_reference.py`, existing aggregate integration, Playwright configuration/smoke and browser prerequisite installer, Dockerfile for required system libraries, documents 09/10.

Implement section 3.4. Acceptance: lint/type/API/client/browser/build gates pass on the intended source; an injected type/lint error and generated-file addition/removal/change each fail their relevant gate; a failed subprocess is not swallowed. Check mode leaves tracked source/locks unchanged. Unit checks need no live service. Legacy and v0.2 suites pass in separate processes without archive changes. Temporary API/Next processes and ports are cleaned on success/failure; existing unrelated processes are preserved. This is one meaningful shell smoke, not a broad product E2E suite or invented coverage target.

**Execution checklist:**

- [ ] Resolve/lock the selected quality tools; configure handwritten/generated/reference scopes and include all P-001 infrastructure unit tests.
- [ ] Provision browser/system dependencies on ARM64, documenting any host image rebuild before running the smoke.
- [ ] Implement non-mutating codegen, product and isolated reference check runners; reuse the built shell for one Chromium smoke.
- [ ] Exercise negative lint/type/codegen/process tests in owned temporary copies, verify exits/cleanup and no tracked/lock changes, and preserve original reference bytes.
- [ ] Record each focused/aggregate command, installed tool/browser version, actual time/resource failures and acceptance result.

### P-001.05 — Verify fresh installs, image references and editor reproducibility

**Depends on:** P-001.04. **Files:** `scripts/check_fresh_installs.py`, Dockerfile/build args, relevant Compose/host image references, `devcontainer.json`, ignore rules and documents 09/10.

Implement section 3.5's local/build requirements. Acceptance: empty temporary install includes source required by the build backend and every workspace package; built wheel installs/imports independently; fresh-install probes leave the working install/manifests/locks unchanged; existing service data and historical probe evidence are preserved, with intentional editor/lifecycle changes recorded. Verify image digests and native architecture at the retained versions. A recreated editor uses the project interpreter and can be attached through the existing host helpers, without making a new database or wiping state. Record what is immutable and what remains OS/package-manager input; do not silently claim byte-identical rebuilds.

**Execution checklist:**

- [ ] Extend the now-working fresh-install copier into full locked workspace and independent-wheel verification without inherited editable/source paths.
- [ ] Verify and record retained-version ARM64 image digests; update every helper/reference consistently.
- [ ] Rebuild/reconnect the actual editor, select the project interpreter and attach to existing running services; distinguish lifecycle observations from immutable probe evidence.
- [ ] Verify fresh installs, current service health and no unintended data/receipt/lock drift; record reproducibility limits and recovery instructions.

### P-001.06 — Add disposable ARM64 CI and the merge gate

**Depends on:** P-001.05. **Files:** `.github/workflows/ci.yml`, `ci/compose.yaml`, `scripts/run_ci.sh`, minimal shared image/config representation if required, task verification record.

Implement the selected CI design. Acceptance: actual `GRE / foundation` run passes for the current PR candidate with source/base/tested SHAs recorded; deliberate failing check, partial-start failure and handled interruption return nonzero and clean only labeled job resources; no developer volumes/credentials/ports appear in the disposable topology. Tool versions, image architecture, codegen, references, fresh installation and browser prerequisites are recorded. Secrets stay out of logs/artifacts. Confirm runner/minute availability and required-check enforcement or its explicit administrative limitation. No paid capacity increase or cloud deployment is implied.

**Execution checklist:**

- [ ] Resolve the G0 Actions/capacity prerequisites and build the disposable non-root topology using shared pins and explicit job configuration.
- [ ] Compose each required gate once with bounded logs, exact revision metadata, resource ownership and timeout/cancellation cleanup.
- [ ] Prove deliberate gate/startup/interruption failures, then obtain a successful native ARM64 run for the actual candidate.
- [ ] Verify the observed check name, current-candidate status and enforced or manual merge rule; record actual minutes/runtime and remaining administrative limits.

### P-001.07 — Reconcile evidence and close the foundation item

**Depends on:** P-001.06. **Files:** verification record, documents 00/09/10/11 and relevant developer instructions; code changes only to resolve a demonstrated P-001 defect.

Acceptance: prepare the .07 documentation with a stable final-evidence link to issue #11; merge after its PR check passes without auto-closing #11 or #4. Then run final non-destructive Mac/container checks and confirm push-to-main CI for that exact merged revision. Record SHA, command/exit, relevant versions, preserved data/receipt evidence, tested limitations and run/task PR links in issue #11's final-result section. The repository verification record explicitly points to that section for post-merge observations; do not loop through documentation commits trying to record a file's own commit SHA. An implementation defect requires a normal corrective commit/PR and fresh evidence at the corrected revision before closure. Confirm the original ZIP hash and absence of unintended reference/schema changes. Update commands/layout/status descriptions to the actual implementation, retaining historical observations with dates. Close the parent only when acceptance is evidenced; no child is completed by a planning-only PR. Handoff the next engineering item P-004; P-002/P-003 business work keeps its real status. A missing buyer/provider does not block this synthetic foundation.

**Execution checklist:**

- [ ] Reconcile A01–A12, all child evidence, actual docs/layout/commands and original reference hash; identify any unresolved required result.
- [ ] Merge the .07 documentation after its candidate passes CI, then verify Mac and push-to-main CI at that exact merged revision.
- [ ] Record the post-merge SHA/results in issue #11 via the stable verification-record link; resolve any demonstrated defect before closure.
- [ ] Close the completed task/parent only after evidence passes; hand off P-004 with the package/config/client/gate boundaries and known limits, keeping P-002/P-003 truthful.

## 5. Acceptance matrix and completion rule

| Evidence ID | Demonstrated behavior | Task owner |
|---|---|---|
| A01 | Current health/configuration works without retained Temporal history; true failures and stuck checks terminate correctly in standalone and aggregate use | .01 |
| A02 | Historical missing/malformed/denied/mismatched results stay distinguishable; receipts unchanged | .01 |
| A03 | One installable Python package; wheel usable outside checkout; side-effect-free imports | .02, .05 |
| A04 | Typed liveness, explicit worker defaults/precedence and secret-safe failure; domain/fixture/import boundaries enforced | .02 |
| A05 | Independent product/setup contracts and live client probes; fixture200/422 retained | .03 |
| A06 | Deterministic codegen check detects changed, added and removed artifacts without rewriting them | .03, .04 |
| A07 | All P-001 unit/quality scopes run; browser prerequisites exist; lint/type/test/build/Chromium failures propagate and owned processes clean up | .04 |
| A08 | Both reference suites run separately; original ZIP unchanged | .04, .07 |
| A09 | Locked fresh installs and recorded immutable image references on native ARM64 | .05 |
| A10 | Editor `.venv` and current-container host attachment work with existing data preserved | .05, .07 |
| A11 | Disposable CI, bounded logs/permissions, failure/interruption cleanup, revision provenance and final merged-main pass | .06, .07 |
| A12 | Each task preserves working predecessor commands; actual evidence/limits and post-merge closeout/P-004 handoff reconciled | All; .07 consolidates |

Completion requires A01–A12 and all seven task outcomes. Store observed results in the verification record, linking redacted CI/task evidence. Do not collect real customer data for these checks or repeat database restart/restore proofs merely for an additional green badge. No product coverage percentage or performance SLA is asserted by this task.

## 6. Local handoff before implementation

**G0 is pending.** After this planning update is published, perform the local confirmation with Vishal before starting P-001.01:

1. Inspect Git status, remote, current branch and actual files; preserve uncommitted work. Fetch and safely bring local `main` to the published planning baseline. No forced reset/clean or silent disposal. Verify repository-local commit identity and fetch/push availability without changing unrelated global settings or making a test push to `main`.
2. Confirm the active session is the intended ARM64 editor container and its current ID. Inspect host Docker memory allocation/free disk and registry/package connectivity needed for the pinned builds; record actual constraints, not a promised duration. Host inspection/attachment happens from the Mac session when the editor cannot access Docker.
3. For already running services use the existing `attach` helpers. If startup is needed, record any expected lifecycle `server.json` refresh separately and preserve the original workflow probe. Snapshot Git/lock state and receipt hashes before subsequent checks; do not publish secrets or whole environment dumps.
4. Run only current read-only readiness checks: `python .devcontainer/check_environment.py --expect-arch arm64`, installed-version/lock inspection and direct service checks using the already-installed Python environment. Do not run `uv sync`, `pnpm install` or the current combined `scripts.check_environment` in the working checkout merely to confirm readiness: the combined check currently rewrites tracked schema/client files. If dependencies are missing or an isolated legacy combined run is needed, record that and handle it as a distinct bounded environment action. G0 is not allowed to repair files silently.
5. Bound the old service command externally while its .01 timeout fix is pending. Record exact commands/exits. A reproduced historical Temporal lookup failure may carry into .01 only with independent current read-only connectivity evidence. Report that baseline failure honestly; do not delete the receipt or label unrelated errors as retention.
6. Inspect repository Actions policy, native ARM64 eligibility, available minutes/existing spending limits and ability to administer required checks. Record verified facts or unavailable access, owner and resolution step now; actual runner execution remains .06. No paid increase or credentials in Git are authorized by planning. An unresolved hard prerequisite prevents a claim that the full sprint is ready; unrelated authorized work may proceed with the dependency visible.
7. Record Vishal's available implementation/review time or leave it explicitly unset; no fixed sprint end date is assumed. Put G0 observations/blockers in the verification record and parent issue, then obtain Vishal's instruction to begin the selected task. This preserves plan here → confirm Mac/environment → begin development.

Local Codex's initial assignment is confirmation, not replanning. For implementation, read this plan and the selected issue, make the bounded change, execute its acceptance checks and report evidence/limits. Commit/PR completion, a changed runner prerequisite or a version fallback must update the proper artifact. A task encountering a material conflict should state the failed requirement and proposed change; it must not silently substitute a different architecture or remove the gate.

## 7. Dependencies and later work

No new cloud, Clerk, model, OCR or provider account is needed to plan P-001. The existing GitHub/VS Code/Codex connection and Docker setup support the intended local work. Actions policy/access/capacity and build-download prerequisites are checked at G0; .04/.05/.06 prove their actual compatible execution. Unresolved access is recorded early rather than guessed.

Production images/deployment, host-to-cloud parity, durable provider workflows, real backups/restores, authorization/RLS and live identity/data protections remain the later backlog's responsibility. Shared modules grow through their first real caller. Multi-architecture production proof, larger CI caches/matrices, broad UI/property suites and automated dependency-update rollout can be added when justified; they are not hidden requirements to complete this foundation. Pin/update policy and any known relevant dependency vulnerabilities must be reviewed during tooling selection, without a blanket all-packages upgrade.

## 8. Primary implementation references

Repository code at the inspected commit is the evidence for the starting state. The following official guidance was checked September 8, 2026; use it with the pinned versions and retain actual compatibility evidence:

- [uv build backend](https://docs.astral.sh/uv/concepts/build-backend/): explicit source/module configuration and build-system requirements.
- [uv locking and synchronization](https://docs.astral.sh/uv/concepts/projects/sync/): locked installation and project packaging behavior.
- [Next.js ESLint configuration](https://nextjs.org/docs/app/api-reference/config/eslint): ESLint CLI and monorepo configuration; build is separate.
- [GitHub runner selection](https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job): private-repository ARM64 runner label; account capacity remains to be verified.
- [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use): minimal permissions, trusted action sources and immutable commit pins.
- [GitHub workflow events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows): PR merge revision versus source head and push revision.
- [Python asyncio runner](https://docs.python.org/3.14/library/asyncio-runner.html): executor shutdown is separate from cancellation of an awaitable.
- [Playwright browser prerequisites](https://playwright.dev/docs/browsers) and [web server lifecycle](https://playwright.dev/docs/test-webserver): browser installation and owned server behavior.
- [Pydantic error configuration](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.hide_input_in_errors): invalid input can appear in errors; verify actual redacted output.
- [GitHub workflow cancellation](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-cancellation): interruption and forced termination are distinct.

## 9. Sprint review disposition — September 8, 2026

Rechecked against current repository source, all eight tracking issues and independent package/CI/task-sequence reviews. The seven implementation tasks remain the full P-001 scope. Corrections assign compatibility repairs to .02/.03, browser prerequisites to .04, hard health deadlines to .01, early external/capacity discovery to G0 and exact revision/closeout evidence to .06/.07. Worker/probe configuration and negative secret/import tests are now explicit. No runtime code or completion evidence was produced by this review. The wider Pilot backlog and future-family boundaries are unchanged.
