import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def entry(shots, sid):
    text = (ROOT / shots).read_text()
    m = re.search(rf"^### {re.escape(sid)} — .*?(?=^### |\Z)", text, re.S | re.M)
    if not m:
        sys.exit(f"Không thấy {sid} trong {shots}")
    return m.group(0)


def main():
    shots, sid = sys.argv[1], sys.argv[2]
    e = entry(shots, sid)
    target = re.search(r"\*\*Chèn vào:\*\* `([^`]+)` — ngay sau heading `([^`]+)`", e)
    alt = re.search(r"\*\*Alt \+ chú thích:\*\* `(!\[[^`]+\))`\s*—\s*(\*[^\n]+\*)", e)
    if not target or not alt:
        sys.exit(f"{sid}: không đọc được Chèn vào / Alt")
    md, heading = ROOT / target.group(1), target.group(2)
    image, caption = alt.group(1), alt.group(2)
    png = re.search(r"\(([^)]+)\)", image).group(1)
    if not (md.parent / png).resolve().exists():
        sys.exit(f"{sid}: chưa có file ảnh {png}")
    lines = md.read_text().split("\n")
    if any(png in line for line in lines):
        print(f"{sid}: đã nhúng sẵn trong {target.group(1)}")
        return
    idx = [i for i, line in enumerate(lines) if line.strip() == heading.strip()]
    if len(idx) != 1:
        sys.exit(f"{sid}: heading '{heading}' xuất hiện {len(idx)} lần trong {target.group(1)}")
    i = idx[0] + 1
    lines[i:i] = ["", image, caption]
    md.write_text("\n".join(lines))
    print(f"{sid}: nhúng vào {target.group(1)} sau '{heading}'")


if __name__ == "__main__":
    main()
