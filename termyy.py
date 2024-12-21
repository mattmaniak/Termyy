#! /usr/bin/env python3

import os
import sys

import modules.controls
import modules.menu
import modules.render


def main_loop(mode):
    while True:
        if not modules.render.skip_next_frame_rendering:
            modules.menu.welcome(mode)

        if modules.controls.key_event(modules.state.Screens.PAUSE_MENU):
            round()

        if not modules.render.skip_next_frame_rendering:
            modules.render.flushFrame()


def round():
    while True:
        if not modules.render.skip_next_frame_rendering:
            modules.render.display_window(modules.render.Player.x,
                                          modules.render.Player.y)

        if modules.controls.key_event(modules.state.Screens.GAMEPLAY):
            while True:
                main_loop(modules.state.Screens.PAUSE_MENU)

        if not modules.render.skip_next_frame_rendering:
            modules.render.flushFrame()


if __name__ == "__main__":
    if os.name != "posix":
        sys.stderr.write("Your OS is not supported!\n")
        exit(1)

    main_loop(modules.state.Screens.MAIN_MENU)
else:
    sys.stderr.write("Do not import this file as a module. Run it directly.\n")
