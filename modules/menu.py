import random
import sys
import modules.gui as gui
import modules.render as render


selected_button = 1  # Selected button ID. "New game" by default.
quotes = ("           ~ Find the text.", "      ~ You have much time.",
          "      ~ This area is small.")  # Random quotes as subtitle.
quote = quotes[random.randrange(len(quotes))]


class Button:
    def __init__(self, id, text, size, left):
        global selected_button

        fill_rest_button = int(size - len(text))
        render.Center("horizontal", ' ')  # Centering and the upper border.

        sys.stdout.write('|')
        for i in range(left):  # Position from the left border (X axis).
            sys.stdout.write(' ')

        if selected_button == id:
            sys.stdout.write(gui.Color.invert)  # Invert colors if selected.
        sys.stdout.write(gui.Color.yellow + text)  # Yellow now as background.

        for i in range(fill_rest_button):  # Stretch the button to width of 20.
            sys.stdout.write(gui.Color.yellow + ' ')
        sys.stdout.write(gui.Color.reset)

        for i in range(render.Map.width - size - left):
            sys.stdout.write(' ')  # Area after the button.
        sys.stdout.write("|\n")


def welcome(mode, play_button_text):  # Main menu.
    global selected_button, quote

    render.Fill.upper()
    for y in range(10):  # Position from up (Y axis).
        render.empty_line()

    if mode == "Termyy":
        Button(0, mode, len(mode),
               int(render.Map.width / 2) - int(len(mode) / 2))
        Button(selected_button, quote, 28, 25)

    elif mode == "               Game paused! ":
        render.empty_line()
        Button(selected_button, mode, 28, 25)

    for i in range(6):  # Position from up (Y axis).
        render.empty_line()

    Button(1, play_button_text, 20, 5)
    Button(2, " Exit", 20, 5)

    if mode == "Termyy":  # After-game-started screen.
        render.empty_line()  # - upper position (15) = 2.

        Button(0,
               "Use 'w', 's', 'a', 'd' as arrows, SHIFT+P to pause the game.",
               60, 10)

    elif mode == "               Game paused! ":  # Pause screen.
        for i in range(2):
            render.empty_line()

    render.Fill.lower()
