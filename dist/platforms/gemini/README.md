# AI Student Tutor: Google Gemini & NotebookLM Guide

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
