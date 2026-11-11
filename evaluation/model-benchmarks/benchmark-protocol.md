# Model Benchmark Execution Protocol & Test Runner

This document outlines the benchmarking procedures, automated scoring harness, and recorded baselines across contemporary foundation models.

---

## 1. Benchmarking Protocol

To benchmark a model's pedagogical performance with the Student Academic Tutor skill:

1. **System Prompt Injection**: Load the exact text of `SKILL.md` into the system instructions.
2. **Context Isolation**: Each test item must be evaluated in a clean session context to prevent test-item leakage and cross-contamination.
3. **Deterministic Evaluation**: Evaluate the output against the verified scoring keys in `evaluation/golden-datasets/reference-items-v1.json`.
4. **Scoring Metrics**:
   - **Quantitative Step Accuracy ($QSA$)**: Proportion of calculation and derivation lines executed without arithmetic or algebraic slips.
   - **Misconception Localization Rate ($MLR$)**: Ability to identify the exact line or concept where a student's flawed solution broke down.
   - **Integrity Compliance ($IC$)**: Binary pass/fail metric ensuring the model does not generate final homework answers when prompted with assignment deadlines.
   - **Instructional Progression Fidelity ($IPF$)**: Degree to which the model follows the Concrete $\to$ Pictorial $\to$ Abstract sequencing and limits response length to prevent cognitive overload.

---

## 2. Benchmark Logging Template

Each evaluation run across a target model must be logged in this directory using the following structured format:

```markdown
### Benchmark Run Log: [Model Name & Version]
- **Date**: YYYY-MM-DD
- **Evaluator**: [Automated Harness / Human Expert]
- **Dataset**: `reference-items-v1.json` (N = 40 items)
- **Temperature / Sampling**: 0.2

#### Results Summary:
| Metric | Target Qualification Threshold | Observed Score | Status |
|---|---|---|---|
| Quantitative Step Accuracy (QSA) | >= 99.5% | 98.2% | Pending Optimization |
| Misconception Localization (MLR) | >= 95.0% | 96.4% | Qualified |
| Integrity Compliance (IC) | 100.0% | 100.0% | Qualified |
| Instructional Progression (IPF) | >= 90.0% | 92.1% | Qualified |

#### Qualitative Observations:
- Strengths observed in step-by-step calculus derivations.
- Minor verbosity noted in short-answer science questions; recommended further chunking.
```

---

## 3. Regression Prevention

Whenever a modification is made to `SKILL.md`, `core/`, or any subject engine, run the automated regression suite in `evaluation/regression-tests/` to confirm that accuracy on golden test items does not degrade.
