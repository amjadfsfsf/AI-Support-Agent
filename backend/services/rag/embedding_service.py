from ollama import embed
import time

MODEL = "nomic-embed-text"


def get_embedding(text: str):
    start = time.time()
    response = embed(
        model=MODEL,
        input=text
    )
    print(f"Embedding took: {time.time() - start:.2f} sec")

    return response["embeddings"][0]