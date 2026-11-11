# Evaluation Criteria: Pedagogical Quality & Instructional Effectiveness

Evaluating an educational AI requires measuring instructional behavior, diagnostic sensitivity, feedback utility, and adaptive pacing rather than raw text generation fluency.

---

## 1. Core Pedagogical Rubric

Evaluate each tutoring interaction across five instructional pillars:

| Pillar | Unsatisfactory (Score 1) | Competent (Score 2) | Exemplary (Score 3) |
|---|---|---|---|
| **1. Diagnostic Grounding** | Jumps immediately into lecture or full answer without assessing prior knowledge. | Briefly asks what the student knows before explaining. | Administers a calibrated prerequisite check; isolates missing foundational gaps. |
| **2. Scaffolding & Gradual Release** | Provides the complete solution immediately, creating answer dependency. | Gives hints when requested, but hints are overly direct or vague. | Uses Socratic questioning; provides targeted hints; fades support systematically. |
| **3. Misconception Rectification** | Merely marks answer wrong and provides the correct version. | Explains why the answer is wrong in general terms. | Identifies the precise cognitive flaw; explains the mechanism; tests with an isomorphic counter-item. |
| **4. Cognitive Load Management** | Overwhelms student with multiple dense paragraphs and simultaneous new terms. | Explains concepts clearly, but introduces abstract ideas before concrete examples. | Uses Concrete $\to$ Pictorial $\to$ Abstract progression; chunks information; uses dual coding. |
| **5. Metacognitive Development** | Leaves student passive; no reflection or self-assessment. | Asks generic questions like "Does that make sense?" | Prompts student to explain the mechanism in their own words; calibrates confidence. |

---

## 2. Quantitative Benchmark Criteria

To achieve certification as an effective academic tutor, the LLM must attain:
1. **Scaffolding Ratio**: $\ge 85\%$ of remedial interactions must provide guided prompts or partial steps rather than terminal answers.
2. **Checking for Understanding**: 100% of concept explanations must conclude with an active diagnostic question or formative prompt.
3. **Adaptive Branching**: If a student fails a guided practice question, the tutor must branch to an alternative explanation or prerequisite check in 100% of observed cases.

