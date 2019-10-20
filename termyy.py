#! /usr/bin/env python3

import os
import sys

import modules.menu as menu
import modules.controls as controls
import modules.render as render


def game(mode, play_button_text):
    while 1:
        menu.welcome(mode, play_button_text)
        if controls.key_event("menu") == 1:
            round()
        render.flushFrame()


def round():
    while 1:
        render.window(render.Player.x, render.Player.y)
        if controls.key_event("game") == 1:
            while 1:
                game("               Game paused! ", " Continue game")
        render.flushFrame()


if __name__ == "__main__":
    if os.name != "posix":
        sys.stderr.write("Your OS is not supported!\n")
        exit(1)
    game("Termyy", " New game")

else:
    sys.stderr.write("Do not import this file as a module. Run it directly.\n")
