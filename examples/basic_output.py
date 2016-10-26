from beary import Terminal, colors
import time


with Terminal() as t:

    t.title = "Beary: basic output"
    t.color = "white"
    t.size = (80, 25)
    t.clear()

    # Wide color range
    n = t.puts(2, 1, "[color=orange]1.[/color] Wide color range: ")
    long_word = "antidisestablishmentarianism."
    long_word_length = len(long_word)
    for i in range(long_word_length):
        factor = i / long_word_length
        red = int((1 - factor) * 255)
        green = int(factor * 255)
        x = 2 + n + i
        y = 1
        t.puts(long_word[i], x, y, color=(255, red, green, 0))

    t.puts("[color=orange]2.[/color] Backgrounds: [color=black][bkcolor=gray] grey [/bkcolor] [bkcolor=red] red ", 2, 3)

    t.puts("[color=orange]3.[/color] Unicode support: Кириллица Ελληνικά α=β²±2°", 2, 5)

    t.puts("[color=orange]4.[/color] Tile composition: a + [color=red]/[/color] = a[+][color=red]/[/color], a vs. a[+][color=red]¨[/color]", 2, 7)

    t.puts("[color=orange]5.[/color] Box drawing symbols:", 2, 9)

    t.puts(
        "   ┌────────┐  \n"
        "   │!......s└─┐\n"
        "┌──┘........s.│\n"
        "│............>│\n"
        "│...........┌─┘\n"
        "│<.@..┌─────┘  \n"
        "└─────┘        \n",
        5, 11
    )

    t.puts("Press any key to close.", 2, 20, color=(0, 255, 255))

    t.refresh()

    t.key()  # Wait until a keypress to close.
