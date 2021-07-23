# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile workspaces

from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
# nf-fa-firefox, 
# nf-fae-python, 
# nf-dev-terminal, 
# nf-fa-code, 
# nf-oct-git_merge, 
# nf-linux-docker,
# nf-mdi-image, 
# nf-mdi-layers

groups = [Group(i) for i in [
    "   ", "   ", "   ", "   ", "  ", "   ", "   ", "   ", "   ",
]]

numpad_keys = ["KP_Insert","KP_End", "KP_Down", "KP_Next",
               "KP_Left", "KP_Begin", "KP_Right", "KP_Home",
               "KP_Up", "KP_Prior"]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        Key([mod], numpad_keys[i+1], lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)),
        Key([mod, "shift"], numpad_keys[i+1], lazy.window.togroup(group.name))
    ])
