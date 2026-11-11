# Diagnostic Engine — Student Academic Tutor

## Purpose
The Diagnostic Engine identifies a student's current knowledge state before teaching begins. It detects prerequisite gaps, determines the appropriate entry point into a topic, and feeds results into the Personalised Learning Engine. Never skip diagnosis — assumptions about student knowledge lead to mismatched instruction.

---

## 1. Opening Diagnostic Questions by Subject Area

### Mathematics
- "Can you solve this equation for x: 3x + 7 = 22?"
- "What is the derivative of x²?"
- "Expand and simplify: (x + 3)(x − 2)"
- "Sketch the graph of y = sin(x) for 0 ≤ x ≤ 2π"

### Physics
- "A ball is thrown upward at 10 m/s. How high does it go? (g = 10 m/s²)"
- "What is the difference between speed and velocity?"
- "State Ohm's Law."

### Chemistry
- "Balance this equation: H₂ + O₂ → H₂O"
- "What is the difference between an atom and a molecule?"
- "Describe what happens during electrolysis."

### Biology
- "Describe the process of mitosis in three sentences."
- "What is the role of ATP in a cell?"
- "Explain natural selection using an example."

### Economics
- "What is the difference between a normative and a positive economic statement?"
- "Draw a supply and demand diagram and label the equilibrium point."

### English / Essay Subjects
- "Read this paragraph and identify the main argument."
- "What is the difference between a theme and a motif?"
- "Write one sentence that evaluates the effectiveness of a metaphor."

### History / Humanities
- "What do historians mean by 'causation'?"
- "Give two causes of [a topic-relevant event]."
- "What is the difference between a primary and secondary source?"

---

## 2. Identifying Prerequisite Gaps

When a student struggles with a topic, the root cause is often a gap in a **prerequisite concept**, not the topic itself. The diagnostic engine must trace errors back to their source.

### Detection Protocol
1. Set a topic-level question (e.g., differentiation).
2. If the student answers incorrectly or incompletely, probe one level deeper.
3. Continue probing until the student answers correctly — this is the **knowledge floor**.
4. Everything between the floor and the target topic becomes the **repair zone**.

### Example — Calculus Student with Weak Algebra

| Symptom | Root Cause |
|---|---|
| Cannot differentiate x³ + 2x | May not understand index notation |
| Cannot expand (x+1)² | Weak on binomial expansion |
| Differentiates incorrectly: dy/dx of 3x = 3x | Doesn't know the power rule |
| Substitutes x = 2 into formula incorrectly | Arithmetic or substitution error |

Probe these in reverse order. Fix the deepest gap first.

---

## 3. Prerequisite Dependency Graphs

### A-Level Mathematics — Calculus Topic

```
Arithmetic & Number Sense
        ↓
Algebraic Manipulation (expand, factorise, simplify)
        ↓
Index Laws (xⁿ × xᵐ = xⁿ⁺ᵐ)
        ↓
Coordinate Geometry (gradient of a line)
        ↓
Functions and Notation (f(x), domain, range)
        ↓
Limits (informal understanding)
        ↓
Differentiation from First Principles
        ↓
Power Rule (d/dx of xⁿ = nxⁿ⁻¹)
        ↓
Chain / Product / Quotient Rules
        ↓
Integration (reverse differentiation)
        ↓
Definite Integrals and Area Under a Curve
```

**Rule:** Do not teach any node until all parent nodes are secure.

### Physics — Electricity

```
Arithmetic and Units
        ↓
Basic Atomic Structure
        ↓
Charge and Current
        ↓
Potential Difference (Voltage)
        ↓
Resistance and Ohm's Law
        ↓
Series and Parallel Circuits
        ↓
Power and Energy in Circuits
```

### Biology — Genetics

```
Cell Structure (nucleus, chromosomes)
        ↓
DNA Structure and Base Pairing
        ↓
Mitosis (cell replication)
        ↓
Meiosis (gamete formation)
        ↓
Mendelian Inheritance (dominant/recessive)
        ↓
Genetic Crosses and Punnett Squares
        ↓
Codominance, Sex-Linkage, Mutations
```

---

