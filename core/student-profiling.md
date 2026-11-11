# Student Profiling — Student Academic Tutor

> *"If you are teaching the same lesson to thirty students, you are teaching no student at all."*
> — Adapted from Vygotsky's concept of the Zone of Proximal Development

---

## 1. Why Student Profiles Matter

The most powerful affordance of one-on-one tutoring — human or AI — is the ability to **know the student**. Not generically, but specifically: what they know, what they misunderstand, how confident they are, what they last studied, and what they are ready for next.

Without a profile, every session starts from scratch. The tutor asks the same opening questions, risks repeating content already mastered, and misses the quiet accumulation of knowledge gaps that explain why a student is struggling weeks later.

With a profile, the tutor picks up exactly where the last session ended, retrieves topics that are due for spaced repetition, anticipates likely misconceptions, and calibrates challenge appropriately from the first question.

**A student's academic profile is a living document.** It is built through conversation (not formal testing), updated after every interaction, and always provisional — a student who appeared to understand may reveal a gap in the next session, and a student who was confused may demonstrate surprising mastery days later after self-study.

---

## 2. The Student Academic Profile Schema

The following schema defines the data structure for a student's academic profile. This profile is built and maintained entirely through tutoring conversation — no external data is required.

```yaml
student_profile:

  # --- IDENTITY AND CONTEXT ---
  level: "secondary"              # primary | secondary | sixth-form | university | adult
  year_group: "Year 12"           # e.g. Year 7, Grade 10, First Year University
  curriculum: "Cambridge A-Level" # See supported curricula list in SKILL.md
  primary_language: "English"     # Student's first/home language
  language_of_instruction: "English"
  learning_preference: "standard" # standard | attention_friendly | deep_learning | visual | exam_focused

  # --- LEARNING & PACING PREFERENCES ---
  # Explicit preferences, NOT medical diagnoses
  delivery_preferences:
    preferred_pacing: "progressive"     # progressive | fast | comprehensive
    chunking_intensity: "standard"      # high (short chunks) | standard | deep
    example_first: true                 # start with concrete example before abstract theory
    step_by_step_breakdown: true        # show every intermediate transformation
    working_memory_anchors: true        # show current step in multi-stage problems

  # --- SUBJECTS ---
  subjects:
    - name: "Mathematics"
      exam_board: "Cambridge"
      exam_code: "9709"
      tier: "higher"              # higher | foundation | n/a
    - name: "Physics"
      exam_board: "Cambridge"
      exam_code: "9702"
      tier: "higher"
    - name: "Economics"
      exam_board: "Cambridge"
      exam_code: "9708"
      tier: "n/a"

  # --- KNOWLEDGE AND MASTERY MAP ---
  # Topic-level mastery, not a single overall score
  mastery_map:
    mathematics:
      pure:
        algebra:
          quadratics: "mastered"               # mastered | developing | weak | not_started
          binomial_theorem: "developing"
          partial_fractions: "weak"
          factor_theorem: "not_started"
        calculus:
          differentiation_basic: "mastered"
          differentiation_chain_rule: "developing"
          integration_basic: "weak"
          integration_by_parts: "not_started"
        trigonometry:
          basic_ratios: "mastered"
          sine_cosine_rules: "developing"
          radians: "weak"
      statistics:
        probability: "developing"
        normal_distribution: "not_started"

  # --- IDENTIFIED GAPS ---
  knowledge_gaps:
    - subject: "Mathematics"
      topic: "Integration"
      gap_description: "Student can find basic antiderivatives but does not understand the relationship between integration and area under a curve. Confuses indefinite and definite integrals."
      identified_date: "2026-01-15"
      status: "active"

    - subject: "Mathematics"
      topic: "Partial Fractions"
      gap_description: "Student has not been taught this topic yet. It is a prerequisite for integration of rational functions."
      identified_date: "2026-01-15"
      status: "active"

  # --- KNOWN MISCONCEPTIONS ---
  misconceptions:
    - subject: "Mathematics"
      topic: "Integration"
      misconception: "Student believes that ∫x² dx = 2x (confusing differentiation with integration)"
      corrected: false
      correction_date: null
      notes: "Common misconception — has been shown counterexample but requires further practice"

  # --- CONFIDENCE CALIBRATION ---
  # Tracks stated confidence vs. actual performance to detect over/underconfidence
  confidence_calibration:
    - subject: "Mathematics"
      topic: "Quadratics"
      stated_confidence: 8          # Student's self-rating out of 10
      actual_performance: 9         # Based on practice question accuracy
      calibration_status: "well_calibrated"   # well_calibrated | overconfident | underconfident

    - subject: "Mathematics"
      topic: "Integration"
      stated_confidence: 5
      actual_performance: 2
      calibration_status: "overconfident"     # Believes they know more than they do

  # --- LEARNING OBJECTIVES ---
  current_objectives:
    - "Master integration by parts before end of term exam (3 weeks)"
    - "Understand and apply binomial theorem to expand expressions"
    - "Revise all Pure 1 content for mock examination"

  # --- PERFORMANCE LOG ---
  performance_log:
    - date: "2026-01-14"
      subject: "Mathematics"
      topic: "Differentiation — Chain Rule"
      activity: "guided_practice"
      questions_attempted: 5
      questions_correct: 3
      error_analysis: "Errors on composite functions involving trigonometric expressions"
      notes: "Student understands chain rule conceptually but makes arithmetic errors under time pressure"

    - date: "2026-01-15"
      subject: "Mathematics"
      topic: "Integration — Basic"
      activity: "independent_practice"
      questions_attempted: 4
      questions_correct: 1
      error_analysis: "Attempting to differentiate rather than integrate; forgetting + C"
      notes: "Significant confusion persists — requires full re-teaching with worked examples"

  # --- REVISION HISTORY AND SPACED REPETITION SCHEDULE ---
  revision_schedule:
    - topic: "Quadratics"
      last_retrieved: "2026-01-10"
      performance_at_retrieval: "strong"
      next_retrieval_due: "2026-01-31"
      interval_days: 21

    - topic: "Differentiation — Basic Rules"
      last_retrieved: "2026-01-14"
      performance_at_retrieval: "moderate"
      next_retrieval_due: "2026-01-18"
      interval_days: 4

  # --- LEARNING PREFERENCES AND NOTES ---
  learning_notes:
    responds_well_to: "Numerical concrete examples before abstract generalisation"
    responds_poorly_to: "Being given answers without explanation"
    pace: "medium"                 # slow | medium | fast | variable
    best_session_length: "45 minutes"
    exam_date: "2026-05-15"
    days_until_exam: 120
    special_considerations: "English is second language — occasionally needs vocabulary support"
```

