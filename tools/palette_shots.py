"""Click từng palette trang Color (chỉ khi Resolve đang ở trên cùng) rồi chụp vùng palette."""
import subprocess, time, sys
from PIL import Image

pos = {}
for line in open("/tmp/palette_pos.txt"):
    parts = line.strip().split("|")
    if len(parts) == 5 and parts[0] not in pos and int(parts[2]) > 600:
        name, x, y, w, h = parts[0], *map(int, parts[1:])
        pos[name] = (x + w // 2, y + h // 2)

def frontmost():
    return subprocess.run(["osascript", "-e", 'tell application "System Events" to get name of first process whose frontmost is true'],
                          capture_output=True, text=True).stdout.strip()

def win_id():
    out = subprocess.run(["/tmp/wl/winlist"], capture_output=True, text=True).stdout
    return next(l.split()[0] for l in out.splitlines() if "So tay DaVinci" in l)

wid = win_id()
for name, slug in [("Color Wheels", "wheels"), ("Curves", "curves"), ("Qualifier", "qualifier"),
                   ("Window", "window"), ("Tracker", "tracker"), ("Blur", "blur"), ("Key", "key"), ("Color Warper", "warper")]:
    if frontmost() != "Resolve":
        print("DỪNG: Resolve không còn ở trên cùng"); sys.exit(1)
    x, y = pos[name]
    subprocess.run(["osascript", "-e", f'tell application "System Events" to click at {{{x}, {y}}}'], check=True)
    time.sleep(1.2)
    subprocess.run(["screencapture", "-x", "-o", "-l", wid, "/tmp/pal.png"], check=True)
    im = Image.open("/tmp/pal.png").convert("RGB")
    W, H = im.size
    crop = im.crop((0, round(H * 0.615), W, round(H * 0.965)))
    crop = crop.resize((1600, round(crop.height * 1600 / crop.width)), Image.LANCZOS)
    crop.save(f"assets/img/color-pal-{slug}.png", optimize=True)
    print("ok", name)
