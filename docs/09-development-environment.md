# Development environment — first container

**Status:** Language-toolchain and editor/agent setup verified on Vishal’s Mac on September 6, 2026, based on his local Codex reports. The image build, offline ARM64 check, and actual VS Code/Codex container session passed. Local services and application dependency compatibility remain pending.

## What this step establishes

The first container provides the project language toolchains and development utilities. Docker Desktop runs on the Mac; Python, Node, uv, pnpm, Git, and build utilities run inside the Linux container. Host-level Node/Python installations are optional for later use and are not required for this route. The Mac's Apple-provided Python stays in place.

| Component | Initial pin | Source |
| --- | --- | --- |
| Python | 3.14.7, Debian Bookworm slim image | [Official Python image definitions](https://github.com/docker-library/official-images/blob/master/library/python) |
| Node.js | 24.20.0, Debian Bookworm slim image | [Official Node image definitions](https://github.com/docker-library/official-images/blob/master/library/node) |
| uv | 0.12.10, copied from Astral's published image | [uv Docker integration](https://docs.astral.sh/uv/guides/integration/docker/) |
| pnpm | 11.10.0, explicit npm package version | [pnpm installation and compatibility](https://pnpm.io/installation) |

pnpm's documentation still identifies version 11 as the default npm release line. The 11.10.0 pin retains that installation model; evaluate a major upgrade separately. The registry install and pinned binary combination passed the first ARM64 build and environment check. These pins are an initial setup selection, not a claim that application dependencies have been resolved.

Image tags and OS package repositories can change. Exact tool versions improve consistency; immutable image digests and application lockfiles remain follow-up setup work after a successful build. Do not describe this image as bit-for-bit reproducible yet. Docker selects the native image architecture; the image definitions list ARM64 support for the selected Python and Node tags.

The container runs as the `vscode` user and mounts the selected repository at `/workspaces/global-recovery-engine`. Its build context is the `.devcontainer` directory; the Dockerfile does not copy the project or case material into the image. The initial container has no application services, published ports, or Docker socket mount. The development session can write its mounted repository; it is not an isolation boundary protecting that checkout from edits.

## Open the environment in VS Code

1. Leave Docker Desktop running. Open the actual GRE Git repository folder. A shell prompt showing `GRE Development` is not enough to establish the root; verify with `git rev-parse --show-toplevel`.
2. Inspect local Git status, fetch the remote, and check out the prepared `setup/devcontainer` branch without discarding local changes. If a local branch already exists, inspect it before updating; do not reset it blindly.
3. Install [Dev Containers by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) if it is not already installed.
4. Run **Dev Containers: Reopen in Container** from the Command Palette. The first build downloads the base images, OS utilities, and pinned pnpm package. Open the build log if it fails.
5. Once the container opens, the post-create command runs the environment check. For the M4-specific verification, run:

```sh
python .devcontainer/check_environment.py --expect-arch arm64
```

Expected final line: `GRE development toolchain: PASS (linux/arm64)`.

The check verifies Linux/non-root execution, all four version pins, compatible Node/Python architecture, Git/npm availability, repository write access, uv creation/execution of a Python virtual environment, SSL/SQLite imports, and pnpm execution of Node. It uses temporary files and removes them afterward; it does not install application dependencies. A pass does not verify Next.js/FastAPI libraries, database connectivity, provider integrations, or any product behavior.

VS Code is configured to install the Codex, Python, Pylance, and Ruff extensions in the development environment. Confirm Codex is available after reconnecting; complete sign-in if requested by its UI. Session reach and credentials depend on that actual environment. Use the project files as context when starting a new agent conversation.

## Local Codex task before opening the editor container

Codex on the Mac can build and test the image through Docker before the UI reconnect. From the repository root on the host:

```sh
docker build --file .devcontainer/Dockerfile --tag gre-dev:local .devcontainer
docker run --rm --network none \
  --mount "type=bind,source=$(pwd),target=/workspaces/global-recovery-engine" \
  --workdir /workspaces/global-recovery-engine \
  gre-dev:local \
  python .devcontainer/check_environment.py --expect-arch arm64
```

These commands use the same Dockerfile defaults checked against the Dev Container build arguments. The mount is read/write because the verification creates a temporary environment in the checkout. The test container is removed after exit; the image remains cached. After the smoke check succeeds, use the VS Code reopen command above to establish the actual editor session too.

If a build or check fails, keep the first relevant error and diagnose it on this branch. Record any needed version/configuration change and repeat the affected check. Do not substitute broad permissions, root sessions, or an emulated architecture solely to make the check pass. This is a configuration/compatibility check; no user app-data permission is required by this design, although a host integration may have its own specific request to assess.

## Verification record and following work

Verified on the Mac before this step: Homebrew 6.0.22 at `/opt/homebrew`; Docker Desktop 4.89.0, engine/client 29.7.2; Compose 5.5.0; a successful ARM64 `hello-world` download and execution. The prior VS Code privacy dialog's final choice was not reported.

Verified locally on September 6, 2026 from branch baseline `445db9a` plus the check-script fix:

- `docker build --file .devcontainer/Dockerfile --tag gre-dev:local .devcontainer` exited 0.
- The documented `docker run` check exited 0 with `--network none`, ending in `GRE development toolchain: PASS (linux/arm64)` as non-root `vscode`.
- Observed Python 3.14.7, Node 24.20.0, pnpm 11.10.0, uv 0.12.10, npm 11.19.0, and Git 2.39.5.
- The first runtime check failed its exact stdout comparison: pnpm successfully executed Node but automatically ran dependency preflight and printed update notices. The temporary project's `pnpm-workspace.yaml` now sets `verifyDepsBeforeRun: false` and `updateNotifier: false`. The corrected check passed offline; no pins or image configuration changed.
- Microsoft Dev Containers `ms-vscode-remote.remote-containers@0.466.0` confirmed using the installed VS Code CLI. No extension installation was needed.

Build-resolved image references (recorded observations, not yet digest pins in the Dockerfile):

| Image | Resolved digest |
| --- | --- |
| `python:3.14.7-slim-bookworm` | `sha256:9ab8d9c8514b44f90cf0029dd42fdd7e9e211e639c8b995304cc04568dee900f` |
| `node:24.20.0-bookworm-slim` | `sha256:ba849c60be29959425b8734d57b8b4b7d56f98edd9504c9af091d5281095a71e` |
| `ghcr.io/astral-sh/uv:0.12.10` | `sha256:2bb3ebca0a796a155094a27773d290c4b074572e6107f171d88d086682fd2500` |
| Local `gre-dev:local` image ID | `sha256:49b1d04e826ba31bdbd0b68e06cad505410ea2cf0767b7758476d1e0877ebb18` |

Vishal subsequently supplied the successful editor/agent verification: Codex executed in `/workspaces/global-recovery-engine` on Debian GNU/Linux 12 (bookworm), Linux `7.0.12-linuxkit`, `aarch64` / ARM64, as non-root `vscode` with UID/GID `1000`. The Docker marker and VS Code container server were present. The environment check exited 0 with `GRE development toolchain: PASS (linux/arm64)`, including all pinned versions, Python virtual environment/SSL/SQLite, pnpm execution, and workspace write checks. GitHub confirms the earlier check fix and build records in commit `c937128`; the report did not include the current local HEAD. See [the setup checkpoint](00-start-here.md) for the next increment.

The PostgreSQL and Temporal increments and their verification are recorded below. Next establish local Azurite, application dependency compatibility/lockfiles, and the remaining environment checks needed for backlog planning. These remain setup work. The agreed sequence continues with prioritized backlog and document reconciliation before product feature development.

[VS Code Dev Containers guide](https://code.visualstudio.com/docs/devcontainers/containers) and the [Dev Container specification](https://github.com/devcontainers/spec/blob/main/docs/specs/devcontainerjson-reference.md) define the editor and lifecycle behavior used here.

## Local PostgreSQL 18

This increment adds only a local development service and a synthetic environment
probe. Run Docker commands on the **Mac host**; the editor container has neither
Docker CLI nor socket access.

`.devcontainer/compose.postgres.yaml` selects `postgres:18.6-bookworm` and explicitly
requests `linux/arm64`. The [official image metadata](https://github.com/docker-library/official-images/blob/master/library/postgres)
lists `arm64v8` for this tag. This pins the database patch version and Debian suite;
the tag is not immutable. The host startup command reports its resolved digest and
architecture for the verification record.

The named volume `gre-postgres18-data` mounts `/var/lib/postgresql`; PostgreSQL 18
stores the cluster in `/var/lib/postgresql/18/docker`, following the
[official image layout](https://hub.docker.com/_/postgres). Normal stop/start and
restart preserve the volume. Do not use `down --volumes` or remove that volume as
part of routine lifecycle work.

The internal Docker network `gre-database` has **no published database port**.
The attached development container connects to `gre-postgres:5432`, database/user
`gre_dev`. The development container retains its original network for internet
access. The database is accessible only to containers attached to its private
network (and administrators controlling Docker), with SCRAM password authentication.
There is no Mac/LAN database listener or VS Code port forwarding.

Startup generates a random local password at `local-data/postgres/password`,
which Git already ignores. Compose mounts it as a secret; its path, not its value,
appears in configuration. The parent directory is mode 700; the file is readable
inside the database container so its `postgres` user can initialize the cluster.
Keep this file with the local volume: changing it alone does not change an already
initialized database password. `gre_dev` is the image's local bootstrap superuser;
application roles and migrations belong to later implementation work.

### Mac host commands

From this checkout's root in **Mac Terminal**, with Docker Desktop running:

```sh
# Find the GRE editor container; confirm the workspace mount if several exist.
docker ps --format 'table {{.ID}}\t{{.Names}}\t{{.Image}}'
# Replace GRE_CONTAINER_ID with the running editor container's ID.
bash .devcontainer/postgres-host.sh up GRE_CONTAINER_ID
```

`up` initializes the password only when absent, waits for database health, checks
that the supplied container mounts this checkout, and attaches it to the database
network. It prints the downloaded image architecture/digest and PostgreSQL version.
The existing session at implementation time was `9b0a594f1f29`; IDs change after
recreation. No editor rebuild is required. After rebuilding/recreating the editor
container, rerun `up` with its new ID (or `attach` if the database is already up).
This explicit host attachment is required; `devcontainer.json` remains standalone.

```sh
bash .devcontainer/postgres-host.sh status
bash .devcontainer/postgres-host.sh stop
bash .devcontainer/postgres-host.sh up
bash .devcontainer/postgres-host.sh restart
bash .devcontainer/postgres-host.sh attach GRE_CONTAINER_ID
```

`stop` keeps the container, volume, network, and editor attachment. `up` starts it
again. `restart` performs a normal database restart and waits for health. `status`
reports service health, `Internal=true`, actual host port bindings, and the named volume mount. Empty host bindings (`{}`) mean there is no published database port. If `up` fails,
inspect `docker compose -f .devcontainer/compose.postgres.yaml logs --tail 80 postgres`
and correct the failure before running the probe.

### Connectivity and persistence check

Run in the **development container**:

```sh
uv run --frozen --script .devcontainer/check_postgres.py connect
uv run --frozen --script .devcontainer/check_postgres.py seed
```

The script's adjacent lockfile pins its isolated Psycopg environment (3.3.5,
including the binary package). This is an environment-check dependency, not an
application dependency lock. The initial run downloads wheels; subsequent cached
runs can use `--offline`. The check requires PostgreSQL 18.6, native aarch64 server
build, and the expected data directory, and authenticates over TCP from the editor.

`seed` commits one UUID-tagged synthetic row in
`gre_environment_check.restart_probe` and writes its receipt under ignored
`local-data/postgres/`. It refuses to overwrite an outstanding receipt.
Then run on the **Mac host**:

```sh
bash .devcontainer/postgres-host.sh restart
```

Back in the **development container**:

```sh
uv run --frozen --script .devcontainer/check_postgres.py verify
uv run --frozen --script .devcontainer/check_postgres.py cleanup
```

`verify` requires both the same stored payload and a changed PostgreSQL server
start time, so reading before restart cannot falsely pass. `cleanup` removes only
this probe's row and receipt; the empty environment-check table may remain.
No application tables are created. This verifies normal-restart persistence,
not backup/restore or disaster recovery.

### PostgreSQL verification record

Verified September 6, 2026 after clean fast-forward of `setup/devcontainer` from
`c937128` to `2c80392`; no pre-existing local changes were present.

- Vishal's Mac host output confirms image pull, named-volume/network creation,
  database health, and attachment of editor container `9b0a594f1f29`.
- Docker reports `linux/arm64`, PostgreSQL `18.6 (Debian 18.6-1.pgdg12+2)`,
  and resolved image digest
  `postgres@sha256:1c59e2c3c818eaa0f0628f695b36e7c9e362d6b219b36a54a32df645cbd7e1af`.
  This is an observed digest; Compose pins the patch/suite tag.
- The isolated Psycopg 3.3.5 CPython 3.14 ARM64 binary installed successfully.
  The agent's TCP connection from the running development container passed,
  confirming server build `aarch64-unknown-linux-gnu` and data directory
  `/var/lib/postgresql/18/docker`.
- The probe committed synthetic record `9faf60cb-cb80-4db2-8a07-1310bb2ce1d1`.
  Vishal ran the normal host restart helper; the database returned healthy.
  The agent's subsequent offline-client verification passed: the row was unchanged
  and server start time advanced from `2026-09-06 23:01:51.424061+00` to
  `2026-09-06 23:04:02.668422+00`.
- Probe cleanup passed; the synthetic row and local receipt were removed.
  The database remains running with its persistent volume.
- Host status confirms `Internal=true`. The first status helper encountered
  Compose's `invalid IP:0` when querying an unpublished port; it now uses
  `docker inspect` for port bindings and volume details. The corrected helper
  passed on the Mac: `Host port bindings={}` and
  `Volume=gre-postgres18-data -> /var/lib/postgresql`; the database was healthy.
- Host shell syntax, script CLI, Git whitespace/secret-ignore checks, and the
  existing ARM64 language-toolchain check passed. No application features,
  application schema/migrations, or cloud resources were added.

Recreated editor containers need the documented host `attach` command. This step
verifies a normal PostgreSQL restart; volume recreation and backup restore were
not tested.

## Local Temporal development server

This increment uses the official Temporal CLI's embedded development server,
with SQLite persistence separate from GRE's PostgreSQL business-record database.
It adds only a synthetic workflow and environment probe. The official
[Docker image](https://hub.docker.com/r/temporalio/temporal) and
[server command reference](https://docs.temporal.io/cli/command-reference/server)
describe `server start-dev` and persistent `--db-filename` storage.

`.devcontainer/compose.temporal.yaml` pins CLI image `temporalio/temporal:1.8.3`
**and** multi-platform digest
`sha256:cea463d98a8d6def4420f903ea5c3fcd0d85c8d10fbcc2770a50c12fff2eb26d`,
with `platform: linux/arm64`. Docker Hub's tag metadata lists native Linux ARM64.
The CLI version identifies the image; its embedded server version is reported by
`temporal --version` and recorded below after runtime verification.

The named volume `gre-temporal-dev-data` mounts `/home/temporal`, the image's
non-root user's home, so the initialized volume inherits writable ownership.
The server writes `/home/temporal/gre-temporal.db` and its SQLite companion files
there. Normal stop/start/restart keeps this volume. Do not remove the volume or
use `down --volumes` for routine lifecycle work. CLI upgrades may require a new
development database; this increment does not establish an upgrade/restore path.

The internal `gre-temporal` Docker network carries gRPC at `gre-temporal:7233`.
A second dedicated bridge network, `gre-temporal-ui`, allows Docker Desktop to
serve the published localhost UI port; publishing from an internal-only network
did not work on the verified Mac. Only the Temporal server joins this bridge.
It permits server egress and does not publish gRPC; other Docker containers would
need explicit network attachment to reach the server.
No gRPC host port is published. The only host binding is
**`127.0.0.1:8233`**, for the embedded UI at <http://127.0.0.1:8233/>. No VS Code
port forwarding is configured. The development server has no production
authentication/TLS and must contain only synthetic data; access is limited to
attached containers, local Mac users through the UI, and Docker administrators.
The editor retains its original network for internet access. The database and
Temporal services use separate internal networks and volumes.

### Mac host lifecycle and editor attachment

Run from this GRE checkout's root in **Mac Terminal**:

```sh
docker ps --format 'table {{.ID}}\t{{.Names}}\t{{.Image}}'
# Replace GRE_CONTAINER_ID with the GRE editor container ID.
bash .devcontainer/temporal-host.sh up GRE_CONTAINER_ID
curl --fail --silent --output /dev/null --write-out 'Temporal UI HTTP %{http_code}\n' http://127.0.0.1:8233/
```

`up` starts Temporal, waits for gRPC health, checks that the supplied editor
container mounts this checkout, and attaches it to the private network. It
reports CLI/server versions, native architecture, runtime user, resolved digest,
port bindings, and volume mount. The editor container during initial verification
is `9b0a594f1f29`; recreated containers have a new ID.

```sh
bash .devcontainer/temporal-host.sh status
bash .devcontainer/temporal-host.sh stop
bash .devcontainer/temporal-host.sh up
bash .devcontainer/temporal-host.sh restart
bash .devcontainer/temporal-host.sh attach GRE_CONTAINER_ID
```

`stop` preserves the volume, network, and editor attachment; `up` starts the
existing service again. `restart` performs a normal restart, waits for health,
and refreshes the ignored server-start receipt used by the probe. `status`
reports actual Docker configuration, including `Internal=true`, the sole
localhost UI binding, and the persistent volume. Rebuilding/recreating the
editor requires `attach` with its new ID; `devcontainer.json` stays standalone.
All Docker orchestration runs on the Mac; the editor has no Docker CLI/socket.

If startup fails, inspect:

```sh
docker compose -f .devcontainer/compose.temporal.yaml logs --tail 100 temporal
```

### Locked Python SDK connectivity and restart probe

`.devcontainer/check_temporal.py.lock` locks the isolated `temporalio==1.32.0`
SDK and transitive packages for Python `>=3.14,<3.15`. Its published ARM64 stable
ABI wheel installs on CPython 3.14. This is an environment-probe lock, not an
application dependency decision. The first run downloads packages; after caching,
`--offline` prevents further network package access.

Run in the **development container**:

```sh
uv run --frozen --script .devcontainer/check_temporal.py connect
uv run --frozen --script .devcontainer/check_temporal.py seed
```

`seed` starts an isolated worker and a UUID-named synthetic workflow on a unique
task queue in namespace `default`. It queries the workflow to verify it is
waiting for a signal, saves the exact workflow/run IDs and host restart receipt
under ignored `local-data/temporal/`, then shuts down the worker. No background
probe worker is left running. Workflow execution timeout is one day; complete
the restart check within that window.

Restart the **server on the Mac host**:

```sh
bash .devcontainer/temporal-host.sh restart
```

Run in a **new development-container process**:

```sh
uv run --frozen --offline --script .devcontainer/check_temporal.py resume
```

`resume` checks the same server container has a changed start timestamp, launches
a new worker with a different identity, opens the saved workflow **and run ID**,
and queries that it is still waiting. It then signals that execution, verifies
its exact synthetic result and completed status without following another run,
and checks history contains exactly one start, signal, and completion. Both
commands have a 60-second overall timeout. The separate workflow module preserves
the SDK's default workflow sandbox.

The completed execution/history remains available for inspection in the local UI,
subject to the development namespace's retention. The ignored receipt records
the verification. To run a fresh probe after success, archive the receipt first:

```sh
mv -n local-data/temporal/workflow-probe.json local-data/temporal/workflow-probe.previous.json
```

The command does not overwrite an existing archive; rename that archive first
if you need to archive another receipt. A pending
receipt is deliberately not overwritten by `seed`; finish or diagnose that
execution before starting another probe. This establishes normal development
server/worker restart recovery, not production durability, backup restoration,
application replay compatibility, activity retries, or external-effect handling.

### Temporal verification record

Verified September 6, 2026 from clean `setup/devcontainer` at `ea7cb38` plus
this increment. Origin was fetched and the branch was already up to date.

- Vishal's Mac output confirms the pinned image digest above, `linux/arm64`,
  runtime `aarch64`, and non-root `temporal` UID/GID 1000. The image reports
  **CLI 1.8.3, embedded Server 1.31.2, UI 2.50.1**.
- The named volume is `gre-temporal-dev-data -> /home/temporal`; the SDK network
  reports `Internal=true`. Docker reports exactly
  `{"8233/tcp":[{"HostIp":"127.0.0.1","HostPort":"8233"}]}` as host port bindings.
  No gRPC port is published. The Mac UI request returned HTTP 200.
- The initial internal-only network allowed SDK access but the Mac UI request
  returned HTTP 000. Adding the dedicated UI bridge resolved host access while
  retaining the localhost-only binding and internal SDK network. The service
  was recreated for this adjustment before the synthetic workflow was started.
- SDK 1.32.0 and its locked dependencies installed successfully on CPython 3.14.7
  ARM64. The agent's `connect`, `seed`, and `resume` commands passed from the
  development container using the locked environment; workflow checks ran with
  offline package access and the SDK's default workflow sandbox.
- Synthetic workflow ID:
  `gre-environment-bd049407-ba8c-4ca1-8c2b-0c42cbceb85b`.
  Exact run ID: `01a07906-7524-703d-9f22-507260b910c5`.
  The first worker confirmed it was waiting for a signal, then exited cleanly.
- Vishal ran the normal server restart helper. Container
  `45f07f76c4cf8dacd346e28a1d8956a2018e2f983abbfbefd2e7f6a77827a2e7`
  remained the same; its start timestamp changed from
  `2026-09-06T23:20:18.814375214Z` to `2026-09-06T23:21:34.82863468Z`.
- The replacement worker used identity
  `gre-environment-worker-ead561fc-ec4c-4441-8a8c-d5e19f201ed4`, replacing
  `gre-environment-worker-ef16acfb-4996-436c-9af3-880c5035180b`.
  It queried the same run as waiting, signaled it, and verified completion with
  result `GRE synthetic probe completed: bd049407-ba8c-4ca1-8c2b-0c42cbceb85b`.
  The nine-event history has exactly one start, signal, and completion.
  The replacement worker also exited cleanly.
- Host helper syntax, Python parsing/CLI, lockfile parsing, Git whitespace, and
  local receipt ignore checks passed. No unrelated changes were present.

Temporal remains running; its completed synthetic history and ignored receipt
are retained for inspection. Recreated editor containers need manual host network
attachment. The UI bridge permits outbound networking; the development service
has no production authentication/TLS. Normal server and worker restart recovery
passed, but backup/restore, data-volume loss, server upgrades, production
operations, and application workflow/activity behavior were not tested. The
Python lock is specific to this environment probe. Azurite and application
compatibility/locks remain subsequent setup work.
