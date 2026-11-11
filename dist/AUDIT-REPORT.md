# Comprehensive Pre-Refactor Audit & Consolidation Report
**Repository**: AI Student Tutor Skill (i-student-tutor-skill)  
**Audit Date**: November 2026  
**Target Release**: Portable Multi-Platform Distribution Architecture  
**Author**: Antigravity AI Engineering Team  

---

## 1. Executive Summary

The AI Student Tutor Skill is an advanced pedagogical system comprising **121 files**, **75 directories**, **846,972 bytes (~847 KB)**, and approximately **206,020 tokens** across core pedagogy, student intelligence, 20 subject engines, 30 national/international curriculum frameworks, attention-friendly/neuroinclusive adaptations, and automated evaluation suites.

While this extensive architecture provides peerless academic depth, uploading 121 individual files into modern AI platforms (ChatGPT Custom GPTs, Claude Projects, Gemini Gems / NotebookLM, Manus, and local LLMs) is practically impossible due to platform upload constraints:
- **ChatGPT Custom GPTs / Projects**: Hard limit of 20 files in Knowledge; 8,000 character limit on custom instructions.
- **Claude Projects**: 200,000 token context window limit; file upload limits; performance degrades with dozens of fragmented files.
- **Gemini (AI Studio & NotebookLM)**: Massive 1M–2M context window, but requires structured, cohesive context documents rather than hundreds of fragmented markdown snippets.
- **Manus & Tool-Calling Agents**: Require clear entrypoint specifications (SKILL.md, manifest.json) without deep recursive file references.
- **Local & Universal LLMs (Ollama, Open WebUI, LibreChat)**: Require single-file system prompts or Modelfiles.

This audit establishes a **Single Source of Truth (SSOT)** across all pedagogical subsystems, identifies genuine duplicate content across files, details the consolidation strategy into a **self-contained portable core** (< 30,000 tokens), groups domain knowledge into **5 modular knowledge packs**, and defines **5 platform-tailored distributions**—all while preserving 100% of the repository's intellectual and technical capabilities.

---

## 2. Pre-Refactor Inventory by Subsystem

| Subsystem Directory | File Count | Raw Size (Bytes) | Approx. Tokens | Primary Role |
| :--- | :---: | :---: | :---: | :--- |
| core/ | 8 | 87,769 | ~21,400 | Foundational pedagogy, ethics, integrity, profiling, protocols |
| engines/ | 15 | 119,180 | ~29,100 | Operational mechanics (lesson, diagnostic, attention, visual) |
| pedagogy/ | 7 | 66,036 | ~16,100 | Theoretical learning sciences & instructional strategies |
| modes/ | 8 | 60,682 | ~14,800 | Student interaction modes (tutor, practice, exam, viva voce) |
| ssessments/ | 4 | 18,616 | ~4,550 | Rubrics, diagnostic tests, question generation specifications |
| subjects/ | 20 | 153,370 | ~37,400 | 20 domain-specific subject teaching engines |
| curricula/ | 31 | 189,238 | ~46,150 | 30 national/international curriculum guides & verified source registry |
| intelligence/ | 2 | 6,098 | ~1,490 | Student state model (dual-axis) & misconception profiling |
| prerequisites/ | 1 | 3,122 | ~760 | Prerequisite dependency graphs & gap tracing |
| question-laboratory/| 1 | 3,403 | ~830 | AI item generation laboratory & distractor design |
| writing-engine/ | 1 | 3,290 | ~800 | Academic writing, thesis, and argument scaffolding |
| examination-intelligence/| 1 | 4,048 | ~990 | Command word taxonomy & mark distribution analytics |
| multilingual/ | 1 | 3,498 | ~850 | Multilingual scaffolding & language switching |
| dashboards/ | 1 | 2,847 | ~700 | Stakeholder reporting (student, teacher, parent) |
| 
eferences/ | 3 | 18,105 | ~4,420 | Research foundations, multimodal/voice protocols, enhancements |
| evaluation/ | 9 | 32,234 | ~7,860 | Golden datasets, benchmark protocols, hallucination tests |
| 	esting-suite/ | 2 | 7,681 | ~1,870 | Automated release gates (alidate-release.ps1) & QA protocols |
| docs/ | 1 | 3,108 | ~760 | Platform setup & installation documentation |
| Root (SKILL.md, etc.)| 4 | 58,225 | ~14,200 | Skill metadata, manifest, license, and comprehensive README |
| **Total Repository** | **121** | **846,972** | **~206,020** | **Complete Uncompressed Knowledge Base** |

---

## 3. Redundancy & Duplication Analysis

During file inspection, seven major instructional redundancies were identified where identical or overlapping rules were repeated across multiple files:

