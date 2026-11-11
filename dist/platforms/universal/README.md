# AI Student Tutor: Universal Distribution Guide

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
