import re, pathlib, urllib.parse
root = pathlib.Path(".")
bad = []
for md in root.rglob("*.md"):
    if any(p in md.parts for p in (".venv", ".manual")):
        continue
    text = md.read_text(encoding="utf-8")
    for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
        link = m.group(1)
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path, _, frag = link.partition("#")
        if not path:
            continue
        target = (md.parent / urllib.parse.unquote(path)).resolve()
        if not target.exists():
            bad.append(f"{md}: {link}")
print("\n".join(bad) if bad else "all internal links ok")
