#!/bin/zsh
# Chụp cả màn hình (bắt được menu xổ, hộp thoại) rồi cắt theo toạ độ point. Dùng: screen-crop.sh <tên> <x> <y> <w> <h> [rộng]
set -e
NAME=$1; X=$2; Y=$3; W=$4; H=$5; WIDTH=${6:-1200}
DIR=${0:A:h}/..
screencapture -x /tmp/screen_raw.png
"$DIR/.venv/bin/python" - "$NAME" "$X" "$Y" "$W" "$H" "$WIDTH" <<'PY'
import sys
from PIL import Image
name, x, y, w, h, width = sys.argv[1], *map(float, sys.argv[2:6]), int(sys.argv[6])
im = Image.open("/tmp/screen_raw.png").convert("RGB")
s = im.width / 1728
c = im.crop((round(x * s), round(y * s), round((x + w) * s), round((y + h) * s)))
if c.width > width:
    c = c.resize((width, round(c.height * width / c.width)), Image.LANCZOS)
dest = f"assets/img/{name}.png"
c.save(dest, optimize=True)
print(dest, c.size)
PY
