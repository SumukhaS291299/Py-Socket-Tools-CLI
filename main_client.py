import time
from TransportProtocol import TransmitterTx
from CLI import RichCLI
from Client import clientConnect

if __name__ == '__main__':
    cli = RichCLI.Styler()
    CLIENT_HOST = cli.console.input("Enter the host name to connect:\n")
    client = clientConnect.TCPClient(HOST=CLIENT_HOST, PORT=8080)
    client.showConnInfo()
    # with open("Aria Math.wav", "rb") as f:
    #     data = f.read()
    # client.Connect()
    # TransmitterTx.Tx(data=data, instruction="Send", conn=client.soc, cli=cli).tx_protocol_file_transfer()
    client.Connect()
    TransmitterTx.Tx(data=b"",instruction="Chat",conn=client.soc,cli=cli).tx_protcol_chat()