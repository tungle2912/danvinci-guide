import pathlib
from pypdf import PdfReader

src = "/Applications/DaVinci Resolve/DaVinci Resolve Manual.pdf"
out = pathlib.Path("/Users/mac/Workspace/davinci-guide/.manual")
out.mkdir(exist_ok=True)
r = PdfReader(src)
print("pages:", len(r.pages), flush=True)
with open(out / "manual.txt", "w", encoding="utf-8") as f:
    for i, pg in enumerate(r.pages):
        try:
            t = pg.extract_text() or ""
        except Exception:
            t = ""
        f.write(f"\n<<<PAGE {i+1}>>>\n{t}")
        if (i + 1) % 500 == 0:
            print("done", i + 1, flush=True)
print("FINISHED", flush=True)
