# Student State Model & Dynamic Learner Modeling

The Student State Model maintains a probabilistic, multi-dimensional representation of a learner's cognitive state. It moves beyond static score tracking by separating demonstrated conceptual mastery from student self-reported confidence.

---

## 1. Dual-Axis State Representation: Mastery vs. Confidence

A critical failure in tutoring is conflating high student confidence with high competence (the **Dunning-Kruger quadrant**), or misinterpreting low confidence as cognitive deficiency (**Imposter hesitation**).

```
          High Confidence
                 ▲
   Dunning-Kruger│    Mastered & Calibrated
   (Overconfident│    (Accurate Self-Awareness)
   - High Error) │
─────────────────┼────────────────────────► High Mastery
   Struggling &  │    Imposter Hesitancy
   Aware         │    (High Competence
   (Ready to     │    - Anxious Hesitation)
   Learn)        ▼
          Low Confidence
```

The tutor maintains a 4-quadrant diagnostic classification:

1. **Quadrant 1 (Mastered & Calibrated)**: Accuracy $\ge 85\%$, Confidence $\ge 80\%$.
   - *Pedagogical Action*: Extend review intervals; present Tier 3 synoptic challenges; introduce interdisciplinary transfer tasks.
2. **Quadrant 2 (The Overconfidence Trap)**: Accuracy $< 60\%$, Confidence $\ge 80\%$.
   - *Pedagogical Action*: Gentle cognitive dissonance. Administer a non-routine diagnostic counter-example that reveals the flaw in their intuition without shaming.
3. **Quadrant 3 (Struggling & Aware)**: Accuracy $< 60\%$, Confidence $< 50\%$.
   - *Pedagogical Action*: High-scaffolding zone. Deploy fully narrated worked examples, decrease extraneous cognitive load, and reinforce small early wins.
4. **Quadrant 4 (Imposter Hesitancy)**: Accuracy $\ge 85\%$, Confidence $< 50\%$.
   - *Pedagogical Action*: Positive evidence feedback. Show objective historical data verifying their accuracy; gradually remove reassurance scaffolding to build self-efficacy.

---

## 2. Dynamic Bayesian Student State Vector

For each discrete curriculum syllabus objective ($k$), the state vector tracks four latent parameters:

$$S_k = \langle P(L_k), P(C_k), P(G_k), P(S_k), \tau_k \rangle$$

- $P(L_k) \in [0, 1]$: Probability of genuine latent mastery.
- $P(C_k) \in [0, 1]$: Calibrated self-efficacy / confidence rating.
- $P(G_k)$: Probability that a correct response was the result of a guess.
- $P(S_k)$: Probability that an incorrect response was a careless slip rather than a conceptual void.
- $\tau_k$: Timestamp of last active retrieval event (used by the Ebbinghaus forgetting decay function).

---

## 3. Session State Schema

During interactive tutoring dialogues, the tutor maintains the following JSON state in context:

```json
{
  "student_id": "anon_learner_92",
  "curriculum": "Cambridge A-Level (9709)",
  "subject": "Mathematics",
  "active_topic": "Calculus - Chain Rule",
  "cognitive_quadrant": "Imposter Hesitancy",
  "state_vector": {
    "P_mastery": 0.88,
    "P_confidence": 0.42,
    "consecutive_unassisted_correct": 4,
    "last_misconception_logged": "none_recent",
    "days_since_last_retrieval": 3
  },
  "recommended_action": "Affirm objective performance data and withdraw hint scaffolding."
}
```
