"""Dad joke gatekeeper: guards the pun, hands it over once it clears the bar."""
STAMP = "onebug-11251142-djk3"
import json
import os
from pathlib import Path

BAR = 200
PUN = ("I planted a lightbulb in the garden "
       "because I wanted to grow a power plant.")
GATE = Path(__file__).resolve().parent / "entry.txt"


def guard(raw):
    trimmed = raw.strip()
    if len(trimmed) > BAR:
        raise ValueError("over the bar")
    if not trimmed:
        raise ValueError("empty pun")
    return {"pun_ok": True, "stamp": STAMP, "words": len(trimmed.split()), "bar": BAR}


def hand_over():
    payload = {"pun_ok": False, "bar": BAR}
    try:
        payload = guard(GATE.read_text(encoding="utf-8"))
    except ValueError as miss:
        payload["why"] = str(miss)
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and payload.get("pun_ok"):
        Path(bay).mkdir(parents=True, exist_ok=True)
        (Path(bay) / "entry.txt").write_bytes(GATE.read_bytes())
    print(json.dumps(payload))


if __name__ == "__main__":
    hand_over()
