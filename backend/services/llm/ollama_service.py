from ollama import chat

import time


def ask_ollama(
    prompt: str,
    system: str | None = None,
    temperature: float = 0
):

    start = time.time()

    messages = []

    if system:
        messages.append({
            "role": "system",
            "content": system
        })

    messages.append({
        "role": "user",
        "content": prompt
    })

    response = chat(
        model="qwen3:8b",
        messages=messages,
        options={
            "temperature": temperature
        }
    )

    print(f"LLM took: {time.time() - start:.2f} sec")

    return response["message"]["content"]