from bearlibterminal import terminal as term
import beary.colors as colors

class Terminal():

    _color = 'white'  # Default foreground color.
    _title = 'Beary Terminal'  # Default title.

    def __init__(self, title=None):
        if title is not None:
            term.title(self._title)
        term.color(self._color)
        term.set('window.size=80x25')

    def title(self, title):
        self._title = title
        term.set("window.title='{}'".format(title))

    def color(self, color):
        self._color = color
        term.color = color

    def open(self):
        term.open()

    def clear(self):
        term.clear()

    def close(self):
        term.composition(False)
        term.close()

    def puts(self, text, x=0, y=0, color=None):
        if color is not None:
            if len(color) == 3:
                color = colors.rgb(*color)
            elif len(color) == 4:
                color = colors.argb(*color)
        if color is not None and color != self._color:
            term.color(color)
        n = term.print_(x, y, str(text))
        self._cursor = n
        if color != self._color:
            term.color(self._color)
        return n

    def refresh(self):
        term.refresh()

    def key(self):
        return term.read()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()
