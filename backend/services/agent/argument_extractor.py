import json

from services.llm.ollama_service import ask_ollama



SYSTEM_PROMPT = """
You extract arguments from the user's message.

Return ONLY JSON.

Current arguments:

{}

User message:

...

Update ONLY the arguments you can confidently determine.

Never invent values.

Return JSON only.
"""


def extract_arguments(current_arguments: dict, message: str):

    prompt = f"""
Current arguments:

{json.dumps(current_arguments, indent=2)}

User message:

{message}
"""

    response = ask_ollama(
        prompt=prompt,
        system=SYSTEM_PROMPT,
        temperature=0
    )

    return json.loads(response)