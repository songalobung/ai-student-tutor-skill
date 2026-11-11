# Evaluation Criteria: Learning Outcomes & Delayed Retention

The primary standard of an educational AI is not conversational engagement or user praise, but measurable, persistent learning. This protocol defines the longitudinal validation methodology for measuring academic gains.

---

## 1. Experimental Design: The Pre/Post/Delayed Paradigm

To establish empirical efficacy, instructional trials must execute a 4-phase evaluation protocol:

```
[Phase 1: Pre-Test] (3 unassisted diagnostic items -> Baseline Score S_pre)
        |
        v
[Phase 2: Instructional Intervention] (AI delivers personalized lesson / guided practice)
        |
        v
[Phase 3: Immediate Post-Test] (3 isomorphic items -> Post Score S_post)
        |
        v
[Phase 4: Delayed Post-Test (+72 hrs)] (3 transfer items -> Retention Score S_delay)
```

---

## 2. Quantitative Metrics & Calculation

### 2.1 Normalized Learning Gain ($g$)
Calculated according to Hake's normalized gain metric:

$$g = \frac{S_{\text{post}} - S_{\text{pre}}}{100 - S_{\text{pre}}}$$

- **High Gain**: $g \ge 0.70$
- **Medium Gain**: $0.30 \le g < 0.70$
- **Low Gain**: $g < 0.30$
- **Target Threshold for Tutor Certification**: $g \ge 0.65$ across all standard curricular units.

### 2.2 Retention Index ($R_{\text{index}}$)
Measures the durability of learned material against the forgetting curve:

$$R_{\text{index}} = \frac{S_{\text{delay}}}{S_{\text{post}}}$$

- **Target Threshold**: $R_{\text{index}} \ge 0.85$ (meaning at least 85% of immediately demonstrated understanding persists after 72 hours without re-studying).

---

## 3. Near vs. Far Conceptual Transfer

Validation items must distinguish between superficial pattern matching and deep conceptual transfer:

1. **Near Transfer (Isomorphic)**: Same underlying mathematical structure and context, differing only in numerical values.
2. **Far Transfer (Novel Context)**: Same underlying conceptual principle embedded within an entirely distinct physical, economic, or situational framework.
   - *Example*: Student learns exponential decay via radioactive half-life (Physics), then is tested on capacitor discharge (Physics) or drug metabolism elimination half-life (Pharmacology/Biology).
   - High performance on far transfer confirms genuine conceptual abstraction rather than procedural mimicry.

