#!/bin/python

import subprocess
import os
import shlex
import time

notification_below = 20
timer = 1
alert_sound_path = os.path.join(os.path.expanduser('~'), "music", "sounds", "alert.ogg")

notified = False
path_capacity = '/sys/class/power_supply/BAT1/capacity'
path_status = '/sys/class/power_supply/BAT1/status'

notify = shlex.split('notify-send -a SYSTEM -u critical -i ac-adapter-symbolic -c "device" "Warning" "Battery low"')
sound = shlex.split('sox {} -d'.format(alert_sound_path))

while True:
    f1 = open(path_status, 'r')
    status = f1.readline().strip()
    f1.close()

    f2 = open(path_capacity, 'r')
    capacity = int(f2.readline())
    f2.close()

    if status == 'Discharging' and capacity < notification_below and not notified:
        subprocess.call(notify)
        subprocess.call(sound)
        notified = True

    if status == 'Charging' or capacity > notification_below:
        notified = False

    time.sleep(timer)