## 4. Short vs Full Diagnostic Procedures

### Short Diagnostic (3–5 minutes)
Use when:
- Student has specified a clear topic (e.g., "I need help with quadratic equations")
- Time is limited
- Topic is narrow and self-contained

**Protocol:**
1. Ask 3 targeted questions on the specific topic.
2. Ask 1–2 prerequisite probing questions if errors appear.
3. Classify: *Secure*, *Partial*, or *Needs Repair*.

### Full Diagnostic (10–20 minutes)
Use when:
- Student is new and no prior data exists
- Student has generalised difficulty ("I'm struggling with maths")
- Student is preparing for a major examination

**Protocol:**
1. Work through each major topic cluster with 1–2 representative questions.
2. Record performance per cluster.
3. Identify 3–5 priority repair zones.
4. Output a full diagnostic report (see Section 6).

---

## 5. Interpreting Diagnostic Results

### Classification Scale

| Score | Classification | Action |
|---|---|---|
| 0–40% | Foundational gaps | Begin prerequisite repair immediately |
| 41–65% | Partial understanding | Targeted gap-filling before advancing |
| 66–80% | Mostly secure | Light revision of weak sub-topics, then advance |
| 81–100% | Mastered | Advance to next topic; use extension challenges |

### Error Pattern Analysis
- **Consistent error type** (e.g., always forgets negative when differentiating) → Misconception; use Misconception Engine.
- **Random errors with no pattern** → Likely carelessness or test anxiety; reinforce checking habits.
- **Correct reasoning, wrong arithmetic** → Algebra/arithmetic gap, not conceptual gap.
- **Cannot attempt question** → Concept is entirely unknown; begin from scratch.

---

## 6. Example Full Diagnostic — A-Level Maths (Calculus)

**Step 1: Prerequisite Check**

> "Simplify: x³ × x⁴"
> Expected: x⁷ | Tests: index laws

> "Expand: (2x − 1)(x + 3)"
> Expected: 2x² + 5x − 3 | Tests: algebraic manipulation

> "Find the gradient of the line joining (1, 2) and (3, 8)"
> Expected: 3 | Tests: coordinate geometry

**Step 2: Core Calculus Questions**

> "Differentiate: f(x) = x⁵"
> Expected: f'(x) = 5x⁴ | Tests: power rule

> "Differentiate: y = 3x² − 4x + 7"
> Expected: dy/dx = 6x − 4 | Tests: sum rule

> "Find the stationary points of y = x³ − 3x"
> Expected: set dy/dx = 0, solve | Tests: application

**Step 3: Interpretation**

If the student correctly handles Step 1 but fails Step 2 → teach the power rule.
If the student fails Step 1 → repair algebra/index laws before touching calculus.

---

## 7. What to Do with Diagnostic Results

### Decision Tree

```
Is the student at or above 80% on prerequisite topics?
├── YES → Begin target topic lessons immediately
└── NO  → Identify deepest gap
         ├── Single gap → Run a focused repair lesson (20–30 min)
         └── Multiple gaps → Schedule repair pathway (oldest/deepest first)
                            → Reassess after each repair before advancing
```

### Repair vs Advance Policy
- **Repair first** when gaps are foundational (prerequisite nodes).
- **Advance with scaffolding** when gaps are minor or non-blocking.
- **Never skip prerequisite repair** in STEM subjects — gaps compound rapidly.
- In essay subjects, gaps are often skill-based (analysis, structure) not knowledge-based; remediate through modelled examples and guided practice.

### After Diagnosis — Output to Learning Engine
Emit the following structured summary:

```
DIAGNOSTIC RESULT
-----------------
Student: [Name or ID]
Subject: [Subject]
Topic Target: [e.g., Differentiation]
Prerequisite Status:
  - Index Laws: SECURE
  - Algebraic Manipulation: PARTIAL (errors with negative coefficients)
  - Functions: SECURE
Target Topic Status: NOT STARTED
Recommended Entry Point: Repair algebraic manipulation (1 session), then begin power rule
Priority Misconceptions Flagged: None yet
```

Pass this output to the Personalised Learning Engine to generate the student's pathway.
