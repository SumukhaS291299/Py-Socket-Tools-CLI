import datetime
import random
import socket
import sys
import time

import pygame
from faker import Faker
from rich.panel import Panel
from rich.text import Text
import CLI.RichCLI
from CLI import RichCLI


class TCPClient:
    def __init__(self, PORT: int, HOST="", NAME=""):
        self.PORT = PORT
        self.HOST = HOST
        self.NAME = NAME
        self.checkName()

    def checkName(self):
        fake = Faker()
        if self.NAME == "":
            self.NAME = fake.user_name()

    def Connect(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.HOST == "":
            self.soc.connect((TCPClient.getHostIP(), self.PORT))
        else:
            self.soc.connect((self.HOST, self.PORT))

    @staticmethod
    def GetSizeOf(data) -> bytes:
        return str(sys.getsizeof(data)).encode()

    def PLayAudio(self, data: bytes, schedule: str):
        pygame.init()
        sound = pygame.mixer.Sound(data)
        PlayTime = datetime.datetime.strptime(schedule, "%Y-%m-%d %H:%M:%S.%f")
        print((PlayTime - datetime.datetime.now()).total_seconds())
        time.sleep((PlayTime - datetime.datetime.now()).total_seconds())
        print("Starting...")
        print(datetime.datetime.now())
        sound.play()
        time.sleep(1000)

    def ChatSend(self, message: str):
        self.Send(message.encode())

    def DataSend(self, data: bytes):
        self.Send(data)

    def Send(self, data: bytes):
        self.soc.sendall(data)

    def Receive(self, size: int):
        self.soc.recv(size)

    @staticmethod
    def getHostIP():
        return socket.gethostbyname(socket.gethostname())

    def showConnInfo(self):
        text = Text("Connection initilized with Host:\n")
        text.append(text=f"\t{TCPClient.getHostIP()}\n", style="bold magenta")
        text.append(text="with name:\n")
        text.append(text=f"\t{self.NAME}\n", style="bold gold")
        text.append(text="using port:\n")
        text.append(text=f"\t{self.PORT}\n", style="bold cyan")
        cli_style = RichCLI.Styler()
        cli_panel = Panel(title="Connection Details", renderable=text, title_align="left")
        cli_style.Show(cli_panel)
