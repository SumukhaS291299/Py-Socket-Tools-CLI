import datetime
import io
import random
import socket
import sys
import time
from TransportProtocol import ReceiverRx

import pygame
from rich.text import Text
from rich.panel import Panel

import CLI.RichCLI
from CLI import RichCLI


class TCPServe:
    def __init__(self, PORT: int):
        self.PORT = PORT

    def showConnInfo(self):
        text = Text("Starting Server, initialized with Host:\n")
        text.append(text=f"\t{TCPServe.getHostIP()}\n", style="bold magenta")
        text.append(text="using port:\n")
        text.append(text=f"\t{self.PORT}\n", style="bold cyan")
        cli_style = RichCLI.Styler()
        cli_panel = Panel(title="Connection Details", renderable=text, title_align="left")
        cli_style.Show(cli_panel)

    def PLayAudio(self, data: bytes, schedule: str):
        pygame.init()
        sound = pygame.mixer.Sound(data)
        PlayTime = datetime.datetime.strptime(schedule, "%Y-%m-%d %H:%M:%S.%f")
        time.sleep((PlayTime - datetime.datetime.now()).total_seconds())
        print("Starting...")
        sound.play()
        time.sleep(1000)

    def AcceptConn(self, conn, addr):
        text = Text("Connected to host:\n", style="italic bold red")
        text.append(f"\t{addr}")
        cli = RichCLI.Styler()
        cli.Show(text)
        Anim = RichCLI.Styler()
        Anim.Animation(["🎶", "🎼", "🎼", "🎵", "🎶", "🎙", "🎚", "🎛", "🎧", "📻", "🎷", "🎸", "🎹", "🎺", "🪈", "🪇", "🥁", "🪕", "🎻"],
                       sleep=0.5, end="\r")
        cli.Show(Text(f"Waiting for instruction from {addr}"))
        BufferData, Scheduler = ReceiverRx.Rx(conn, cli).Rx_Protocol()
        self.PLayAudio(data=BufferData, schedule=Scheduler)

    def ListenConnections(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.bind((TCPServe.getHostIP(), self.PORT))
        self.soc.listen()
        conn, addr = self.soc.accept()
        self.AcceptConn(conn, addr)

    @staticmethod
    def getHostIP():
        return socket.gethostbyname(socket.gethostname())
