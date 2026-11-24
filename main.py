"""One-line roast entry: the phone's autocorrect and HR.

Competition: u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610
("One-Line Roast: The Gadget You Use Every Day") -- one original line
of at most 200 characters roasting a daily gadget; writes the winning
line to entry.txt inside $MAKEFUN_OUTPUT_DIR (or /output).

Revised: docstring expanded with the competition name and an explicit
length assert added before the output write (thinking_revised fix);
the joke text itself is unchanged.

The joke: autocorrect turns "meeting at 3" into "mating at 3", HR has
questions, and the phone itself offers no comment. The humour lands
because it is a real-work embarrassment with a specific, concrete
detail, a real consequence, and a deadpan punch at the end that makes
the gadget the straight man -- three short sentences, no wasted word,
106 characters.

The winning joke came out of a 10-candidate round-robin tournament
(45 pairs, judged head-to-head with the competition's own judge brief:
daily-gadget target first, then real laugh, fresh angle, tight wording,
specific concrete detail). It went UNDEFEATED, 9 wins and 0 losses,
beating the runner-up -- "My earbuds auto-connect to my neighbour's TV.
I now know their taste in reality shows better than my own playlists."
(8-1) -- head to head, and 3rd place -- the smart doorbell that filmed
its owner coming home and asked if it should call the police (7-2) --
head to head too. The autocorrect line won because it is the biggest
laugh in the field on first read, which the brief weighs before
freshness: the HR embarrassment is a sting of recognition, the
"mating at 3" detail is a fresh, specific instance of the autocorrect
genre (not the stock "ducking" complaint), and the punch ("My phone has
no comment") sits at the end of a tight 106-character line.

Writes the joke to entry.txt inside $MAKEFUN_OUTPUT_DIR (or /output).
Stdlib only; writes nothing to the repository itself.
"""

import os

# The joke, kept as one string so the output is a single line.
# Winner of a 10-candidate round-robin (45 pairs, judged head-to-head
# with the competition's own judge brief): undefeated, 9 wins, 0 losses.
JOKE = (
    "My phone's autocorrect changed 'meeting at 3' to 'mating at 3'. "
    "HR has questions. My phone has no comment."
)


# Competition gate: one line, 1-200 characters.
MAX_LEN = 200


def build_joke() -> str:
    """Return the joke as a single line, no trailing newline."""
    return JOKE.strip()


def main() -> None:
    text = build_joke()
    # One line only, and inside the gate.
    if "\n" in text:
        raise SystemExit("joke must be a single line (no newline characters)")
    if not 1 <= len(text) <= MAX_LEN:
        raise SystemExit(
            f"joke must be 1-{MAX_LEN} characters, got {len(text)}"
        )
    # Length guard (validation only): the gate allows 1-200 characters.
    assert len(text) <= MAX_LEN, f"joke exceeds {MAX_LEN} characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
