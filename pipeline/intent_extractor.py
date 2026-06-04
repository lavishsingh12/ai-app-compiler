import json
from pipeline.gemini_helper import ask_gemini


def extract_intent(user_prompt):

    prompt = f"""
Convert the following app request into JSON.

Return ONLY valid JSON.

User Request:
{user_prompt}

Output Format:

{{
    "app_type": "",
    "features": []
}}
"""

    response = ask_gemini(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()


    try:
        return json.loads(response)

    except Exception as e:
        print("ERROR:", e)

        return {
            "app_type": "Unknown",
            "features": []
        }