---

## 3. How to Build the Profile Through Conversation

A formal intake questionnaire is not necessary and can feel clinical. Instead, build the profile **organically through the natural flow of tutoring interaction**.

### 3.0 The Five Explicit Academic Delivery Preferences

The tutor supports five user-selected delivery preferences. These are **instructional presentation modes**, not medical or psychological labels:

1. **Standard Learning (`standard`)**: Balanced pacing, standard 10-stage lesson progression, standard paragraphs, periodic checks for understanding.
2. **Attention-Friendly Learning (`attention_friendly`)**: High chunking intensity, 6-stage progressive explanation sequence, visual bolding of key terms, intermediate calculations explicitly shown, breadcrumb reorientation, active engagement check after major concepts.
3. **Detailed / Deep Learning (`deep_learning`)**: Extended theoretical derivations, historical context, underlying proofs, academic literature connections, epistemological counter-arguments.
4. **Visual Learning (`visual`)**: Emphasis on ASCII diagrams, Mermaid concept maps, LaTeX matrices, and direct visual parameter exploration (Desmos, GeoGebra, PhET).
5. **Exam-Focused Learning (`exam_focused`)**: Strict command-word orientation, mark allocation formulas ($M, A, B, FT$ marks), past-paper structural conventions, time management focus.

> **Operational Boundary**: Students may switch between these modes at any time by saying *"Switch to attention-friendly mode"*, *"Break it down into smaller steps"*, or *"Give me more depth"*. The tutor must never infer or label a student as having ADHD, dyslexia, or any cognitive disability based on their choice of delivery preference.

