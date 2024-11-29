import os
import sys

import modules.gui


# Namespaces for the most important elements.
class Player:
    model = "[*;*]"
    width = len(model)
    height = 1
    x = 0
    y = 0


class Window:
    width = 80
    height = 24

    def count_centered_object_vertical_padding(obj_width):
        return int((Window.width - obj_width) / 2)


class Map:
    __borders_size = 2
    width = Window.width - __borders_size
    height = Window.height - __borders_size


def size(axis):
    width, height = os.get_terminal_size()

    if width < Window.width or height < Window.height:
        print("Terminal size must >= 80x24 characters of size.")
        exit(1)

    elif height >= Window.height:  # Centering values.
        if axis == "horizontal":
            size = (width - Window.width) / 2

        elif axis == "vertical":
            size = (height - Window.height) / 2

        elif axis == "height":  # Whole terminal height.
            size = height

    return int(size)


def empty_line():  # X centered line with borders only.
    for x in range(size("horizontal")):
        sys.stdout.write(' ')
    sys.stdout.write('|')

    for x in range(Map.width):  # Rendering empty X axis.
        sys.stdout.write(' ')
    sys.stdout.write('|\n')


def flushFrame():
    for y in range(size("height")):
        modules.gui.clear_line()
    sys.stdout.flush()


class Center:
    def __init__(self, axis, lastChar):
        for x in range(size(axis)):
            sys.stdout.write(lastChar)


class Fill:
    def vertically():
        for y in range(size("height") - size("vertical") - Window.height):
            sys.stdout.write('\n')

    def upper():
        Center("vertical", '\n')
        Center("horizontal", ' ')
        modules.gui.horizontal_border("+\n")

    def lower():
        Center("horizontal", ' ')
        modules.gui.horizontal_border('+')
        Center("horizontal", ' ')
        Fill.vertically()


def window(x, y):  # Main window of the game.
    Fill.upper()
    # Player positioning in Y axis:
    for y in range(Player.y):  # Amount of X axes to render above him.
        empty_line()

    # Player positioning in X axis and rendering:
    for y in range(Player.height):
        Center("horizontal", ' ')

        sys.stdout.write('|')  # Left border.
        for x in range(Player.x):
            sys.stdout.write(' ')  # Spaces without newlines as positioning.

        modules.gui.Model(modules.gui.Color.yellow + Player.model
                          + modules.gui.Color.reset,
                          Player.width, Player.height)

        for x in range(Map.width - Player.x - Player.width):
            sys.stdout.write(' ')  # Spaces at the right side of the Player...
        sys.stdout.write("|\n")  # ...to set position of this border properly.

    # Horizontal areas (X axes) below the Player:
    for y in range(Map.height - Player.y - Player.height):
        empty_line()

    Fill.lower()
