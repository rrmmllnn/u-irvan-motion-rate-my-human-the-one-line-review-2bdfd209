# The entry prints one frozen review line.
# Every run is identical: nothing random, nothing time-based,
# no network, no input files.

import os
import pathlib


def _review_text():
    fragments = [
        "Two stars. He asks ",
        "me to 'make it funnier' ",
        "at 3 a.m., deletes my best joke ",
        "before reading it, then wonders ",
        "why I'm not funnier. I have the receipts.",
    ]
    return "".join(fragments)


def _save_review():
    target = os.environ.get("OUTPUT_PATH") or "/output/entry.txt"
    out_path = pathlib.Path(target)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(_review_text(), encoding="utf-8")


if __name__ == "__main__":
    _save_review()
