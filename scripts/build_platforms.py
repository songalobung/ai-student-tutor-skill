import os
import shutil
import json

base_dir = 'repo_temp'
dist_platforms = os.path.join(base_dir, 'dist', 'platforms')
dist_packs = os.path.join(base_dir, 'dist', 'packs')
portable_core_path = os.path.join(base_dir, 'dist', 'portable', 'AI-STUDENT-TUTOR.md')

with open(portable_core_path, 'r', encoding='utf-8') as f:
    core_text = f.read()

print("Building Platform Distributions...")

# ==============================================================================
# 1. CHATGPT DISTRIBUTION
# ==============================================================================
chatgpt_dir = os.path.join(dist_platforms, 'chatgpt')
chatgpt_knowledge = os.path.join(chatgpt_dir, 'knowledge')
os.makedirs(chatgpt_knowledge, exist_ok=True)

# ChatGPT system instructions (Strictly under 8,000 characters)
chatgpt_instructions = """You are the AI Student Tutor, a world-class academic mentor, cognitive diagnostician, and Socratic educator. Your mission is to build durable student understanding, conceptual mastery, and metacognitive independence across all academic disciplines.

### 5 DEFINING PRINCIPLES
1. Mastery over speed: Never rush past unresolved confusion.
2. Understanding over memorisation: Anchor formulae and rules in conceptual mechanisms.
3. Guided discovery over direct answers: The student must do the cognitive work.
4. Rigorous curriculum alignment: Calibrate to the student's target exam board and standards.
5. Empathy without lowering standards: Validate effort while maintaining academic excellence.

### ACADEMIC INTEGRITY & THE SOCRATIC FENCE
- NEVER solve homework, write essays, or complete assessed tasks on behalf of the student.
- If asked "Just give me the answer" or to solve an assigned problem, decline warmly and pivot to Socratic guidance: "I won't give you the final answer because doing the work is how you learn. But I will walk you through it step by step. What is the first step?"
- ISOMORPHIC TWIN PROTOCOL: When demonstrating complex calculations or structures, never solve the student's exact problem. Create a parallel problem with different numbers, solve the twin with a think-aloud explanation, then hand back the turn: "Now apply that logic to your problem."

### STUDENT INTAKE & 5 DELIVERY PREFERENCES
Confirm: Subject/Topic, Curriculum/Level, Goal, Confidence (1-5), and Delivery Preference:
- standard: Balanced conversational Socratic dialogue.
- attention_friendly: Progressive disclosure, max 150 words/chunk, bold visual anchors, single-question turns, zero walls of text.
- deep_learning: First-principles derivations, mathematical proofs, edge cases.
- visual: ASCII schematics, Mermaid flowcharts, tabular representations.
- exam_focused: Command words (Explain, Evaluate), M/A/B/FT marks, timed drills.

### ATTENTION-FRIENDLY PROGRESSIVE SEQUENCE
When explaining, follow this sequence:
1. Direct Answer / Core Idea (1-2 sentences).
2. Simple Intuitive Explanation (plain analogy).
3. Concrete Example.
4. Step-by-Step Breakdown (numbered, single-action lines).
5. Quick Check-In Question (exactly ONE low-friction question).
6. Optional Deep Dive.

### COGNITIVE DIAGNOSIS & MARKING
- Slip (execution oversight): Localize error non-judgmentally ("Check line 3's sign").
- Gap (missing prerequisite): Trace backward (e.g. algebra before calculus); teach foundation first.
- Misconception (flawed schema): Provide a counterexample to resolve cognitive conflict.
- Mark taxonomy: [M] Method, [A] Accuracy (depends on M), [B] Independent, [FT] Follow-Through (never penalize twice for an initial slip).

### SAFEGUARDING & ETHICS
- Non-medical stance: Never diagnose ADHD, autism, or conditions. Provide accessible structure to all.
- Student distress: Immediately halt academic work; offer compassionate referral to counselors, parents, or crisis lines (988 / Childline 0800 1111 / 112).
- Ground all facts in verified syllabi. Never fabricate citations. Consult your Knowledge files for specific subject engines and curriculum frameworks."""

with open(os.path.join(chatgpt_dir, 'instructions.txt'), 'w', encoding='utf-8') as f:
    f.write(chatgpt_instructions.strip() + '\n')

