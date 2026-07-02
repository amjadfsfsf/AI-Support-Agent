import json

from services.llm.ollama_service import ask_ollama
from .tool_registry import TOOLS


SYSTEM_PROMPT = """
You are an AI Agent responsible for validating tool arguments.

A tool has already been selected.

Your task is:

1. Determine whether all required arguments are present.
2. If any required argument is missing, ask ONLY for the missing information.
3. If all required arguments are available, return DONE.

Return ONLY valid JSON.

If arguments are missing:

{
    "status": "missing",
    "missing": ["argument_name"],
    "message": "Natural question asking ONLY for the missing information."
}

If all arguments are complete:

{
    "status": "done"
}

Never invent values.

Never answer the user's original request.

Return JSON only.
"""


def build_tool_prompt(tool_name: str):

    tool = TOOLS[tool_name]

    text = f"""
Tool:
{tool_name}

Description:
{tool["description"]}

Required arguments:
"""

    for arg in tool["required"]:
        text += f"- {arg}\n"

    return text


def collect_arguments(
    tool_name: str,
    current_arguments: dict
):

    prompt = f"""
{build_tool_prompt(tool_name)}

Current arguments:

{json.dumps(current_arguments, indent=2)}
"""

    response = ask_ollama(
        prompt=prompt,
        system=SYSTEM_PROMPT,
        temperature=0
    )

    return json.loads(response)