### Session 1 — Foundation Gathering (First 3 minutes)

Ask these questions naturally, not as a list:

1. **"What subject are you working on today, and what year/level are you in?"**
   → Populates: `level`, `year_group`, `subjects`

2. **"Which exam board or curriculum? E.g. Cambridge, AQA, IB?"**
   → Populates: `curriculum`

3. **"When's your next exam or assessment?"**
   → Populates: `exam_date`, `days_until_exam`, creates urgency context

4. **One targeted diagnostic question on the specific topic**
   → Begins populating: `mastery_map`, `knowledge_gaps`, `misconceptions`

### Ongoing — Passive Profile Building

After Session 1, most profile data is gathered passively as the tutoring session proceeds:

- Every time a student answers a question **incorrectly** → update `mastery_map` and `performance_log`
- Every time a student correctly explains a concept **in their own words** → update `mastery_map` toward "mastered"
- Every time a student expresses a belief that is incorrect → add to `misconceptions`
- Every time a student rates their own confidence → update `confidence_calibration`
- Every time a topic is retrieved from memory → update `revision_schedule`

### Profile Building Best Practices

- **Ask "how confident are you?" after every independent practice attempt** — this builds the confidence calibration picture over time
- **Never ask the student directly about gaps or weaknesses** — this feels like criticism. Discover gaps through diagnostic questions and practice errors.
- **Always record the specific error type, not just "wrong"** — "student added exponents instead of multiplying" is infinitely more useful than "got it wrong"
- **Update the profile during and immediately after the session**, not from memory afterwards

---

## 4. The Mastery Model — Topic-Level, Not Single Score

This tutor **never uses a single overall grade or score** to represent a student's knowledge. A student can have an A-grade average but be completely unable to do integration by parts. A student can have a C-grade average but have exceptional mastery of probability and statistics.

Instead, mastery is tracked at **topic level** within each subject, using four states:

### Mastery States

| State | Definition | Tutoring Response |
|-------|------------|-------------------|
| **Not Started** | Topic has not been taught or attempted | Plan introduction when topic comes up in curriculum sequence |
| **Weak** | Attempted but performance is consistently poor (< 50% accuracy) | High priority for direct instruction; treat as novice |
| **Developing** | Partial mastery — correct sometimes, errors on harder applications (50–79% accuracy) | Guided practice, targeted gap-filling, increase challenge gradually |
| **Mastered** | Consistent independent accuracy, can explain and transfer (≥ 80% accuracy on varied problems) | Maintain with spaced retrieval; begin extending to harder material |

### Mastery Thresholds

A topic moves to **Mastered** only when the student has demonstrated:

1. ✅ **At least 80% accuracy** on independent practice problems (no hints)
2. ✅ **Correct performance on a problem with varied surface features** (transfer)
3. ✅ **Ability to explain the concept verbally** (not just do the procedure)
4. ✅ **Correct performance maintained at the NEXT retrieval session** (1–3 days later)

Condition 4 is critical. Many students demonstrate mastery in a session and have forgotten it by the next day. Mastery is only confirmed when it survives the first spaced retrieval.

---

## 5. Confidence Calibration

**Metacognitive accuracy** — the ability to accurately judge what you know and don't know — is one of the strongest predictors of academic success. Students who know what they don't know can study effectively. Students who don't know what they don't know study inefficiently and are blindsided by exams.

This tutor tracks the gap between **stated confidence** and **actual performance** for every topic.

### Calibration Categories

| Category | Pattern | Tutoring Response |
|----------|---------|-------------------|
| **Well-calibrated** | Confidence matches performance (within 1–2 points) | Healthy — maintain |
| **Overconfident** | States 7/10 confidence but performs at 3/10 level | Most dangerous pattern — explicitly flag the gap: "You said you were 7/10 confident, but you got 1 of 4 right. That gap is worth paying attention to." |
| **Underconfident** | States 3/10 confidence but performs at 7/10 level | Encourage and build confidence — point out the gap positively: "You're better at this than you think." |
| **Anxious** | Confidence and performance both very low | Requires confidence-building before skill-building — reduce difficulty, increase success rate temporarily |

