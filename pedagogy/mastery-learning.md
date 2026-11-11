# Mastery Learning

## Mastery Learning Theory

Mastery learning, developed by Benjamin Bloom (1968) and elaborated by Carroll (1963) and later Block (1971), is built on the proposition that virtually all students can achieve high levels of learning if given sufficient time and appropriately structured instruction. The critical departure from conventional schooling is this: in mastery learning, **time is the variable and achievement is the constant** — rather than time being fixed and achievement varying.

Bloom's Learning for Mastery (LFM) model involves:
1. Defining mastery clearly in advance (a mastery criterion)
2. Breaking curriculum into discrete units, each with its own mastery test
3. Requiring students to demonstrate mastery of each unit before proceeding
4. Providing corrective instruction to students who do not reach mastery on the first attempt
5. Administering a parallel test to confirm mastery after corrective instruction

**Core principle for AI tutoring:** A topic is not "done" when it has been taught. It is done when the student has demonstrated consistent, accurate performance at or above the mastery threshold.

---

## Mastery Thresholds

### Standard Threshold: 80–85% Accuracy
Bloom's original work and subsequent implementations typically set mastery at 80–85% accuracy on a unit assessment. This threshold:
- Is high enough to ensure solid understanding without demanding perfection
- Leaves room for careless errors that do not indicate conceptual gaps
- Has been validated across a wide range of subjects and age groups

### Applying the Threshold in AI Tutoring

For quantitative subjects (Maths, Physics, Chemistry):
- Accuracy is calculated over a minimum of 5–8 problems of similar type
- 80% = at least 4/5 or 7/8 correct
- Errors must be classified: **conceptual errors** (indicate non-mastery) vs **arithmetic slips** (may still indicate underlying mastery)

For qualitative subjects (History, English, Economics essays):
- Accuracy is replaced by rubric-score threshold: student must meet or exceed the "competent" band on 80% of rubric dimensions
- Over 2–3 assessed essay paragraphs or short answers

### Consistency Requirement
A single successful performance is not sufficient evidence of mastery. Require consistency:
- **Minimum:** Correct performance on 3 consecutive problems of the same type, OR
- **Minimum:** 80% accuracy across 5 problems drawn from the same topic

A student who solves a quadratic equation correctly once but fails the next two attempts has not demonstrated mastery.

### Time-Stability Requirement
Performance at mastery level must persist over time, not just immediately after instruction. After confirming immediate mastery:
- Administer 2–3 retrieval questions on the same topic at the next session (minimum 24 hours later)
- Mastery is confirmed if the student still performs at 80%+ without re-teaching
- If performance drops, treat as partial mastery and revisit with spaced practice

---

## What to Do When Mastery Isn't Reached

Failure to reach mastery is an instructional signal, not a student failure. The response depends on the type of error.

### Diagnostic Step (Always First)
Before re-teaching, identify the nature of the error:
> *"Can you walk me through what you were thinking when you did this step?"*

This reveals whether the error is:
- **Conceptual:** Student holds a wrong belief or uses an incorrect procedure
- **Procedural:** Student knows the concept but executes incorrectly (arithmetic, notation)
- **Retrieval failure:** Student knew this but forgot; needs retrieval practice, not re-teaching
- **Prerequisite gap:** Student lacks the foundational knowledge required for this topic

### Response Protocols by Error Type

**Conceptual error:**
- Use a different explanation approach (not the same one again)
- Try a concrete example, analogy, or visual representation
- Use the incorrect worked example format: show the student's error explicitly, then correct it
- After re-teaching, attempt a fresh parallel problem before returning to the mastery test

**Procedural error:**
- Identify the specific step where the error occurs
- Provide a targeted mini-worked example of just that step
- Ask the student to repeat the specific step several times before attempting the full problem

**Retrieval failure:**
- Confirm whether the material was understood at the time of learning (ask the student)
- If yes: implement spaced retrieval practice (not re-teaching)
- If no: revisit the concept, then immediately schedule retrieval practice

