from bearlibterminal import terminal as term
import beary.colors as colors

class Terminal():

    _color = 'white'  # Default foreground color.
    _title = 'Beary Terminal'  # Default title.
    _settings = None  # {}
    _open = False

    def __init__(self, title=None):
        self._settings = {}
        self.title(title or self._title)
        term.color(self._color)

    def title(self, title):
        self.config("window.title", title)
        self._title = title

    def config(self, key, val):
        val = str(val.replace("'", "''"))
        self._settings[key] = val
        if self._open is True:
            term.set("{}='{}'".format(key, val))

    def color(self, color):
        self._color = color
        term.color = color

    def open(self):
        term.open()
        self.load_settings()
        self._open = True

    def load_settings(self):
        for key, val in self._settings.items():
            val = str(val.replace("'", "''"))
            term.set("{}='{}'".format(key, val))

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
        return self

    def __exit__(self, *args):
        self.close()
