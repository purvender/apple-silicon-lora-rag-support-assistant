import subprocess
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BASE_MODEL = "mlx-community/Llama-3.2-1B-Instruct-4bit"
ADAPTER_PATH = PROJECT_ROOT / "adapters-llama3-1b"
MAX_RETRIES = 3
RETRY_DELAY_SEC = 2


def parse_mlx_output(text: str) -> str:
    if "==========" in text:
        parts = [p.strip() for p in text.split("==========") if p.strip()]
        for part in parts:
            if part.startswith(("Calling `python", "Prompt:", "Generation:", "Peak memory:")):
                continue
            if "tokens-per-sec" in part or "Peak memory" in part:
                continue
            return part.strip()
    return text.strip()


def run_mlx(prompt: str, use_adapter: bool = True, max_tokens: int = 200) -> str:
    cmd = [
        sys.executable, "-m", "mlx_lm", "generate",
        "--model", BASE_MODEL,
        "--prompt", prompt,
        "--max-tokens", str(max_tokens),
    ]
    if use_adapter:
        cmd.extend(["--adapter-path", str(ADAPTER_PATH)])

    last_error = ""
    for attempt in range(1, MAX_RETRIES + 1):
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(PROJECT_ROOT),
        )
        if result.returncode == 0:
            return parse_mlx_output(result.stdout)

        last_error = result.stderr.strip() or "MLX generation failed"
        if attempt < MAX_RETRIES:
            time.sleep(RETRY_DELAY_SEC)

    raise RuntimeError(last_error)
