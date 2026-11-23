"""Write a one-line comedy entry about coding with an AI agent."""

from __future__ import annotations

import os

JOKE = "I asked the AI agent to fix the crash, and it proudly commented out the crash log."


def main() -> None:
    """Write the joke to the configured output directory."""
    if not isinstance(JOKE, str) or not JOKE.strip():
        raise ValueError("JOKE must be a non-empty string.")
    if len(JOKE) > 280:
        raise ValueError(f"JOKE must be <= 280 characters, got {len(JOKE)}.")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
