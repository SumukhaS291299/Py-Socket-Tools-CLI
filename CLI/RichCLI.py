import time
from typing import Union

from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich import print as rich_print


class Styler:

    def __init__(self):
        self.console = Console()

    def Show(self, richObj: Union[Text, Panel, str]):
        rich_print(richObj)

    def Animation(self, textList: list[str],
                  sleep: float, sep=" ", end="\n"):
        for data in textList:
            rich_print(data, sep=sep, end=end)
            time.sleep(sleep)

    def Animationstr(self, text: str, sep=" ", end="\n"):
        rich_print(text, sep=sep, end=end)
