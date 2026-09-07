# GRE reference contracts 0.2.0

Current offline baseline for **Foundation plus Trade Pilot**. The represented corridor is India creditor → U.S. business obligor, commercial goods/services. Consumer and Private remain inactive future examples. All actors, source evidence, mandates, credentials, payments and enabled/reviewed states are fictional test assumptions. Passing this package does not authorize an activity or establish runtime enforcement.

Read [Domain and data contracts](../../docs/05-domain-data-contracts.md) for canonical semantics and [the complete migration crosswalk](migration.md) for all 29 legacy records, 23 operations, execution modes and retained states.

| File | Purpose |
|---|---|
| `recovery-contracts.schema.json` | Draft 2020-12 closed shapes for 30 record types (29 retained plus `provider_acceptance_profile`), retained 23 operation admissions and six composition views. |
| `worked-trade.json` | 60 synthetic records across 27 types; two assessment checkpoints, independent provider-review starting point, provider payment report and uncertain GRE transmission receipt. No reconciled collection result is asserted. |
| `worked-consumer-inactive.json` | Inactive institutional U.S.-origin/India-resident classification on the shared synthetic Foundation shapes. Operational admission is rejected. |
| `worked-private-inactive.json` | Inactive private-origin classification and limited participant/private/shared access example with declined participation. No Private service is released. |
| `contract-compositions.json` | Six closed source-reference compositions; no duplicated balances, grants or outcome ledger. |
| `foundation_checks.py` | Retained offline source/reference/history/money/selected-state checks derived from the original validator; the legacy settlement `CommitHarness` is deliberately omitted. |
| `validate_contracts.py` | Snapshot validation, composition resolution and narrow in-memory Trade review/acceptance/appointment/activation/access helpers. No transport command handlers or actual dispatch. |
| `test_contracts.py` | 42 focused conformance tests, with negative subcases for represented semantics. |
| `requirements.txt` | Reference-only direct pins: `jsonschema[format]==4.26.0`, `rfc8785==0.1.4`; does not modify or choose application lockfiles. |

From the repository root, using Python 3.10 or later:

```bash
python -m venv /tmp/gre-reference-env
/tmp/gre-reference-env/bin/python -m pip install -r reference/v0.2/requirements.txt
/tmp/gre-reference-env/bin/python reference/v0.2/validate_contracts.py
/tmp/gre-reference-env/bin/python reference/v0.2/validate_contracts.py reference/v0.2/worked-consumer-inactive.json
/tmp/gre-reference-env/bin/python reference/v0.2/validate_contracts.py reference/v0.2/worked-private-inactive.json
/tmp/gre-reference-env/bin/python -m unittest discover -s reference/v0.2 -p test_contracts.py -q
```

Snapshot validation accepts the inactive examples' representational shapes. The conformance suite separately proves that the operative gate rejects those profiles, including Network & Control entitlement. The prototype's hardcoded synthetic IDs and actor values are test inputs, not identity resolution.

**Executed September 7, 2026:** Python 3.12.13; all three v0.2 fixture validators passed 60 records and six compositions each; **42 tests passed**. Exact direct dependencies were installed in a scratch virtual environment. Schema metaschema and date/time format checks are enabled. The suite covers the complete represented Trade path, incomplete/conditional/rejected/expired placement, current release/source/policy/authority checks, changed requirements/corrected facts/packet, exact money, payment report and custody denial, permitted disclosure/export/correction access, uncertain receipts/cutover and inactive profile isolation.

The original ZIP remains unchanged, SHA-256 `14d24f856ade2c0b508a208d32a98c14a37723f4708b43c82f58213396bfaf72`. Extract it into a **separate** directory and run its `validate_contracts.py` and `python -m unittest -q test_contracts` with its pinned requirements. The reconciliation run separately passed its 89 records, four checkpoints and **51 tests**. Do not combine its module imports with v0.2 or claim its settlement commit profile is the Trade Pilot implementation.

The reference has no network, persistence, authenticated identity, trusted signature/source verification, complete command handlers, durable outbox, transactional/idempotent/concurrent effects, provider delivery, bank/PSP adapter, deployed tenant/participant isolation, retention/deletion enforcement, corridor legal determination or performance evidence. A plain accepted snapshot does not prove that runtime gates were enforced. Static checks preserve represented history; `PilotHarness` tests decisions against explicit synthetic time and state. Full database/worker/API/effect tests, correction-content disclosure, real recall and second-provider switching remain required implementation work.

No automatic migration script is supplied. Preserve old snapshots and provenance, resolve every material scope/authority ambiguity, create new proposals/approvals when bindings change, and fail closed on unmappable inputs. Future pricing, provider requirements, legal permissions and regional coverage require their own evidence. These fixtures cannot supply it.
