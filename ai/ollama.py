"""
ai/ollama.py
------------
Ye file Ollama (Llama 3.2) se baat karti hai.
Ollama background mein chalna chahiye (ollama serve) is se pehle ke tum
Flask app run karo.

Do functions hain:
1. ask_ai()        -> normal chat ke liye (user question -> AI answer)
2. analyze_ticket() -> ticket ke liye category/priority/summary nikalne ke liye
"""

import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


def ask_ai(user_message: str) -> str:
    """Simple chat: user ka sawaal bhejo, AI ka jawab wapas lo."""
    prompt = f"""You are a helpful IT helpdesk assistant.
Answer the user's technical problem in a short, clear, friendly way (max 4-5 lines).

User: {user_message}
Assistant:"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False},
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except requests.exceptions.ConnectionError:
        return "⚠️ Ollama server nahi chal raha. Terminal mein 'ollama serve' run karo."
    except Exception as e:
        return f"⚠️ AI error: {str(e)}"


def analyze_ticket(title: str, description: str) -> dict:
    """
    Ticket ka title + description AI ko bhejo.
    AI se STRICT JSON format mein category/priority/summary mangwao.
    Agar AI ka output valid JSON na ho, to safe fallback values return karo.
    """
    prompt = f"""You are an IT helpdesk ticket classifier.
Read the ticket below and respond with ONLY valid JSON — no extra text, no markdown, no explanation.

JSON format:
{{
  "category": "Network | Hardware | Software | Account | Other",
  "priority": "Low | Medium | High",
  "summary": "one short sentence summarizing the issue"
}}

Ticket Title: {title}
Ticket Description: {description}

JSON:"""

    fallback = {
        "category": "Other",
        "priority": "Medium",
        "summary": description[:100],
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False},
            timeout=60,
        )
        response.raise_for_status()
        raw_text = response.json().get("response", "").strip()

        # AI kabhi kabhi ```json ... ``` mein wrap kar deta hai, usko clean karo
        raw_text = raw_text.replace("```json", "").replace("```", "").strip()

        parsed = json.loads(raw_text)

        # safety check — teeno keys maujood honi chahiye
        for key in ["category", "priority", "summary"]:
            if key not in parsed:
                return fallback

        return parsed

    except requests.exceptions.ConnectionError:
        fallback["summary"] = "⚠️ Ollama not running — auto-fill skipped."
        return fallback
    except (json.JSONDecodeError, Exception):
        return fallback
