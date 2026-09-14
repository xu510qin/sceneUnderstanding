# Weekly Submission Plan

This document is the shared weekly plan for the 2026 top-conference submission. It is written for both Ruiqin and Pavel. Chinese explains the intent; English labels make the execution points easy to scan.

Target submission window: mid November 2026  
Current date: 2026-09-14  
Research direction: 3D Scene Understanding / Embodied 3D Perception, to be narrowed this week

## Core Rule

我们不是先堆一个复杂模型，而是先完成一个可复现的研究闭环：

```text
problem -> data -> baseline -> failure mode -> mechanism -> experiment -> paper claim
```

Every proposed idea must have:

- Failure mode: what existing methods fail at
- Mechanism hypothesis: why our idea should help
- Minimal experiment: the smallest test that can falsify it
- Metric: how we know it worked
- Cost: whether it can be finished before the deadline

## Hard Deadlines

| Date | Deadline | Must Have |
| --- | --- | --- |
| 2026-09-20 | Problem and data freeze v1 | One-sentence problem, dataset list, baseline candidates |
| 2026-09-27 | Baseline check | At least one baseline or data loader running |
| 2026-10-11 | Go / No-Go | Keep one main idea and at most one auxiliary idea |
| 2026-10-25 | Main experiments mostly complete | Main table, key ablations, one generalization or robustness result |
| 2026-11-02 | Paper v0 | All main sections have draft text |
| 2026-11-09 | Method Freeze | No new main modules after this date |
| 2026-11-13 | Content Freeze | No new claims or major experiment conclusions |
| 2026-11-15 | Final internal review | Main PDF ready for submission |
| 2026-11-16 | Main paper target submission | Submit main paper, depending on official deadline |

## Week 1: 2026-09-14 to 2026-09-20

Goal: define the research boundary and prepare data.

Ruiqin:

- Narrow the main task: 3D grounding, 3D VQA, or embodied 3D perception.
- Build a pool of 25 to 30 candidate papers.
- Read the most relevant 8 to 12 papers first.
- Write a one-sentence problem statement.
- Decide the first dataset set: likely ScanNet v2 plus ScanRefer / ReferIt3D.

Pavel:

- Inspect 2 to 3 baseline repositories.
- Record installation cost, required dataset format, checkpoints, and expected GPU cost.
- Help identify the minimum ScanNet v2 files needed for the first baseline.

Deliverables:

- Problem statement v1
- Dataset plan v1
- Baseline candidate list
- Literature pool v1
- AutoDL data directory plan

## Week 2: 2026-09-21 to 2026-09-27

Goal: make the data and first baseline runnable.

Ruiqin:

- Freeze 8 to 10 core papers.
- Write an innovation matrix: method, input, output, weakness, reusable mechanism.
- Define 3 to 5 failure modes of current methods.

Pavel:

- Prepare ScanNet v2 minimal data.
- Run one baseline demo, inference, or data loader.
- Create a reproduction note with command, config, and error log if it fails.

Deliverables:

- Core paper list
- Failure mode table
- At least one runnable baseline or data loader
- Unified data path config
- Experiment log format

Decision rule:

If no baseline or data loader works by 2026-09-27, shrink the task immediately.

## Week 3: 2026-09-28 to 2026-10-04

Goal: propose 2 to 3 candidate ideas and run minimal tests.

Ruiqin:

- Write candidate idea A / B / C as mechanisms, not model names.
- For each idea, define expected behavior and failure condition.
- Design the smallest experiment for each idea.

Pavel:

- Implement the smallest version of candidate A and B.
- Run short-epoch or 10 to 20 percent data smoke tests.

Deliverables:

- Candidate idea document
- Minimal experiment design
- Smoke test result v1
- Risk and cost estimate for each idea

## Week 4: 2026-10-05 to 2026-10-11

Goal: eliminate weak ideas and choose the final story.

Ruiqin:

- Compare candidate ideas by evidence, novelty, cost, and paper story.
- Simulate three reviewer objections: novelty, evidence, clarity.
- Make the final Go / No-Go decision.

Pavel:

- Add second seed or second setting for ideas with positive trend.
- Run the most important ablation needed to test the mechanism.

Deliverables:

