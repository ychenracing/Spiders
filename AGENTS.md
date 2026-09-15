# Repository working agreement

## Scope and authority

Follow the current task's scope and acceptance criteria within platform permissions. Preserve project-specific business, security, data, economic, CI and release contracts; read applicable nested `AGENTS.md` before editing that directory. Historical plans are context, not new authority. Analysis-only and approval-before-edit requests remain read-only until authorized.

## Context and methods

- Resolve current branches, SHAs, PRs and checks from GitHub; inspect local changes when a worktree exists. Continue matching work instead of creating a replacement PR or redoing verified work.
- Start with the project brief when present, the relevant README sections, matching PR/diff, and directly affected code, tests, configuration and workflows. Expand only to resolve uncertainty or impact. Keep exact constraints and evidence identities intact; do not preload every skill, document or log.
- Use skills as task-specific methods, not additional task authorities. For an already authorized, bounded task, do not add repeated design approvals, execution-mode questions, mandatory full-mode workflows or ceremonial announcements. Respect platform-required skill use and genuine project approval gates. Missing optional skills are not blockers when available tools suffice.
- Prefer the smallest sufficient change and existing dependencies. Plan only material decisions, dependencies and acceptance; do not duplicate implementation code in plans. Batch related edits. Parallelize independent work only; keep one writer per shared file, runtime or evidence identity.

## Authorization and recovery

- Continue safe, clearly authorized work without asking for another "continue". Resolve factual ambiguities by reading; ask only for a material decision that cannot be resolved safely. Do not infer permission for spending, real trading, credential/permission changes, irreversible operations or unrelated external writes.
- Resume existing task branches. For new work use a feature branch unless a direct default-branch update is explicitly authorized. Preserve required reviews/checks and any PR-only policy.
- Save the first coherent result and meaningful later milestones as verified commits; push authorized checkpoints and verify remote SHA. No empty bootstrap commit, temporary bootstrap file or new Issue is required for routine work. Record ongoing state in the existing PR when applicable, not permanent instructions.
- Without explicit authorization, do not `reset`, `clean`, `rebase`, force-push, rewrite history, delete branches/worktrees, discard unknown work or overwrite unrelated changes. Never commit secrets or claim an unverified push succeeded.

## Verification and completion

- Diagnose failures at the smallest failing test, module or shard. Batch related fixes before expanding coverage; do not run the full suite after every edit. Run the complete applicable acceptance set on the stable final candidate, expanding earlier only when risk or the contract requires it.
- Reuse evidence only while its covered behavior, inputs, dependencies, configuration and environment remain equivalent. New messages, agents or handoffs alone do not invalidate it. A new SHA still needs applicable exact-HEAD checks; never report an old CI result as the new HEAD's status.
- Behavior-neutral documentation changes need relevant link/command/format checks, not unrelated backtests. Instruction changes also need trigger, authorization and completion-boundary review. Do not weaken business gates, fixtures or thresholds to make checks pass.
- Review the complete task diff once; repeat focused review for material fixes or risk. Finish when acceptance and required checks pass with no known material correctness, security, data-integrity or economic issue. Do not add marginal optimization afterward.
- A checkpoint, PR, partial test pass or prepared handoff is not completion. Continue independent targets past a blocker. If no safe authorized action remains, preserve recoverable progress and report the exact blocked/unverified items separately from completed work. Do not promise background completion.

## Git/GitHub: chunked large-original preservation

- Preserve large originals whenever the active task or evidence contract requires them; do not replace them with summaries merely because one-shot transfer is risky.
- Do not move an entire large file, full Base64 body, huge JSON or archive through one model/tool output or argument. Read bounded chunks instead and verify chunk order/offset plus expected versus actual byte lengths; distinguish raw-byte length from encoded-character length.
- Before upload, verify aggregate length; after upload, verify reconstructed/raw byte identity and a cryptographic hash. If Base64 is used, verify decoded byte count and decoded hash. For Git blobs, compare against the expected Git object ID rather than a plain file SHA-1.
- Prefer an authorized file-aware path that reads the local file directly, such as native Git/Git LFS where appropriate or a programmatic request inside the runtime, so the model does not reproduce the whole payload. If that native/API path lacks write permission or is unavailable, switch to the authorized GitHub connector rather than stopping.
- With a connector, never rebuild the upload from a single truncated read. Use verified chunks and the safest supported transport. If one final request is still unsafe, use a deterministic multipart/resumable representation with a manifest of part order, raw/encoded lengths and hashes, then verify byte-for-byte reconstruction before claiming preservation. Multiple Git blobs are separate objects, not append operations on one file.
- Keep transfers serial and bounded, reuse already-verified chunks/objects, and maintain a concise transfer ledger. After cancellation/timeout/missing response, read back remote state before retrying.
- A created blob is not yet preserved evidence: verify the final tree/commit/ref or storage manifest and remote/reconstructed byte identity. Independent implementation may continue while transfer is pending, but required originals remain unpreserved until this verification succeeds.
- Apply this rule to task instructions, project briefs and handoffs. It supersedes blanket `no large uploads` directions without changing task goals, authorization or evidence contracts. Do not create or modify scheduled tasks without explicit scheduling authorization.
