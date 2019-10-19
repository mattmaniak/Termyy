#! /usr/bin/python3

# Termyy - an experminantal ASCII-based game with 2D view from the top.

# Main info
# I can occasionally do some fixes but generally the project is discontinued
# due the my Git experiments. Do what do you want with that. The only thing to
# do is add map because now it's empty. Development lasted from 2018-04-26 to
# 2018-05-26 with few breaks. Refactored in late 2019. Whole rendering has been
# written in the clear Python 3 - without curses/ncurses modules.

# Workflow
# There is only one branch: master. Generally everything should be stable.

# System requirements
# Your computer must have *nix and the Python 3 installed. You need also
# a terminal with size >= 80x24 chars. Linux or even *nix (not tesed).

# Gameplay
# To run type: "./termyy.py". Keymap is very intuitive: 'w', 's', 'a', 'd' as
# arrows and SHIFT+P to pause.

import os
import sys

import modules.menu as menu
import modules.physics as physics
import modules.render as render


def game(mode, playButtonText):
    while 1:
        menu.welcome(mode, playButtonText)
        if physics.keyEvent("menu") == 1:
            round()
        render.flushFrame()


def round():
    while 1:
        render.window(render.Player.x, render.Player.y)
        if physics.keyEvent("game") == 1:
            while 1:
                game("               Game paused! ", " Continue game")
        render.flushFrame()


if __name__ == "__main__":
    if os.name != "posix":
        print("Your OS is not supported!")
        exit(1)
    game("Termyy", " New game")

else:
    sys.stderr.write("Do not import this file as a module. Run it directly.\n")
