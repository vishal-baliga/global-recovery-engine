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
| [09 — Development environment](09-development-environment.md) | Initial container configuration, exact toolchain pins, and Mac verification task |
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
| Clone on the Mac | Fetched origin successfully; clean working tree safely switched to `setup/devcontainer`, tracking `origin/setup/devcontainer` at `445db9a` before local setup fixes. Correct remote `vishal-baliga/global-recovery-engine`. |
| Git | 2.50.1; authenticated fetch from the private GitHub origin succeeded on the Mac. |
| Apple Command Line Tools | Installed and selected; package version 26.6.0.0.1781586589 |
| Homebrew | Installed and verified by user-provided terminal output: 6.0.22, prefix `/opt/homebrew`, `brew doctor` reports “Your system is ready to brew.” |
| Docker | User output verifies Desktop 4.89.0 (238018), client/engine 29.7.2, client `darwin/arm64`, server `linux/arm64`, context `desktop-linux`; Compose 5.5.0. ARM64 `hello-world` image download and container execution succeeded; user supplied the complete “Hello from Docker!” output. |
| Dev Containers | Microsoft `ms-vscode-remote.remote-containers` 0.466.0 confirmed installed through the VS Code CLI. GRE image build and offline ARM64 check passed; editor reopen remains pending. |
| Node/pnpm | Absent from the host PATH at the initial inspection. Container Node 24.20.0 and pnpm 11.10.0 built and verified on ARM64. |
| Python/uv | Apple Python 3.9.6 remains on the host. Container Python 3.14.7 and uv 0.12.10 built and verified on ARM64. |
| Other CLIs | GitHub, PostgreSQL, Temporal, Azure, Terraform, and Dev Container CLIs not found on PATH; install only when their setup stage requires them |
| Local database, Temporal, Azurite, provider fakes | Not yet established |
| Cloud and service accounts | Azure, Temporal Cloud, Clerk, runtime AI, and integration provisioning not verified; architecture selection alone does not provision them |
| Product build/tests | No application scaffolding, dependency locks, CI pipeline, or executable product acceptance checks yet |

Treat PATH checks as observations of the inspected environment, not proof that a tool cannot exist elsewhere. Update this table with actual results as setup progresses. Use a project-managed Python later; leave the Apple-provided Python in place.

## Next action on the Mac

Reopen this checkout in VS Code using **Dev Containers: Reopen in Container**. Microsoft Dev Containers 0.466.0 is installed. The image built successfully on the Mac's Docker Desktop engine 29.7.2 (`linux/arm64`) from branch baseline `445db9a`, and the corrected check ended with `GRE development toolchain: PASS (linux/arm64)` with networking disabled.

The check initially rejected pnpm's successful execution because automatic dependency preflight and update notices added stdout. The temporary check project now disables those behaviors; all exact version, non-root, architecture, workspace-write, Python virtual-environment/SSL/SQLite, and pnpm execution checks passed. No runtime pins changed. See [the development-environment guide](09-development-environment.md) for commands and image digests.

The actual VS Code container session and Codex availability still need confirmation after reopening. The image smoke check does not establish editor readiness. No product features or application dependencies were added.

Following editor confirmation, establish local PostgreSQL, Temporal, Azurite, application dependency compatibility/lockfiles, and the required environment checks. These remain setup work, followed by backlog prioritization and document reconciliation.
