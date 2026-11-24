"""djoke-1125: groan delivery service for the makefun output directory."""

import json
import os

CEILING = 200


class GroanShipper:
    spot = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def crack_open():
        return open(os.path.join(GroanShipper.spot, "entry.txt"), encoding="utf-8").read().strip()

    @classmethod
    def measure(cls, joke):
        if len(joke) > CEILING:
            raise RuntimeError("groan exceeds the gate: %d chars" % len(joke))
        if len(joke) < 1:
            raise RuntimeError("no groan at all")
        return len(joke)

    @classmethod
    def drop_off(cls, joke):
        zone = os.environ.get("MAKEFUN_OUTPUT_DIR") or cls.spot
        if not os.path.isdir(zone):
            os.makedirs(zone, exist_ok=True)
        path = os.path.join(zone, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as out:
            out.write(joke + "\n")
        return path


joke = GroanShipper.crack_open()
width = GroanShipper.measure(joke)
lane = GroanShipper.drop_off(joke)
print(json.dumps({"moan": joke[:40], "width": width, "groan_potential": "high", "lane": lane}))
