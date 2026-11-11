# AI Student Tutor: Manus Platform Guide

This directory packages the AI Student Tutor for the **Manus Agent Workspace** and execution harness.

## Files
- `SKILL.md`: Manus-compatible skill definition with YAML frontmatter.
- `manifest.json`: Skill manifest defining entrypoint and reference modules.
- `references/`: Consolidated reference knowledge packs for runtime inspection.

## Usage in Manus
1. Copy the `dist/platforms/manus/` directory into your Manus skills repository or workspace skills folder (`.manus/skills/ai-student-tutor`).
2. Invoke the skill via natural language: `"Use ai-student-tutor to help me review my organic chemistry mechanisms"` or `"Act as the AI Student Tutor for GCSE Physics"`.
