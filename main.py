"""djk6: the dinner-table pun gate. One line of dad comedy in, verdict out."""
import json
import os
import sys
from pathlib import Path

LIMIT = 200
TAG = "djk6-table-gate-r11251422"


class TableGate:
    def __init__(self, ceiling):
        self.ceiling = ceiling
        self.payload = None
        self.reason = "unread"

    def serve(self, source: Path, out_dir: Path) -> dict:
        raw = source.read_text(encoding="utf-8")
        text = raw.strip()
        self.payload = {"tag": TAG, "chars": len(text), "ceiling": self.ceiling}
        if 0 < len(text) <= self.ceiling and text and not text.isspace():
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / "entry.txt").write_bytes(text.encode("utf-8"))
            self.reason = "served"
            self.payload["served"] = True
        else:
            self.reason = "off the table"
            self.payload["served"] = False
        return self.payload

    def verdict_line(self, report):
        return "VERDICT " + json.dumps({"served": report["served"], "chars": report["chars"], "tag": report["tag"], "why": self.reason})


def main() -> int:
    here = Path(__file__).resolve().parent
    drop = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    gate = TableGate(LIMIT)
    report = gate.serve(here / "entry.txt", drop)
    print(gate.verdict_line(report))
    return 0 if report.get("served") else 1


if __name__ == "__main__":
    sys.exit(main())
