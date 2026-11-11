# Empirical Learning Experiments & Case Study Archive

This directory records empirical learning experiments, controlled trial data, and longitudinal retention case studies validating the instructional efficacy of the Student Academic Tutor.

---

## 1. Study Protocol Design (The Randomized Micro-Trial)

To test the skill's impact on actual student learning, experimental micro-trials follow a standardized 4-stage empirical protocol:

```
[Target Cohort Recruited]
           |
           v
[Stage 1: Pre-Test Diagnostic (T0)]
(Administer 3 unassisted benchmark questions -> Baseline Score S_pre)
           |
           v
[Stage 2: Instructional Intervention]
(Group A: Student Academic Tutor with Socratic Scaffolding)
(Group B: Standard Base LLM with Direct Solution Output)
           |
           v
[Stage 3: Immediate Post-Test (T1)]
(Administer 3 isomorphic transfer items -> Immediate Score S_post)
           |
           v
[Stage 4: Delayed Retention Test (T2: +72 Hours)]
(Administer 3 far-transfer items without prior notice -> Delayed Score S_delay)
```

---

## 2. Experimental Metric Formulations

1. **Normalized Learning Gain ($g$)** (Hake, 1998):
   $$g = \frac{S_{\text{post}} - S_{\text{pre}}}{100 - S_{\text{pre}}}$$
2. **Retention Durability Ratio ($RDR$)**:
   $$RDR = \frac{S_{\text{delay}}}{S_{\text{post}}}$$
   - Measures how much acquired understanding survives the forgetting curve after 72 hours.

---

## 3. Case Study Log Format

All future empirical trials conducted with students or simulated cognitive agents must be logged using the following schema:

```markdown
### Trial Record: [Study ID e.g., EXP-2026-MATH-01]
- **Date**: YYYY-MM-DD
- **Target Topic**: High School Calculus (Optimization & Related Rates)
- **Cohort Size**: N = 24 students
- **Experimental Condition**: Student Academic Tutor (ZPD Adaptive Scaffolding)
- **Control Condition**: Base LLM Unrestricted Q&A

#### Quantitative Findings:
| Metric | Tutor Condition | Control Condition | p-value / Significance |
|---|---|---|---|
| Pre-Test Mean (S_pre) | 28.4% | 29.1% | p > 0.5 (Equivalent baseline) |
| Immediate Post (S_post) | 84.2% | 88.6% | p = 0.12 (Base LLM scored slightly higher on familiar items) |
| Delayed 72h Post (S_delay)| 76.5% | 41.2% | p < 0.001 (Tutor condition retained 90.8% vs 46.5% in control) |
| Normalized Gain (g) | 0.78 (High Gain)| 0.84 (Immediate) -> 0.17 (Delayed) | Significant long-term advantage |

#### Qualitative Findings:
- Students in the control condition experienced cognitive offloading, reporting high satisfaction initially but struggling when prompted to explain the calculus mechanism without AI assistance.
- Students in the tutor condition demonstrated far-transfer success when solving novel physics optimization problems.
```
