# Evaluation Criteria: Subject Accuracy & Factual Correctness

Academic accuracy is non-negotiable. An intelligent tutoring system that delivers fluent but mathematically or conceptually flawed explanations damages student learning and destroys academic trust.

---

## 1. Subject-Specific Accuracy Standards

### 1.1 Mathematics & Quantitative Computing
- **Absolute Computational Integrity**: Zero tolerance for algebraic missteps, incorrect negative signs, erroneous index arithmetic, or faulty integration/differentiation.
- **Notation Rigor**: Use formal mathematical notation via standard LaTeX formatting. Distinguish between strict inequalities ($<, >$) and non-strict inequalities ($\le, \ge$). Use proper interval notation ($[a, b]$ vs. $(a, b)$).
- **Proof Completeness**: Proofs (e.g., proof by induction, proof by contradiction) must explicitly state base cases, inductive hypotheses, algebraic derivations, and formal concluding statements.

### 1.2 Natural Sciences (Physics, Chemistry, Biology)
- **Unit Precision**: Every physical quantity must include its correct SI or derived unit (e.g., $\text{J}$, $\text{N}\cdot\text{m}$, $\text{mol/dm}^3$, $\text{m/s}^2$). Dimensional analysis must balance across all derivations.
- **Micro-Macro Coherence**: In chemistry, never conflate macroscopic properties (melting point, color) with atomic properties (electronegativity, bond energy). For example: *"Sodium chloride has a high melting point because of strong electrostatic attractions throughout its giant ionic lattice"*, never *"because the NaCl molecule is strong"*.
- **Thermodynamics vs. Kinetics**: Clearly separate kinetic claims (rate of reaction, activation energy) from thermodynamic claims (equilibrium position, $\Delta G$, $\Delta H$).

### 1.3 Humanities & Social Sciences (Economics, History, Psychology, English)
- **Factual & Chronological Accuracy**: Primary events, treaties, economic policy acts, and empirical studies must have verified names, dates, and documented outcomes.
- **Distinguishing Theory from Empirics**: In economics and psychology, clarify whether a conclusion is an axiomatic deduction from a theoretical model (under *ceteris paribus* assumptions) or an observed empirical consensus.

---

## 2. Test Suite Validation Scoring

For automated evaluation passes across the 2,000-item benchmark suite:
- **Pass Threshold**: $\ge 99.5\%$ calculation and factual correctness.
- **Critical Fails (Immediate Rejection)**:
  1. Generating an incorrect numerical answer to an algebraic equation or calculus integral.
  2. Stating an incorrect chemical formula or unbalanced equation.
  3. Reversing historical causation or inventing non-existent legal/constitutional clauses.
  4. Misidentifying the direction of an economic curve shift.

