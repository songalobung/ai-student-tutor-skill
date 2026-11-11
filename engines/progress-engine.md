# Academic Progress Tracking Engine

The Progress Engine monitors, calculates, and maintains a granular, topic-level model of student mastery over time. Rather than reducing a student's capability to a single holistic percentage or letter grade, this engine evaluates multidimensional competency across discrete syllabus objectives.

---

## 1. Topic-Level Mastery Criteria

Mastery is defined as durable, independent, and generalizable competence. A topic is categorized into one of four mastery states:

| Mastery Level | Score Threshold | Behavioral Indicators | Recommended Action |
|---|---|---|---|
| **Novice** | 0% – 49% | Relies heavily on scaffolding; frequent fundamental misconceptions; cannot solve unassisted. | Diagnostic review of prerequisite foundations; concrete worked examples. |
| **Developing** | 50% – 74% | Understands basic definitions; solves routine problems with minor hints; struggles with multi-step or non-standard questions. | Guided practice; scaffolded problem solving; error analysis. |
| **Proficient** | 75% – 89% | Consistently solves standard curriculum problems independently; explains conceptual mechanisms correctly; minimal hints needed. | Independent practice; timed questions; retrieval practice. |
| **Mastered** | 90% – 100% | Solves complex, unfamiliar, and synoptic exam-style problems with high accuracy and speed; demonstrates retention after delay. | Spaced review intervals extended; introduce extension/interdisciplinary tasks. |

---

## 2. Multidimensional Mastery Calculation

Mastery scores must not be derived solely from single in-lesson performance. The engine weights four key factors:

$$\text{Mastery Score} = 0.35(A) + 0.25(I) + 0.20(C) + 0.20(R)$$

1. **Accuracy ($A$)**: Percentage of correct solutions across questions attempted.
2. **Independence ($I$)**: Proportion of questions completed without requesting hints or step-by-step guidance.
3. **Complexity Level ($C$)**: Ratio of routine recall questions to multi-step analytical/evaluative questions successfully solved.
4. **Delayed Retention ($R$)**: Performance on retrieval practice questions presented across subsequent sessions.

---

## 3. Progress State Schema

The tutor updates an internal progress state during learning dialogues. Format representation:

```json
{
  "student_id": "session_learner_01",
  "subject": "Mathematics",
  "curriculum": "Cambridge A-Level",
  "topic_progress": {
    "pure_algebra_polynomials": {
      "mastery_level": "Proficient",
      "score": 82,
      "last_tested": "2026-11-04",
      "persistent_errors": ["Sign errors in polynomial long division"]
    },
    "differentiation_chain_rule": {
      "mastery_level": "Developing",
      "score": 64,
      "last_tested": "2026-11-10",
      "persistent_errors": ["Omitting inner function derivative"]
    },
    "integration_by_parts": {
      "mastery_level": "Novice",
      "score": 35,
      "last_tested": "2026-11-11",
      "persistent_errors": ["Incorrect selection of u and dv/dx via LIATE rule"]
    }
  },
  "overall_trajectory": "Steady Improvement",
  "confidence_calibration_gap": "+15% (Overconfident on integration)"
}
```

---

## 4. Identifying Warning Signs

1. **The Plateau Effect**: When a student repeatedly stalls at 60–70% on a specific topic, do not provide more identical drill questions. Intervene by diagnosing foundational prerequisites from earlier curricula.
2. **Confidence-Accuracy Mismatch**:
   - *Overconfidence*: High student self-rating paired with recurring errors. Intervene with gentle, objective diagnostic challenges.
   - *Imposter Hesitancy*: Student repeatedly scores >90% but hesitates to attempt independent tasks or expresses fear of failure. Intervene by pointing to objective performance data and gradually removing reassurance scaffolding.
3. **Fluency Illusion**: Student follows worked examples fluently, mistaking recognition for generative mastery. Force an immediate "cover-and-solve" unassisted retrieval check before marking the topic proficient.

