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
| Docker | User output verifies Desktop 4.89.0 (238018), client/engine 29.7.2, client `darwin/arm64`, server `linux/arm64`, context `desktop-linux`; Compose 5.5.0. Image download and `hello-world` execution not yet confirmed. |
| Dev Containers | Not found during the initial inspection; installation confirmation still pending. No GRE Dev Container configuration established yet. |
| Node/pnpm | Node, npm, pnpm, and Corepack not found on PATH |
| Python/uv | Apple Python 3.9.6 available; Python 3.14 and uv not found on PATH |
| Other CLIs | GitHub, PostgreSQL, Temporal, Azure, Terraform, and Dev Container CLIs not found on PATH; install only when their setup stage requires them |
| Local database, Temporal, Azurite, provider fakes | Not yet established |
| Cloud and service accounts | Azure, Temporal Cloud, Clerk, runtime AI, and integration provisioning not verified; architecture selection alone does not provision them |
| Product build/tests | No application scaffolding, dependency locks, CI pipeline, or executable product acceptance checks yet |

Treat PATH checks as observations of the inspected environment, not proof that a tool cannot exist elsewhere. Update this table with actual results as setup progresses. Use a project-managed Python later; leave the Apple-provided Python in place.

## Next action on the Mac

Finish the Docker smoke check and confirm the Microsoft Dev Containers extension. Docker client/server connectivity and native ARM64 execution architecture are verified; this is not yet evidence of a successful container run.

### Resolve the permission prompt and collect the remaining output

The user shared a macOS dialog asking whether Visual Studio Code may access data from other apps. The screenshot does not identify the target app/container or the triggering VS Code process, terminal command, or extension. Apple describes this permission as protecting another developer's application data container. [Apple privacy explanation](https://developer.apple.com/videos/play/wwdc2023/10053/)

The recommendation is to choose **Don't Allow for now**, then observe the current command's result. No evidence yet establishes that this access is required for the GRE setup. The user's actual choice has not been reported. If an access error occurs, diagnose the specific operation and requested resource before changing permissions.

The last supplied Docker line was:

```text
Unable to find image 'hello-world:latest' locally
```

This line alone is normal on a first run: the default image policy initiates a download when an image is absent locally. It does not establish that the download or execution completed. [Docker image pull policy](https://docs.docker.com/reference/cli/docker/container/run/#set-the-pull-policy---pull)

Let the existing command finish and supply the remaining output. Success includes **Hello from Docker!**; an error should be recorded exactly. If the original command has already ended and no complete result is available, retry once in the same VS Code terminal:

```sh
docker run --rm hello-world
```

### Confirm the editor extension

In VS Code Extensions, confirm that [Dev Containers by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers), ID `ms-vscode-remote.remote-containers`, is installed. Install it if still absent. The `code` shell command remains unverified, so use the Extensions UI.

After these results, configure and verify the GRE Dev Container and language toolchains. The shell prompt shows a directory named `GRE Development`; inspect `git rev-parse --show-toplevel` before repository edits rather than inferring the repository root from the prompt. Docker's smoke command itself may run from any directory.

Before local repository edits, inspect Git status and bring in the latest GitHub documentation with a fast-forward update when the working tree permits it. Preserve local changes. The first inspection's read-only scope does not prohibit later setup already authorized by the user.
