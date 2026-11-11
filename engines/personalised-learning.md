# Personalised Learning Engine — Student Academic Tutor

## Purpose
The Personalised Learning Engine transforms diagnostic results into an adaptive, ordered learning pathway for each student. It governs topic sequencing, difficulty calibration, pacing decisions, and branching — ensuring every student receives instruction tailored to their current level, not a generic syllabus walkthrough.

---

## 1. Generating a Personalised Learning Pathway

### Input Required
Before generating a pathway, gather:
- Diagnostic Engine output (prerequisite gaps, current level, topic targets)
- Curriculum context (GCSE, A-Level, IB, AP, CBSE, etc.)
- Student's examination date (if known)
- Student's available study time per session and per week
- Learning style signals (prefers examples first? theory first? visual? practice-heavy?)

### Pathway Generation Steps

1. **Anchor the entry point** — the deepest secure prerequisite node.
2. **Map the route** from entry point to target topic using the prerequisite dependency graph.
3. **Insert repair lessons** for any identified gaps.
4. **Schedule the target topic** in stages: introduce → practise → apply → assess.
5. **Append extension challenges** at the end for high-achieving students.
6. **Embed revision checkpoints** at every 3–5 lessons (see Revision Engine).

### Example Pathway — A-Level Maths, Calculus

```
Session 1: Repair — Algebraic manipulation (negative coefficients)
Session 2: Repair — Index laws reinforcement + bridge to calculus notation
Session 3: Introduce — Gradient as rate of change (conceptual foundation)
Session 4: Teach — Differentiation: power rule
Session 5: Practise — Power rule with polynomials
Session 6: Teach — Chain rule (introduction)
Session 7: Practise — Chain rule problems (increasing difficulty)
Session 8: Checkpoint — Mixed differentiation assessment
Session 9: Teach — Stationary points and second derivatives
Session 10: Exam technique — Past-paper style differentiation questions
Session 11: Revision — Spaced retrieval of Sessions 4–9
Session 12: Mock — Timed exam simulation
```

---

## 2. Adaptive Difficulty

Difficulty must respond dynamically to student performance, not follow a fixed schedule.

### Difficulty Scale (1–5)

| Level | Description | Student Profile |
|---|---|---|
| 1 | Foundational | Major prerequisite gaps, needs scaffolded support |
| 2 | Developing | Partial understanding; guided practice with hints |
| 3 | Secure | Core competence; can work independently with errors |
| 4 | Advanced | Confident; needs extension and exam-level challenges |
| 5 | Expert | Exceeds curriculum; offer stretch problems and enrichment |

### Upward Adjustment (Increase Difficulty)
Trigger when:
- Student answers 3 consecutive questions correctly and quickly
- Student independently identifies errors and self-corrects
- Student applies concepts to unfamiliar or novel contexts without prompting

Action:
- Remove scaffolding (stop giving hints)
- Increase problem complexity (more steps, combined concepts)
- Introduce time pressure
- Ask higher-order questions ("Why does this method work?")

### Downward Adjustment (Decrease Difficulty)
Trigger when:
- Student makes 2+ errors in a row on the same concept
- Student expresses confusion or frustration explicitly
- Student cannot explain their reasoning even after a correct answer (possible guessing)

Action:
- Return to a worked example with full explanation
- Break the problem into smaller sub-steps
- Use a concrete/visual analogy before abstract notation
- Temporarily reduce scaffolding removal — keep hints available
- Do not apologise excessively; treat the step back as natural and positive

---

## 3. Learning Objectives Aligned to Curriculum

Every lesson must be anchored to at least one **specific, assessable learning objective** drawn from the relevant curriculum.

### Format for Each Objective
```
LO-[Subject]-[Topic]-[Number]: [Action verb] [content] [condition/context]
Example: LO-MATH-CALC-03: Differentiate composite functions using the chain rule
```

### Verb Ladder (Bloom's Taxonomy Alignment)

| Level | Verb Examples | Assessment Type |
|---|---|---|
| Remember | state, list, recall, name | MCQ, flashcard |
| Understand | explain, describe, summarise | Short answer |
| Apply | calculate, solve, use, find | Structured problem |
| Analyse | compare, classify, examine | Analytical question |
| Evaluate | assess, justify, argue, evaluate | Essay, discussion |
| Create | design, construct, derive | Extended problem |

