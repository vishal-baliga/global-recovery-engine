# P-001 verification and execution record

**Created:** September 8, 2026. **Updated:** September 8, 2026, P-001.01 local acceptance recorded. **Owner:** Vishal.

**Plan:** [P-001 implementation plan](P-001-development-foundation.md). **Tracking:** [Parent issue #4](https://github.com/vishal-baliga/global-recovery-engine/issues/4).

## Current state

The readiness-document change was reviewed and merged in [PR #14](https://github.com/vishal-baliga/global-recovery-engine/pull/14), merge revision `e8b616c4e6e6c3dc65a87d024a8b5bba3ace0805`. **P-001.01 is implemented on `p001/01-service-health` with local A01/A02 evidence passing and implementation review/merge pending.** The implementation PR and exact tested commit are recorded in [issue #5](https://github.com/vishal-baliga/global-recovery-engine/issues/5). P-001.02 and all later tasks remain unstarted.

Normal health now checks current services independently of retained Temporal history. The optional historical diagnostic reports the original local `NOT_FOUND` as unavailable evidence with unverified cause; it no longer fails an otherwise healthy normal gate. No historical receipt was replaced and no historical persistence PASS is claimed. Readiness and task evidence below retain the earlier failures and their disposition.

Full-sprint readiness is not claimed. Actions minutes/spending limits and actual runner execution remain open for .06; actual artifact downloads are checked at the first dependent build/install. The recorded private-repository enforcement limitation has the plan’s manual-check alternative. Implementation/review availability remains unset.

## G0 local confirmation

| Evidence | Observed value / result |
|---|---|
| Date and executor | September 8, 2026, Codex in the actual Mac-mounted editor container. Prior observations at 21:53, 22:21 and 22:35 UTC are retained; identity and local readiness reconciled after the latest owner handoff on issue #4. |
| Repository remote; branch; HEAD; published planning revision included | `https://github.com/vishal-baliga/global-recovery-engine.git`; initially clean `main`, HEAD and fetched `origin/main` both `ba476b7e1418892378c6710edc159257c0a7d135`. Requested revision already included; no fast-forward necessary. Evidence edits use local branch `docs/p001-g0-readiness-20260908` at the same HEAD. |
| Working-tree state and preservation of local changes | Initial G0 started clean; this continuation began with the existing uncommitted verification record on the readiness branch. All 91 tracked files and five local-data files matched the continuation snapshot after service checks. Only this record is intentionally updated; earlier observations are retained. No reset, clean, stash, install, regeneration or agent service lifecycle command. |
| Repository-local commit identity and GitHub fetch/push availability | Confirmed in the editor: repository-local `user.name=Vishal Baliga`, `user.email=69427695+vishal-baliga@users.noreply.github.com`; both lookups and `git var GIT_AUTHOR_IDENT` exit 0 with that name/address. No global configuration changed. Initial G0 fetch/dry-run push passed; fetch also succeeded before this publication. Actual readiness commit/push/PR evidence follows in GitHub. |
| Session path; OS/architecture; user; actual container identity | `/workspaces/global-recovery-engine`; Debian 12, Linux `7.0.12-linuxkit`, `aarch64`; non-root `vscode`, UID/GID 1000. Container `9b0a594f1f29c28b8d55282ff6b579e6e26fd87ea2275a0e913e0ad612779a0a` verified from hostname and Docker mount metadata. Virtiofs source identifies `diztort/GRE Development/global-recovery-engine`; Docker marker and ARM64 VS Code server present. VS Code 1.136.2, build `88e44fa0e00b08f7758b4f6d05632e4fd5e4df6f`. Docker CLI/socket and `gh` absent in editor. |
| Existing toolchain check: command and exit | `timeout --signal=TERM --kill-after=5s 60s python .devcontainer/check_environment.py --expect-arch arm64` → 0. Python 3.14.7, Node 24.20.0, pnpm 11.10.0, uv 0.12.10; Git 2.39.5, npm 11.19.0. Temporary venv/SSL/SQLite, pnpm execution and workspace write checks passed; no application dependency installation. |
| Existing read-only service checks: exact interpreter/command, outer timeout, exit and redacted result | `timeout --signal=TERM --kill-after=5s 45s .venv/bin/python -B -m scripts.check_services` → 1 on continuation: PostgreSQL 18.6 read-only/Alembic revision read and authenticated Azurite API 2025-11-05 pass; historical Temporal `handle.describe()` raises RPC status 5 / `NOT_FOUND`. Outer deadline 45 seconds plus 5-second kill allowance; timeout not reached. Initial DNS failure is retained below as earlier evidence, now superseded for current connectivity. No aggregate PASS. |
| Independent current connectivity if historical Temporal lookup fails | `timeout --signal=TERM --kill-after=5s 30s .venv/bin/python -B /tmp/gre-p001-g0-temporal-6fgnthaw/temporal-current.py` → 0 at 22:21:53 UTC and again at 22:35:36 UTC, using installed SDK 1.32.0. Current gRPC health true; `DescribeNamespace(default)` succeeds with exact name `default` and state `NAMESPACE_STATE_REGISTERED`. Each RPC has a 5-second timeout in addition to the outer deadline. No workflow/receipt lookup in this probe; full source and outcome below. |
| Git/lock and receipt snapshots; attachment versus lifecycle refresh | Continuation snapshot `/tmp/gre-p001-g0-temporal-6fgnthaw/before.json` includes existing uncommitted work and five local-data files. All three receipts match both continuation and initial G0 hashes below; all five locks unchanged. Vishal reports starting existing services in Docker Desktop. No agent attach/start/restart/status/probe recreation; no local `server.json` refresh. Stored lifecycle timestamps were not reverified against current host state. |
| Docker memory/free disk and required download connectivity | Owner-supplied Mac Terminal evidence, reconciled on issue #4: Docker `aarch64`, 10 CPUs, `MemoryBytes=8319504384` (about 7.75 GiB), checkout filesystem 146 GiB available. `docker system df` showed existing images, four local volumes and build cache. Host memory/free-disk confirmation is satisfied. Earlier editor endpoint reachability is retained; actual artifact downloads/host pulls remain untested until the first dependent build/install. |
| Actions policy/ARM64 eligibility; available minutes/existing limit; required-check administration | GitHub API: private personal repository, account plan `free`; Actions enabled, all actions allowed, SHA pinning not required by policy; default workflow permission `read`, PR approval disabled; zero workflows. Admin access verified, but protection/ruleset APIs return 403 requiring Pro or public visibility. Preserve privacy/current plan and document manual merge-gate enforcement per the plan. GitHub documents native `ubuntu-24.04-arm` for private repositories; actual execution remains .06. Billing endpoints return 404: available minutes and existing spending/stop limits unverified. |
| Available implementation/review time and any agreed sprint window | Unset; no duration commitment |
| Blocker, affected task, owner and next resolution step | No remaining local prerequisite blocks P-001.01. Publish this existing readiness draft, then implement only .01 on its own branch under the owner’s instruction. Carry historical Temporal `NOT_FOUND`; preserve its receipt. Vishal owns Actions minutes/spending/stop limits before .06, actual artifact-download evidence at first dependent build/install and any implementation/review availability. The private Free-plan enforcement limitation uses the plan’s manual current-candidate check alternative. |
| Vishal's instruction to begin P-001.01 | Authorized in the latest owner handoff and current request, after readiness publication. Stop before P-001.02. |


Parent issue observation: [G0 inspection — September 8, 2026](https://github.com/vishal-baliga/global-recovery-engine/issues/4#issuecomment-5592461046), published successfully (HTTP 201; posting command exit 0). The issue remains open and implementation tasks remain unstarted.

### G0 command and preservation evidence

The initial sandbox invocation failed before command execution with `bwrap` namespace creation denied (exit 1). Subsequent checks used approved execution outside the unavailable sandbox, still as non-root `vscode`. An interrupted inspection batch yielded no usable results and was rerun; no pass is inferred from it. The patch helper encountered the same sandbox failure, so this record was written through approved shell execution.

| Command / inspection | Exit / observation |
|---|---|
| `git status --short --branch`, `git branch --show-current`, `git remote -v` | 0; clean `main`, expected origin |
| `git fetch origin` | 0 |
| `git rev-parse main origin/main`; `git merge-base --is-ancestor ba476b7e1418892378c6710edc159257c0a7d135 main` | 0 each; requested revision included |
| `timeout --signal=TERM --kill-after=5s 30s git push --dry-run origin HEAD:refs/heads/g0-access-check-ba476b7` | 0; receive negotiation succeeds; no remote ref created |
| `git config --local --get user.name`; `git config --local --get user.email`; `git var GIT_AUTHOR_IDENT` | 1, 1, 128; identity unset; config unchanged |
| `uname -srm`, `id`, `hostname`, selected OS/mount reads; `code --version` | 0; actual session values above |
| `.venv/bin/python -B -` with `importlib.metadata`, TOML lock and installed `package.json` inspection | 0; ten inspected Python distributions match `uv.lock`; nine external JS workspace dependencies match exact manifests. Metadata inspection is not a fresh-install/build check. |
| `df -h /workspaces/global-recovery-engine /`; selected `/proc/meminfo` and cgroup reads | 0; container-only observations above |
| `curl --head --location --silent --show-error --connect-timeout 5 --max-time 15 --output /dev/null --write-out '%{http_code}' URL` | Every process 0. Docker registry `/v2/`: 401; GHCR: 405; MCR: 200; PyPI `uv-build/0.12.10`, Python files host, npm `pnpm/11.10.0` and `@hey-api/openapi-ts/0.99.0`, Debian Bookworm/security release endpoints: 200; Playwright CDN root: 400. |
| `curl --silent --show-error --connect-timeout 5 --max-time 15 --output /dev/null --write-out 'ghcr.io GET HTTP %{http_code}\n' https://ghcr.io/v2/` | 0, HTTP 401; GET resolves HEAD-method limitation. Registry challenges and CDN root response establish reachability only. |
| Authenticated GitHub GET audit using existing Git credential in memory and no redirects | Audit process 0; endpoint HTTP results below. Credential neither printed nor stored. |
| SHA-256 comparison before recording results | 0; all 91 tracked files and three receipts unchanged |
| `git switch -c docs/p001-g0-readiness-20260908` | 0; documentation branch at tested HEAD |
| `git diff --check`; final SHA-256 and Markdown table audit | 0; only this record changed, all locks/receipts unchanged. A line-format error found by the first table audit was corrected before the passing rerun. |

Installed Python versions inspected: FastAPI 0.141.1, Pydantic 2.13.5, SQLAlchemy 2.0.52, Psycopg and Psycopg binary 3.3.5, Alembic 1.19.2, Temporal SDK 1.32.0, Azure Blob 12.30.1, Uvicorn 0.52.4 and HTTPX 0.28.1. JS: Next 16.3.4, React/React DOM 19.2.8, TypeScript **6.0.3**, Hey API 0.99.0, tsx 4.23.13, Node types 24.13.3, React types 19.2.18 and React DOM types 19.2.7. `uv-build`, Ruff, Pyright and pytest are absent from the existing project environment; installation/compatibility remains in their owning implementation tasks. No tools were installed for G0.

During the initial DNS failure, the independent service command was the following stdin probe, with a 40-second outer deadline plus 5-second termination allowance. It exited 1 in under one second:

```sh
timeout --signal=TERM --kill-after=5s 40s .venv/bin/python -B - <<'PROBE'
import asyncio, socket
from datetime import timedelta
from temporalio.client import Client
from temporalio.api.workflowservice.v1 import DescribeNamespaceRequest
async def main():
    failures=0
    for host,port in [('gre-postgres',5432),('gre-temporal',7233),('gre-azurite',10000)]:
        try:
            socket.getaddrinfo(host,port,type=socket.SOCK_STREAM)
            with socket.create_connection((host,port),timeout=5): pass
            print(f'{host}:{port}: DNS and TCP PASS',flush=True)
        except OSError as e:
            failures+=1
            print(f'{host}:{port}: FAIL {type(e).__name__} errno={e.errno}',flush=True)
    try:
        client=await Client.connect('gre-temporal:7233', namespace='default')
        health=await client.service_client.check_health(timeout=timedelta(seconds=5))
        info=await client.workflow_service.describe_namespace(DescribeNamespaceRequest(namespace='default'),timeout=timedelta(seconds=5))
        ok=health and info.namespace_info.name=='default'
        print(f'Independent current Temporal health and default namespace: {"PASS" if ok else "FAIL"}',flush=True)
        failures+=not ok
    except Exception as e:
        failures+=1
        print(f'Independent current Temporal: FAIL {type(e).__name__}; historical receipt not consulted',flush=True)
    return 1 if failures else 0
raise SystemExit(asyncio.run(main()))
PROBE
```

Receipt SHA-256 values before and after readiness checks:

| Ignored receipt | Unchanged SHA-256 |
|---|---|
| `local-data/azurite/server.json` | `10c18640f0486c3b6f457add30d99d4bc7ab221bb2381a28ff13deb8d4d26b28` |
| `local-data/temporal/server.json` | `be54703124b3872dc866c2ccb7217ff4d764f123da59cc99993cee37a6b22390` |
| `local-data/temporal/workflow-probe.json` | `1c672b23879961c7bd340daeed862096a0b82e9a56133c294fc5694d982c27d5` |

Both application locks and all three isolated probe locks were unchanged. Application lock SHA-256: `uv.lock` = `a7af8cf6374e8f26130b583117d6e394785252c6fedb3b66e57752603a6ccdde`; `pnpm-lock.yaml` = `6173190f52dbac510bf9b04940cb11794878331c4c71b4586063d120865e4b49`. Local audit metadata remains under `/tmp/gre-p001-g0-lu91sn9j/`; it is temporary supporting evidence, not a portable repository artifact.

GitHub GET results (repository prefix `/repos/vishal-baliga/global-recovery-engine`): `/user`, repository metadata, `/actions/permissions`, `/actions/permissions/workflow`, `/actions/workflows` and `/issues/4` returned 200. `/branches/main/protection` and `/rulesets` returned 403 with the explicit private-repository plan restriction. `/users/vishal-baliga/settings/billing/actions` and `/users/vishal-baliga/settings/billing/usage` returned 404; this does not mean zero usage or unlimited capacity. [GitHub's runner table](https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job) lists `ubuntu-24.04-arm` for private repositories; this is documented eligibility, not proof of account capacity or a successful job.

### Initial host handoff (service startup/attachment now superseded)

The following Mac Terminal commands were supplied during the initial DNS failure and are retained as handoff history. Vishal subsequently reported starting the existing services through Docker Desktop; current service connectivity is now verified. Host resource/identity inspection remains outstanding, but no additional service startup or attachment is requested:

```sh
cd "/Users/diztort/GRE Development/global-recovery-engine"
docker inspect 9b0a594f1f29 --format 'ID={{.Id}} Running={{.State.Running}} Networks={{range $name, $network := .NetworkSettings.Networks}}{{$name}} {{end}}{{range .Mounts}}{{if eq .Destination "/workspaces/global-recovery-engine"}} Workspace={{.Source}}{{end}}{{end}}'
docker ps --format 'table {{.ID}}\t{{.Names}}\t{{.Status}}'
docker info --format 'Architecture={{.Architecture}} CPUs={{.NCPU}} MemoryBytes={{.MemTotal}}'
df -h .
docker system df
git var GIT_AUTHOR_IDENT
```

Initial attachment commands supplied for already running services (historical handoff, not a current action):

```sh
bash .devcontainer/postgres-host.sh attach 9b0a594f1f29
bash .devcontainer/temporal-host.sh attach 9b0a594f1f29
bash .devcontainer/azurite-host.sh attach 9b0a594f1f29
```

The existing helpers verify the checkout mount and attach only if necessary; they do not refresh receipts. If a service is stopped/missing, record that host observation before selecting its documented `up` command. Temporal/Azurite `status/up` refresh `server.json`, so they were not used as inspection commands. Preserve the original workflow receipt and document any necessary lifecycle refresh separately.

The requested bounded service follow-up is completed below. Vishal still needs to confirm remaining Actions minutes and current budget/stop settings in [account billing](https://github.com/settings/billing), establish intended repository-local commit identity, provide host Docker resource/download evidence and any implementation/review availability. No paid increase or visibility change is proposed. Full sprint readiness and authorization to start .01 remain unset.

### G0 continuation — current Temporal verified, historical lookup carried into .01

Parent update: [observed G0 continuation](https://github.com/vishal-baliga/global-recovery-engine/issues/4#issuecomment-5592704373) (HTTP 201, posting command exit 0).

**Observed:** September 8, 2026, 22:21 UTC. Same readiness branch, HEAD `ba476b7e1418892378c6710edc159257c0a7d135`, installed Python 3.14.7 / Temporal SDK 1.32.0 and ARM64 editor `9b0a594f1f29`. The existing uncommitted report was snapshotted and preserved before updating it. Vishal reported starting the three existing services through Docker Desktop; no service lifecycle command was executed by Codex.

| Check | Exact command and result |
|---|---|
| Independent current Temporal | `timeout --signal=TERM --kill-after=5s 30s .venv/bin/python -B /tmp/gre-p001-g0-temporal-6fgnthaw/temporal-current.py` — exit **0**, under one second. Current gRPC health and access to registered namespace `default` passed. No historical workflow/receipt access in this probe. |
| Existing aggregate baseline | `timeout --signal=TERM --kill-after=5s 45s .venv/bin/python -B -m scripts.check_services` — exit **1**, without reaching the outer timeout. PostgreSQL 18.6 authenticated read-only transaction/Alembic revision read `()` passed; Azurite authenticated API 2025-11-05 properties/listing passed (zero containers). Only the historical Temporal describe failed, with RPC status 5 / `NOT_FOUND`. |
| Commit identity | `git config --local --get user.name`; `git config --local --get user.email`; `git var GIT_AUTHOR_IDENT` — exits **1, 1, 128**; still unset, unchanged. |
| Preservation after baseline process exit | SHA-256 audit — exit **0**; all 91 tracked files including the prior uncommitted record, all five locks and all five local-data files unchanged. Three receipt hashes also match the initial G0 hash table. |

The independent probe calls only current service health and `DescribeNamespace`; connecting with a namespace alone was not treated as proof of namespace access. It runs under the external process deadline (30 seconds, TERM then KILL after 5 seconds), with additional 5-second RPC timeouts. Its exact temporary audit source is preserved here; no runtime script or dependency was added to the repository:

```python
import asyncio
from datetime import datetime, timedelta, timezone
from importlib.metadata import version
from temporalio.api.enums.v1 import NamespaceState
from temporalio.api.workflowservice.v1 import DescribeNamespaceRequest
from temporalio.client import Client
from temporalio.service import RPCError

async def main():
    print("UTC:", datetime.now(timezone.utc).isoformat(), flush=True)
    print("Installed Temporal SDK:", version("temporalio"), flush=True)
    client = await Client.connect("gre-temporal:7233", namespace="default")
    healthy = await client.service_client.check_health(timeout=timedelta(seconds=5))
    if not healthy:
        raise RuntimeError("Current service health is false")
    print("PASS current Temporal gRPC service health", flush=True)
    info = await client.workflow_service.describe_namespace(
        DescribeNamespaceRequest(namespace="default"),
        timeout=timedelta(seconds=5),
    )
    if info.namespace_info.name != "default":
        raise RuntimeError("Unexpected namespace")
    state = NamespaceState.Name(info.namespace_info.state)
    if state != "NAMESPACE_STATE_REGISTERED":
        raise RuntimeError("Namespace is not registered")
    print("PASS namespace default: accessible, " + state, flush=True)
    print("No workflow or historical receipt lookup performed", flush=True)

try:
    asyncio.run(main())
except RPCError as error:
    print("FAIL current Temporal RPC:", error.status.name, flush=True)
    raise SystemExit(1)
except Exception as error:
    print("FAIL current Temporal:", type(error).__name__, flush=True)
    raise SystemExit(1)
```

The separate existing aggregate reads the original workflow/run identifiers and fails in `scripts/check_services.py` at `await handle.describe()`. This confirms historical evidence is presently unavailable, while independently established current health remains valid. **Disposition: carry this baseline lookup failure into P-001.01 as plan section 6.5 permits.** Retention or deletion is a possible explanation, not a proven cause. Historical persistence was not reverified, no replacement probe was created, and the existing aggregate is still recorded as failing. P-001.01/A01–A02 remain unimplemented and unpassed.

Remaining G0 items are unchanged except that current service connectivity is resolved: intended repository-local author identity; actual host Docker allocation/free-disk and host download evidence; Actions available minutes and existing budget/stop limits (initial API inspection returned 404); the recorded private Free-plan required-check administration limitation; implementation/review availability and Vishal’s instruction to begin .01. No billing or host prerequisite is inferred from healthy services. No further service restart/attachment is required for this observed result.

### G0 repeat observation — 22:35 UTC

Repeat current-health observation — September 8, 2026, 22:35:36 UTC.

At the user's renewed request, the same installed-SDK independent command was rerun:

`timeout --signal=TERM --kill-after=5s 30s .venv/bin/python -B /tmp/gre-p001-g0-temporal-6fgnthaw/temporal-current.py`

Exit **0**, under one second, using Temporal SDK 1.32.0. Current gRPC health passed; `DescribeNamespace(default)` again returned accessible namespace `default` in `NAMESPACE_STATE_REGISTERED`. The probe performed no workflow or historical receipt lookup. The hard external deadline remains 30 seconds plus a 5-second kill allowance, with additional 5-second RPC timeouts.

Local `user.name` and `user.email` remain unset (exit **1** each); effective `git var GIT_AUTHOR_IDENT` still exits **128**. Before/after hashes confirm all tracked files (including the existing uncommitted record), five locks and five local-data files were unchanged through the check. Only the verification record was subsequently updated. Snapshot/result metadata: `/tmp/gre-p001-g0-refresh-xqizdde8/`.

The 22:21 PostgreSQL/Azurite PASS and separate historical `NOT_FOUND` observations remain the preceding evidence; that aggregate was not rerun for this refresh. The historical failure remains carried into P-001.01 under section 6.5. No persistence PASS or proven retention cause is claimed, and .01 remains unstarted.

Remaining G0 items are unchanged: intended repository-local commit identity; host Docker resource/download evidence; Actions remaining minutes and current spending/stop limits (unavailable from the initial API inspection); the recorded required-check enforcement limitation; implementation/review availability and an instruction to begin .01. No service lifecycle action, probe recreation, dependency installation or runtime edit occurred.

### Final local readiness reconciliation — September 8, 2026

The [latest reconciliation and local handoff on issue #4](https://github.com/vishal-baliga/global-recovery-engine/issues/4#issuecomment-5592704373) incorporates the previously supplied Mac Terminal evidence: Docker native `aarch64`, 10 CPUs, 8,319,504,384 bytes of memory and 146 GiB available on the checkout filesystem. `docker system df` reported existing images, four local volumes and build cache. Services were stopped at that host inspection and were subsequently started by Vishal through Docker Desktop; the already recorded current service/namespace results are the relevant connectivity evidence. A host resource observation is not a new registry-pull/build result.

In this editor, `git config --local --get user.name`, `git config --local --get user.email` and `git var GIT_AUTHOR_IDENT` each exited **0**, confirming `Vishal Baliga <69427695+vishal-baliga@users.noreply.github.com>`. This supersedes earlier unset-identity observations. `git fetch origin` exited **0**; remote `main` still includes the exact published planning revision. No toolchain or service check was repeated merely for a new timestamp. Existing readiness work was preserved before this edit; data, locks and receipts remain unchanged.

**Disposition: local readiness for P-001.01 is confirmed, with the owner’s instruction to implement after this documentation is safely published.** Its historical `NOT_FOUND` is an accepted carried defect for .01, not a passing historical persistence test. Required artifact-download proof remains at the first build/install that depends on it. Actions available minutes/spending/stop limits and actual runner execution remain open for .06. Required-check administration is a recorded limitation with a manual review/check alternative, not an unrecorded waiver. Sprint availability remains explicitly unset. Full-sprint or product readiness is not claimed.

Publication uses this existing readiness branch and only this document. Before .06 supplies CI, the plan requires actual affected checks and diff review: readiness validation comprises `git diff --check`, relative-document-link checks, Markdown table structure, confirmation of the source issue reconciliation and a SHA-256 preservation audit. Runtime source, locks, original reference bytes and local data are unchanged. GitHub PR history records the reviewed publication and merge; no implementation task is completed by this documentation PR.

## Task evidence

Issue state tracks progress. Add one entry per task with its PR and tested revision; do not paste credentials, whole terminal environments or private files.

| Task | Implementation PR / commit | Acceptance evidence | Remaining limits |
|---|---|---|---|
| [P-001.01](https://github.com/vishal-baliga/global-recovery-engine/issues/5) | Implemented on `p001/01-service-health`; exact PR/commit in issue #5; review/merge pending | A01–A02 local PASS: 26 unit tests, existing live services/historical diagnostic, and affected combined setup command | Historical evidence unavailable; no persistence reverification. No CI yet; generation remains mutating until later codegen work. |
| [P-001.02](https://github.com/vishal-baliga/global-recovery-engine/issues/6) | Not started | A03–A04 pending | — |
| [P-001.03](https://github.com/vishal-baliga/global-recovery-engine/issues/7) | Not started | A05–A06 pending | — |
| [P-001.04](https://github.com/vishal-baliga/global-recovery-engine/issues/8) | Not started | A06–A08 pending | — |
| [P-001.05](https://github.com/vishal-baliga/global-recovery-engine/issues/9) | Not started | A03, A09–A10 pending | — |
| [P-001.06](https://github.com/vishal-baliga/global-recovery-engine/issues/10) | Not started | A11 pending | G0 checks policy/capacity; actual runner/gate proof pending |
| [P-001.07](https://github.com/vishal-baliga/global-recovery-engine/issues/11) | Not started | A08, A10–A12 and parent closeout pending | — |

For each executed check record: exact command, date, code/lock revision, environment/architecture, exit code, observed behavior, redacted log/run link and whether it used live local or disposable services. For CI also record event, PR head/base, tested checkout SHA, actual check name and elapsed time. Include failed/stuck-check and handled-cancellation evidence where required. Keep known regressions/blockers visible and update evidence with each task PR. A repeated focused check is supporting evidence, not an extra suite count. Report a cached fresh install accurately.

### P-001.01 acceptance — September 8, 2026

**Owner/implementer:** Vishal / local Codex. **Base:** merged readiness revision `e8b616c4e6e6c3dc65a87d024a8b5bba3ace0805`. **Environment:** existing non-root `vscode` ARM64 editor `9b0a594f1f29`, Python 3.14.7, installed Temporal SDK 1.32.0; runtime pins and locks unchanged. Tests ran on the proposed implementation tree; the exact published commit/PR is linked in issue #5, with preserved source hashes at `/tmp/gre-p001-01/tested-source.json`. A documentation commit does not establish its own acceptance SHA.

Implemented section 3.3 without changing product scope: strict complete JSON configuration and secret-file loading; current service/namespace health separate from optional historical inspection; exact typed historical `NOT_FOUND` classification; common process-group supervision in `scripts/_process.py` for standalone and aggregate callers; receipt comparison even after failures, timeout and handled termination. The aggregate forwards the same options, preserves its setup coverage and bounds its remaining phases. Its existing generation still writes artifacts, so compatibility validation used an owned temporary copy.

| Command / evidence | Exit / observed result |
|---|---|
| `timeout --signal=TERM --kill-after=5s 90s .venv/bin/python -B -m unittest discover -s tests -p test_check_services.py -v` | **0**; final 26 tests passed in 12.378 seconds. Standard-library tests with synthetic temporary files/fake SDK responses/owned subprocesses; no live service writes. |
| `timeout --signal=TERM --kill-after=5s 45s .venv/bin/python -B -m scripts.check_services --inspect-historical-temporal --timeout 30` | **0**; actual PostgreSQL 18.6 authenticated read-only/Alembic revision read, Azurite API 2025-11-05 authenticated properties/listing, and current Temporal service/configured-namespace health passed. Original historical describe returned typed `NOT_FOUND`, reported separately as unavailable evidence with cause unverified. Receipt comparison passed. |
| `timeout --signal=TERM --kill-after=5s 600s .venv/bin/python -B -m scripts.check_environment --config service-config.json --timeout 30` from `/tmp/gre-p001-01-setup-u4tpsptl` | **0** after correcting the temporary dependency layout. Complete explicit-config service check, FastAPI valid/invalid request checks, OpenAPI export, Hey API 0.99.0 generation, both workspace type checks, real generated-client HTTP 200/422 and Next 16.3.4 production fixture build passed. Source matched the working implementation; installed dependencies were reused, not reinstalled. |
| First run of that temporary aggregate | **1** at Next build: Turbopack rejected `fixtures/web/node_modules` pointing outside its root. Earlier phases passed. Copied the existing installed root/fixture dependency directories inside the owned copy, preserving relative package links; no runtime/pin change. A temporary copy helper also initially expected an absent client-package `node_modules` directory; it was corrected to copy only existing installed directories. The complete aggregate was then rerun successfully. |
| Post-run preservation/generated-byte audit | **0**; temporary generated schema/client bytes equal the working baseline. All five locks, isolated probes, reference artifacts and five developer local-data files unchanged; original three receipt hashes still match G0. Removed only the temporary raw-key copy created for the explicit-config check. |
| `git diff --check`, changed-document link/table checks and manual diff review | PASS before publication; final exact-head review evidence is in the implementation PR/issue #5. No unrelated source, secret or reference changes. |

A01 tests cover strict default/explicit configuration, missing/unknown/duplicate/malformed fields, relative/absolute/unreadable secret files, secret-free CLI/SDK error output, actual configured namespace access and true health failures. Stuck subprocesses deliberately ignore TERM; the shared boundary kills/reaps them within the deadline plus the cleanup allowance, preserves an unrelated process, and runs the receipt comparison on failure/timeout. Aggregate tests prove option forwarding, the same real service boundary, no continuation after service failure, and propagation of a failed setup subprocess. Handled TERM also cleans its worker, compares receipts and exits 143.

A02 tests cover absent, valid completed, typed not-found, malformed, denied, timeout/other-RPC and mismatched-status/run historical outcomes; message text containing `NOT_FOUND` is not accepted as typed not-found. Normal health does not parse/describe the historical receipt. Synthetic receipt-change failures are detected in owned test directories; no synthetic historical receipt was substituted into developer data. The live original receipt remained byte-for-byte unchanged.

**Limitations and remaining work:** These are local service/setup foundation checks, not product behavior, historical durability, a new image/fresh install or CI execution. The setup aggregate still regenerates artifacts; its non-mutating generation change remains in .03/.04. No dependencies or tools were installed. Actual artifact-download proof remains with the first dependent build/install. Actions capacity/runner proof and the recorded enforcement limitation remain for .06. P-001.01 remains open pending implementation PR review/merge; P-001.02 has not started. Final full-P-001 Mac/CI proof and parent closeout remain .07/issue #11 work.

## Final P-001 closeout

| Required result | Evidence |
|---|---|
| A01–A12 satisfied against the intended implementation | Pending |
| Final implementation revision and all task PRs | Pending |
| Actual Mac ARM64 package/service/setup checks | Pending |
| Final merged-main SHA; matching Mac checks and push-to-main `GRE / foundation` run | Pending; final post-merge observations are recorded in issue #11 as explained below |
| Required-check enforcement or explicit administrative limitation | Pending |
| Resolved new check/build dependencies; existing runtime pins preserved or justified | Pending |
| Registry/digest/architecture record; developer data and receipts preserved | Pending |
| Original reference ZIP SHA-256 | Expected `14d24f856ade2c0b508a208d32a98c14a37723f4708b43c82f58213396bfaf72`; final verification pending |
| Actual commands/layout/limitations reflected in documents 00/09/10/11 | Pending |
| Parent issue closed with evidence; P-004 handoff; P-002/P-003 actual status | Pending |

The .07 PR records the pre-merge summaries and pending final check here. It must not auto-close #11/#4. After it merges, [issue #11](https://github.com/vishal-baliga/global-recovery-engine/issues/11) owns the **Final post-merge result**: actual merged SHA, Mac commands/exits, push-to-main CI URL/result and remaining blockers. That stable linked result completes this record without a commit trying to contain its own SHA. Close .07/#4 only after that result passes; any code/config/lock correction requires fresh evidence for the corrected revision. Never infer success merely from issue closure.

A plan or merged planning PR must never fill these cells with PASS. Record failures and corrective work; leave unresolved required evidence pending.
