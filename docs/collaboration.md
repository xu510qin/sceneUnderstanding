# Collaboration Protocol

## Daily Work

Every work session should leave a trace:

- What changed
- Which command was run
- Which config was used
- Which data version was used
- Whether the result is trusted, suspicious, or failed

## Pull Request Checklist

Before merging code, check:

- The branch has a focused purpose.
- The change can be explained in one paragraph.
- The config or command needed to reproduce the result is included.
- Large files are not committed.
- A smoke test or manual run note is included.

## Experiment Naming

Use names that encode the date, method, dataset, and short purpose:

```text
2026-09-12_baseline-openscene_scannet_smoke
2026-09-18_method-a_scanrefer_seed0
```

## Decision Records

Important decisions should be added as short notes under `docs/decisions/`.

Recommended format:

```text
Date:
Decision:
Why:
Evidence:
Rejected alternatives:
Next check:
```

