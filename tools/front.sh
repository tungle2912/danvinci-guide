#!/bin/zsh
# Đưa Resolve lên trên cùng; thoát mã 1 nếu không được (tránh click nhầm sang app khác).
osascript -e 'tell application "DaVinci Resolve" to activate'
sleep 0.6
[[ $(osascript -e 'tell application "System Events" to get name of first process whose frontmost is true') == Resolve ]] || { echo "Resolve không ở trên cùng" >&2; exit 1; }
