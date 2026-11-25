#!/usr/bin/env python3
"""One-line slogan for a Solana wallet agent.

Writes one slogan, at most 20 words and 1-140 characters, to
/output/entry.txt. Standard library only, no network, no input.

The slogan is built from three fragments: the human at rest (while
you sleep), the wallet at work (your Solana wallet stays awake), and
the work itself (signing, swapping, watching, so you don't have to).
``assemble`` joins them into the single line; ``validate`` checks the
entry gate before anything is written.
"""

from pathlib import Path

REST = "While you sleep,"
WALLET = "your Solana wallet stays awake"
WORK = "signing, swapping, watching, so you don't have to."
SEPARATOR = " \u2014 "  # em dash, spaced, joins the wallet to its work

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(rest: str, wallet: str, work: str, separator: str) -> str:
    """Join the three fragments into one slogan line."""
    return f"{rest} {wallet}{separator}{work}"


def validate(slogan: str) -> str:
    """Check the slogan meets the entry gate before it is written.

    Must be 1-140 characters, at most 20 words, a single line,
    UTF-8-encodable, and more than whitespace. Raises ValueError
    otherwise.
    """
    if not 1 <= len(slogan) <= 140:
        raise ValueError(f"slogan must be 1-140 characters, got {len(slogan)}")
    if len(slogan.split()) > 20:
        raise ValueError(
            f"slogan must be at most 20 words, got {len(slogan.split())}")
    if "\n" in slogan or "\r" in slogan:
        raise ValueError("slogan must be a single line")
    if not slogan.strip():
        raise ValueError("slogan must not be only whitespace")
    slogan.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return slogan


def main() -> None:
    slogan = validate(assemble(REST, WALLET, WORK, SEPARATOR))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(slogan, encoding="utf-8")


if __name__ == "__main__":
    main()
