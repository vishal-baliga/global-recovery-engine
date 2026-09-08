# Scope decisions and reconciliation record

**Effective planning date:** September 7, 2026.

**Owner:** Vishal.

**Owns:** Current source precedence, material decisions, artifact ownership, scope-change history and reconciliation evidence.

**Authority:** The owner's latest instruction selects the shared Foundation and one best family for the market-facing Pilot, with all other families recorded as future development. This supersedes the earlier concurrent Trade/Private program.

## 1. Current decisions

| ID | Decision | Consequence |
|---|---|---|
| D01 | Pilot is the sole release concept | No separate MVP scope or quality tier. Build and take the defined Pilot to market through explicit release gates. |
| D02 | Select Foundation + Trade & Receivables | The current implementation backlog contains only shared capabilities needed by Trade and the complete Trade service. |
| D03 | Include the Trade-required Network & Control capabilities | Named-provider requirements, preflight, direct placement, corrections, observation and portability support are part of the Trade bundle; standalone Network is future commercialization. |
| D04 | First directional profile: India creditor → U.S. business obligor, commercial goods/services claims | A concrete build/discovery target, not verified market fit or nationwide coverage. Actual buyer, state/activity profile and provider coverage gate live operation. |
| D05 | Primary buyer hypothesis: recurring creditor-side owner with repeated preparation/intake needs | Reachability and repeated preparation/intake cost matter more than a prestigious channel category. Agencies/providers are important users and partners. |
| D06 | GRE supplies preparation and continuity; independent providers execute recovery | Preserve direct creditor appointment, provider judgment and accurate residual duties. No GRE principal collection, post-default obligor outreach or payment custody. |
| D07 | Private Resolution and Consumer Credit are future families | Preserve domestic friend-loan preparation/voluntary resolution and institutional U.S.–India mobility requirements with reopening conditions. They are not concurrent Pilot lanes. |
| D08 | Retain the selected stack and verified development setup | Product requirements may justify future ADRs; no reinstallation, automatic version upgrade or wholesale replatforming follows this scope change. |
| D09 | Reuse one canonical owner per fact | Six strategic contracts compose/extend the existing domain where possible; modular code does not imply shared cross-tenant access. |
| D10 | Reconcile documents and reference semantics before the implementation backlog | A versioned reference baseline is planning/conformance work; product code, migrations and runtime behavior follow bounded stories. |
| D11 | GitHub current documents are the development authority | A checked-out commit identifies the baseline. Research archives and older attachments cannot override current scope. Preserve history and trace replacements. |
| D12 | Keep software, market and operating readiness separate | Tests do not create customers, provider acceptance, legal approval or paid-service permission. Each live capability needs its actual evidence. |

The single-family decision intentionally narrows the previous promise. Direct personal-loan acquisition, bilateral invitation/negotiation, Private plan servicing and institutional Consumer work leave the current backlog. Trade still delivers a useful assessed/no-route outcome and a complete accepted-provider/continuity path; it is not reduced to a referral link.

## 2. Why Trade was selected

Trade makes greatest use of the existing evidence, balance, rights, authority and independent-provider design, with a testable recurring budget for preparation and re-intake. Private adds a distinct two-sided participation/privacy/safety operation with episodic demand. Consumer adds substantial institutional integration, account-history, data-role and assurance dependencies. The stack could serve all three; the narrower complete job and accessible commercial proof determine the first family.

This is an informed project choice, not proof of demand. Established agencies already provide convenient online collection. GRE must prove total-work savings, consequential-error reduction and paid repeat use. The evidence, counterarguments and stop/narrow rules are in [14](14-market-validation-and-proof.md).

## 3. Artifact ownership and reading order

| Artifact | Authoritative subject | Boundary |
|---|---|---|
| [00 — Start here](00-start-here.md) and root README | Current stage, navigation, actual environment evidence and next work | Summaries point to owning specifications |
| [01 — Business](01-business-project-overview.md) | Business definition, buyers, value and economic/role boundaries | Does not invent release coverage or legal permission |
| [02 — Offering and strategy](02-product-offering-competitive-strategy.md) | Portfolio, packages, differentiation and capability disposition | Current Pilot detail is owned by 06; research is dated |
| [03 — Operating model](03-operating-model.md) | Responsibilities, invariants, service/authority/financial/observation semantics | Workflow sequence in 04; machine shape in 05 |
| [04 — Workflow](04-workflow-interaction-specification.md) | User/provider interactions, transitions and realistic exceptions | Does not reinterpret contract fields or create actor authority |
| [05 — Domain contracts](05-domain-data-contracts.md) and [reference](../reference/README.md) | Versioned records/operations, compatibility and executable reference conformance | A reference test is not runtime application enforcement |
| [06 — Pilot brief](06-pilot-brief.md) | Included customer outcomes, exclusions, manual/partner routes and success scope | One current family; no secondary MVP tier |
| [07 — Future register](07-future-development-and-business-deliverables.md) | Deferred families/product/business depth and excluded models | Inclusion in a register is not a scheduled commitment |
| [08 — Architecture](08-stack-and-environment-decision.md) | Stack, modules, data/effect ownership and change practice | Exact installed versions belong to 10 |
| [09 — Environment](09-development-environment.md), [10 — Dependencies](10-dependency-baseline.md) | Actual setup, commands, pins, observed checks and remaining integration limits | Preserve historical observations rather than claiming they were rerun |
| [11 — Backlog](11-prioritized-pilot-backlog.md) | Ordered Foundation/Trade implementation and business tasks | Rebuild from the consistent document baseline; preserve legacy dispositions |
| This record | Owner decisions, precedence and cross-file reconciliation | New user decisions take precedence and must be propagated |
| [13 — Release/assurance](13-pilot-release-and-assurance.md) | Evidence and ownership before real data/live service | No default legal or operational approval |
| [14 — Market proof](14-market-validation-and-proof.md) | Discovery, economic and quality measurement, public claims | No market-leadership claim without bounded comparative evidence |
| [Research directive1.1](research/2026-09-07-scope-directive-1.1.md) | Historical rationale, source research and broader portfolio context | Its two-lane scope and update instructions are superseded by D01–D12 |