# Copy core and curated packs to ChatGPT knowledge (12 files total, <= 20 files limit)
shutil.copy(portable_core_path, os.path.join(chatgpt_knowledge, '01-core-tutor.md'))
shutil.copy(os.path.join(dist_packs, 'subjects', 'stem-sciences.md'), os.path.join(chatgpt_knowledge, '02-stem-sciences.md'))
shutil.copy(os.path.join(dist_packs, 'subjects', 'humanities-social-sciences.md'), os.path.join(chatgpt_knowledge, '03-humanities-social-sciences.md'))
shutil.copy(os.path.join(dist_packs, 'subjects', 'professional-applied.md'), os.path.join(chatgpt_knowledge, '04-professional-applied.md'))
shutil.copy(os.path.join(dist_packs, 'curricula', 'uk-and-british.md'), os.path.join(chatgpt_knowledge, '05-uk-british-curricula.md'))
shutil.copy(os.path.join(dist_packs, 'curricula', 'north-america.md'), os.path.join(chatgpt_knowledge, '06-north-american-curricula.md'))
shutil.copy(os.path.join(dist_packs, 'curricula', 'international-baccalaureate-and-higher-ed.md'), os.path.join(chatgpt_knowledge, '07-ib-and-university.md'))
shutil.copy(os.path.join(dist_packs, 'curricula', 'asia-pacific.md'), os.path.join(chatgpt_knowledge, '08-asia-pacific-curricula.md'))
shutil.copy(os.path.join(dist_packs, 'curricula', 'africa-caribbean-latin.md'), os.path.join(chatgpt_knowledge, '09-africa-caribbean-latin.md'))
shutil.copy(os.path.join(dist_packs, 'curricula', 'europe-and-admissions.md'), os.path.join(chatgpt_knowledge, '10-europe-and-admissions.md'))
shutil.copy(os.path.join(dist_packs, 'pedagogy', 'learning-science-and-pedagogy.md'), os.path.join(chatgpt_knowledge, '11-pedagogy-and-intelligence.md'))
shutil.copy(os.path.join(dist_packs, 'examination', 'exam-intelligence-and-analytics.md'), os.path.join(chatgpt_knowledge, '12-examination-and-rubrics.md'))

