"""Chụp cửa sổ DaVinci Resolve, cắt bỏ thanh menu macOS và Dock, lưu PNG nhẹ vào assets/img."""
import subprocess, sys, time, pathlib
from PIL import Image

name = sys.argv[1]
width = int(sys.argv[2]) if len(sys.argv) > 2 else 1600
out_dir = pathlib.Path(__file__).resolve().parent.parent / "assets" / "img"
raw = pathlib.Path("/tmp/resolve_raw.png")

subprocess.run(["osascript", "-e", 'tell application "DaVinci Resolve" to activate'], check=False)
time.sleep(1.5)
subprocess.run(["screencapture", "-x", "-t", "png", str(raw)], check=True)

im = Image.open(raw)
W, H = im.size
# Thanh menu macOS ~ 2.9% chiều cao trên cùng; Dock ~ 6.9% dưới cùng (đo trên màn 3456x2234)
top = round(H * 0.0295)
bottom = round(H * 0.929)
im = im.crop((0, top, W, bottom))
if im.width > width:
    im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
dest = out_dir / f"{name}.png"
im.save(dest, optimize=True)
print(dest, im.size, f"{dest.stat().st_size // 1024} KB")
