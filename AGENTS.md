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

## Git/GitHub: bounded large-file transfer and preservation

- Large originals remain required whenever the active task or evidence contract requires them. This section applies to both downloads and uploads; do not substitute summaries merely because one-shot transfer is risky.
- Preflight before moving a potentially large body: resolve path/object identity and obtain metadata such as byte size, Git/blob SHA, LFS OID/size, artifact ID/size, or equivalent. If size is unknown, do not blindly fetch the full body first.
- For downloads, prefer file-to-file paths that write directly to runtime storage without returning the payload through model/tool output: native Git with partial clone/sparse checkout where useful, selective Git LFS fetch/pull, resumable HTTP/range download, or a connector download action that returns a file reference. If native/API read access is unavailable, use an authorized connector path that is bounded or file-aware; never extract connector credentials.
- For large text needed only for analysis, search first and read bounded line/range chunks; process or filter locally and return only small relevant excerpts. For binary files, archives, workflow artifacts and logs, avoid full inline fetches when a file reference, range read, job-step summary, manifest/listing or selective extraction can answer the task. Do not `cat`, print, Base64-dump, hex-dump or otherwise stream the entire large body into the conversation.
- When a download must be chunked, record and verify chunk offset/order plus expected versus actual byte length, use resumable/range semantics when supported, and reuse already verified chunks after interruption. After completion verify aggregate byte length and a cryptographic hash or expected Git/LFS object identity before treating the local copy as complete.
- For uploads, prefer an authorized file-aware path that reads the local file directly, such as native Git/Git LFS or a programmatic request inside the runtime, so the model does not reproduce the payload. If native/API write access is unavailable, switch to the authorized GitHub connector rather than stopping.
- Never rebuild a large upload from a single truncated read. Use verified chunks and the safest supported transport. If one final request is unsafe, use a deterministic multipart/resumable representation with a manifest of part order, raw/encoded lengths and hashes, then verify byte-for-byte reconstruction. Multiple Git blobs are separate objects, not append operations on one file.
- If Base64 is used anywhere, distinguish encoded character count from decoded byte count and verify the decoded hash. For Git object verification compare against the expected Git object ID rather than a plain file SHA-1.
- Keep large transfers serial and bounded and maintain a concise transfer ledger. After cancellation, timeout or missing response, inspect local/remote state before retrying so completed chunks, downloads or writes are not duplicated.
- A partial local file, downloaded archive reference or created Git blob is not completion. Verify the final local file or extracted target, and for uploads verify the final tree/commit/ref or storage manifest plus reconstructed byte identity before claiming preservation.
- Large-file transfer must not unnecessarily block independent implementation or validation, but required originals remain incomplete until their download/upload and integrity verification succeeds. Never fabricate evidence, weaken acceptance or call a summary/hash a backup.
- Apply this rule to task instructions, project briefs and handoffs. It supersedes blanket `no large uploads` or one-shot-download directions without changing task goals, authorization or evidence contracts. Do not create or modify scheduled tasks without explicit scheduling authorization.
