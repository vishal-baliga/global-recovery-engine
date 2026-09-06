# Development environment — first container

**Status:** Configuration prepared; JSON/Python syntax and version-pin consistency checked. The GRE image has not been built or run in this hosted workspace, which has no Docker engine. The first ARM64 build and runtime checks are the next task on Vishal's Mac.

## What this step establishes

The first container provides the project language toolchains and development utilities. Docker Desktop runs on the Mac; Python, Node, uv, pnpm, Git, and build utilities run inside the Linux container. Host-level Node/Python installations are optional for later use and are not required for this route. The Mac's Apple-provided Python stays in place.

| Component | Initial pin | Source |
| --- | --- | --- |
| Python | 3.14.7, Debian Bookworm slim image | [Official Python image definitions](https://github.com/docker-library/official-images/blob/master/library/python) |
| Node.js | 24.20.0, Debian Bookworm slim image | [Official Node image definitions](https://github.com/docker-library/official-images/blob/master/library/node) |
| uv | 0.12.10, copied from Astral's published image | [uv Docker integration](https://docs.astral.sh/uv/guides/integration/docker/) |
| pnpm | 11.10.0, explicit npm package version | [pnpm installation and compatibility](https://pnpm.io/installation) |

pnpm's documentation still identifies version 11 as the default npm release line. The 11.10.0 pin retains that installation model; evaluate a major upgrade separately. The registry install and all binary combinations still need validation in the first build. These pins are an initial setup selection, not a claim that application dependencies have been resolved.

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
docker run --rm \
  --mount "type=bind,source=$(pwd),target=/workspaces/global-recovery-engine" \
  --workdir /workspaces/global-recovery-engine \
  gre-dev:local \
  python .devcontainer/check_environment.py --expect-arch arm64
```

These commands use the same Dockerfile defaults checked against the Dev Container build arguments. The mount is read/write because the verification creates a temporary environment in the checkout. The test container is removed after exit; the image remains cached. After the smoke check succeeds, use the VS Code reopen command above to establish the actual editor session too.

If a build or check fails, keep the first relevant error and diagnose it on this branch. Record any needed version/configuration change and repeat the affected check. Do not substitute broad permissions, root sessions, or an emulated architecture solely to make the check pass. This is a configuration/compatibility check; no user app-data permission is required by this design, although a host integration may have its own specific request to assess.

## Verification record and following work

Verified on the Mac before this step: Homebrew 6.0.22 at `/opt/homebrew`; Docker Desktop 4.89.0, engine/client 29.7.2; Compose 5.5.0; a successful ARM64 `hello-world` download and execution. The prior VS Code privacy dialog's final choice was not reported.

Pending: actual GRE image build; check-script success on ARM64; Dev Containers installation/editor reopen; Codex availability in the container; image digest recording. Record the results in [the setup checkpoint](00-start-here.md) with the actual commit and observed versions before considering this task complete.

Then establish local PostgreSQL, Temporal, and Azurite, application dependency compatibility/lockfiles, and the initial environment checks needed for backlog planning. These remain setup work. The agreed sequence continues with prioritized backlog and document reconciliation before product feature development.

[VS Code Dev Containers guide](https://code.visualstudio.com/docs/devcontainers/containers) and the [Dev Container specification](https://github.com/devcontainers/spec/blob/main/docs/specs/devcontainerjson-reference.md) define the editor and lifecycle behavior used here.
