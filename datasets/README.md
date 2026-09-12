# Dataset Setup

This folder stores dataset documentation only. Do not commit raw data, processed data, checkpoints, or large generated files.

For each dataset, create one setup note under this folder:

```text
datasets/
  README.md
  dataset_name.md
```

Each dataset note should include:

- Official name
- Official download URL
- License and access restrictions
- Download date
- Expected raw directory structure
- Preprocessing command
- Expected processed directory structure
- Train/val/test split policy
- File count or checksum checks
- Known issues

## Shared Rules

Use fixed splits. Do not let each collaborator create a different random split.

Keep data paths local through `configs/paths.local.yaml`. The repository should only contain `configs/paths.example.yaml`.

Every experiment result must record:

- Git commit
- Config file
- Dataset version
- Split version
- Random seed
- Checkpoint path
- Log path

