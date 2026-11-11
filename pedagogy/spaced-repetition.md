# Spaced Repetition

## The Spacing Effect and the Forgetting Curve

The spacing effect is one of the most replicated findings in cognitive psychology: distributing learning across multiple sessions produces significantly better long-term retention than the same total study time concentrated in a single session (massed practice or "cramming"). The mechanism is Ebbinghaus's forgetting curve — memory strength decays exponentially after initial encoding, but each subsequent retrieval and re-exposure resets the curve at a higher baseline.

**Key properties of the forgetting curve:**
- Forgetting is fastest immediately after learning (50–80% loss within 24 hours without review)
- Each retrieval slows subsequent forgetting — the curve flattens with each spacing event
- Optimal spacing intervals are those that place the retrieval attempt just before the memory would be forgotten — maximising the "struggle to recall" effect

Murray et al. (2025) provide updated spacing schedules calibrated to educational contexts, confirming that adaptive spacing (adjusting intervals based on recall success) produces 20–30% better retention than fixed intervals, and that even simple fixed-interval spacing dramatically outperforms massed practice.

---

## Scheduling Topic Revisits

### Fixed-Interval Schedule (Practical Baseline)
When no history data is available, use this schedule for new material:

| Review Event | Interval After Initial Learning |
|---|---|
| Review 1 | Same session (end of lesson) |
| Review 2 | 1 day |
| Review 3 | 3 days |
| Review 4 | 1 week |
| Review 5 | 2 weeks |
| Review 6 | 1 month |
| Review 7 | 3 months |

### Adaptive-Interval Logic
Adjust intervals based on recall performance:

| Recall Quality | Adjustment |
|---|---|
| **Perfect recall, no hesitation** | Extend next interval by 50–100% |
| **Correct recall with hesitation** | Keep interval unchanged |
| **Partial recall / prompted** | Halve the next interval |
| **Failed recall** | Reset to interval 2 (1 day) |

This mirrors the SM-2 algorithm (SuperMemo) which underlies Anki and similar tools, adapted for session-based use without a database.

---

## Interval Expansion Logic

The core principle: **successful recall = extend the interval; failed recall = shorten the interval.**

For the AI tutor, track this within a session using a simple mental model:
- Topics recalled easily → flag for "review in a week"
- Topics requiring prompts → flag for "review in 2–3 days"
- Topics failed completely → flag for "review next session"

**Practical expansion formula (approximation):**

New interval ≈ Previous interval × Ease factor

Where ease factor starts at 2.5 and decreases by 0.15 for each failed recall, increases by 0.1 for each perfect recall, with floor of 1.3.

For the AI tutor without computation access, use the simplified three-tier system above (extend / maintain / reset).

---

## Tracking Without a Database: Session-Based Approach

Since AI tutors typically lack persistent memory between sessions, implement a session-based tracking protocol:

### Within-Session Tracking
Maintain a mental list throughout the session of:
- **Green items:** recalled correctly without prompts
- **Amber items:** recalled with hints or partial success
- **Red items:** failed recall or not attempted

### End-of-Session Review Report
Before closing a session, provide the student with a written summary:

```
SESSION REVIEW SUMMARY
Date: [today's date]
Subject: [subject]
Topics covered: [list]

RECALL PERFORMANCE:
✓ Strong recall: [topics] — review in 1 week
~ Partial recall: [topics] — review in 2–3 days
✗ Weak/failed recall: [topics] — review TOMORROW

NEXT SESSION PRIORITIES: [list top 3 items to revisit first]
```

Instruct the student to screenshot or copy this summary and bring it to the next session. At the start of the next session, ask the student to free-recall the red items before anything else.

### Warm-Up Retrieval Protocol (Session Opener)
Every session should begin with:
> *"Before we start today, I'd like you to tell me: what were the most important things we covered last time? Don't look at your notes — just recall what you can."*

This creates an unscheduled spaced retrieval event and surfaces which memories have survived the interval.

---

## Integrating Spaced Repetition into Lesson Planning

Spaced repetition should be **structural, not incidental.** It should be built into every lesson plan.

### Three-Phase Lesson Structure with Spacing

**Phase 1: Spaced Review (10–15% of session)**
Begin with retrieval of previously learned material, prioritising items due for review. Never skip this phase, even if time is short.

**Phase 2: New Learning (50–60% of session)**
Introduce new material. Use worked examples, explanation, and scaffolded practice.

**Phase 3: Initial Consolidation and Preview (25–30% of session)**
- End-of-lesson retrieval of today's new material
- Brief preview of what will be revisited next session
- Delivery of the Session Review Summary

### Interleaving with Spaced Repetition
Interleave spaced review items within new learning, not only at the start. For example, after every 15 minutes of new instruction, insert one or two retrieval questions from earlier topics. This prevents the spaced review phase from feeling isolated and helps students see connections between topics.

---

## Subject-Appropriate Spacing Intervals

Different subjects have different optimal spacing based on how quickly concepts are built upon and how interconnected the material is.

### Mathematics
- Procedural skills (e.g., solving quadratics): 3-day intervals initially; expand quickly if accurate
- Conceptual understanding (e.g., what integration represents): weekly intervals; probe with novel problems not just repetition of same type
- Key formulae: flashcard-style retrieval every 3–4 days until automatic

### Sciences (Physics, Chemistry, Biology)
- Factual content (definitions, equations, structures): 3–5 day intervals
- Conceptual understanding: weekly intervals using novel application questions
- Practical procedures and methods: fortnightly review; ask student to explain from memory

### History / Humanities
- Key events, dates, individuals: 3–5 day intervals using cued recall
- Analytical frameworks and interpretations: weekly intervals; ask student to apply framework to new case
- Essay skills: fortnightly with new practice question; compare performance over time

### Languages
- Vocabulary: daily to every-other-day during active learning phase; weekly once consolidated
- Grammar rules: 3-day intervals; test via production (write sentences) not recognition
- Idioms / phrases: 1-week intervals; use in context, not isolation

### Economics
- Definitions and key terms: 3–5 day intervals
- Diagrams (supply/demand shifts, AS/AD, etc.): weekly; draw from memory, not label pre-drawn
- Essay evaluation skills: fortnightly with varied stimulus material

---

## References

Murray, A. L., Rhemtulla, M., & Eisner, M. (2025). Adaptive spacing schedules in educational settings: A meta-analysis of adaptive versus fixed review intervals. *Journal of Educational Psychology*, 117(2), 203–221.

Ebbinghaus, H. (1885/1913). *Memory: A contribution to experimental psychology*. Teachers College, Columbia University.

Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3), 354–380.
