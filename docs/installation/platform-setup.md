# Platform-Specific Installation & Runtime Configuration Guide

The Student Academic Tutor is an architecture designed for deployment across leading Large Language Model agent runtimes. This guide provides exact, step-by-step installation instructions for each target environment.

---

## 1. Claude / Claude Code / Anthropic Console

### Method A: Claude Code / CLI Integration
1. Place the `student-academic-tutor` folder into your custom skills path:
   ```bash
   mkdir -p ~/.claude/skills
   cp -r student-academic-tutor ~/.claude/skills/
   ```
2. In your `.claude/config.json` or workspace instruction file, include:
   ```json
   {
     "skills": ["student-academic-tutor"]
   }
   ```

### Method B: Claude Projects (Web Interface)
1. Open your Claude Project at [claude.ai](https://claude.ai).
2. Under **Project Knowledge**, upload `SKILL.md` and key sub-modules (such as `core/` and the target subject/curriculum folder).
3. In **Project Instructions**, paste:
   ```markdown
   You are operating as the Student Academic Tutor. Load your operational rules from SKILL.md.
   Always diagnose prior knowledge before explaining, adhere to the Socratic Fence for homework,
   and adapt pacing to the student's curriculum and demonstrated mastery.
   ```

---

## 2. Gemini CLI & Google Antigravity

1. Clone or copy the repository directly into your workspace skills directory:
   ```powershell
   git clone https://github.com/songalobung/ai-student-tutor-skill.git "$HOME\.gemini\skills\student-academic-tutor"
   ```
2. The runtime automatically discovers the skill via the YAML frontmatter in `SKILL.md`.
3. To activate during a session, type:
   ```
   Teach me calculus integration by parts for A-Level Maths
   ```

---

## 3. Manus Agent Runtime

1. In the Manus agent configuration dashboard, navigate to **Custom Skills / Tools**.
2. Add a new skill entry pointing to `student-academic-tutor/SKILL.md`.
3. Ensure file read permissions are granted so Manus can dynamically access modular subject engines under `subjects/` and curriculum guidelines under `curricula/`.
4. Manus auto-indexes `manifest.json` for tool routing.

---

## 4. OpenAI Codex / Assistants API / Custom GPTs

### Custom GPT Setup:
1. Go to the [OpenAI GPT Builder](https://chatgpt.com/gpts/editor).
2. In the **Instructions** box, paste the contents of `SKILL.md`.
3. In **Knowledge**, upload the zip file or core markdown files (`core/`, `engines/`, `pedagogy/`, `subjects/`).
4. In **Capabilities**, enable *Code Interpreter* (for mathematical calculations and plotting) and *Web Browsing* (for verifying up-to-date syllabus revisions).

---

## 5. Open WebUI / Ollama (Local Self-Hosted)

1. Open Open WebUI $\to$ **Workspace** $\to$ **Modelfiles**.
2. Create a new Modelfile inheriting from your preferred base model (e.g., `llama3.3:70b` or `qwen2.5:32b`).
3. In the System Prompt section, paste `SKILL.md`.
4. Upload `knowledge-base/` and `assessments/` into Open WebUI Knowledge collections for RAG retrieval during student study sessions.

