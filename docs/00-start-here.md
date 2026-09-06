# Current decisions and setup checkpoint

**Checkpoint date:** September 6, 2026  
**Project:** Global Recovery Engine (working name)  
**Owner/developer:** Vishal  
**Repository:** `vishal-baliga/global-recovery-engine` — private

## Current direction

The user has proceeded from the two-track pilot brief to stack selection and incremental environment setup. Use the pilot brief and stack document as the working baselines for this stage. Their original proposal/version labels are preserved; component compatibility and service configuration remain to be verified during implementation.

The pilot includes domestic U.S. personal/friend loan assistance and India-origin B2B recovery against U.S. businesses. Domestic personal loans are an initial acquisition priority; both journeys remain pilot commitments. Cross-border personal loans and general remittance are future or separate scope, as recorded in the future register.

The agreed sequence is **brief → stack/environment → prioritized backlog → project/delivery document updates → development**. Preparing this repository is environment and context setup. It does not establish a runnable application or a prioritized product backlog.

## How to read the documents

| Files | Current use |
| --- | --- |
| [06 — Pilot MVP brief](06-pilot-mvp-brief.md) | Required pilot outcomes, real-case readiness, and operating/business dependencies |
| [07 — Future register](07-future-development-and-business-deliverables.md) | Preserved future deliverables and scope-change rules |
| [08 — Stack and environment](08-stack-and-environment-decision.md) | Working architecture and proposed runtime targets |
| [01 — Business overview](01-business-project-overview.md), [02 — Product strategy](02-product-offering-competitive-strategy.md) | Earlier business/product baseline; B2B-only and MVP-unselected passages await reconciliation |
| [03 — Operating model](03-operating-model.md), [04 — Workflow](04-workflow-interaction-specification.md), [05 — Domain contracts](05-domain-data-contracts.md) | Domain/reference detail to apply and extend for selected pilot stories |
| [Contract package](../reference/README.md) | Preserved offline schemas, synthetic example, and validator |

This checkpoint resolves historical scope/status conflicts during setup. The two-track pilot and chosen architecture take precedence over older scope/status passages. Preserve applicable evidence, authority, financial, privacy, and outcome principles. Reconcile the original documents substantively at the agreed documentation stage; this import only converts their companion links into repository-relative links.

## Environment status

The initial findings come from the read-only local Codex inspection pasted by Vishal after cloning. That inspection made no file changes or installations. Later user-reported installation results are recorded below. Each observation describes the Mac at the time of its report; repository updates are tracked in Git.

| Item | Evidence/status |
| --- | --- |
| Development machine | MacBook Air M4 (2025), native `arm64`, 16 GiB RAM, macOS 26.6.2 |
| VS Code and Codex | VS Code 1.136.1 and Codex extension present; user reports signed in; `code` command unavailable in the inspected shell |
| ChatGPT GitHub connection | Account and private repository access verified |
| Repository baseline | Project references and Codex guidance committed in `e6dcf64`; later setup findings are incremental documentation updates |
| Clone on the Mac | Present and clean at inspection; `main` tracks `origin/main`; correct remote `vishal-baliga/global-recovery-engine`; local commit `e6dcf64` |
| Git | 2.50.1; live GitHub authentication from the Mac was not tested during the inspection |
| Apple Command Line Tools | Installed and selected; package version 26.6.0.0.1781586589 |
| Homebrew | Installed and verified by user-provided terminal output: 6.0.22, prefix `/opt/homebrew`, `brew doctor` reports “Your system is ready to brew.” |
| Docker | CLI and `/Applications/Docker.app` not found; engine readiness unverified |
| Dev Containers | VS Code extension not found; no repository configuration or CLI present |
| Node/pnpm | Node, npm, pnpm, and Corepack not found on PATH |
| Python/uv | Apple Python 3.9.6 available; Python 3.14 and uv not found on PATH |
| Other CLIs | GitHub, PostgreSQL, Temporal, Azure, Terraform, and Dev Container CLIs not found on PATH; install only when their setup stage requires them |
| Local database, Temporal, Azurite, provider fakes | Not yet established |
| Cloud and service accounts | Azure, Temporal Cloud, Clerk, runtime AI, and integration provisioning not verified; architecture selection alone does not provision them |
| Product build/tests | No application scaffolding, dependency locks, CI pipeline, or executable product acceptance checks yet |

Treat PATH checks as observations of the inspected environment, not proof that a tool cannot exist elsewhere. Update this table with actual results as setup progresses. Use a project-managed Python later; leave the Apple-provided Python in place.

## Next action on the Mac

Install Docker Desktop and the Microsoft Dev Containers extension. Homebrew setup is complete. Docker runs the local Linux containers; Dev Containers connects VS Code to the project's reproducible development environment once its configuration is created.

### 1. Install and start Docker Desktop

Close VS Code for installation and use the macOS Terminal app. Install the [Homebrew Docker Desktop cask](https://formulae.brew.sh/cask/docker-desktop):

```sh
brew install --cask docker-desktop
```

After installation succeeds, launch Docker:

```sh
open -a Docker
```

Complete Docker's first-run setup, review its terms, and select the recommended settings. Enter any requested Mac administrator password directly in the local dialog. Wait for the engine to finish starting before verification. [Docker Desktop installation for Mac](https://docs.docker.com/desktop/setup/install/mac-install/)

### 2. Install the VS Code extension

Reopen VS Code and the GRE folder. Open Extensions (`Cmd+Shift+X`) and install [Dev Containers by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers), extension ID `ms-vscode-remote.remote-containers`. This UI route works even though the `code` shell command is not yet configured. [VS Code Dev Containers setup](https://code.visualstudio.com/docs/devcontainers/containers#_installation)

The extension installation does not create the GRE Dev Container configuration. That repository setup follows the host readiness checks.

### 3. Verify the container runtime

In a fresh terminal, run:

```sh
docker version
docker compose version
docker run --rm hello-world
```

Report the output and confirm the Dev Containers extension is installed. `docker version` should include both client and server details; `hello-world` checks image download and container execution. Its temporary container is removed when it exits. Record actual architecture/version details and any errors. Docker and Dev Containers remain pending until these results are available.

After host readiness is established, configure and verify the project's Dev Container and language toolchains. The Mac has 16 GiB RAM; measure container resource use as the local services are introduced. Keep this stage scoped to environment setup in the agreed delivery sequence.

This checkpoint is updated through GitHub. Before the next local repository edit, inspect Git status and fetch/pull the latest documentation with a fast-forward update when the working tree permits it. Preserve any local changes. The read-only restriction applied to the completed first inspection; subsequent setup follows the user's active instructions and authorization.
