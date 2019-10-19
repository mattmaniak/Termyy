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


def menuEvent(pressedKey):
    global w, s, a, d, capital_p, enter

    if pressedKey in Chars.w:  # Y axis is inverted in comparison to math.
        if menu.selectedButton <= 1:
            menu.selectedButton = 1
        else:
            menu.selectedButton -= 1

    elif pressedKey in Chars.s:
        if menu.selectedButton >= 2:
            menu.selectedButton = 2
        else:
            menu.selectedButton += 1

    elif menu.selectedButton == 1 and ord(pressedKey) == Chars.enter:
        render.flushFrame()  # New game button.
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)  # Flush input buffer.
        return 1

    elif menu.selectedButton == 2 and ord(pressedKey) == Chars.enter:
        render.flushFrame()  # Exit button.
        exit(0)


def gameEvent(pressedKey):
    global w, s, a, d, capital_p, enter

    if pressedKey in Chars.w:
        if render.Player.y <= 0:
            render.Player.y = 0
        else:
            render.Player.y -= 1

    elif pressedKey in Chars.s:
        if render.Player.y >= render.Map.height - render.Player.height:
            render.Player.y = render.Map.height - render.Player.height
        else:
            render.Player.y += 1

    elif pressedKey in Chars.a:
        if render.Player.x <= 0:
            render.Player.x = 0
        else:
            render.Player.x -= 1

    elif pressedKey in Chars.d:
        if render.Player.x >= render.Map.width - render.Player.width:
            render.Player.x = render.Map.width - render.Player.width
        else:
            render.Player.x += 1

    elif pressedKey in Chars.capital_p:  # Exit key.
        render.flushFrame()
        return True


def keyEvent(type):  # https://code.activestate.com/recipes/134892/
    global w, s, a, d, capital_p, enter

    fd = sys.stdin.fileno()
    oldSettings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        pressedKey = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)

    if type == "menu":
        return menuEvent(pressedKey)

    elif type == "game":
        return gameEvent(pressedKey)
