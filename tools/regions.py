import argparse
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PREVIEW_W = 1600


def window_id():
    out = subprocess.run(["/tmp/wl/winlist"], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if "So tay DaVinci" in line:
            return line.split()[0]
    sys.exit("Không thấy cửa sổ Resolve")


def main():
    p = argparse.ArgumentParser(description="Chụp cửa sổ Resolve, cắt vùng theo toạ độ ảnh xem trước rộng 1600")
    p.add_argument("name")
    p.add_argument("box", nargs="+", type=float, help="x0 y0 x1 y1, lặp lại để ghép nhiều vùng ngang")
    p.add_argument("--width", type=int, default=1400)
    p.add_argument("--raw", help="dùng ảnh chụp sẵn thay vì chụp mới")
    a = p.parse_args()
    if len(a.box) % 4:
        sys.exit("box phải là bội số của 4")
    raw = a.raw or "/tmp/shot_raw.png"
    if not a.raw:
        subprocess.run(["screencapture", "-x", "-o", "-l", window_id(), raw], check=True)
    im = Image.open(raw).convert("RGB")
    k = im.width / PREVIEW_W
    parts = [im.crop(tuple(round(v * k) for v in a.box[i:i + 4])) for i in range(0, len(a.box), 4)]
    gap = round(24 * k) if len(parts) > 1 else 0
    out = Image.new("RGB", (sum(x.width for x in parts) + gap * (len(parts) - 1), max(x.height for x in parts)), (31, 31, 35))
    x = 0
    for part in parts:
        out.paste(part, (x, 0))
        x += part.width + gap
    if out.width > a.width:
        out = out.resize((a.width, round(out.height * a.width / out.width)), Image.LANCZOS)
    dest = ROOT / "assets/img" / f"{a.name}.png"
    out.save(dest, optimize=True)
    print(dest.relative_to(ROOT), out.size)


if __name__ == "__main__":
    main()