Repository filenames 01–05 and 07–11 remain stable. `06-pilot-mvp-brief.md` is replaced by `06-pilot-brief.md`; current links use the new filename. The historical file remains accessible through Git history. Existing attachments are historical source copies until explicitly synchronized from a reviewed Git revision; do not edit two competing specifications.

## 4. Preserved baseline and reconciliation sequence

The inspected baseline before this update was `main` at `3fca8a93ac86852fbc44b0b3265143045bc5eecd`, `setup/devcontainer` at `5511b1ef3096b7791a3c8be62a916c469c9f3a73`, and `docs/pilot-backlog` at `2f8721b928e0faa728bb7697226b272a6d9693e4`. PR #1 was draft and PR #2 open/non-draft. These are historical observations, not a permanent statement of current PR status.

The reconciliation builds on the descendant containing the setup and old backlog, preserving runtime source/locks and Git history. The existing reference ZIP is preserved byte-for-byte. Readable v0.2 sources carry the new reference contract and migration explanation, rather than silently reinterpreting0.1.0.

| Pass | Files/decision surface | Purpose |
|---|---|---|
| R0 | Source inventory and current owner direction | Establish precise single-family scope and preserve verified work |
| R1 | 01,02,06,07 and this decision record | Reconcile business promise, portfolio, current scope and all futures |
| R2 | 03,04,08,13,14 | Define operation, modular design, data/effect boundaries, market proof and live gates |
| R3 | 05 and reference v0.2/README | Version meaningful contract changes and execute reference checks |
| R4 | 11,00,README,AGENTS and 09/10 references | Build backlog after design, reconcile every old item and remove stale instructions |
| R5 | Cross-file/reference review and publication | Check links, terminology, ownership, test evidence and preserved files; publish a coherent Git baseline |

Sequential publication follows this dependency order. Independent drafting/review may occur in parallel when file ownership is explicit. No product feature is implemented merely to make a planning document appear complete.

## 5. Material change matrix

| Prior surface | Disposition | Current owner and impact |
|---|---|---|
| B2B/operator-only original business story | GENERALIZE/REPLACE | 01/02: broad portfolio with creditor-first Trade Pilot; agencies remain partners |
| Concurrent domestic personal-loan and Trade commitment | REPLACE/MOVE_TO_FAMILY_PROFILE | 06/07: one Trade Pilot; Private capability and acquisition hypotheses preserved as future |
| Institutional U.S.-origin/India-resident borrower expansion | MOVE_TO_FAMILY_PROFILE | 07: gated Consumer family; no live or shadow real-data work implied |
| Intelligence/Operations/Network/Control as top-level families | REPLACE | 02: capability domains; Network & Control is horizontal commercial packaging |
| End-to-end GRE contact/negotiation/plan-operation promise | REPLACE | 03/04/06: independent provider execution; GRE owns its scoped platform and continuity duties |
| Evidence/authority/exact money/service separation/outcome truth | KEEP/GENERALIZE | 03/05/08: shared invariants, current gates and source lineage |
| Universal or directionless corridor | MOVE_TO_CORRIDOR_PACK | 03/05/13: exact family/actor/activity/data-flow release and review conditions |
| Authority Envelope/Action Receipt/Scorecard | GENERALIZE | 05/08: composed canonical records, not duplicate ledgers |
| Provider requirements versus per-case placement | GENERALIZE | 03/05: standing provider profile separate from validation/acceptance/activation |
| Schema0.1/29records/23operations | KEEP as historical; version current contract | 05/reference: full legacy mapping, source-readable new version and explicit validation limits |
| Old GRE-001–048 backlog | REPLACE/SPLIT/DEFER | 11: complete legacy disposition map, current P-series order and future IDs |
| F-P01–16, F-B01–07, X01–05 | KEEP/GENERALIZE | 07: retain IDs, Pilot minima, future triggers and true exclusions; add family candidates |
| Stack/setup/dependency verification | KEEP | 08–10: preserve exact observed pins/results, refine scope references and remaining tasks |
| Old next-step and two-track instructions in agent/checkpoint docs | REPLACE | AGENTS/00/README: current authoritative reading order and first implementation item |
| Legal/vendor research | NEEDS_COUNSEL/NEEDS_VALIDATION flags | 02/13/14 and historical research: dated sources and specific review/data conditions; no market/legal certainty |

