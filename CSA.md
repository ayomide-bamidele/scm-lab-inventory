# Configuration Status Accounting (CSA)

## Branches
- dev
- main

## Commits per maintenance task

### Corrective maintenance
- `959271a` 2026-11-22 - fix(corrective): stock value used quantity + price; now quantity * price. Guard empty inventory, add main()

### Adaptive maintenance
- `2cb432f` 2026-11-22 - feat(adaptive): Python 3.12 dataclass(slots) Item model and new low_stock() feature

### Perfective maintenance
- `dfb8f62` 2026-11-22 - feat(perfective): formatted inventory report table with totals and thousands separators

### Preventive maintenance
- `8bd2b04` 2026-11-22 - refactor(preventive): docstrings, unit tests and requirements for maintainability

## Baseline
- `509c38a` 2026-11-22 - chore: initial inventory project (baseline before maintenance)

## Releases
- v1.0: all four maintenance types complete (merged dev into main)
