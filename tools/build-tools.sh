#!/bin/zsh
# Biên dịch winlist và click vào /tmp/wl (thư mục /tmp bị xoá sau khi khởi động lại máy).
set -e
DIR=${0:A:h}
mkdir -p /tmp/wl
swiftc -O "$DIR/winlist.swift" -o /tmp/wl/winlist
swiftc -O "$DIR/click.swift" -o /tmp/wl/click
echo "ok: /tmp/wl/winlist /tmp/wl/click"
