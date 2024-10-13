import os.path
import time,io
from threading import Thread
from CLI import RichCLI
from Client import clientConnect
import pygame


# text = Text("Starting Server, initialized with Host:\n")
# text.append(text=f"\t{TCPServe.getHostIP()}\n", style="bold magenta")
# text.append(text="using port:\n")
# text.append(text=f"\t{self.PORT}\n", style="bold cyan")
# cli_style = RichCLI.Styler()
# cli_panel = Panel(title="Connection Details", renderable=text, title_align="left")
# cli_style.Show(cli_panel)


class Music:

    def __init__(self, path):
        self.path = path
        self.isFile = os.path.isfile(self.path)

    def BufferPlay(self):
        pygame.mixer.init()
        with open(self.path, "rb") as audioFile:
            self.audioBuffer = audioFile.read()

    def RecieveAudioBuffer(self):
        client = clientConnect.TCPClient(8080, 'wild_sumukha_audio')
        client.showConnInfo()
        client.DataSend(self.audioBuffer)