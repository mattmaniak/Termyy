import random
import sys

import modules.gui
import modules.state
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


# Main menu.
def welcome(mode):
    global selected_button, quote_frame

    infobox_width = 28
    menu_button_width = 20
    menu_button_height = 5

    modules.render.Fill.upper()

    for y in range(10):  # Position from up (Y axis).
        modules.render.empty_line()

    if mode == modules.state.Screens.MAIN_MENU:
        logo_text = "Termyy"

        Button(0, logo_text, len(logo_text),
               modules.render.Window.
               count_centered_object_vertical_padding(len(logo_text)))

        Button(selected_button, quote_frame, infobox_width,
               modules.render.Window.
               count_centered_object_vertical_padding(infobox_width))

    elif mode == modules.state.Screens.PAUSE_MENU:
        modules.render.empty_line()
        Button(selected_button, "Game paused!".rjust(quote_frame_width, ' '),
               infobox_width,
               modules.render.Window.
               count_centered_object_vertical_padding(infobox_width))

    for i in range(6):  # Position from up (Y axis).
        modules.render.empty_line()

    if mode == modules.state.Screens.MAIN_MENU:
        Button(1, " New Game", menu_button_width, menu_button_height)
    elif mode == modules.state.Screens.PAUSE_MENU:
        Button(1, " Continue Game", menu_button_width, menu_button_height)

    Button(2, " Exit", menu_button_width, menu_button_height)

    if mode == modules.state.Screens.MAIN_MENU:  # After-game-started screen.
        modules.render.empty_line()  # - upper position (15) = 2.

        button_text = "Use 'w', 's', 'a', 'd' as arrows, SHIFT+P to pause" \
                      + " the game."

        Button(0, button_text, len(button_text),
               modules.render.Window.
               count_centered_object_vertical_padding(len(button_text)))

    elif mode == modules.state.Screens.PAUSE_MENU:  # Pause screen.
        for i in range(2):
            modules.render.empty_line()

    modules.render.Fill.lower()
