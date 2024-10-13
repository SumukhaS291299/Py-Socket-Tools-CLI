import time

from CLI import RichCLI
from Client import clientConnect

if __name__ == '__main__':
    cli = RichCLI.Styler()
    client = clientConnect.TCPClient(8080)
    client.showConnInfo()
    with open("Aria Math.wav", "rb") as f:
        data = f.read()
    client.Connect()
    client.Tx_Protocol(data=data, instruction="Senddd", conn=client.soc, cli=cli)
