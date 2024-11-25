import sys
import termios
import tty

import modules.menu
import modules.render


class Chars:
    w = ('w', 119)
    s = ('s', 115)
    a = ('a', 97)
    d = ('d', 100)
    capital_p = ('P', 80)
    enter = 13


def menu_event(pressed_key):
    if pressed_key in Chars.w:  # Y axis is inverted in comparison to math.
        if modules.menu.selected_button <= 1:
            modules.menu.selected_button = 1
        else:
            modules.menu.selected_button -= 1

    elif pressed_key in Chars.s:
        if modules.menu.selected_button >= 2:
            modules.menu.selected_button = 2
        else:
            modules.menu.selected_button += 1

    elif modules.menu.selected_button == 1 and ord(pressed_key) == Chars.enter:
        modules.render.flushFrame()  # New game button.
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)  # Flush input buffer.
        return 1

    elif modules.menu.selected_button == 2 and ord(pressed_key) == Chars.enter:
        modules.render.flushFrame()  # Exit button.
        exit(0)


def game_event(pressed_key):
    if pressed_key in Chars.w:
        if modules.render.Player.y <= 0:
            modules.render.Player.y = 0
        else:
            modules.render.Player.y -= 1

    elif pressed_key in Chars.s:
        if modules.render.Player.y >= modules.render.Map.height \
                - modules.render.Player.height:
            modules.render.Player.y = modules.render.Map.height \
                                      - modules.render.Player.height
        else:
            modules.render.Player.y += 1

    elif pressed_key in Chars.a:
        if modules.render.Player.x <= 0:
            modules.render.Player.x = 0
        else:
            modules.render.Player.x -= 1

    elif pressed_key in Chars.d:
        if modules.render.Player.x >= modules.render.Map.width \
                - modules.render.Player.width:
            modules.render.Player.x = modules.render.Map.width \
                                      - modules.render.Player.width
        else:
            modules.render.Player.x += 1

    elif pressed_key in Chars.capital_p:  # Exit key.
        modules.render.flushFrame()
        return True


def key_event(type):  # https://code.activestate.com/recipes/134892/
    file_descriptor = sys.stdin.fileno()
    old_settings = termios.tcgetattr(file_descriptor)
    try:
        tty.setraw(sys.stdin.fileno())
        pressed_key = sys.stdin.read(1)

    finally:
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)

    if type == "menu":
        return menu_event(pressed_key)
    elif type == "game":
        return game_event(pressed_key)
