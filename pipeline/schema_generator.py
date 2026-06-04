import json
from pipeline.gemini_helper import ask_gemini


def generate_schema(system_design):

    prompt = f"""
    You are a software architect.

    Based on this architecture:

    {system_design}

    Generate SIMPLE and CONCISE schemas.

    Rules:
    - Keep output short
    - Maximum 5 UI pages
    - Maximum 5 API endpoints
    - Maximum 5 database tables
    - Maximum 3 roles
    - No descriptions
    - No nested objects
    - No long explanations

    Return ONLY valid JSON.

    Format:

    {{
    "ui_schema": {{
        "pages": []
    }},

    "api_schema": {{
        "endpoints": []
    }},

    "db_schema": {{
        "tables": []
    }},

    "auth_schema": {{
        "roles": []
    }}
    }}
    """

    response = ask_gemini(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        return json.loads(response)

    except Exception as e:
        print("SCHEMA ERROR:", e)

        return {
            "ui_schema": {},
            "api_schema": {},
            "db_schema": {},
            "auth_schema": {}
        }