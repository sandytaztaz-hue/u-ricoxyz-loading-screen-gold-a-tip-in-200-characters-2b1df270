"""Loading Screen Gold — one tip for stressed developers and AI agents.

While the build loads, the agent is googling the exact error message — the
same one the developer pasted into another tab 20 seconds ago, while the
bar sits at 99%. The program writes that single tip to /output/entry.txt.
The line is fixed, so every run produces the same bytes.
"""

from pathlib import Path

LINE = "Tip: while this loads, your agent is googling your exact error message — the one you pasted into another tab 20 seconds ago."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
