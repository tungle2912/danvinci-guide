#!/bin/zsh
# Chụp riêng cửa sổ chính của Resolve theo ID, không đưa Resolve lên trước. Dùng: winshot.sh <tên> [rộng]
set -e
NAME=$1; WIDTH=${2:-1600}
DIR=${0:A:h}/..
ID=$(/tmp/wl/winlist | awk '/So tay DaVinci/ {print $1; exit}')
screencapture -x -o -l "$ID" /tmp/winshot_raw.png
"$DIR/.venv/bin/python" - "$NAME" "$WIDTH" <<'PY'
import sys
from PIL import Image
name, width = sys.argv[1], int(sys.argv[2])
im = Image.open("/tmp/winshot_raw.png").convert("RGB")
im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
dest = f"assets/img/{name}.png"
im.save(dest, optimize=True)
print(dest, im.size)
PY