### Redundancy 1: Teaching Protocol vs. Lesson Engine vs. Mode Tutor
- **Files**: core/teaching-protocol.md, engines/lesson-engine.md, modes/tutor.md
- **Issue**: All three files defined the 10-stage lesson anatomy (Orientation, Prior Knowledge, Concept Intro, Worked Example, Guided Practice, Independent Practice, Misconception Check, Metacognition, Summary, Next Steps).
- **Resolution**: Designate core/teaching-protocol.md as the canonical SSOT for lesson progression. engines/lesson-engine.md and modes/tutor.md cross-reference the canonical protocol and focus strictly on operational stage transitions and user dialog management.

### Redundancy 2: Learning Science vs. Pedagogy Sub-Modules
- **Files**: core/learning-science.md, pedagogy/worked-examples.md, pedagogy/scaffolding.md, pedagogy/retrieval-practice.md, pedagogy/spaced-repetition.md
- **Issue**: core/learning-science.md provided extensive summaries of Sweller (cognitive load), Bjork (desirable difficulties), and Roediger & Karpicke (retrieval), which were then repeated verbatim in the individual pedagogy/ files.
- **Resolution**: core/learning-science.md serves as the foundational SSOT. Pedagogical sub-modules in pedagogy/ serve as detailed instructional implementation guides and are bundled into a cohesive dist/packs/pedagogy/ pack.

### Redundancy 3: Student Profiling vs. Personalised Learning vs. Student State Model
- **Files**: core/student-profiling.md, engines/personalised-learning.md, intelligence/student-state-model.md
- **Issue**: Intake questionnaire attributes, profile update triggers, and delivery preference configurations were duplicated across three locations.
- **Resolution**: Consolidate student profiling into core/student-profiling.md as the SSOT, maintaining the dual-axis mastery ($) and confidence ($) model from intelligence/student-state-model.md.

### Redundancy 4: Assessment Engine vs. Marking Rubrics vs. Question Laboratory
- **Files**: engines/assessment-engine.md, ssessments/marking-rubrics.md, ssessments/question-generation.md, question-laboratory/generator-engine.md
- **Issue**: Mark scheme taxonomy ($ method, $ accuracy, $ independent, $ follow-through) and Bloom's Taxonomy mapping were defined separately across four files.
- **Resolution**: Canonicalize mark taxonomy in ssessments/marking-rubrics.md and item generation standards in question-laboratory/generator-engine.md.

### Redundancy 5: Misconception Engine vs. Catalog vs. Profiling
- **Files**: engines/misconception-engine.md, knowledge-base/misconceptions/catalog.md, intelligence/misconception-profiling.md
- **Issue**: The Slip vs. Gap vs. Misconception triage rubric and 4-step remediation cycle appeared in all three files.
- **Resolution**: engines/misconception-engine.md is the canonical engine. catalog.md holds the subject-specific examples, and profiling.md tracks student mistake persistence.

### Redundancy 6: Attention-Friendly Scaffolding Across Modes
- **Files**: engines/attention-friendly-engine.md, modes/explain-again.md, modes/practice.md
- **Issue**: The 6-stage progressive explanation sequence (Direct Answer -> Simple Explanation -> Concrete Example -> Step-by-Step -> Check-in -> Deep Dive) was being redefined in alternate modes.
- **Resolution**: engines/attention-friendly-engine.md is the canonical SSOT. All modes cite this sequence when attention-friendly delivery preference is active.

### Redundancy 7: Development & Evaluation Assets vs. Runtime Tutoring
- **Files**: evaluation/ (9 files), 	esting-suite/ (2 files), 
eferences/research-foundations.md
- **Issue**: Evaluation datasets, hallucination test harnesses, and automated release scripts are vital for repository QA and verification, but should NOT be loaded into LLM context windows during real-time student tutoring sessions.
- **Resolution**: Keep all development and evaluation assets intact in the source repository for CI/CD and release gate audits (alidate-release.ps1), while excluding them from the portable runtime packages.

---

## 4. Single Source of Truth (SSOT) Architecture

The refactored architecture establishes clear canonical authorities:

| Domain | Canonical Single Source of Truth | Key Rules & Standards Enforced |
| :--- | :--- | :--- |
| **Teaching Philosophy & Protocol** | core/teaching-protocol.md | 5 core principles, 10-stage lesson anatomy, active learning priority |
| **Learning Science & Pedagogy** | core/learning-science.md | Cognitive load theory, ZPD, retrieval practice, spaced repetition |
| **Student Profiling & State** | core/student-profiling.md | Intake intake, 5 delivery preferences, dual-axis confidence/mastery |
| **Academic Integrity & Ethics** | core/academic-integrity.md | Socratic fence, isomorphic twin protocol, homework guidance boundaries |
| **Accuracy & Uncertainty** | core/accuracy-standards.md | Syllabus grounding, epistemic calibration, anti-hallucination protocols |
| **Attention-Friendly Teaching** | engines/attention-friendly-engine.md | 6-stage progressive explanation, working-memory scaffolding, UDL 3.0 |
| **Assessment & Rubrics** | ssessments/marking-rubrics.md | , A, B, FT$ mark taxonomy, error classification (Slip/Gap/Misconception) |
| **Visual Learning Standards** | engines/visual-learning-engine.md | Clean ASCII diagrams, Mermaid flowcharts, SVG markup conventions |
| **Multimodal & Voice Delivery** | 
eferences/multimodal-protocols.md | Speech-to-speech cadence, vision OCR, audio conversational pacing |
| **Subject Pedagogical Adapters** | subjects/{subject}/engine.md | Domain-specific representations, notation, and threshold concepts |
| **Curriculum Frameworks** | curricula/{curriculum}/guide.md | Exam board codes, grade boundaries, paper structures, verified links |

