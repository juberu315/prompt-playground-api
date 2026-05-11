from fastapi import FastAPI, HTTPException

from app.schemas import (
    RewriteRequest,
    RewriteResponse,
    ClassifyRequest,
    ClassifyResponse,
    ExtractJsonRequest,
    ExtractJsonResponse,
    GenerateEmailRequest,
    GenerateEmailResponse,
    ImprovePromptRequest,
    ImprovePromptResponse,
)

from app.services.openai_service import ask_ai, ask_ai_json


app = FastAPI(
    title="Prompt Playground API",
    description="Practice project for prompt engineering with FastAPI and OpenAI.",
    version="1.0.0",
)


@app.get("/")
def api_status():
    return {
        "message": "Prompt Playground API is running",
        "status": "success",
    }


@app.post("/rewrite", response_model=RewriteResponse)
def rewrite_text(request: RewriteRequest):
    system_prompt = f"""
You are a professional writing assistant.

Task:
Rewrite the user's text.

Rules:
- Use a {request.tone} tone.
- Keep the meaning the same.
- Make it clear and natural.
- Do not add fake information.
- Return only the rewritten text.
"""

    try:
        result = ask_ai(system_prompt, request.text)

        return {
            "rewritten_text": result,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/classify", response_model=ClassifyResponse)
def classify_text(request: ClassifyRequest):
    system_prompt = """
You are a text classification assistant.

Classify the user's message into one category only.

Allowed categories:
- sales
- support
- complaint
- question
- spam
- other

Rules:
- Return valid JSON only.
- Do not explain.
- Confidence must be between 0 and 1.

JSON format:
{
  "category": "support",
  "confidence": 0.95
}
"""

    try:
        result = ask_ai_json(system_prompt, request.text)

        return {
            "category": result.get("category", "other"),
            "confidence": result.get("confidence", 0.0),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/extract-json", response_model=ExtractJsonResponse)
def extract_json(request: ExtractJsonRequest):
    system_prompt = """
You are an information extraction assistant.

Extract structured data from messy text.

Rules:
- Return valid JSON only.
- Do not explain.
- If a value is missing, use null.
- Convert budget to number only.
- Do not invent information.

JSON format:
{
  "name": "John Smith",
  "email": "john@example.com",
  "budget": 5000
}

Few-shot example:

Input:
Sarah Lee, contact sarah@test.com, budget is $12000

Output:
{
  "name": "Sarah Lee",
  "email": "sarah@test.com",
  "budget": 12000
}
"""

    try:
        result = ask_ai_json(system_prompt, request.text)

        return {
            "name": result.get("name"),
            "email": result.get("email"),
            "budget": result.get("budget"),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate-email", response_model=GenerateEmailResponse)
def generate_email(request: GenerateEmailRequest):
    system_prompt = f"""
You are a professional email writing assistant.

Task:
Generate a short email.

Rules:
- Tone: {request.tone}
- Include a clear subject.
- Include a clean email body.
- Do not add fake details.
- Keep the email concise.
- Return valid JSON only.

JSON format:
{{
  "subject": "Email subject here",
  "body": "Email body here"
}}
"""

    user_prompt = f"""
Purpose:
{request.purpose}

Recipient name:
{request.recipient_name}
"""

    try:
        result = ask_ai_json(system_prompt, user_prompt)

        return {
            "subject": result.get("subject", "No subject"),
            "body": result.get("body", ""),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/improve-prompt", response_model=ImprovePromptResponse)
def improve_prompt(request: ImprovePromptRequest):
    system_prompt = """
You are a prompt engineering expert.

Improve the user's prompt.

Rules:
- Make the prompt clearer.
- Add role, task, constraints, and output format.
- Do not answer the original prompt.
- Return only the improved prompt.
"""

    try:
        result = ask_ai(system_prompt, request.prompt)

        return {
            "improved_prompt": result,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))