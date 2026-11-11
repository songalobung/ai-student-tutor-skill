# AI Student Tutor: ChatGPT Installation Guide

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
