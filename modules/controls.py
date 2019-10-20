import sys
import termios
import tty

import modules.menu as menu
import modules.render as render


class Chars:
    w = ('w', 119)
    s = ('s', 115)
    a = ('a', 97)
    d = ('d', 100)
    capital_p = ('P', 80)
    enter = 13


def menu_event(pressed_key):
    if pressed_key in Chars.w:  # Y axis is inverted in comparison to math.
        if menu.selected_button <= 1:
            menu.selected_button = 1
        else:
            menu.selected_button -= 1

    elif pressed_key in Chars.s:
        if menu.selected_button >= 2:
            menu.selected_button = 2
        else:
            menu.selected_button += 1

    elif menu.selected_button == 1 and ord(pressed_key) == Chars.enter:
        render.flushFrame()  # New game button.
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)  # Flush input buffer.
        return 1

    elif menu.selected_button == 2 and ord(pressed_key) == Chars.enter:
        render.flushFrame()  # Exit button.
        exit(0)


def game_event(pressed_key):
    if pressed_key in Chars.w:
        if render.Player.y <= 0:
            render.Player.y = 0
        else:
            render.Player.y -= 1

    elif pressed_key in Chars.s:
        if render.Player.y >= render.Map.height - render.Player.height:
            render.Player.y = render.Map.height - render.Player.height
        else:
            render.Player.y += 1

    elif pressed_key in Chars.a:
        if render.Player.x <= 0:
            render.Player.x = 0
        else:
            render.Player.x -= 1

    elif pressed_key in Chars.d:
        if render.Player.x >= render.Map.width - render.Player.width:
            render.Player.x = render.Map.width - render.Player.width
        else:
            render.Player.x += 1

    elif pressed_key in Chars.capital_p:  # Exit key.
        render.flushFrame()
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
