"""Expand ](PQ:passage) ](SQ:passage) ](P1:passage) placeholders into verified fragment links.
usage: python build.py in.md out.md"""
import sys, re
from pathlib import Path
sys.path.insert(0, str(Path.home() / "Research/.bin"))
from lib import link as L
T = str(Path(__file__).resolve().parent.parent) + "/"
SRC = {
 "PQ": (T+"web/quillette-pinker-2026-11-23-reply.html", "https://quillette.com/2026/11/23/will-we-all-go-together-when-we-go-ai-alignment-scott-alexander-doomerism/"),
 "SQ": (T+"reply-check/sources/B-acx-live-2026-11-24.html", "https://www.astralcodexten.com/p/an-open-letter-to-steven-pinker-on"),
 "P1": (T+"web/quillette-pinker-2026-09-26-letter.html", "https://quillette.com/2026/09/26/an-open-letter-to-scott-alexander-steven-pinker-ai-alignment-safety/"),
}
texts = {k: L.page_text(open(f, encoding="utf-8", errors="replace").read()) for k, (f, _) in SRC.items()}
md = open(sys.argv[1], encoding="utf-8").read()
errs = 0
def rep(m):
    global errs
    k, p = m.group(1), m.group(2)
    try:
        d, n = L.build_fragment(texts[k], p)
    except Exception as e:
        errs += 1
        print(f"ERROR {k}: {p!r}: {e}", file=sys.stderr)
        return m.group(0)
    return f"]({SRC[k][1]}#:~:{d})"
out = re.sub(r"\]\((PQ|SQ|P1):([^)]+)\)", rep, md)
open(sys.argv[2], "w", encoding="utf-8").write(out)
print(f"done, {errs} errors", file=sys.stderr)
