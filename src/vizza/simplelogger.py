from sys import stderr
from vizza.assets import ASCIIColors as AC


class SimpleLogger:
    SPACING: int = 15

    @classmethod
    def info(self, msg):
        tag = "[INFO]"
        color = AC.white
        print(f"{color}{tag:{self.SPACING}}{msg}{AC.reset}", file=stderr)

    @classmethod
    def warning(self, msg):
        tag = "[WARNING]"
        color = AC.yellow
        print(f"{color}{tag:{self.SPACING}}{msg}{AC.reset}", file=stderr)

    @classmethod
    def error(self, msg):
        tag = "[ERROR]"
        color = AC.bold_red
        print(f"{color}{tag:{self.SPACING}}{msg}{AC.reset}", file=stderr)

    @classmethod
    def success(self, msg):
        tag = "[SUCCESS]"
        color = AC.bold_white
        print(f"{color}{tag:{self.SPACING}}{msg}{AC.reset}", file=stderr)
