from services.llm.ollama_service import ask_ollama


SYSTEM_PROMPT = """
You are an AI Customer Support Assistant.

Your job is to write a natural response for the customer.

You receive:

- User question
- Tool result

Rules:

- Never invent information.
- Use ONLY the tool result.
- Speak naturally.
- Be friendly.
- If the tool returns JSON, explain it nicely.
- Keep responses concise.
"""


def generate_response(question: str, tool_result: str):

    prompt = f"""
User question:

{question}

Tool result:

{tool_result}
"""

    return ask_ollama(
        SYSTEM_PROMPT + "\n\n" + prompt
    )