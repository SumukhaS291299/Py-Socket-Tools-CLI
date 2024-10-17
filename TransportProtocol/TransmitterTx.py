import CLI.RichCLI
from rich.text import Text
import datetime
import sys


class Tx:

    def __init__(self, conn, data: bytes,instruction:str, cli: CLI.RichCLI.Styler):
        self.conn = conn
        self.cli = cli
        self.data = data
        self.instruction = instruction

    def Tx_Protocol(self):
        self.cli.Show(Text("Transmission protocol:", style="italic blue"))
        # --------------------------------------------------------------------------------------
        Inst = Text("Instruction:", style="bold")
        self.cli.Show(Inst.append(Text(self.instruction, style="bold brown")))
        self.conn.sendall(self.instruction.encode())
        self.cli.Show(Text(f"Ack for {self.conn.recv(100).decode()} bytes received from connected device"))
        # --------------------------------------------------------------------------------------
        START_INSTRUCTION = "~|START|~"
        self.conn.sendall(START_INSTRUCTION.encode())
        self.cli.Show(Text(f"Ack for {self.conn.recv(100).decode()} bytes received from connected device"))
        # --------------------------------------------------------------------------------------
        SIZE_INSTRUCTION = str(sys.getsizeof(self.data))
        self.conn.sendall(SIZE_INSTRUCTION.encode())
        # --------------------------------------------------------------------------------------
        SCHEDULE_INSTRUCTION = (datetime.datetime.now() + datetime.timedelta(seconds=15)).strftime(
            "%Y-%m-%d %H:%M:%S.%f")
        self.conn.sendall(SCHEDULE_INSTRUCTION.encode())
        self.cli.Show(Text(f"Scheduling for {SCHEDULE_INSTRUCTION}"))
        self.cli.Show(Text(f"Scheduling received  {self.conn.recv(100).decode()} from connected device"))
        # --------------------------------------------------------------------------------------
        self.cli.Show(Text("Sending Data....", style="bold green"))
        self.conn.sendall(self.data)
        self.cli.Show(Text("Full Data transfered....", style="bold green"))
        self.cli.Show(Text("Requesting Close connection", style="bold green"))
        self.conn.close()