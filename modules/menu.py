import random
import sys
import modules.gui as gui
import modules.render as render

selectedButton = int(1) # Selected button ID. "New game" by default.
quotes = ("           ~ Find the text.", "      ~ You have much time.",
"      ~ This area is small.") # Random quotes as subtitle.
quote = quotes[random.randrange(len(quotes))]

class Button:
    def __init__(self, id, text, size, left):
        global selectedButton

        fillRestButton = int(size - len(text))
        render.Center("horizontal", ' ') # Centering and the upper window border.

        sys.stdout.write('|')
        for i in range(left): # Position from the left border (X axis).
            sys.stdout.write(' ')

        if selectedButton == id:
            sys.stdout.write(gui.Color.invert) # Invert colors if selected.
        sys.stdout.write(gui.Color.yellow + text) # Yellow now as background.

        for i in range(fillRestButton): # Stretch the button to width of 20.
            sys.stdout.write(gui.Color.yellow + ' ')
        sys.stdout.write(gui.Color.reset)

        for i in range(render.Map.width - size - left): # Area after the button.
            sys.stdout.write(' ')
        sys.stdout.write("|\n")

def welcome(mode, playButtonText): # Main menu.
    global selectedButton, quote

    render.Fill.upper()
    for i in range(10): # Position from up (Y axis).
        render.emptyLine()

    if mode == "Termyy":
        title = Button(0, mode, len(mode), int(render.Map.width / 2)
        - int(len(mode) / 2)) # Centered.
        subtitle = Button(selectedButton, quote, 28, 25) # Centered.

    elif mode == "               Game paused! ":
        render.emptyLine()
        subtitle = Button(selectedButton, mode, 28, 25) # Centered.

    for i in range(6):  # Position from up (Y axis).
        render.emptyLine()

    play = Button(1, playButtonText, 20, 5)
    exit = Button(2, " Exit", 20, 5)

    if mode == "Termyy": # After-game-started screen.
        render.emptyLine()  # - upper position (15) = 2.

        steering = Button(0,
        "Use: 'w', 's', 'a','d' as arrows, SHIFT+P to pause the game.", 60, 10)

    elif mode == "               Game paused! ": # Pause screen.
        for i in range(2):
            render.emptyLine()

    render.Fill.lower()