- Go / No-Go decision record
- One main idea
- At most one auxiliary idea
- Frozen paper story line

Decision rule:

After 2026-10-11, do not keep switching ideas unless the main idea completely fails.

## Week 5: 2026-10-12 to 2026-10-18

Goal: produce main result v1.

Ruiqin:

- Define the main table and the minimum acceptable evidence chain.
- Start writing the method outline while experiments run.

Pavel:

- Train the main method.
- Run key baselines under the same protocol.
- Prepare at least one key ablation.

Deliverables:

- Main table v1
- Key ablation v1
- Generalization or cross-setting result v1
- Stability judgment

Decision rule:

If the main metric is unstable, look for mechanism, robustness, or efficiency evidence, but only if the evidence is clear.

## Week 6: 2026-10-19 to 2026-10-25

Goal: finish the core experiment package.

Ruiqin:

- Interpret results and decide which experiments are necessary for the paper.
- Organize failure cases and method limitations.

Pavel:

- Complete the main table.
- Complete core ablations.
- Run one reviewer-facing robustness or generalization experiment.
- Make every number traceable to config, seed, log, and checkpoint.

Deliverables:

- Main table
- Core ablation table
- One robustness or generalization result
- Failure cases
- Experiment index

Decision rule:

After 2026-10-25, stop low-value expansion experiments.

## Week 7: 2026-10-26 to 2026-11-01

Goal: start serious paper writing.

Ruiqin:

- Write the one-sentence claim.
- Write three contributions.
- Draft Introduction, Method, Experiment Setup, and Main Results.
- Sketch the main figure.

Pavel:

- Provide exact commands, configs, and result tables for the paper.
- Help regenerate clean figures and tables.

Deliverables:

- Paper v0 at 60 to 70 percent
- Main figure draft
- Main table draft
- Contribution list

## Week 8: 2026-11-02 to 2026-11-08

Goal: move from paper v0 to paper v1.

Ruiqin:

- Finish Related Work, Ablation, Analysis, and Failure Cases.
- Build a reviewer issue list.
- Rewrite the story for clarity.

Pavel:

- Run only high-value missing experiments.
- Verify table numbers and figure scripts.

Deliverables:

- Paper v1
- Reviewer issue list
- 90 percent figures and tables
- Supplement outline

## Week 9: 2026-11-09 to 2026-11-15

Goal: freeze the method and prepare the submission package.

Ruiqin:

- Freeze the method on 2026-11-09.
- Freeze content on 2026-11-13.
- Polish writing, figures, citations, notation, and anonymity.
- Export and inspect the final PDF.

Pavel:

- Freeze code and experiment logs.
- Prepare README commands for minimal reproduction.
- Check that all paper numbers match logs.

Deliverables:

- Main paper PDF ready
- Code snapshot
- Experiment log archive
- Supplement checklist
- Submission metadata: title, authors, abstract, keywords

## Week 10: 2026-11-16 to 2026-11-23

Goal: submit the main paper and finish supplement.

Ruiqin:

- Submit the main paper around 2026-11-16, depending on the official deadline.
- Finish supplement text.
- Check final archive.

Pavel:

- Prepare extra visualizations, code notes, and reproduction commands.
- Help verify supplement experiments.

Deliverables:

- Main paper submitted
- Supplement ready
- Final backup of paper, supplement, code, logs, tables, and checkpoints index

## This Week Immediate Tasks

For 2026-09-14 to 2026-09-20:

- Decide whether the first track is 3D grounding or 3D VQA.
- Download only the minimal ScanNet v2 files needed for the first baseline.
- Prepare ScanRefer / ReferIt3D annotations if the track is 3D grounding.
- Choose the first baseline repository.
- Write `docs/problem_statement.md`.
- Write `datasets/DATASET_PLAN.md`.

## Weekly Meeting Questions

Every Friday, answer these seven questions:

1. What did we actually falsify this week?
2. What is the mechanism evidence for the main idea?
3. What is the most dangerous reviewer objection?
4. Which experiment looks nice but is not necessary?
5. Are code, data protocol, and logs reproducible?
6. What is the most important Go / No-Go decision next week?
7. If we had to submit today, can we explain the core claim in one sentence?

