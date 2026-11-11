# Worked Examples

## Why Worked Examples Reduce Cognitive Load

Cognitive load theory (Sweller, 1988; van Merriënboer & Sweller, 2005) distinguishes between three types of cognitive load:

- **Intrinsic load:** The inherent complexity of the material itself
- **Extraneous load:** Unnecessary cognitive effort caused by poor instructional design
- **Germane load:** Productive cognitive effort directed toward schema formation

When novice learners encounter a problem without guidance, they typically resort to means-ends analysis — a weak, inefficient search strategy that uses most of working memory for problem-solving mechanics and leaves little capacity for learning the underlying structure. Worked examples replace means-ends analysis with a goal-free study of the solution procedure, freeing working memory for the development of problem schemas.

**Research finding (Sweller & Cooper, 1985):** Novice students who studied worked examples before practice problems significantly outperformed those who attempted all problems, completing them faster and with fewer errors. This "worked example effect" is strongest with novices and diminishes as expertise grows — an important signal for when to remove worked examples.

**Implication for AI tutoring:** When a student is new to a topic or has demonstrated failure on a problem type, default to a worked example before asking them to practise. Do not give them five problems and correct all five from scratch.

---

## Fully Narrated Worked Example Format

A fully narrated worked example explains every step, including the reasoning behind it, not just the mechanical execution.

### Structure:
1. **State the problem type and goal** — What kind of problem is this? What are we trying to find?
2. **Identify the relevant knowledge** — What formula, rule, or principle applies?
3. **Execute each step — show and explain** — What is happening at each step, and why?
4. **State the result and check** — What is the answer? Does it make sense?

### Example — Quadratic Equation (Mathematics)

> **Problem:** Solve x² − 5x + 6 = 0
>
> **Step 1 — Identify the problem type:**  
> This is a quadratic equation in the form ax² + bx + c = 0, with a = 1, b = −5, c = 6. I'll try factorising first because a = 1 and the numbers are small.
>
> **Step 2 — Factorise:**  
> I need two numbers that multiply to c (= 6) and add to b (= −5). Those are −2 and −3.  
> So: x² − 5x + 6 = (x − 2)(x − 3)
>
> **Step 3 — Solve:**  
> Setting each factor to zero:  
> x − 2 = 0 → x = 2  
> x − 3 = 0 → x = 3
>
> **Step 4 — Check:**  
> Substitute x = 2: 4 − 10 + 6 = 0 ✓  
> Substitute x = 3: 9 − 15 + 6 = 0 ✓
>
> **Result:** x = 2 or x = 3

After the worked example, ask: *"Before I give you a practice problem, can you explain back to me what we did in Step 2 and why?"*

---

## Completion Problems (Student Fills In Remaining Steps)

A completion problem provides the initial steps of a worked example and asks the student to complete the remainder. This is an intermediate scaffold between a full worked example and an independent problem.

### Why Use Completion Problems:
- Reduces initial cognitive load while still requiring productive thinking
- Ensures students engage actively rather than passively reading a solution
- Allows the tutor to pinpoint exactly where in the procedure a student gets stuck

### Format:

> **Problem:** Solve 2x² + 7x + 3 = 0
>
> **Step 1 (provided):** This is a quadratic with a = 2, b = 7, c = 3. Since a ≠ 1, I'll use the quadratic formula:
> x = (−b ± √(b² − 4ac)) / 2a
>
> **Step 2 (provided):** Substituting values:  
> x = (−7 ± √(49 − 24)) / 4  
> x = (−7 ± √25) / 4
>
> **Your turn — complete steps 3 and 4:**

Evaluate the student's completion. If they make an error, identify the exact step and explain the error without redoing the whole problem.

---

## Fading Worked Examples (Progressive Reduction of Guidance)

Fading involves gradually removing the amount of guidance provided across a sequence of problems, moving from full worked example → completion problem → independent problem. This matches the gradual release of responsibility model and prevents the "worked example dependency" effect.

### Fading Sequence for a Problem Type:

| Problem | Scaffold Level |
|---|---|
| Problem 1 | Full narrated worked example (tutor does all) |
| Problem 2 | Completion problem: first 60% provided |
| Problem 3 | Completion problem: first 30% provided |
| Problem 4 | Completion problem: first step and method named only |
| Problem 5 | Independent problem: no scaffold |

This sequence can be compressed (3 problems) for simpler procedures or expanded (6–8 problems) for complex multi-step tasks.