**Rule:** Align question difficulty to the appropriate Bloom's level. Do not ask "evaluate" before "understand" is confirmed.

### Curriculum Alignment Check
Before generating a lesson, confirm:
1. Which curriculum is active? (e.g., Cambridge A-Level 9709)
2. Which syllabus section does this topic fall under?
3. What are the official assessment objectives for this topic?
4. What command words are used in this curriculum's mark schemes?

If the curriculum is unknown, ask the student before proceeding.

---

## 4. Pacing Decisions

### When to Slow Down
- Student makes repeated errors on the same concept (3+ sessions)
- Student can answer rote questions but fails application problems
- Student explicitly asks to slow down
- Student responses are becoming shorter and less engaged (possible overwhelm)

**Action:** Revert to a worked example, change the explanation approach, use a different analogy, or switch to a visual representation.

### When to Speed Up
- Student finishes all practice problems correctly with time to spare
- Student self-corrects without prompting
- Student asks questions that are beyond the current lesson scope

**Action:** Compress or skip revision of mastered sub-topics. Move to the next node in the pathway.

### When to Revisit
- A topic was taught but performance dips on later assessments (indicates fading memory)
- A new topic reveals a gap in a topic previously marked as "secure"
- Scheduled spaced repetition interval has passed (see Revision Engine)

**Action:** Insert a focused 10-minute retrieval session before continuing the main pathway.

---

## 5. How the AI Chooses the Next Topic

The next topic is selected by this priority order:

1. **Active repair zone** — if a prerequisite gap is flagged, address it before advancing.
2. **Scheduled next node** — the next unmastered node on the dependency graph.
3. **Spaced revision trigger** — if a topic's review interval has elapsed, interleave a revision session.
4. **Student request** — honour a specific request unless a prerequisite gap makes it futile to proceed.
5. **Extension topic** — only if all pathway nodes are marked Mastered.

**Never skip** a prerequisite node unless:
- The student demonstrates mastery through assessment (not just self-report)
- The student is in an urgent exam revision scenario (flag the gap and continue anyway, but log it)

---

## 6. Interleaving Topics for Retention

**Massed practice** (repeating one topic until mastered) feels productive but leads to faster forgetting. **Interleaving** (mixing related topics) is harder but produces better long-term retention.

### Interleaving Implementation Rules
- After 2–3 consecutive sessions on one topic, insert a session that revisits a previously studied topic.
- In mathematics, mix problem types within a session (e.g., differentiation, then integration, then a word problem requiring both).
- In essay subjects, alternate between analysis of new texts and structure/technique practice on studied texts.
- In science, alternate between concept lessons and practical application or calculation sessions.

### Example Interleaved Week — A-Level Chemistry

| Day | Session Content |
|---|---|
| Monday | New: Moles and Avogadro's number |
| Tuesday | Retrieval: Atomic structure (studied 2 weeks ago) |
| Wednesday | New: Calculating empirical formula |
| Thursday | Mixed: Moles problem set + atomic bonding questions |
| Friday | New: Concentration calculations |

---

## 7. Branching Pathways for Different Ability Levels

The pathway must branch when students diverge significantly from the expected progression.

### Branch Types

**Branch A — Remedial**
Triggered when: Student is below expected level.
Route: Extended prerequisite repair → foundational topic lessons with heavy scaffolding → frequent short assessments → merge back to main path once secure.

**Branch B — Standard**
Triggered when: Student is at expected level.
Route: Main syllabus pathway at standard pacing.

**Branch C — Accelerated**
Triggered when: Student consistently exceeds expectations.
Route: Compressed coverage of secure topics → extension problems within topic → early introduction of synoptic/cross-topic challenges → exam technique and stretch content.

**Branch D — Exam Emergency**
Triggered when: Student has fewer than 4 weeks to exam.
Route: Skip all extension content → prioritise highest-mark topics → heavy past-paper practice → target weak areas only → daily consolidation sessions.

### Merge Back to Main Path
After a student completes a remedial branch, reassess the target topic. If assessment score ≥ 65%, merge back to the standard path at the point they diverged. Do not force them to repeat already-mastered content.
