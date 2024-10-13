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
    def __init__(self, PORT: int, NAME=""):
        self.PORT = PORT
        self.NAME = NAME
        self.checkName()

    def checkName(self):
        fake = Faker()
        if self.NAME == "":
            self.NAME = fake.user_name()

    def Connect(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.connect((TCPClient.getHostIP(), self.PORT))

    @staticmethod
    def GetSizeOf(data) -> bytes:
        return str(sys.getsizeof(data)).encode()

    def PLayAudio(self, data: bytes, schedule: str):
        pygame.init()
        sound = pygame.mixer.Sound(data)
        PlayTime = datetime.datetime.strptime(schedule, "%Y-%m-%d %H:%M:%S.%f")
        time.sleep((PlayTime - datetime.datetime.now()).total_seconds())
        print("Starting...")
        sound.play()
        time.sleep(1000)

    def Rx_Protocol(self, conn, cli: CLI.RichCLI.Styler):
        cli.Show(Text("Receiving protocol:", style="italic blue"))
        # --------------------------------------------------------------------------------------
        cli.Show(Text("Instruction:", style="bold blue"))
        instruction = conn.recv(100)
        instructionText = Text(text="Instruction=  ")
        instructionText.append(Text(text=instruction.decode(), style="purple"))
        conn.sendall(TCPClient.GetSizeOf(instruction))
        # --------------------------------------------------------------------------------------
        cli.Show(Text("Waiting for start token", style="red"))
        start_instruction = conn.recv(100)
        cli.Show(Text("Got Start instruction", style="blue"))
        cli.Show(Text(start_instruction.decode(), style="red"))
        conn.sendall(TCPClient.GetSizeOf(start_instruction))
        # --------------------------------------------------------------------------------------
        cli.Show(Text("Waiting for size token", style="red"))
        size_instruction = conn.recv(100)
        cli.Show(Text("Got Start instruction", style="blue"))
        sizeText = Text("The device is sending:  ", style="blue")
        sizeText.append(Text(f"{size_instruction.decode()} bytes", style="purple"))
        cli.Show(sizeText)
        # --------------------------------------------------------------------------------------
        cli.Show(Text("Waiting for schedule token", style="red"))
        schedule_instruction = conn.recv(100)
        cli.Show(Text("Got schedule instruction", style="blue"))
        scheduleText = Text("The device is sending:  ", style="blue")
        scheduleText.append(Text(f"{schedule_instruction.decode()} bytes", style="purple"))
        cli.Show(scheduleText)
        conn.sendall("OKAY..".encode())
        # --------------------------------------------------------------------------------------
        bufferData = conn.recv(int(size_instruction.decode()))
        cli.Show(Text("Connection closed", style="bold green"))
        conn.close()
        self.PLayAudio(bufferData, schedule_instruction.decode())

    def Tx_Protocol(self, data: bytes, instruction: str, conn, cli: CLI.RichCLI.Styler):
        cli.Show(Text("Transmission protocol:", style="italic blue"))
        # --------------------------------------------------------------------------------------
        Inst = Text("Instruction:", style="bold")
        cli.Show(Inst.append(Text(instruction, style="bold brown")))
        conn.sendall(instruction.encode())
        cli.Show(Text(f"Ack for {conn.recv(100).decode()} bytes received from connected device"))
        # --------------------------------------------------------------------------------------
        START_INSTRUCTION = "~|START|~"
        conn.sendall(START_INSTRUCTION.encode())
        cli.Show(Text(f"Ack for {conn.recv(100).decode()} bytes received from connected device"))
        # --------------------------------------------------------------------------------------
        SIZE_INSTRUCTION = str(sys.getsizeof(data))
        conn.sendall(SIZE_INSTRUCTION.encode())
        # --------------------------------------------------------------------------------------
        SCHEDULE_INSTRUCTION = (datetime.datetime.now() + datetime.timedelta(seconds=15)).strftime("%Y-%m-%d %H:%M:%S.%f")
        conn.sendall(SCHEDULE_INSTRUCTION.encode())
        cli.Show(Text(f"Scheduling for {SCHEDULE_INSTRUCTION}"))
        cli.Show(Text(f"Scheduling received  {conn.recv(100).decode()} from connected device"))
        # --------------------------------------------------------------------------------------
        cli.Show(Text("Sending Data....", style="bold green"))
        conn.sendall(data)
        cli.Show(Text("Full Data transfered....", style="bold green"))
        cli.Show(Text("Requesting Close connection", style="bold green"))
        conn.close()
        self.PLayAudio(data, SCHEDULE_INSTRUCTION)

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
