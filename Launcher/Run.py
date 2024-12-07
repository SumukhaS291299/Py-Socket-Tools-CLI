import time

from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.text import Text


class Start:

    def __init__(self):
        self.console = Console()

    def viewInfo(self):
        text = Text()
        with Live(text,console=self.console,screen=False,refresh_per_second=20):
            text.append("Hello")
            time.sleep(1)
            text.append("How")
            time.sleep(1)
            text.append("are")
            time.sleep(1)
            text.append("you")
            time.sleep(1)
            text.append("doing")

start = Start()
start.viewInfo()