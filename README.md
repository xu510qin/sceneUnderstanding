# 2026 Top Conference 3D Perception Project

This repository is the shared code and experiment workspace for a 2026 top-conference submission on 3D scene understanding / embodied 3D perception.

The first goal is not to build the final model immediately. The first goal is to make the collaboration reproducible: shared code, fixed data protocol, fixed splits, traceable configs, and experiment logs that both collaborators can inspect.

## Collaboration Roles

| Role | Main responsibility |
| --- | --- |
| You | Problem definition, literature filtering, innovation hypotheses, experiment design, result interpretation, paper writing |
| Pavel | Open-source baseline reproduction, environment setup, training scripts, batch experiments, logs and table automation |
| Codex / AI tools | Code reading, refactoring, config generation, tests, log analysis, literature triage support |

## Repository Layout

```text
.
├── configs/                 # Example paths and experiment configs
├── datasets/                # Dataset documentation only; large data is not committed
├── docs/                    # Collaboration notes, decisions, meeting records
├── experiments/             # Lightweight experiment plans and summaries
├── scripts/                 # Utility scripts for environment/data checks
├── src/                     # Project source code
└── tests/                   # Smoke tests and small regression tests
```

Large files such as raw datasets, processed datasets, checkpoints, logs, and training outputs should stay outside git. Put only download instructions, checksums, split files, configs, and small examples in this repository.

## Quick Start

1. Clone the repository.
2. Create a Python environment.
3. Install project dependencies once they are finalized.
4. Copy `configs/paths.example.yaml` to `configs/paths.local.yaml`.
5. Edit the local paths to match your machine or AutoDL instance.
6. Run the environment check.

```bash
python scripts/check_environment.py
python scripts/check_dataset_layout.py --config configs/paths.local.yaml
```

## Branch Rules

Use small branches with clear names:

```text
main
dev
you/problem-definition
pavel/baseline-repro
pavel/dataset-loader
```

Merge into `main` only when the code has a working smoke test or the change is documentation-only.

## First Milestone

Before model development, finish:

- Target dataset list
- Dataset license and access notes
- Fixed train/val/test split policy
- Shared path config
- One dataset loading smoke test
- One baseline reproduction smoke test

