class ColorPrinter:

    COLORS = {
        'reset': "\033[0m",
        'black': "\033[30m",
        'red': "\033[31m",
        'green': "\033[32m",
        'yellow': "\033[33m",
        'blue': "\033[34m",
        'magenta': "\033[35m",
        'cyan': "\033[36m",
        'white': "\033[37m",
        'bright_black': "\033[90m",
        'bright_red': "\033[91m",
        'bright_green': "\033[92m",
        'bright_yellow': "\033[93m",
        'bright_blue': "\033[94m",
        'bright_magenta': "\033[95m",
        'bright_cyan': "\033[96m",
        'bright_white': "\033[97m",
    }

    def _print_with_color(self, color_code, *args, **kwargs):
        
        print(color_code + ' '.join(map(str, args)) + self.COLORS['reset'], **kwargs)

    def black(self, *args, **kwargs):
        self._print_with_color(self.COLORS['black'], *args, **kwargs)

    def red(self, *args, **kwargs):
        self._print_with_color(self.COLORS['red'], *args, **kwargs)

    def green(self, *args, **kwargs):
        self._print_with_color(self.COLORS['green'], *args, **kwargs)

    def yellow(self, *args, **kwargs):
        self._print_with_color(self.COLORS['yellow'], *args, **kwargs)

    def blue(self, *args, **kwargs):
        self._print_with_color(self.COLORS['blue'], *args, **kwargs)

    def magenta(self, *args, **kwargs):
        self._print_with_color(self.COLORS['magenta'], *args, **kwargs)

    def cyan(self, *args, **kwargs):
        self._print_with_color(self.COLORS['cyan'], *args, **kwargs)

    def white(self, *args, **kwargs):
        self._print_with_color(self.COLORS['white'], *args, **kwargs)

    def bright_black(self, *args, **kwargs):
        self._print_with_color(self.COLORS['bright_black'], *args, **kwargs)

    def bright_red(self, *args, **kwargs):
        self._print_with_color(self.COLORS['bright_red'], *args, **kwargs)

    def bright_green(self, *args, **kwargs):
        self._print_with_color(self.COLORS['bright_green'], *args, **kwargs)

    def bright_yellow(self, *args, **kwargs):
        self._print_with_color(self.COLORS['bright_yellow'], *args, **kwargs)

    def bright_blue(self, *args, **kwargs):
        self._print_with_color(self.COLORS['bright_blue'], *args, **kwargs)

    def bright_magenta(self, *args, **kwargs):
        self._print_with_color(self.COLORS['bright_magenta'], *args, **kwargs)

    def bright_cyan(self, *args, **kwargs):
        self._print_with_color(self.COLORS['bright_cyan'], *args, **kwargs)

    def bright_white(self, *args, **kwargs):
        self._print_with_color(self.COLORS['bright_white'], *args, **kwargs)

printer = ColorPrinter()
