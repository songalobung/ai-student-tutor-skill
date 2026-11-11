# Benchmark Test Suite Specification & Operational Plan

This document outlines the operational benchmark framework designed to evaluate the Student Academic Tutor. 

> **Important Distinction**: The target metrics cited in this specification (e.g., $\ge 99.5\%$ subject calculation accuracy, $\ge 95\%$ misconception detection) represent **target pass criteria for system qualification**, not measured empirical performance. Empirical evaluation data is recorded separately in `evaluation/model-benchmarks/`.

---

## 1. Structure of the Proposed 2,000-Item Benchmark Suite

The full 2,000-item suite is designed across five core disciplines and general academic domains:

| Subject Domain | Proposed Target Items | In-Repository Executable Golden Items | Primary Focus Area |
|---|---|---|---|
| **Mathematics** | 500 items | 10 verified items (Set M-01) | Derivations, proof verification, algebra, calculus, "Show me where I went wrong" |
| **Physics** | 300 items | 5 verified items (Set P-01) | Mechanics, vectors, dimensional analysis, circuit laws |
| **Chemistry** | 300 items | 5 verified items (Set C-01) | Stoichiometry, equilibrium, redox, organic mechanisms |
| **Biology** | 300 items | 5 verified items (Set B-01) | Genetics, physiology, cellular energetics, experimental design |
| **Economics** | 200 items | 5 verified items (Set E-01) | Positive vs. normative analysis, elasticity, market failure |
| **Other Subjects** | 400 items | 10 verified items (Set O-01) | CS, history, English literature, psychology, accounting |
| **Total** | **2,000 items (Target)** | **40 Reference Golden Items** | Systematic evaluation across all 15 capabilities |

*The initial reference set of 40 fully worked, scored golden test items is maintained in `evaluation/golden-datasets/reference-items-v1.json`.*

---

## 2. Evaluation Dimensions & Target Thresholds

When evaluating an LLM agent loaded with this skill, trials are graded across six explicit dimensions:

```
[System Evaluation Run]
   |-- 1. Subject Calculation Accuracy (Target: >= 99.5% on quantitative steps)
   |-- 2. Misconception Detection Rate (Target: >= 95.0% on deliberate error cases)
   |-- 3. Academic Integrity Compliance (Target: 100% adherence to pedagogical boundaries)
   |-- 4. Scaffolding Pacing (Target: >= 85% of remedial responses use guided prompts)
   |-- 5. Anti-Hallucination Grounding (Target: 0.0% fabricated citations or syllabus codes)
   \-- 6. Learning Gain Delta (Target: Normalized gain g >= 0.65 on pre/post trials)
```

---

## 3. Evaluation Procedure & Runner

To run a benchmark trial:
1. Load `SKILL.md` into the target model environment (Claude, Gemini, Codex, etc.).
2. Present items from `evaluation/golden-datasets/` without system prompt leakage.
3. Record the model's unedited response.
4. Score the response using the deterministic rubrics in `assessments/marking-rubrics.md`.
5. Log scores and error discrepancies in `evaluation/model-benchmarks/`.
