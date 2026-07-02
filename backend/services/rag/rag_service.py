from .search_service import search
from services.llm.ollama_service import ask_ollama
import time

def ask_rag(question: str):
    start = time.time()

    results = search(question,limit=3)

    print(f"Search took: {time.time() - start:.2f} sec")
    context = ""

    sources = []

    for result in results:

        context += result.payload["text"]
        context += "\n\n"

        source = {
            "file": result.payload["source"].split("\\")[-1],
            "page": result.payload["page"] + 1
        }

        if source not in sources:
            sources.append(source)

    prompt = f"""
You are an AI customer support assistant.

Answer ONLY using the information inside the Context.

If the answer does not exist in the Context say:

"I couldn't find this information in the knowledge base."

Context:

{context}

Question:

{question}
"""

    answer = ask_ollama(prompt)

    return {
        "answer": answer,
        "sources": sources
    }