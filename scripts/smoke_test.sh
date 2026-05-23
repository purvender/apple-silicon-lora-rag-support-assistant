#!/usr/bin/env bash
# Quick end-to-end smoke test (index + two RAG queries). Run from project root.
set -euo pipefail
cd "$(dirname "$0")/.."

if [[ ! -d .venv ]]; then
  echo "Missing .venv. Create it: python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt"
  exit 1
fi

# shellcheck disable=SC1091
source .venv/bin/activate

echo "==> Indexing FAQs..."
python scripts/rag_index.py

echo "==> Refund query..."
out=$(python scripts/rag_query.py "Can I get a refund for my annual plan?")
echo "$out"
echo "$out" | grep -q "refunds.txt"

echo "==> Password query..."
out=$(python scripts/rag_query.py "I forgot my password and the reset email never arrived.")
echo "$out"
echo "$out" | grep -q "passwords.txt"

echo "==> Retrieval quality check..."
python scripts/check_retrieval.py

echo "==> Empty index guard..."
rm -rf chroma
python scripts/rag_query.py "test" && exit 1 || true
python scripts/rag_index.py

echo "Smoke test passed."
