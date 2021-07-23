#!/bin/python

# Remove every certain time some folders that not are necessary

import subprocess
import os
import re
import shlex
import time

timer = 1                       # Minutes
actual = 0
dirs = [".mozilla",
        ".pki",
        ".Xauthority",
        ".local/share/pki",
        ".local/share/recently-used.xbel",
        ".cache/fontconfig",
        ".cache/mesa_shader_cache",
        ".cache/mozilla",
        ".cache/event-sound-cache.tdb.*",
        ".config/dconf",
        ".config/pulse",
        ]
user_path = os.path.join(os.path.expanduser('~'))

def rm(path):
    command = shlex.split('rm -rf {}'.format(path))
    subprocess.call(command)

# Init loop
# while 1:
for d in dirs:
    path = user_path + '/' + d
    if not d.endswith('*'):
        if os.path.exists(path):
            print("🟢 Exists: {} - Removing...".format(path))
            rm(path)
        else:
            print("🔴 No Exists: {}".format(path))
    else:
        path_r = path.rsplit('/', 1)
        regex = re.compile(path_r[1])
        print('Special regex - {}'.format(path_r[0]))

        for root_r, dirs_r, files_r in os.walk(path_r[0]):
            for f in files_r:
                if regex.match(f):
                    print("🟢 Exists: {} - Removing...".format(path_r[0] + '/' + f))
                    rm(path_r[0] + '/' + f)

#time.sleep(timer * 60)

