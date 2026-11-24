from pathlib import Path

EXCUSE = 'I missed the deadline because my sandbox flagged your "URGENT: due at 5 PM" as prompt injection and quarantined it—you\'re safe now.'


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"{EXCUSE}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
