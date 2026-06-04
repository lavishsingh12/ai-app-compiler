import json
from pipeline.gemini_helper import ask_gemini


def design_system(intent_data):

    prompt = f"""
You are a software architect.

Given this intent:

{intent_data}

Generate a SIMPLE architecture.

Rules:
- Keep output concise
- No descriptions
- No nested objects
- Only names

Return ONLY JSON.

Format:

{{
  "entities": [],
  "roles": [],
  "modules": []
}}
"""

    response = ask_gemini(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        return json.loads(response)

    except:
        return {
            "entities": [],
            "roles": [],
            "modules": []
        }