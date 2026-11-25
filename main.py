import json
import os
from pathlib import Path

DAD_MAX = 200


def perform():
    source = Path(__file__).resolve().parent / "entry.txt"
    raw = source.read_text(encoding="utf-8")
    raw = raw.replace("\r", "")
    rows = raw.split("\n")
    line = ""
    index = 0
    while index < len(rows):
        if rows[index].strip():
            line = rows[index].strip()
            break
        index += 1
    if not 1 <= len(line) <= DAD_MAX:
        raise ValueError("dad joke is %d characters, gate wants 1..%d" % (len(line), DAD_MAX))
    bucket = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
    bucket.mkdir(parents=True, exist_ok=True)
    served_to = bucket / "entry.txt"
    served_to.write_text(line, encoding="utf-8")
    if served_to.read_text(encoding="utf-8") != line:
        raise ValueError("the file came back different from the joke told")
    print(json.dumps({"state": "served", "count": len(line), "served_to": str(served_to)}))


if __name__ == "__main__":
    perform()
