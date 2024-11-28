import sys

import modules.render


class Color:
    reset = "\033[0m"
    invert = "\033[7m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    cyan = "\033[36m"


def clear_line():
    sys.stdout.write("\033[F\033[K")  # Back to a previous line and clear line.


class horizontal_border:
    def __init__(self, ending):
        sys.stdout.write('+')

        for x in range(modules.render.Window.width - 2):
            sys.stdout.write('-')
        sys.stdout.write(ending)


class Model:  # Structure of square 2D model, e.g. player.
    def __init__(self, model, width, height):
        sys.stdout.write(model)
