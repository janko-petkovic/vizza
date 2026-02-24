from sys import stderr
from vizza.assets import ASCIIColors as AC


class SimpleLogger:
    SPACING: int = 15

    @classmethod
    def _printer(self, color, tag, *msgs):
        '''Handles multiline printing'''
        print(f"{color}{tag:{self.SPACING}}{msgs[0]}{AC.reset}", file=stderr)
        for m in msgs[1:]:
            print(f"{color}{'':{self.SPACING}}{m}{AC.reset}", file=stderr)

    @classmethod
    def info(self, *msgs):
        tag = "[INFO]"
        color = AC.white
        self._printer(color, tag, *msgs)

    @classmethod
    def warning(self, *msgs):
        tag = "[WARNING]"
        color = AC.yellow
        self._printer(color, tag, *msgs)

    @classmethod
    def error(self, *msgs):
        tag = "[ERROR]"
        color = AC.bold_red
        self._printer(color, tag, *msgs)

    @classmethod
    def success(self, *msgs):
        tag = "[SUCCESS]"
        color = AC.bold_white
        self._printer(color, tag, *msgs)