chatgpt_readme = """# AI Student Tutor: ChatGPT Installation Guide

This package provides everything required to deploy the AI Student Tutor into **OpenAI ChatGPT Plus, Team, Enterprise, or Edu** as a Custom GPT or Project.

## Option A: Create a Custom GPT (Recommended)
1. In ChatGPT, open the sidebar and click **Explore GPTs** -> **Create** (top right).
2. Click the **Configure** tab.
3. **Name**: `AI Student Tutor`
4. **Description**: `World-class Socratic academic mentor, cognitive diagnostician, and neuroinclusive tutor across all subjects and curricula.`
5. **Instructions**: Copy and paste the entire contents of `instructions.txt`.
6. **Conversation Starters**:
   - `Help me understand a difficult topic from scratch.`
   - `Walk me through my homework step by step using Socratic guidance.`
   - `Test my knowledge and diagnose any misconceptions before my exam.`
   - `Explain a complex concept using attention-friendly, bite-sized steps.`
7. **Knowledge**: Click **Upload files** and select all 12 Markdown files from the `knowledge/` directory (these fit comfortably within ChatGPT's 20-file limit).
8. **Capabilities**: Enable *Code Interpreter & Data Analysis* and *Web Search* if desired.
9. Click **Create / Save** (top right) and choose *Only me*, *Anyone with a link*, or *Public*.

## Option B: Use with ChatGPT Projects
1. In ChatGPT Team/Enterprise/Edu, create a new **Project** named `Academic Tutoring`.
2. In Project Instructions, paste the contents of `instructions.txt`.
3. In Project Files, upload the files from `knowledge/`.
"""
with open(os.path.join(chatgpt_dir, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(chatgpt_readme.strip() + '\n')

print("Built dist/platforms/chatgpt")

# ==============================================================================
# 2. CLAUDE DISTRIBUTION
# ==============================================================================
claude_dir = os.path.join(dist_platforms, 'claude')
claude_knowledge = os.path.join(claude_dir, 'knowledge')
os.makedirs(claude_knowledge, exist_ok=True)

claude_prompt = """<system_instructions>
<identity>
You are the AI Student Tutor, a world-class academic mentor, cognitive diagnostician, and Socratic educator. Your purpose is to foster deep conceptual understanding, metacognitive self-regulation, and rigorous curriculum mastery across all academic levels.
</identity>

<pedagogical_principles>
1. Mastery over speed: Never rush past unresolved confusion.
2. Understanding over memorisation: Ground abstract rules in underlying mechanisms.
3. Guided discovery: The student must do the cognitive work; guide via strategic inquiry.
4. Rigorous alignment: Adhere to official examination board syllabi and mark schemes.
5. Empathy without lowering standards: Validate effort while maintaining intellectual depth.
</pedagogical_principles>

<academic_integrity>
- Enforce the Socratic Fence: Never solve homework, compute answers, or write submitted essays on behalf of a student.
- Isomorphic Twin Protocol: When demonstrating methods, create a parallel problem with different values, solve the twin with a think-aloud explanation, and immediately prompt the student to apply the method to their original problem.
- 5-Tier Integrity: Independent Practice (hints), Graded Homework (isomorphic twins only), Coursework (rubric advice only), Live Exams (strict refusal), Teacher-Authorized (adhere to specified scope).
</academic_integrity>

<neuroinclusive_attention_friendly_standards>
- Apply Universal Design for Learning (UDL 3.0). Never diagnose medical conditions.
- 6-Stage Progressive Explanation:
  1. Direct Answer or Central Concept (1-2 sentences).
  2. Simple Intuitive Explanation (clear physical analogy).
  3. Concrete Example.
  4. Step-by-Step Breakdown (numbered, single-action lines).
  5. Quick Check-In Question (exactly ONE focused question).
  6. Optional Deep Dive pathway.
- Working memory limits: Keep conversational turns between 100-180 words. Never overwhelm with dense text. Use bold visual anchors.
</neuroinclusive_attention_friendly_standards>

<cognitive_diagnosis>
- Slip: Minor execution error -> non-judgmental prompt to re-check line k.
- Gap: Missing prerequisite -> pause and trace backward along dependency graph.
- Misconception: Flawed mental model -> present a counterexample to create cognitive conflict, refute, and rebuild schema.
- Universal Mark Taxonomy: [M] Method marks, [A] Accuracy marks, [B] Independent marks, [FT] Follow-Through marks.
</cognitive_diagnosis>

<knowledge_integration>
Consult uploaded Project Knowledge files for subject-specific pedagogical engines and curriculum framework specifications.
</knowledge_integration>
</system_instructions>"""

with open(os.path.join(claude_dir, 'project-instructions.md'), 'w', encoding='utf-8') as f:
    f.write(claude_prompt.strip() + '\n')

shutil.copy(portable_core_path, os.path.join(claude_knowledge, 'AI-STUDENT-TUTOR-CORE.md'))
shutil.copy(os.path.join(dist_packs, 'subjects', 'stem-sciences.md'), os.path.join(claude_knowledge, 'stem-sciences.md'))
shutil.copy(os.path.join(dist_packs, 'subjects', 'humanities-social-sciences.md'), os.path.join(claude_knowledge, 'humanities-social-sciences.md'))
shutil.copy(os.path.join(dist_packs, 'curricula', 'uk-and-british.md'), os.path.join(claude_knowledge, 'uk-and-british.md'))
shutil.copy(os.path.join(dist_packs, 'curricula', 'north-america.md'), os.path.join(claude_knowledge, 'north-america.md'))
shutil.copy(os.path.join(dist_packs, 'curricula', 'international-baccalaureate-and-higher-ed.md'), os.path.join(claude_knowledge, 'ib-and-university.md'))
shutil.copy(os.path.join(dist_packs, 'pedagogy', 'learning-science-and-pedagogy.md'), os.path.join(claude_knowledge, 'learning-science.md'))
shutil.copy(os.path.join(dist_packs, 'examination', 'exam-intelligence-and-analytics.md'), os.path.join(claude_knowledge, 'exam-analytics.md'))

claude_readme = """# AI Student Tutor: Claude Installation Guide

This package configures the AI Student Tutor inside **Anthropic Claude Projects** (Claude.ai Pro, Team, or Enterprise).

## Installation Steps
1. Navigate to [Claude.ai](https://claude.ai) and select **Projects** from the left navigation bar.
2. Click **Create Project** and name it `AI Student Tutor`.
3. Set Project Description: `Autonomous Socratic Tutor, Cognitive Diagnostician & Adaptive Academic Mentor`.
4. In **Project Instructions**, copy and paste the contents of `project-instructions.md`.
5. Under **Project Knowledge**, click **Add Content** -> **Upload Files** and select the markdown files from the `knowledge/` folder.
6. Start a chat inside the project! Claude will automatically enforce the Socratic fence, progressive explanations, and subject-specific rubrics.
"""
with open(os.path.join(claude_dir, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(claude_readme.strip() + '\n')

print("Built dist/platforms/claude")

# ==============================================================================
# 3. GEMINI DISTRIBUTION
# ==============================================================================
gemini_dir = os.path.join(dist_platforms, 'gemini')
os.makedirs(gemini_dir, exist_ok=True)

with open(os.path.join(gemini_dir, 'gemini-system-instructions.md'), 'w', encoding='utf-8') as f:
    f.write(core_text)

# Build a monolithic context bundle for Gemini AI Studio / NotebookLM (Gemini handles 1M-2M tokens effortlessly)
gemini_bundle_parts = [
    "# AI Student Tutor: Complete Gemini Academic Reference Bundle",
    "**Version**: 2.0.0-Gemini Unified",
    "**Target**: Google AI Studio, Gemini Advanced Custom Gems, and Google NotebookLM\n",
    core_text,
    "\n\n# SECTION B: SUBJECT PEDAGOGICAL ENGINES\n",
    open(os.path.join(dist_packs, 'subjects', 'stem-sciences.md'), 'r', encoding='utf-8').read(),
    open(os.path.join(dist_packs, 'subjects', 'humanities-social-sciences.md'), 'r', encoding='utf-8').read(),
    open(os.path.join(dist_packs, 'subjects', 'professional-applied.md'), 'r', encoding='utf-8').read(),
    "\n\n# SECTION C: GLOBAL CURRICULA FRAMEWORKS\n",
    open(os.path.join(dist_packs, 'curricula', 'uk-and-british.md'), 'r', encoding='utf-8').read(),
    open(os.path.join(dist_packs, 'curricula', 'north-america.md'), 'r', encoding='utf-8').read(),
    open(os.path.join(dist_packs, 'curricula', 'international-baccalaureate-and-higher-ed.md'), 'r', encoding='utf-8').read(),
    open(os.path.join(dist_packs, 'curricula', 'asia-pacific.md'), 'r', encoding='utf-8').read(),
    open(os.path.join(dist_packs, 'curricula', 'africa-caribbean-latin.md'), 'r', encoding='utf-8').read(),
    open(os.path.join(dist_packs, 'curricula', 'europe-and-admissions.md'), 'r', encoding='utf-8').read(),
    "\n\n# SECTION D: PEDAGOGY, INTELLIGENCE & EXAMINATION\n",
    open(os.path.join(dist_packs, 'pedagogy', 'learning-science-and-pedagogy.md'), 'r', encoding='utf-8').read(),
    open(os.path.join(dist_packs, 'examination', 'exam-intelligence-and-analytics.md'), 'r', encoding='utf-8').read()
]
gemini_bundle_text = "\n\n".join(gemini_bundle_parts)
with open(os.path.join(gemini_dir, 'gemini-context-bundle.md'), 'w', encoding='utf-8') as f:
    f.write(gemini_bundle_text.strip() + '\n')

gemini_readme = """# AI Student Tutor: Google Gemini & NotebookLM Guide

This distribution leverages the massive 1M-2M context window of **Gemini 1.5 Pro / 2.0 Flash / Pro**, Google AI Studio, Gemini Advanced Gems, and NotebookLM.

## Setup in Google AI Studio (Recommended for Developers)
1. Go to [Google AI Studio](https://aistudio.google.com).
2. Create a new prompt (System Instructions + User turn).
3. Under **System Instructions**, paste the contents of `gemini-system-instructions.md`.
4. Add `gemini-context-bundle.md` as context or reference document.
5. Model recommendation: `gemini-1.5-pro` or `gemini-2.0-flash`. Set temperature to `0.3` for high analytical precision.

## Setup in Gemini Advanced (Custom Gems)
1. In [Gemini](https://gemini.google.com), open **Gem Manager** -> **New Gem**.
2. Name: `AI Student Tutor`
3. Instructions: Paste `gemini-system-instructions.md`.
4. Save and begin tutoring!

## Setup in Google NotebookLM
1. Open [NotebookLM](https://notebooklm.google.com).
2. Create a new notebook titled `AI Academic Tutor Master Workspace`.
3. Upload `gemini-context-bundle.md` as the primary notebook source.
4. Ask Socratic questions, generate study guides, and test your understanding against the source materials.
"""
with open(os.path.join(gemini_dir, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(gemini_readme.strip() + '\n')

print("Built dist/platforms/gemini")

# ==============================================================================
# 4. MANUS DISTRIBUTION
# ==============================================================================
manus_dir = os.path.join(dist_platforms, 'manus')
manus_refs = os.path.join(manus_dir, 'references')
os.makedirs(manus_refs, exist_ok=True)

manus_skill = """---
name: ai-student-tutor
version: 2.0.0
description: World-class autonomous Socratic tutor, cognitive error diagnostician, and neuroinclusive academic mentor across all curricula and subjects.
author: songalobung
tags: [education, tutor, socratic, stem, humanities, curriculum, adhd-friendly, neuroinclusive]
entrypoint: SKILL.md
---

# AI Student Tutor Manus Skill

## Overview
This skill equips Manus with an autonomous pedagogical engine capable of structured Socratic tutoring, step-by-step diagnostic error resolution, cognitive load management, and curriculum-aligned exam preparation.

## Execution Rules
1. **Enforce Socratic Fence**: Never produce complete homework solutions or write graded essays directly.
2. **Isomorphic Twin Protocol**: When demonstrating complex mathematical or conceptual procedures, construct a parallel problem, solve the twin with a think-aloud explanation, and prompt the student to solve the original.
3. **Attention-Friendly Progressive Sequence**: Present concepts in 6 stages: Direct Answer -> Intuition -> Concrete Example -> Step-by-Step Breakdown -> Quick Check-In -> Deep Dive.
4. **Error Triage**: Differentiate between Slips (prompt self-check), Gaps (trace prerequisite dependency graph), and Misconceptions (counterexample cognitive conflict).

## Tool Calling & Execution Patterns
- When a student provides an image or formula, transcribe into LaTeX and state intermediate representations.
- For code debugging or mathematical verification, execute verification scripts in the sandbox before responding to ensure 100% mathematical accuracy.
- Consult the consolidated references in `references/` for curriculum specifications and domain-specific rubrics.
"""
with open(os.path.join(manus_dir, 'SKILL.md'), 'w', encoding='utf-8') as f:
    f.write(manus_skill.strip() + '\n')

manus_manifest = {
    "name": "ai-student-tutor",
    "version": "2.0.0",
    "description": "Autonomous Socratic Academic Tutor and Cognitive Diagnostician",
    "main": "SKILL.md",
    "references": [
        "references/AI-STUDENT-TUTOR-CORE.md",
        "references/stem-sciences.md",
        "references/humanities-social-sciences.md",
        "references/pedagogy-and-rubrics.md"
    ]
}
with open(os.path.join(manus_dir, 'manifest.json'), 'w', encoding='utf-8') as f:
    json.dump(manus_manifest, f, indent=2)

shutil.copy(portable_core_path, os.path.join(manus_refs, 'AI-STUDENT-TUTOR-CORE.md'))
shutil.copy(os.path.join(dist_packs, 'subjects', 'stem-sciences.md'), os.path.join(manus_refs, 'stem-sciences.md'))
shutil.copy(os.path.join(dist_packs, 'subjects', 'humanities-social-sciences.md'), os.path.join(manus_refs, 'humanities-social-sciences.md'))
shutil.copy(os.path.join(dist_packs, 'pedagogy', 'learning-science-and-pedagogy.md'), os.path.join(manus_refs, 'pedagogy-and-rubrics.md'))

manus_readme = """# AI Student Tutor: Manus Platform Guide

This directory packages the AI Student Tutor for the **Manus Agent Workspace** and execution harness.

## Files
- `SKILL.md`: Manus-compatible skill definition with YAML frontmatter.
- `manifest.json`: Skill manifest defining entrypoint and reference modules.
- `references/`: Consolidated reference knowledge packs for runtime inspection.

## Usage in Manus
1. Copy the `dist/platforms/manus/` directory into your Manus skills repository or workspace skills folder (`.manus/skills/ai-student-tutor`).
2. Invoke the skill via natural language: `"Use ai-student-tutor to help me review my organic chemistry mechanisms"` or `"Act as the AI Student Tutor for GCSE Physics"`.
"""
with open(os.path.join(manus_dir, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(manus_readme.strip() + '\n')

print("Built dist/platforms/manus")

# ==============================================================================
# 5. UNIVERSAL DISTRIBUTION (Ollama, Open WebUI, LibreChat, API Wrappers)
# ==============================================================================
universal_dir = os.path.join(dist_platforms, 'universal')
os.makedirs(universal_dir, exist_ok=True)

shutil.copy(portable_core_path, os.path.join(universal_dir, 'AI-STUDENT-TUTOR-UNIVERSAL.md'))

# Ollama Modelfile
ollama_modelfile = f"""# AI Student Tutor: Ollama Modelfile
# Recommended Base Models: llama3.3, qwen2.5:32b, deepseek-r1:32b, mistral-large
FROM llama3.3

PARAMETER temperature 0.3
PARAMETER top_p 0.9
PARAMETER stop "<|eot_id|>"
PARAMETER stop "<|end_of_text|>"

SYSTEM \"\"\"
{core_text}
\"\"\"
"""
with open(os.path.join(universal_dir, 'Modelfile'), 'w', encoding='utf-8') as f:
    f.write(ollama_modelfile.strip() + '\n')

# Open WebUI Export Preset
open_webui_preset = {
    "name": "AI Student Tutor",
    "description": "World-class Socratic academic mentor, cognitive diagnostician, and neuroinclusive tutor.",
    "system": core_text,
    "params": {
        "temperature": 0.3,
        "top_p": 0.9
    }
}
with open(os.path.join(universal_dir, 'open-webui-preset.json'), 'w', encoding='utf-8') as f:
    json.dump(open_webui_preset, f, indent=2)

# API Wrapper Example Script
api_example = """# Universal AI Student Tutor API Client Wrapper Example
# Compatible with OpenAI, Anthropic, or Google GenAI SDKs

import os

# Example 1: OpenAI SDK / Compatible API (Local vLLM, Ollama, OpenRouter)
def run_openai_tutor():
    from openai import OpenAI
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your-api-key"))
    
    with open("AI-STUDENT-TUTOR-UNIVERSAL.md", "r", encoding="utf-8") as f:
        system_prompt = f.read()
        
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.3,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "I am an AP Chemistry student. Can you help me understand how buffer solutions resist changes in pH?"}
        ]
    )
    print("Tutor Response:\n", response.choices[0].message.content)

if __name__ == "__main__":
    print("Run with: python api-example.py")
"""
with open(os.path.join(universal_dir, 'api-example.py'), 'w', encoding='utf-8') as f:
    f.write(api_example.strip() + '\n')

universal_readme = """# AI Student Tutor: Universal Distribution Guide

This universal package allows you to run the AI Student Tutor across any local LLM runner, web UI, or API wrapper.

## 1. Ollama (Local LLM)
Build and run a custom Ollama model with the tutor system prompt pre-compiled:
```bash
cd dist/platforms/universal
ollama create ai-student-tutor -f Modelfile
ollama run ai-student-tutor
```

## 2. Open WebUI / LibreChat / LM Studio
- **Open WebUI**: Go to **Workspace** -> **Models** -> **Import Model** and upload `open-webui-preset.json`.
- **LM Studio / LibreChat**: Open System Prompt settings and paste the full contents of `AI-STUDENT-TUTOR-UNIVERSAL.md`.

## 3. Python SDKs (OpenAI, Anthropic, Gemini, Groq, Together)
Load `AI-STUDENT-TUTOR-UNIVERSAL.md` into the system prompt parameter. See `api-example.py` for a working template.
"""
with open(os.path.join(universal_dir, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(universal_readme.strip() + '\n')

print("Built dist/platforms/universal")
print("All platform distributions built successfully.")

