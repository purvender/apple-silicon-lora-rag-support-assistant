# Contributing

Thank you for helping others learn from this project.

## Before you open a PR

1. Run from the project root with Ollama running.
2. `bash scripts/smoke_test.sh`
3. `python scripts/check_retrieval.py`

Full four-mode eval (`eval_compare.py`) is optional but appreciated for larger changes.

## What to contribute

- Clearer docs (`docs/LEARNING.md`, `docs/TROUBLESHOOTING.md`)
- Better FAQ wording (fictional AcornDesk only—no real customer data)
- Retrieval checks and exercises
- Bug fixes in `scripts/`

## What not to submit

- Real customer emails, tickets, or company policies
- `.venv/`, `chroma/`, `compare_results.md`, or API keys
- Large unrelated refactors

## JSONL format

Each line in `data/support/*.jsonl`:

```json
{"prompt": "Customer asks: ...", "completion": "Support reply ..."}
```

## Code style

- Keep scripts small and readable.
- Match existing patterns (`pathlib`, project-root paths).
- Run `python scripts/rag_index.py` after FAQ changes.

## Questions

Open a GitHub **Discussion** or **Issue** with your OS version, Python version, and the exact command plus error text.