**Prerequisite gap:**
- Temporarily redirect to the prerequisite topic
- Achieve mastery of the prerequisite before returning to the current topic
- Document the gap for the student: *"Before we can fully master [Topic B], we need to solidify [Topic A]."*

---

## Prerequisite Mastery Before Advancing

Curriculum topics are not independent. Each topic rests on prerequisite knowledge. Advancing before prerequisites are mastered leads to cascading failure — the student appears to fail at Topic C when the real gap is in Topic A.

### Prerequisite Check Protocol
Before beginning a new topic:
1. Identify the 2–3 most critical prerequisites
2. Ask 2–3 diagnostic questions targeting each prerequisite
3. If the student fails a prerequisite check → redirect to that prerequisite first
4. Document the prerequisite gap so it can be addressed systematically

### Example Prerequisite Map (Mathematics)
- Quadratic equations → requires: expanding brackets, collecting like terms, basic arithmetic
- Calculus (differentiation) → requires: understanding of functions, algebraic manipulation, indices
- Integration → requires: differentiation, function notation, algebraic fractions

**Rule:** Never attempt to teach a topic if the student fails the prerequisite diagnostic. This wastes time and can create negative associations with the advanced topic.

---

## Mastery vs Performance: Temporary vs Durable Knowledge

**Performance** refers to what a student can do immediately, right after instruction or during a practice session. **Mastery** refers to durable, long-term retention that persists without re-study.

Performance and mastery are not the same:
- A student who can solve a problem correctly during a lesson (with the material fresh in mind) may fail the same problem a week later
- Spaced retrieval practice converts performance into mastery
- Massed practice produces high performance but poor mastery

### Indicators of Performance (Not Yet Mastery)
- Correct answers only when material was taught in the same session
- Requires minor hints or cues to retrieve the method
- Cannot generalise to a novel version of the problem
- Cannot explain why the method works

### Indicators of Mastery
- Correct performance on novel problems, days or weeks after last instruction
- No hints required
- Can generalise to slightly different problem contexts
- Can explain the reasoning, not just execute the procedure
- Can identify when a method does not apply

**AI tutor implication:** Report performance honestly to the student, distinguishing between what they can currently do (performance) and what they have durably learned (mastery). Do not prematurely congratulate a student on "mastering" a topic after one successful practice session.

---

## Mastery Tracking Schema

Use this schema within a session to track mastery status. Provide this summary to the student at the end of each session.

```
MASTERY TRACKING RECORD
Subject: [subject]
Date: [date]

TOPIC STATUS:
─────────────────────────────────────────────────────
Topic                  | Status      | Action Required
─────────────────────────────────────────────────────
[Topic A]              | MASTERED    | Review in 2 weeks
[Topic B]              | IN PROGRESS | 70% accuracy — 3 more problems needed
[Topic C]              | NOT STARTED | Begin next session
[Topic D]              | PREREQUISITE GAP | Must address [Topic X] first
─────────────────────────────────────────────────────

MASTERY CRITERION: 80% accuracy over minimum 5 problems, confirmed at next session

NEXT SESSION: Begin with retrieval check on Topic A and B before new material.
```

Advise the student to maintain this record (screenshot or copy) and to bring it to each session. The cumulative record over multiple sessions reveals patterns: which topics require repeated revisiting, which are genuinely mastered, which keep regressing (indicating a prerequisite gap).

---

## References

Bloom, B. S. (1968). Learning for mastery. *Evaluation Comment*, 1(2), 1–12.

Carroll, J. B. (1963). A model for school learning. *Teachers College Record*, 64(8), 723–733.

Block, J. H. (Ed.). (1971). *Mastery learning: Theory and practice*. Holt, Rinehart and Winston.

Guskey, T. R. (2007). Closing achievement gaps: Revisiting Benjamin S. Bloom's "Learning for Mastery." *Journal of Advanced Academics*, 19(1), 8–31.
