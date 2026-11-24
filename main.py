"""Dad joke dispatch.

One pun leaves the house wearing a coat. The program walks it to the
output folder, looks back over its shoulder, and confirms the coat came
back too. Exit code stays at zero unless the mirror lies.
"""
import json
import os

JOKE = ("Our kitchen sink stopped draining, so I left it on the table "
        "all week. My wife finally asked what we're waiting for — I said "
        "quiet, I'm letting that sink in.")
KEY = "djk2"
ROUND = "roundtwo"


def route(bucket):
    os.makedirs(bucket, exist_ok=True)
    path = os.path.join(bucket, "entry.txt")
    handle = open(path, "w", encoding="utf-8", newline="\n")
    try:
        handle.write(JOKE)
    finally:
        handle.close()
    with open(path, encoding="utf-8") as reader:
        mirror = reader.read().rstrip("\n")
    return mirror


def main():
    bucket = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    mirror = route(bucket)
    same = mirror == JOKE
    print(json.dumps({"key": KEY, "round": ROUND, "mirror": same, "span": len(mirror)}))
    if not same:
        raise SystemExit(2)


main()
