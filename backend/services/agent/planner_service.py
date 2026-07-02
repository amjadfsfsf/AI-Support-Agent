import json

from services.llm.ollama_service import ask_ollama
from .tool_registry import TOOLS

def build_tools_prompt():

    text = "AVAILABLE TOOLS\n\n"

    for tool_name, tool in TOOLS.items():

        text += f"Tool: {tool_name}\n"
        text += f"Description: {tool['description']}\n\n"

        text += "Required arguments:\n"

        for arg in tool["required"]:
            text += f"- {arg}\n"

        text += "\nDefault arguments:\n"
        text += f"{tool['arguments']}\n\n"

        text += "Examples:\n"

        for example in tool["examples"]:
            text += f"- {example}\n"

        text += "\n-----------------------------\n\n"

    return text
SYSTEM_PROMPT = f"""
You are an AI Agent Planner.

Your ONLY responsibility is to decide whether the user's request should:

1. Use one of the available tools.
2. Be answered using the knowledge base (RAG).

Never answer the question.

Return ONLY valid JSON.

{build_tools_prompt()}

Rules:

- If the user's intent clearly matches one of the available tools,
  ALWAYS return action = "tool".

- If arguments are missing,
  leave them as empty strings.

- Use action = "answer"
  ONLY when none of the available tools can solve the request.

Return ONLY JSON.
"""

def plan(question: str):



    response = ask_ollama(
        prompt=question,
        system=SYSTEM_PROMPT,
        temperature=0
    )
    data = json.loads(response)

    if data.get("action") == "tool":

        if "arguments" not in data:

            arguments = {}

            tool = data.get("tool")

            if tool in TOOLS:

                for arg in TOOLS[tool]["required"]:

                    if arg in data:
                        arguments[arg] = data.pop(arg)
                    else:
                        arguments[arg] = ""

            data["arguments"] = arguments

    return data

