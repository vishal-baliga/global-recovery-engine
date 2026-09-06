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

| Item | Evidence/status |
| --- | --- |
| Development machine | User reports MacBook Air M4, 2025; macOS version and memory not yet checked |
| VS Code and Codex | User reports extension installed and signed in |
| ChatGPT GitHub connection | Account and private repository access verified |
| Repository baseline | Project references, README, agent instructions, and this checkpoint prepared for the initial setup commit |
| Clone on the Mac | Not yet verified; this is the next step |
| Git, Apple command-line tools, Homebrew, Docker | Presence and versions on the Mac not yet verified |
| Node/pnpm, Python/uv, Dev Container | Not yet verified or version-locked |
| Local database, Temporal, Azurite, provider fakes | Not yet established |
| Cloud and service accounts | Azure, Temporal Cloud, Clerk, runtime AI, and integration provisioning not verified; architecture selection alone does not provision them |
| Product build/tests | No application scaffolding, dependency locks, CI pipeline, or executable product acceptance checks yet |

Treat these as observations, not a claim that an unverified tool is absent. Update this table with actual results as setup progresses.

## Next action on the Mac

In VS Code, use the Command Palette (`Cmd+Shift+P`) → **Git: Clone**, enter `https://github.com/vishal-baliga/global-recovery-engine.git`, choose a parent folder such as `~/Developer`, and open the resulting project folder. Complete GitHub sign-in if VS Code requests it. If Git is missing, resolve that prerequisite before retrying. [VS Code cloning instructions](https://code.visualstudio.com/docs/sourcecontrol/quickstart#_option-a-clone-a-repository-locally)

Once open, start a Codex conversation in that folder with:

> Read AGENTS.md and docs/00-start-here.md, then the pilot brief and stack decision. We are setting up GRE incrementally on my MacBook Air M4. Inspect the local repository and development tools, report what is present or missing, and recommend the next setup step. Keep this first check read-only; do not install tools or begin application implementation yet.

The inspection should establish the OS/architecture and memory, Git/remote/working-tree state, and availability of command-line tools, Homebrew, Docker, Node/pnpm, and Python/uv. Report versions and readiness only; do not print environment secrets or credential-file contents. An installed Docker client does not by itself establish that its engine is running.

The repo carries the durable project context for the VS Code agent. After this initial check, resolve the missing prerequisites incrementally, establish and verify the reproducible environment, then use those decisions to prioritize the backlog.
