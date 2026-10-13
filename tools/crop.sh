#!/bin/zsh
# Chụp cửa sổ Resolve rồi cắt một vùng theo tỉ lệ 0..1. Dùng: crop.sh <tên> <x0> <y0> <x1> <y1> [rộng]
set -e
NAME=$1; X0=$2; Y0=$3; X1=$4; Y1=$5; WIDTH=${6:-1200}
DIR=${0:A:h}/..
ID=$(/tmp/wl/winlist | awk '/So tay DaVinci/ {print $1; exit}')
screencapture -x -o -l "$ID" /tmp/crop_raw.png
"$DIR/.venv/bin/python" - "$NAME" "$X0" "$Y0" "$X1" "$Y1" "$WIDTH" <<'PY'
import sys
from PIL import Image
name, x0, y0, x1, y1, width = sys.argv[1], *map(float, sys.argv[2:6]), int(sys.argv[6])
im = Image.open("/tmp/crop_raw.png").convert("RGB")
W, H = im.size
c = im.crop((round(W * x0), round(H * y0), round(W * x1), round(H * y1)))
if c.width > width:
    c = c.resize((width, round(c.height * width / c.width)), Image.LANCZOS)
dest = f"assets/img/{name}.png"
c.save(dest, optimize=True)
print(dest, c.size)
PY
