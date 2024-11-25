#! /usr/bin/env python3

import os
import sys

import modules.menu
import modules.controls
import modules.render


def game(mode, play_button_text):
    while 1:
        modules.menu.welcome(mode, play_button_text)
        if modules.controls.key_event("menu") == 1:
            round()
        modules.render.flushFrame()


def round():
    while 1:
        modules.render.window(modules.render.Player.x, modules.render.Player.y)
        if modules.controls.key_event("game") == 1:
            while 1:
                game("               Game paused! ", " Continue game")
        modules.render.flushFrame()


if __name__ == "__main__":
    if os.name != "posix":
        sys.stderr.write("Your OS is not supported!\n")
        exit(1)
    game("Termyy", " New game")

else:
    sys.stderr.write("Do not import this file as a module. Run it directly.\n")