Disposition and review need are separate: a retained requirement may still need counsel or market validation. When splitting a requirement, record both the Pilot minimum and the future remainder. Existing IDs are never silently reassigned to unrelated work.

## 6. Open decisions and accountable next evidence

| Decision | Owner | Needed before |
|---|---|---|
| Reachable creditor, recurring case flow, supported claim subtype and paid offer | Vishal with buyer | Paid diagnostic scope and measurement |
| Actual provider requirements, eligibility, direct terms and returned-data commitments | Vishal with creditor/provider | Prospective placement and public coverage claims |
| Exact states/activity, data-source and corridor legal treatment, residual duties | Qualified reviewers selected by Vishal | Affected real-data/live service |
| GRE contracting entity, operational competence, insurance/support/absence coverage | Vishal with appropriate advisors/operators | Contracted real service requiring those capabilities |
| Production region/data flows, live identity/OCR/model/PSP admission and budget | Vishal with buyer and providers | Provisioning and real integration |
| Numerical success/stop thresholds and permitted public evidence | Vishal with design partner | Evaluation and publication of performance claims |
| Future Private/Consumer/standalone Network activation | Vishal through a new scope decision | Any expansion of the current backlog or released family |

No named buyer, qualified reviewer, provider commitment, price, funded cloud deployment or live release is invented here. These decisions do not block unrelated synthetic development whose dependencies are met.

## 7. Validation record

Reconciliation checks executed September 7, 2026 in the hosted review workspace:

- Revised reference: all three fixtures passed with 60 synthetic records and six compositions each; 42 conformance tests passed. A separate review reran four scope, authority-freshness, prohibited-action and packet-change regressions successfully. Python 3.12.13 and isolated reference dependencies were used; application locks were not changed.
- Historical reference: the original 89-record/four-checkpoint fixture and 51 tests passed separately. The preserved ZIP matches Git blob `3ece1fbf3ba7ca673a0c6697f2a1e4bba7fd7dba` and SHA-256 `14d24f856ade2c0b508a208d32a98c14a37723f4708b43c82f58213396bfaf72`.
- Documentation: 179 current relative links and Markdown table widths checked; the staged diff against reconstructed source documents passed `git diff --check`. There are 30 ordered parent backlog items, nine reusable assessment slices and all 48 legacy dispositions. All 26 future product/business candidates and five excluded models keep explicit identifiers. Current links point to the renamed Pilot brief.
- Independent review corrected the no-provider assessment dependency path and scoped its release controls. Reference review corrected packet binding, current service/grant scope, mandate-verification freshness, prohibited provider acts and disposed-source handling. The reference remains a narrow offline demonstration; these fixes do not establish production authorization.
- Publication preserves the existing runtime source, setup configuration, dependency manifests/locks and original ZIP from the inspected descendant. New code is limited to the versioned reference package. Sequential commits preserve the replaced planning material in Git history; the incoming directive is separately archived with its superseded scope identified.

The PR/commit history records the exact published revision and review result. The developer's Mac toolchain and services were not rerun during reconciliation. Product migrations, runtime isolation, durable worker delivery, real integrations, backup recovery and commercial/legal readiness remain implementation/release evidence in [11](11-prioritized-pilot-backlog.md) and [13](13-pilot-release-and-assurance.md).

## 8. P-001 planning ownership — September 8, 2026

Vishal directed that implementation planning and task decomposition happen here, with the results published to GitHub before Mac checkout/environment confirmation and development. The [P-001 plan](implementation/P-001-development-foundation.md) owns its concrete design and seven child tasks. Local Codex follows the selected task, records actual evidence and raises material conflicts; it does not replace the plan or generate a separate backlog.

This elaborates the existing P-001 scope and selected architecture, without adding another Pilot family or changing P-002–P-030 priorities. The new [verification record](implementation/P-001-verification-record.md) starts pending. Runtime files, locks, images and reference artifacts are unchanged by the planning update. Local verification and all seven implementation tasks remain outstanding.

### P-001 sprint readiness review — September 8, 2026

At Vishal's request, plan revision 1.1 rechecks the same seven-task sprint against `main` at `5f027b2` and issues #4–#11. It corrects cross-task breakage, hard timeout/aggregate behavior, explicit configuration, browser prerequisites, read-only readiness, receipt/lifecycle distinctions and CI revision/closeout evidence. Execution checklists and early Actions/capacity discovery make the existing scope actionable; no eighth engineering task, new product feature or later-family scope is added. Planning ownership stays here. G0 and implementation remain pending; runtime, configuration, locks and references are unchanged by this review.