**Trigger to accelerate fading:** If the student correctly and confidently explains a step in the worked example before you have presented it, skip one level of fading.

**Trigger to slow fading:** If the student's completion problem shows an error that reveals a conceptual misunderstanding (not an arithmetic slip), return to a full narrated example for that specific concept.

---

## Comparing and Contrasting Examples

Presenting two or more worked examples simultaneously and asking students to identify similarities and differences produces better transfer than studying one example at a time (Rittle-Johnson & Star, 2007).

### How to Structure Comparison:

1. Present two worked examples side by side (or sequentially with explicit comparison prompt)
2. Ask: *"What is the same about how I approached both problems?"*
3. Ask: *"What is different? Why did I use a different step here?"*
4. Ask: *"Which method is more efficient here, and why?"*

### Example — Two Methods for Solving Simultaneous Equations:

**Example A (Substitution):**  
> y = 2x + 1 and 3x + y = 10  
> Substitute: 3x + (2x + 1) = 10 → 5x = 9 → x = 1.8

**Example B (Elimination):**  
> 2x + y = 7 and x + y = 4  
> Subtract: x = 3, then y = 1

> *"Looking at both methods — why did I choose substitution for Example A but elimination for Example B? When would you choose each?"*

Comparison examples are particularly effective for topics with multiple valid methods (e.g., solving equations, integrating functions, structuring essays).

---

## Incorrect Worked Examples (Error Identification)

Presenting a worked example that contains a deliberate error, then asking the student to identify and correct it, produces learning at least as effective as correct examples (Booth et al., 2013). Error-finding tasks:
- Activate deeper processing of each step
- Help students diagnose common misconceptions in themselves
- Build self-monitoring skills

### Format:

> *"The following solution contains an error. Find the mistake and explain what should have been done instead."*
>
> **Problem:** Expand and simplify (x + 3)²
>
> **Student's working (incorrect):**  
> (x + 3)² = x² + 9  ← **ERROR IS HERE**
>
> *"What is wrong? Why is this wrong? What is the correct answer?"*

After the student identifies the error, ask them to show the correct working in full. If they cannot identify the error after reasonable thought, provide the correction and ask them to explain why the correction is right.

**Caution:** Incorrect worked examples can reinforce the error if the student fails to notice the mistake and the correction is not followed up carefully. Always require the student to produce the correct solution after an error-identification task.

---

## Subject-Specific Worked Example Formats

### Mathematics
Full narration with every algebraic step shown. No skipped steps for novice learners. Use fading sequences for each new procedure type.

### Physics
Show: identification of physical scenario → relevant formula → substitution → calculation → unit checking → sense-checking the magnitude of the answer.

> *"The answer is 9.8 m/s² — does that seem physically reasonable for a falling object near Earth? Yes — that's the acceleration due to gravity."*

### Chemistry
Show: identification of reaction type → balanced equation (or stoichiometric reasoning) → calculation. For organic chemistry: draw out the mechanism step by step, naming each stage (e.g., electrophilic addition, nucleophilic substitution).

### Essay Writing (History, English, Economics)
Annotated model paragraph — write a paragraph and then comment on each sentence:

> *"This sentence is the **point** — it makes a direct claim. This sentence is the **evidence** — it supports the claim with specific detail. This sentence is the **explanation** — it connects evidence back to the question. This sentence is the **evaluation** — it weighs the significance of the point."*

### Biology
Diagram-based worked examples: draw a process (e.g., protein synthesis, heart cycle) step by step with narration explaining the biological reason for each step.

### Economics
Diagram analysis: draw a supply and demand diagram step by step, narrating the economic reasoning at each stage. Show how to annotate diagrams for exam purposes, including labelling axes, shading welfare triangles, and writing explanatory notes.

---

## References

Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction*, 2(1), 59–89.

Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257–285.

van Merriënboer, J. J. G., & Sweller, J. (2005). Cognitive load theory and complex learning: Recent developments and future directions. *Educational Psychology Review*, 17(2), 147–177.

Rittle-Johnson, B., & Star, J. R. (2007). Does comparing solution methods facilitate conceptual and procedural knowledge? An experimental study on learning to solve equations. *Journal of Educational Psychology*, 99(3), 561–574.

Booth, J. L., Lange, K. E., Koedinger, K. R., & Newton, K. J. (2013). Using example problems to improve student learning in algebra: Differentiating between correct and incorrect examples. *Learning and Instruction*, 25, 24–34.
