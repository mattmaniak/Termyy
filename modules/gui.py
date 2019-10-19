import sys


class Color:
    reset = str("\033[0m")
    invert = str("\033[7m")
    red = str("\033[31m")
    green = str("\033[32m")
    yellow = str("\033[33m")
    blue = str("\033[34m")
    purple = str("\033[35m")
    cyan = str("\033[36m")


def clear_line():
    sys.stdout.write("\033[F\033[K")  # Back to a previous line and clear line.


class horizontal_border:
    def __init__(self, ending):
        sys.stdout.write('+')

        for x in range(78):
            sys.stdout.write('-')
        sys.stdout.write(ending)


class Model:  # Structure of square 2D model, e.g. player.
    def __init__(self, model, width, height):
        sys.stdout.write(model)
