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
