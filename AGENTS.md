# Agent Working Agreement

These repository-wide instructions apply to ChatGPT Work, Codex, and other coding agents. The user's current task, explicit acceptance criteria, this file, and any more specific nested `AGENTS.md` form the execution contract. Repository-specific business, security, quantitative, testing, CI, release, and Git-safety rules take precedence over generic guidance and must not be weakened.

## Authority and Context

- Accept GitHub tasks in natural language. Do not require a fixed prompt, manual template, branch name, PR number, or Issue when current facts can be resolved safely.
- GitHub live state is authoritative for branches, SHAs, commits, PRs, reviews, checks, and merge status. Treat chat history, memory, plans, summaries, and handoffs only as leads.
- Before creating work, search for a matching open PR, branch, or Issue and continue a unique match in place. Do not duplicate or redo verified work.
- Use the PR body as dynamic state for ordinary single-PR work. Create and populate an Issue automatically only for genuinely multi-PR, long-lived phased or backlog work, or when the user requests one.
- Load the smallest authoritative context first: applicable `AGENTS.md`, `.github/CHATGPT_PROJECT_BRIEF.md` when present, the matching PR and diff, then directly related code, tests, configuration, and workflows. Expand only when evidence is insufficient, contradictory, or the impact boundary grows.
- Do not load the whole repository, conversation, all PRs/Issues/Actions, or large logs by default. Never lossy-compress prohibitions, exceptions, AND/OR logic, thresholds, dates, versions, paths, branches, SHAs, exact results, risks, or unknowns.
- When no local worktree exists, mark local path and working-tree fields as not applicable; never invent them. Use `context-budget-router` and `conversation-continuity-guard` when available.

## Remote Task Bootstrap

These requirements make task state durable before implementation and at meaningful milestones. They supplement, and never replace or weaken, repository-specific rules.

- After the minimum read-only verification and before any substantive modification, establish a remote task-start checkpoint. For a new task, create the feature branch from the verified remote default-branch SHA. If a matching PR or branch already exists, continue it in place, refresh the PR, push the current recoverable state, and verify the remote head before editing.
- Prefer a structured empty bootstrap commit recording: Objective; Acceptance criteria; Included and excluded scope; Non-negotiable constraints; Default branch and baseline SHA; Feature branch; Related PR, branch, or Issue; Current verified state; Risks and unknowns; and Next action.
- Push the bootstrap commit to the remote feature branch and verify its remote head SHA before substantive modification. If empty commits are unsupported, use a temporary branch-only `.github/task-bootstrap/<task-slug>.md` file and delete it before final merge.
- Every formal checkpoint and important milestone must run the minimum necessary verification, commit one coherent atomic state, push it, verify the remote SHA, update the PR, and then continue. Chat, a local workspace, a local commit, or a temporary container alone is not a complete checkpoint. Do not create commits for trivial edits.
- Never push secrets, unrelated changes, or an incomplete atomic modification. Without explicit authorization, do not push the default branch or force-push. If push or remote verification fails, report the exact blocker and do not claim a completed checkpoint.

## Continuous Execution and Recovery

- Complex, multi-step, long-running, GitHub, batch, research, debugging, and multi-tool tasks default to continuous execution while a safe, clear, authorized next step exists.
- Milestones, checkpoints, commits, pushes, PR creation, partial validation, progress updates, and prepared handoffs are not completion. Progress updates are non-blocking; continue without asking the user to say “continue” when the next action is clear.
- After each meaningful milestone, use the formal checkpoint procedure above, refresh the PR with objective, verified work, remaining work, exact evidence, risks, unknowns, and next action, then proceed.
- In a batch, checkpoint each target independently and continue past a blocked target when other work remains. While required checks are pending, do other executable work; long-running non-required checks are not blockers.
- When context may be stale, re-read authoritative repository and PR state, head/base/default SHAs, commits, diff, reviews, checks, and remaining work. Resolve discrepancies through read-only inspection, discard superseded narrative state, and resume rather than restarting.
- Do not stop because the conversation is long, many tools or files were used, a phase is large, or a handoff could be prepared. Do not claim remaining token, message, or context capacity without accurate platform telemetry.

## Progressive Verification

Verification must produce new evidence. Use the smallest scope that safely proves the current change, and expand according to impact and uncertainty rather than ritual.

### Development and Milestones

- For each coherent change, identify the affected scope from the diff and dependency path. Prefer a test method, class, module, package, or subproject over repository-wide checks.
- Run directly relevant unit or integration tests, compilation, lint, static checks, schema checks, or the smallest useful reproduction. Batch related edits and do not rerun checks whose covered behavior and inputs have not changed.
- At a meaningful milestone, run the affected module or subsystem suite when behavior crosses component boundaries or impact cannot be bounded confidently.
- Do not run the complete repository suite after every small edit.

### Final Candidate

- A final candidate is the stable tree intended for delivery or merge. Run the complete required engineering and acceptance suite once on that candidate.
- Repeat the complete suite only when: a failed full run was followed by a result-affecting fix; material behavior changed after a successful run; shared build, dependency, configuration, schema, data, runner, or core infrastructure changed; or evidence shows the prior scope was insufficient.
- Documentation, comments, formatting, renames, provenance, and metadata-only changes do not require repeating expensive full validation unless an explicit contract requires it.

### Failure Handling

1. Diagnose the root cause and confirm the failed path, state, and inputs.
2. Rerun the failed item and directly affected checks first.
3. Expand coverage only after the targeted check passes or when the impact cannot be bounded safely.
4. Do not restart an expensive full suite after every diagnostic edit.

### Expensive Backtests, Benchmarks, and Simulations

When applicable, stage validation as: **L1** targeted unit/regression checks; **L2** affected strategy/module plus a small smoke run; **L3** affected benchmark, regime, or data cohort; **L4** the complete acceptance and robustness matrix. Use L4 for the stable final candidate, not as the inner loop, and repeat it only after a material result-affecting change.

## Completion, Handoff, and Git Safety

- Finish only when the objective and acceptance criteria pass with necessary final verification, the user explicitly stops, safety policy requires termination, the environment cannot perform a required action, or one verified blocker prevents all remaining safe authorized work. If remaining work contains a safe executable item, continue. Do not promise background completion.
- A handoff is required only for an explicit hard tool limit; permission, protection, required approval, or external authorization blocking all remaining work; a material user decision that cannot be inferred safely; an unresolved substantive live-state conflict; critical context unavailable from authoritative sources; material correctness, security, privacy, data-integrity, economic, or irreversible risk; or an explicit user request.
- Task length, many milestones/files/logs/tools, a large next phase, an existing handoff, pending non-required CI, or one blocked repository in an actionable batch are not handoff conditions.
- Before a required handoff, finish the smallest safe atomic action, save and verify a recoverable checkpoint when possible, refresh authoritative state, identify the exact blocker, and report verified repository, branch, SHA, worktree, test, CI, commit, push, risk, and next-step facts. Mark unavailable fields as not verified or not applicable.
- Without explicit authorization, do not run `reset`, `clean`, or `rebase`; force-push or rewrite shared history; delete branches or worktrees; discard tracked, staged, unstaged, or untracked work; overwrite unrelated changes; or redo completed verified work.
- Before merge, handoff, or final completion, verify the applicable live branch, HEAD, remote feature SHA, default-branch SHA, merge base, working state, commits, push state, changed files, reviews, required checks, and exact test results.
