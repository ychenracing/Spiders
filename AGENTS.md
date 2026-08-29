# Agent Working Agreement

## Progressive Verification Strategy

Use progressive, impact-based verification. Do not repeatedly run the full test suite or other expensive validation after small edits.

### During implementation

- For every incremental change, identify the smallest affected scope from the diff and dependency path.
- Run only directly relevant unit tests, targeted integration tests, compilation, lint, static checks, or the smallest useful reproduction.
- Prefer test method, test class, module, package, or subproject scope over repository-wide commands.
- Batch logically related edits before broader verification.
- Do not rerun checks whose covered behavior has not changed.
- Do not run the full repository test suite after every edit.

### Milestone verification

- After a meaningful logical milestone, run the affected module or subsystem suite when cross-component behavior may have changed.
- Expand coverage when impact is uncertain, cross-cutting, or shared infrastructure has changed.

### Final verification

- Run the complete required test/validation suite once after implementation is finished and the final candidate is stable.
- Repeat the complete suite only when:
  1. the previous full run failed and behavior-affecting code was changed to fix it;
  2. material behavior-affecting changes were made after the full run;
  3. shared build/configuration/dependency/schema/core infrastructure changed; or
  4. evidence shows the previous scope was insufficient.
- Documentation, comments, formatting, renames, and metadata-only changes do not require repeating expensive full validation unless explicitly required.

### Failure handling

1. Diagnose the root cause.
2. Rerun the failed test/check and directly affected tests first.
3. Expand coverage only after targeted verification passes or when the impact cannot be bounded safely.
4. Do not restart the entire expensive suite after every diagnostic edit.

### Expensive backtests, benchmarks, or simulations

When applicable, use staged validation:

- **L1:** targeted unit/regression tests;
- **L2:** affected strategy/module plus a small smoke run;
- **L3:** affected benchmark/regime/data cohort;
- **L4:** complete acceptance/robustness matrix.

Use L4 as a final acceptance gate, not as the inner development loop. Repeat L4 only after a material result-affecting change.

### Principle

Verification should produce new evidence. The goal is to establish final correctness with the minimum test scope that safely proves the current change; full validation is a final acceptance gate, not a per-edit ritual.

## Natural-Language Task Entry and Context Governance

These rules govern task entry, context loading, continuity, and handoff. They do not weaken explicit acceptance criteria, verification, security, data-integrity, business, economic, or repository-specific requirements.

- Accept GitHub tasks stated directly in natural language. Do not require a fixed prompt, manually prepared template, branch name, PR number, or mandatory Issue when the facts can be resolved from the conversation and GitHub.
- Use the PR body as dynamic state for ordinary single-PR work. Create and populate an Issue automatically only for genuinely multi-PR, long-lived phased/backlog work or when the user requests one.
- GitHub live state is authoritative for branches, SHAs, commits, PRs, reviews, checks, and merge status. Chat history, memory, plans, summaries, and handoffs are leads, not current facts.
- Search for matching open PRs, branches, and Issues before creating work. Continue an existing match in place; do not duplicate work.
- Load the smallest authoritative context first: this file, `.github/CHATGPT_PROJECT_BRIEF.md` when present, the matching PR and diff, then directly related code, tests, configuration, and workflows. Expand only when evidence is insufficient, contradictory, or impact grows.
- Do not load the full repository, chat history, all PRs/Issues/Actions, or large logs by default. Never lossy-compress prohibitions, AND/OR logic, thresholds, dates, versions, paths, branches, SHAs, exact results, risks, or unknowns.
- If no local worktree is available, mark local path and working-tree fields as not applicable; never invent them.
- Use `context-budget-router` and `conversation-continuity-guard` when available, while following this file regardless.

## Continuous Execution

Complex, multi-step, long-running, GitHub, batch, research, debugging, and multi-tool tasks default to continuous execution.

- Continue while a safe, clear, executable next step remains.
- Milestones, checkpoints, commits, pushes, PR creation, partial validation, progress updates, and prepared handoffs are not completion.
- Do not stop because the conversation is long, many tools/files/logs were used, multiple milestones finished, the next phase is large, a handoff could be prepared, or non-required CI is pending.
- Progress updates are non-blocking: after an update, continue without waiting for a reply. Do not ask the user to say “continue” when the next action is clear.
- Do not claim remaining token, message, or context capacity without explicit accurate platform telemetry.

## Non-Blocking Checkpoints and Recovery

After a meaningful milestone:

1. Save a coherent recoverable checkpoint.
2. For GitHub work, refresh the PR body with current objective, completed/verified work, remaining work, exact verification, risks, unknowns, and next action.
3. Commit and push an understandable state when appropriate, then verify remote head and PR state.
4. Continue directly to the next executable item.

A normal checkpoint must not end the task, emit a handoff as the final response, recommend switching chats, or require confirmation. For batch work, safely checkpoint one target and continue to the next; one blocked target does not end an actionable batch. While required checks are pending, perform other available work first; non-required long-running checks are not blockers.

When context may be stale, re-read the authoritative repository, PR, head/base SHAs, commits, diff, reviews, checks, and remaining work; resolve discrepancies through read-only inspection, discard superseded narrative context, refresh state, and continue. If a prior handoff exists and the user says “continue”, “continue to completion”, or equivalent, re-verify live state and resume.

## Handoff-Required Conditions

Stop and produce a complete handoff only when further safe execution is actually blocked by at least one of:

1. an explicit platform/tool hard limit or unavailable required tool;
2. permissions, branch protection, required approval, or external authorization blocking all remaining work;
3. a material user decision that cannot be inferred safely;
4. a substantive live-state conflict that read-only verification cannot resolve;
5. critical context actually lost and unrecoverable from authoritative sources;
6. material correctness, security, privacy, data-integrity, economic, or irreversible risk;
7. an explicit user request to stop or hand off.

Task length, milestone/interaction counts, many files/logs/tools, a large remaining phase, an existing handoff, pending non-required CI, one blocked repository in a larger actionable batch, or unsupported concern about a future limit are not sufficient reasons.

Before a required handoff, finish the smallest safe atomic action, save a recoverable checkpoint, refresh authoritative state, state the exact blocker, and provide a self-contained handoff with verified—not guessed—repository, branch, SHA, worktree, test, CI, commit, push, risk, and next-step information.

## Completion and Git Safety

End only when the objective and acceptance criteria are satisfied with necessary final verification, the user asks to stop, a true blocker prevents all remaining safe work, safety policy requires termination, or the environment cannot continue required tools. If `Remaining Work` contains a safe executable item, continue. Do not promise background completion.

Without explicit authorization, do not run `reset`, `clean`, or `rebase`; force push or rewrite shared history; delete branches/worktrees; discard tracked, staged, unstaged, or untracked work; overwrite unrelated changes; or redo completed verified work.

Before handoff, merge, or final completion, verify applicable live branch, HEAD, remote feature SHA, default-branch SHA, merge base, working state, commits, push state, reviews, checks, and exact test results. Mark unavailable fields as not verified or not applicable rather than guessing.