### Tracking Confidence Over Time

After every independent practice attempt:

1. **Ask the student to rate confidence (1–10) BEFORE submitting their answer**
2. Record the stated confidence
3. Grade the performance
4. Record the actual accuracy
5. Update the calibration entry
6. If the gap is large, name it explicitly and kindly

Over multiple sessions, patterns in confidence calibration reveal which topics the student systematically over- or underestimates — this is high-value diagnostic information.

---

## 6. How to Update the Profile as Learning Progresses

### After Every Session
- Update `mastery_map` for all topics covered
- Add any new entries to `knowledge_gaps` identified during the session
- Add any new misconceptions to `misconceptions` and update the corrected flag
- Add performance entries to `performance_log`
- Update `revision_schedule` with the next due date for all topics retrieved
- Update `confidence_calibration` with new data points

### Triggering Profile-Based Decisions

The profile should actively drive session planning:

- **Topic mastered + > 7 days since retrieval** → Begin session with spaced retrieval on that topic
- **Topic "developing" in multiple consecutive sessions** → Consider whether a prerequisite gap is the real problem
- **Misconception flagged but uncorrected** → Revisit explicitly in next session
- **Exam date < 30 days away** → Switch entirely to revision mode; use profile to rank topics by weakness and time-since-retrieval
- **Overconfidence pattern detected on a topic** → Generate harder problems to expose the limits of understanding

---

## 7. Example Profile — Secondary Student, A-Level Mathematics

The following is a realistic example of a fully-populated student profile after three tutoring sessions:

---

**Student:** Amara N.
**Year:** Year 12 (Lower Sixth)
**Curriculum:** Cambridge A-Level Mathematics (9709)
**Next Exam:** May 2026 (Paper 1 — Pure Mathematics)

**Mastery Map:**

| Topic | Mastery | Last Practised | Next Retrieval |
|-------|---------|----------------|----------------|
| Algebra — Quadratics | Mastered | 10 Jan | 31 Jan |
| Algebra — Simultaneous equations | Mastered | 8 Jan | 29 Jan |
| Algebra — Partial fractions | Not started | — | — |
| Algebra — Binomial theorem | Developing | 15 Jan | 18 Jan |
| Calculus — Differentiation (basic) | Mastered | 14 Jan | 21 Jan |
| Calculus — Chain rule | Developing | 14 Jan | 18 Jan |
| Calculus — Integration (basic) | Weak | 15 Jan | 17 Jan |
| Calculus — Integration by parts | Not started | — | — |
| Trigonometry — Basic ratios | Mastered | 7 Jan | 28 Jan |
| Trigonometry — Sine/cosine rules | Developing | 11 Jan | 19 Jan |
| Trigonometry — Radians | Weak | 11 Jan | 17 Jan |

**Active Gaps:**
1. Integration — confuses differentiation and integration procedures
2. Partial fractions — not yet taught (prerequisite for integration of rational functions)
3. Radians — understands definition but cannot convert fluently

**Active Misconceptions:**
1. Believes ∫x² dx = 2x (confusing with differentiation). Partially addressed in Session 3. Requires further practice.

**Confidence Calibration:**
- Quadratics: Well-calibrated (8/10 stated, ~85% actual)
- Integration: Overconfident (5/10 stated, ~20% actual)
- Chain rule: Slightly underconfident (4/10 stated, ~65% actual)

**Session Priority (next session):**
1. Spaced retrieval: Binomial theorem (due 18 Jan)
2. Spaced retrieval: Radians (due 17 Jan)
3. Targeted instruction: Integration — reteach from scratch
4. Address misconception: ∫x² = 2x

**Notes:**
Amara responds extremely well to worked examples followed by immediate practice. She learns fastest when she narrates her reasoning aloud. Avoid giving answers — she needs to feel she reached them herself. First language is Swahili; occasional vocabulary support needed for mathematical English.
