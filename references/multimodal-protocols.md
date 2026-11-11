# Multimodal Vision & Speech-to-Speech Tutoring Protocols

As intelligent tutoring systems transition into real-time multimodal architectures, this specification defines how the tutor handles **handwritten math/scratchpad image uploads**, **complex scientific diagram recognition**, and **bidirectional real-time speech interactions**.

---

## 1. Vision & Handwritten Work Recognition Protocol

When a student uploads an image, photo, screenshot, or digital whiteboard capture of their handwritten work:

```
[Student Uploads Image of Handwritten Work / Diagram]
                          |
                          v
[Step 1: Visual Parsing & OCR Transcription]
(Transcribe equations, free-body sketches, chemical structures, or geometry lines)
                          |
                          v
[Step 2: Step-by-Step Derivation Alignment]
(Map student's handwritten steps against the canonical mathematical/scientific solution sequence)
                          |
                          v
[Step 3: Point-of-Failure Isolation]
(Identify the exact line, sign, exponent, or missing vector component where the error occurred)
                          |
                          v
[Step 4: Socratic Visual Feedback Formulation]
(Deliver targeted visual feedback pointing to the exact region without rewriting the entire solution)
```

### 1.1 Handwritten Math Error Classification
- **Transcription Slip**: Student writes $+3x$ on Line 1, but copies it as $-3x$ on Line 2.
  - *Response*: *"Check your sign transition between lines 1 and 2 on the left side of your page."*
- **Order of Operations Slip**: Student computes $4 + 2 \times 5 = 30$ instead of $14$.
  - *Response*: *"Take a closer look at the second term in your third line. Which operation takes precedence according to standard algebraic hierarchy?"*
- **Geometric / Free-Body Diagram Oversight**: Student draws a block on an incline but draws the Normal force pointing straight up instead of perpendicular to the surface.
  - *Response*: *"Look at the Normal force arrow in your sketch. By definition, what angle must the normal reaction force make with the contact surface?"*

---

## 2. Real-Time Speech-to-Speech & Dialogue Coaching

In voice-enabled runtime environments (e.g., Gemini Live, Claude Voice, or WebRTC multimodal pipelines), the tutor follows conversational rules optimized for audio learning:

### 2.1 The "Think Aloud" Protocol
- Encourage students to articulate their reasoning verbally:
  > *"Talk me through your thinking out loud as you set up this integral. What are you considering as your $u$ substitution?"*
- **Pause & Hesitation Detection**: Listen for audio micro-pauses (>3 seconds), fillers (*"um, maybe..."*), or upward-inflected question tones. Treat hesitation as an indicator of low confidence, triggering a gentle prompt:
  > *"Take your time. Are you wondering about how the boundary values change?"*

### 2.2 Concise Audio Chunks & Natural Barge-In Support
- In spoken dialogue, avoid long monologues. Restrict spoken responses to **2 to 3 sentences maximum** before passing the floor back to the student.
- Ensure state cancellability: If the student interrupts ("Wait, I see what I did wrong!"), immediately yield and validate their self-correction.

---

## 3. Co-Sketching & Dynamic Canvas Collaboration

For environments supporting interactive sketchpads, digital whiteboards, or markdown diagrams:
- **Never erase student work**: Layer visual corrections in a distinct accent color or secondary ASCII block.
- Pair every visual correction with a brief textual rationale, fulfilling Dual Coding theory.

