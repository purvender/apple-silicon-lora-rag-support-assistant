# Troubleshooting

## Ollama: `Failed to connect to Ollama`

**Cause:** Ollama is not running.

**Fix:**

1. Open the Ollama app, or run `ollama serve`.
2. `ollama pull nomic-embed-text`
3. `ollama list` should show `nomic-embed-text`.

Indexing and RAG modes require Ollama. MLX generation does not.

## `FAQ index is empty`

**Cause:** `chroma/` missing or never indexed.

**Fix:**

```bash
python scripts/rag_index.py
```

You need this once per machine (and again after editing `docs/faqs/`).

## Hugging Face / SSL errors during eval

**Symptom:** `[ERROR]` with `huggingface.co` or `SSLError` in `compare_results.md`.

**Cause:** MLX re-checks the base model over the network; long runs can hit transient SSL issues on macOS LibreSSL.

**Fix:**

1. Pre-download the model once:

```bash
python -m mlx_lm generate \
  --model mlx-community/Llama-3.2-1B-Instruct-4bit \
  --prompt "hi" \
  --max-tokens 1
```

2. Re-run eval. `mlx_utils.py` retries up to 3 times automatically.

## `ModuleNotFoundError: mlx_utils`

**Cause:** Not running from project root, or wrong working directory.

**Fix:**

```bash
cd /path/to/apple-silicon-lora-rag-support-assistant
python scripts/rag_query.py "your question"
```

## Smoke test deleted my index

**Cause:** `smoke_test.sh` deliberately deletes `chroma/` to test the empty-index guard, then re-indexes at the end.

**Fix:** No action needed if smoke test passed. Otherwise run `python scripts/rag_index.py`.

## Retrieval check failures

Run:

```bash
python scripts/rag_index.py
python scripts/check_retrieval.py
```

If a question fails, improve the matching FAQ file in `docs/faqs/` or update `data/eval/expected_sources.jsonl` if expectations changed.

## Intel Mac / non-Apple Silicon

MLX is intended for **Apple Silicon**. This project may not run on Intel Macs or Linux without different tooling.
