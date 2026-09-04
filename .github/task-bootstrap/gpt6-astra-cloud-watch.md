# GPT-6 Astra Cloud Watch — Public Runner Migration Bootstrap

- Objective: deploy a fully cloud-hosted hourly monitor that verifies the authenticated user's ordinary ChatGPT account exposes an explicitly named, enabled, and successfully selectable `GPT-6 Pro`; sends exactly one verified Gmail notification; then stops permanently.
- Acceptance criteria:
  1. No continuously running user-owned device.
  2. One-time interactive ChatGPT login through a temporary cloud-browser Live View.
  3. Success only after ordinary Chat visibly exposes, enables, accepts a click on, and confirms selection of `GPT-6 Pro`.
  4. Public rollout evidence, generic `Pro`, disabled entries, hidden DOM text, and Work/Codex-only availability are never success.
  5. Normal negative checks remain silent.
  6. First success sends one email titled `GPT-6 Astra 已对我的账户开放`, confirms that exact message in Gmail Inbox, and disables future checks.
- Included scope: Browserbase persistent context; GitHub Actions hourly scheduling; Playwright UI validation; Gmail SMTP/IMAP idempotency; tests and runbook.
- Excluded scope: public rollout monitoring; local-device scheduling; automatic CAPTCHA solving; unrelated spider code.
- Non-negotiable constraints: this repository is public, therefore Browserbase context ID, ChatGPT account identity hint, API keys, Gmail credentials, cookies, screenshots, and other account data must live only in encrypted Actions Secrets or ephemeral workflow storage; no account state may be committed.
- Default branch: `master`.
- Verified baseline SHA: `0a1fc2d306d8c037bec647fb0833b895c1ff84f6`.
- Feature branch: `codex/gpt6-astra-cloud-watch`.
- Related private-repository prototype: `ychenracing/note` PR #4; it proved the implementation shape but private Actions jobs fail before runner assignment (`runner_id=0`, `steps=[]`).
- Current verified state: public feature branch created; no implementation has been migrated.
- Risks/unknowns: public hosted-runner availability must be probed first; Browserbase and Gmail secrets require one-time owner setup; ChatGPT DOM labels and login challenges may change; Browserbase paid proxy capacity may be required.
- Next action: run a one-step public-repository runner probe, then migrate the monitor with all state moved to encrypted Secrets.
