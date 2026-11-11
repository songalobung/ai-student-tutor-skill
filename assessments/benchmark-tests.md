# Benchmark Test Suite & Evaluation Framework

To validate that the Student Academic Tutor operates with genuine instructional intelligence rather than serving as a superficial conversational agent, this specification establishes an objective evaluation suite comprising 2,000 rigorous benchmark items.

---

## 1. Composition of the 2,000-Item Benchmark Suite

The validation dataset spans the full curriculum spectrum:

| Subject Domain | Item Count | Primary Focus Areas | Key Testing Modalities |
|---|---|---|---|
| **Mathematics** | 500 | Algebra, Calculus, Trigonometry, Linear Algebra, Probability, Statistics | Derivation verification, "Show me where I went wrong" error detection, proof construction |
| **Physics** | 300 | Mechanics, Electromagnetism, Thermodynamics, Optics, Quantum/Nuclear | Free-body analysis, dimensional checks, physical intuition vs. formula rote |
| **Chemistry** | 300 | Stoichiometry, Equilibrium, Organic Mechanisms, Electrochemistry, Bonding | 3-level representation (macro/submicro/symbolic), error distinction |
| **Biology** | 300 | Genetics, Physiology, Cellular Processes, Ecology, Experimental Design | Linked biological systems, textual diagram description, experimental controls |
| **Economics** | 200 | Microeconomics, Macroeconomics, Market Failure, International Trade, Econometrics | Positive vs. normative separation, diagram shifts, policy evaluation |
| **Other Subjects** | 400 | Computer Science, History, English, Psychology, Accounting, Geography | Code tracing, source criticism, essay rubrics, double-entry ledgers |
| **Total** | **2,000** | Full cross-curricular validation | Complete automated & human-in-the-loop scoring |

---

## 2. Evaluation Dimensions & Pass Criteria

Each system run across the benchmark suite is scored against six core pedagogical dimensions:

```
[System Evaluation Across Benchmark Suite]
   |-- 1. Subject Accuracy & Calculation Rigour (>99.5% accuracy required)
   |-- 2. Misconception Detection Rate (>95.0% correct identification of deliberate student errors)
   |-- 3. Academic Integrity Compliance (100% refusal to complete homework outright)
   |-- 4. Pedagogical Adaptation (Appropriate step-by-step scaffolding vs. answer-dumping)
   |-- 5. Anti-Hallucination & Citation Honesty (0% fabricated sources or mark schemes)
   \-- 6. Delayed Retention Impact (Measured via longitudinal pre/post-intervention delta)
```

---

## 3. Deliberately Faulty Response Test Cases

A critical subset of the benchmark tests the tutor's diagnostic capability by presenting deliberately flawed student solutions:

### Test Case Sample: Physics (Energy vs. Momentum)
- **Student Prompt**: *"A 1000 kg car traveling at 20 m/s hits a stationary 1000 kg car. They stick together. Since momentum is conserved, kinetic energy must also be conserved, so initial KE = final KE. Therefore, speed after impact is 20 m/s. Did I do this right?"*
- **Required Tutor Behavior**:
  1. Identify the conceptual misconception: An inelastic collision conserves momentum, but kinetic energy is **not** conserved (dissipated as thermal energy, deformation, sound).
  2. Compute correct momentum: $p_{\text{initial}} = (1000)(20) = 20,000\text{ kg}\cdot\text{m/s}$.
  3. Compute correct final velocity: $v_f = \frac{20,000}{2000} = 10\text{ m/s}$.
  4. Compare KE before ($(0.5)(1000)(20^2) = 200,000\text{ J}$) vs. after ($(0.5)(2000)(10^2) = 100,000\text{ J}$) to demonstrate the energy loss concretely.
  5. Validate that the tutor refrained from simply providing the answer without addressing the misconception.

---

## 4. The Pre-Test $\to$ Teach $\to$ Post-Test Protocol

To measure true learning rather than conversational satisfaction, evaluation involves a 3-stage validation cycle:
1. **Pre-Test**: Administer 3 unfamiliar diagnostic items on a target topic.
2. **Instructional Intervention**: The tutor delivers a scaffolded lesson based on pre-test gaps.
3. **Immediate Post-Test**: Administer 3 isomorphic (structurally equivalent but numerically/contextually distinct) questions.
4. **Delayed Post-Test (72 hours)**: Re-test the topic via retrieval practice to measure delayed retention.
- **Pass Threshold**: A statistically significant normalized learning gain:
  $$g = \frac{\text{Post} - \text{Pre}}{100 - \text{Pre}} \ge 0.65$$

