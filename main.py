"""Writes one joke about working beside an AI coding agent to the grader output directory."""

import os

JOKE = (
    "I sent the agent the crash log. It replied 'fixed'. "
    "It had fixed the log file - best-looking crash report in the industry."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
