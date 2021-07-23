#!/bin/sh

# systray volume
volumeicon &
# Battery notification
$HOME/.config/scripts/notify_battery.py &
# Dynamic Wallpaper
$HOME/.config/scripts/wallpaper.py &
