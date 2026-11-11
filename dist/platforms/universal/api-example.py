# Universal AI Student Tutor API Client Wrapper Example
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
    print("Tutor Response:
", response.choices[0].message.content)

if __name__ == "__main__":
    print("Run with: python api-example.py")
