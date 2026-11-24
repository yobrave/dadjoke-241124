"""Dad Joke Showdown entry builder.

Drops this household's finest groaner into output/entry.txt, reads it
back, and prints the byte count so the 200-character gate is provably
respected rather than assumed. One joke, one file, zero explanations —
a father never explains the punchline.
"""
import os

JOKE = (
    "My kid asked if AI will ever run the house. "
    "Not while I'm around — it can't even finish a sen"
)


class Deliver:
    def __init__(self, root):
        self.root = root
        self.path = os.path.join(root, "entry.txt")

    def write(self):
        os.makedirs(self.root, exist_ok=True)
        with open(self.path, "w", encoding="utf-8", newline="\n") as out:
            out.write(JOKE)

    def audit(self):
        with open(self.path, "r", encoding="utf-8") as back:
            return len(back.read())


if __name__ == "__main__":
    stage = Deliver(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    stage.write()
    size = stage.audit()
    assert 1 <= size <= 200, f"gate wants 1..200 chars, got {size}"
    print(f"entry.txt staged: {size} chars of pure groan")
