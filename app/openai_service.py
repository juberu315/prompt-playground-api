import os
import json
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def ask_ai(system_prompt: str, user_prompt: str) -> str:
    """
    Basic reusable OpenAI function.
    Returns plain text.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content


def ask_ai_json(system_prompt: str, user_prompt: str) -> dict:
    """
    Reusable OpenAI function for JSON output.
    Forces valid JSON response.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=0.1,
        response_format={"type": "json_object"},
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "error": "AI returned invalid JSON",
            "raw": content,
        }