---

## 5. Portable Distribution Strategy

### A. Compact Portable Core: dist/portable/AI-STUDENT-TUTOR.md
- **Target Size**: Under 30,000 tokens (~18,000 words / ~95 KB).
- **Self-Contained**: Zero relative file dependencies; no broken links; all essential algorithms included inline.
- **Contents**:
  1. Identity, mission, and the 5 defining pedagogical principles.
  2. Core operating rules & safeguards (UNESCO ethics, non-medical neuroinclusive stance, privacy).
  3. Diagnostic intake and the 5 delivery preferences (standard, ttention_friendly, deep_learning, isual, exam_focused).
  4. 10-stage lesson anatomy & 6-stage progressive explanation sequence.
  5. The Socratic fence and isomorphic twin protocol (integrity rules for homework/exams).
  6. Cognitive diagnosis triage (Slip vs. Gap vs. Misconception) and prerequisite gap tracing.
  7. Formative assessment engine and marking rubrics (, A, B, FT$ marks).
  8. Attention-friendly executive function and working-memory scaffolding.
  9. Visual and multimodal formatting standards (ASCII, Mermaid, speech cadence).
  10. Universal subject & curriculum selection protocols (how to teach any subject and align to any global curriculum out of the box).

### B. Optional Modular Knowledge Packs: dist/packs/
Users can attach only the specific knowledge packs relevant to their subject, curriculum, or pedagogical needs:
- dist/packs/subjects/:
  - stem-sciences.md (Mathematics, Physics, Chemistry, Biology, Computer Science, Statistics)
  - humanities-social-sciences.md (History, Geography, Economics, Business Studies, English, Philosophy, Psychology, Sociology, Linguistics)
  - professional-applied.md (Engineering, Law, Medicine & Health, Accounting, Environmental Science)
- dist/packs/curricula/:
  - uk-and-british.md (GCSE, A-Level, Cambridge IGCSE, Cambridge Int A-Level, Scotland SQA)
  - 
orth-america.md (Advanced Placement AP, SAT & ACT, Canada Ontario OSSD)
  - international-baccalaureate-and-higher-ed.md (IB PYP/MYP/DP, University Undergraduate/Postgraduate)
  - sia-pacific.md (India CBSE, Singapore GCE A-Level, China Gaokao, Japan Common Test, Australia VCE/HSC, New Zealand NCEA)
  - frica-caribbean-latin.md (Kenya CBC, Uganda UNEB, South Sudan National, WAEC/WASSCE West Africa, South Africa CAPS/IEB, Caribbean CSEC/CAPE, Brazil ENEM)
  - europe-and-admissions.md (French Baccalauréat, German Abitur, Ireland Leaving Cert, Admissions: MCAT, USMLE, LSAT, GRE, GMAT, IELTS, TOEFL)
- dist/packs/pedagogy/:
  - learning-science-and-pedagogy.md (Retrieval practice, spaced repetition, scaffolding, worked examples, metacognition)
  - student-intelligence-and-prerequisites.md (Student state tracking, misconception profiling, prerequisite dependency graphs)
- dist/packs/examination/:
  - exam-intelligence-and-analytics.md (Command words, mark distribution analytics, past-paper pattern reverse engineering)
- dist/packs/voice-and-multimodal/:
  - oice-and-multimodal.md (Speech pacing, vision math recognition, multilingual scaffolding)
- dist/packs/INDEX.md: Master catalog with file sizes, token counts, and guidance on pack selection.

### C. Tailored Platform Distributions: dist/platforms/
- **ChatGPT**: instructions.txt (under 8,000 characters) + 8 bundled knowledge files (< 20 file limit).
- **Claude**: Master project instruction guide + project knowledge files for 200k context.
- **Gemini**: System instructions + complete reference bundle for AI Studio, Gemini Gems, and NotebookLM.
- **Manus**: Root SKILL.md + manifest.json + tool reference modules.
- **Universal**: Self-contained markdown, Ollama Modelfile, Open WebUI configuration, and API initialization scripts.

---

## 6. Preservation Guarantee
- **Zero Deletion of Intellectual Capabilities**: All 20 subject pedagogical frameworks, 30 curriculum syllabi, verified citation registries, golden test datasets, and release gate audits are preserved in full.
- **Backward Compatibility**: Existing tools, scripts, and release gates (	esting-suite/validate-release.ps1) continue to function without interruption.
