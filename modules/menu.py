import random
import sys

import modules.gui
import modules.render


selected_button = 1  # Selected button ID. "New game" by default.
quote_frame_width = 27

# Random quotes as a subtitle.
quote_prefix = "~ "
quote_sufix = '.'
quotes = ["Find the text", "You have much time", "This area is small"]

for idx in range(len(quotes)):
    quotes[idx] = quote_prefix + quotes[idx] + quote_sufix
    quotes[idx] = quotes[idx].rjust(quote_frame_width, ' ')

quote_frame = quotes[random.randrange(len(quotes))]


class Button:
    def __init__(self, id, text, size, left):
        global selected_button

        fill_rest_button = int(size - len(text))

        # Centering and the upper border.
        modules.render.Center("horizontal", ' ')

        sys.stdout.write('|')
        for i in range(left):  # Position from the left border (X axis).
            sys.stdout.write(' ')

        if selected_button == id:
            # Invert colors if selected.
            sys.stdout.write(modules.gui.Color.invert)

        # Yellow now as background.
        sys.stdout.write(modules.gui.Color.yellow + text)

        for i in range(fill_rest_button):  # Stretch the button to width of 20.
            sys.stdout.write(modules.gui.Color.yellow + ' ')
        sys.stdout.write(modules.gui.Color.reset)

        for i in range(modules.render.Map.width - size - left):
            sys.stdout.write(' ')  # Area after the button.
        sys.stdout.write("|\n")


def welcome(mode, play_button_text):  # Main menu.
    global selected_button, quote_frame

    infobox_width = 28
    menu_button_width = 20
    menu_button_height = 5

    modules.render.Fill.upper()

    for y in range(10):  # Position from up (Y axis).
        modules.render.empty_line()

    if mode == "Termyy":
        Button(0, mode, len(mode),
               int(modules.render.Map.width / 2) - int(len(mode) / 2))
        Button(selected_button, quote_frame, infobox_width,
               modules.render.Window.
               count_centered_object_vertical_padding(infobox_width))

    elif mode == "               Game paused! ":
        modules.render.empty_line()
        Button(selected_button, mode, infobox_width, modules.render.Window.
               count_centered_object_vertical_padding(infobox_width))

    for i in range(6):  # Position from up (Y axis).
        modules.render.empty_line()

    Button(1, play_button_text, menu_button_width, menu_button_height)
    Button(2, " Exit", menu_button_width, menu_button_height)

    if mode == "Termyy":  # After-game-started screen.
        modules.render.empty_line()  # - upper position (15) = 2.

        button_text = "Use 'w', 's', 'a', 'd' as arrows, SHIFT+P to pause" \
                      + " the game."

        Button(0, button_text, len(button_text),
               modules.render.Window.
               count_centered_object_vertical_padding(len(button_text)))

    elif mode == "               Game paused! ":  # Pause screen.
        for i in range(2):
            modules.render.empty_line()

    modules.render.Fill.lower()
