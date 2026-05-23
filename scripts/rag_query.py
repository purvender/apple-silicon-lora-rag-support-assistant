import sys
from pathlib import Path

import _bootstrap  # noqa: F401
import chromadb
import ollama
from mlx_utils import PROJECT_ROOT, run_mlx

CHROMA_DIR = PROJECT_ROOT / "chroma"
COLLECTION_NAME = "support_faqs"
EMBED_MODEL = "nomic-embed-text"

if len(sys.argv) < 2:
    print('Usage: python scripts/rag_query.py "your question here"')
    print("Run from the project root after indexing: python scripts/rag_index.py")
    sys.exit(1)

question = sys.argv[1]

client = chromadb.PersistentClient(path=str(CHROMA_DIR))
collection = client.get_or_create_collection(name=COLLECTION_NAME)

if collection.count() == 0:
    print("Error: FAQ index is empty. Run from the project root:")
    print("  python scripts/rag_index.py")
    sys.exit(1)

query_embedding = ollama.embeddings(model=EMBED_MODEL, prompt=question)["embedding"]

results = collection.query(query_embeddings=[query_embedding], n_results=1)

retrieved_docs = results["documents"][0]
retrieved_sources = results["metadatas"][0]
context = "\n\n".join(retrieved_docs)

prompt = f"""You are a customer support assistant.
Answer the customer question using only the FAQ context below.
If the answer is not in the FAQ context, say you do not know.
Be concise and helpful.

FAQ Context:
{context}

Customer Question:
{question}

Answer:
"""

try:
    answer = run_mlx(prompt, use_adapter=True)
except RuntimeError as exc:
    print("Error running MLX model:")
    print(exc)
    sys.exit(1)

print("\n--- Retrieved Sources ---")
for source in retrieved_sources:
    print(source)

print("\n--- Answer ---\n")
print(answer)
