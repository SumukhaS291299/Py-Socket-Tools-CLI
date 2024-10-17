import CLI.RichCLI
from rich.text import Text
import datetime
import sys


class Rx:

    def __init__(self, conn, cli: CLI.RichCLI.Styler):
        self.conn = conn
        self.cli = cli

    @staticmethod
    def GetSizeOf(data) -> bytes:
        return str(sys.getsizeof(data)).encode()

    def Rx_Protocol(self):
        self.cli.Show(Text("Receiving protocol:", style="italic blue"))
        # --------------------------------------------------------------------------------------
        self.cli.Show(Text("Instruction:", style="bold blue"))
        instruction = self.conn.recv(100)
        instructionText = Text(text="Instruction=  ")
        instructionText.append(Text(text=instruction.decode(), style="purple"))
        self.conn.sendall(Rx.GetSizeOf(instruction))
        # --------------------------------------------------------------------------------------
        self.cli.Show(Text("Waiting for start token", style="red"))
        start_instruction = self.conn.recv(100)
        self.cli.Show(Text("Got Start instruction", style="blue"))
        self.cli.Show(Text(start_instruction.decode(), style="red"))
        self.conn.sendall(Rx.GetSizeOf(start_instruction))
        # --------------------------------------------------------------------------------------
        self.cli.Show(Text("Waiting for size token", style="red"))
        size_instruction = self.conn.recv(100)
        self.cli.Show(Text("Got Start instruction", style="blue"))
        sizeText = Text("The device is sending:  ", style="blue")
        sizeText.append(Text(f"{size_instruction.decode()} bytes", style="purple"))
        self.cli.Show(sizeText)
        # --------------------------------------------------------------------------------------
        self.cli.Show(Text("Waiting for schedule token", style="red"))
        schedule_instruction = self.conn.recv(100)
        self.cli.Show(Text("Got schedule instruction", style="blue"))
        scheduleText = Text("The device is sending:  ", style="blue")
        scheduleText.append(Text(f"{schedule_instruction.decode()} bytes", style="purple"))
        self.cli.Show(scheduleText)
        self.conn.sendall("OKAY".encode())
        # --------------------------------------------------------------------------------------
        Rxdata = self.conn.recv(int(size_instruction.decode()))
        self.cli.Show(Text("Connection closed", style="bold green"))
        self.conn.close()
        return Rxdata, schedule_instruction.decode()
