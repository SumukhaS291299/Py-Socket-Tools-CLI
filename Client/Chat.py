from Client import clientConnect
from CLI import RichCLI
from rich.text import Text
from rich.prompt import Prompt


def StartChat():
    text = Text(text="Starting chat..", style="bold red")
    cli = RichCLI.Styler()
    cli.Show(text)
    client = clientConnect.TCPClient(8080, 'wild_sumukha')
    client.showConnInfo()
    client.Connect()
    cli.Show("Chat:")
    while True:
        msg = Prompt.ask(f"[{client.NAME}]:")
        if msg != 'close':
            client.ChatSend(msg)
        else:
            break
