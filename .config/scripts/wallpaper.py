#!/bin/python

import subprocess
import os
import shlex
import time
import random

timer = 15                       # Minutes
actual = 0
extensions_sopported = [".png", ".jpg"]
wallpaper_path = os.path.join(os.path.expanduser('~'), "img", "wallpaper")

def change_bg(path):
    command = shlex.split('feh --bg-scale {}'.format(path))
    subprocess.call(command)

def update():
    files = os.listdir(wallpaper_path)
    cleaned = []
    for f in files:
        success = False
        for ext in extensions_sopported:
            if f.endswith(ext):
                success = True

        if success:
            cleaned.append(f)

    random.shuffle(cleaned)
    return cleaned

# Init loop
while True:
    files = update()
    actual+=1
    if actual >= len(files):
        actual = 0
    actual_path = wallpaper_path + '/' + files[actual]
    change_bg(actual_path)
    time.sleep(timer * 60)

