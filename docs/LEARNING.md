# Learning guide

A short path for developers new to local LLMs (especially from Java backgrounds).

## 1. What you are building

A **support assistant** with two independent knobs:

| Knob | Technology | What it changes |
|------|------------|-----------------|
| **Behavior / tone** | MLX + LoRA | How answers are phrased (polite, product names, structure) |
| **Facts / policy** | RAG (Ollama embed + Chroma) | Which policy text the model must use |

## 2. LoRA (fine-tuning)

The base model is frozen. LoRA adds small trainable matrices—like plugging in a **custom adapter** on a fixed service.

- Training data: `data/support/*.jsonl` (`prompt` + `completion` per line)
- Output: `adapters-llama3-1b/adapters.safetensors`

**Try:** Change one line in `train.jsonl`, re-run `mlx_lm.lora`, and compare `tuned_only` vs `base_only` in eval.

## 3. Embeddings and RAG

- **Embedding** = turning text into a vector of numbers so similar meanings sit close together.
- **Index** (`rag_index.py`): embed each FAQ file with Ollama `nomic-embed-text`, store in Chroma.
- **Query** (`rag_query.py`): embed the question, find the nearest FAQ vector, paste that text into the prompt.

**Java analogy:** embed ≈ hash into semantic space; Chroma ≈ a small search index; RAG ≈ `SELECT policy FROM faq WHERE similarity(question) LIMIT 1` then call the LLM.

## 4. Four evaluation modes

| Mode | LoRA | RAG | Teaches |
|------|------|-----|---------|
| `base_only` | No | No | Generic model |
| `tuned_only` | Yes | No | Style without guaranteed facts |
| `base_rag` | No | Yes | Facts without tuned tone |
| `tuned_rag` | Yes | Yes | Best combined setup |

Run: `python scripts/eval_compare.py -o compare_results.md` (slow) or `python scripts/check_retrieval.py` (fast, retrieval only).

## 5. Hands-on exercises

1. **Break retrieval:** Edit `docs/faqs/refunds.txt`, run `rag_index.py`, ask a refund question again.
2. **Retrieval check:** `python scripts/check_retrieval.py` — should be 10/10 PASS.
3. **Empty index:** Delete `chroma/`, run `rag_query.py` — should refuse with a clear error.
4. **Four modes:** Pick one question in `data/eval/test_prompts.txt` and read all four answers in `compare_results.md`.

## 6. Python imports (`_bootstrap.py`)

`sys.path` is Python’s module search list (like classpath). Only directories on that list are importable. `_bootstrap.py` ensures `scripts/` is on the path so `from mlx_utils import ...` works when you run `python scripts/rag_query.py` from the project root.
