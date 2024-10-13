import time

from Server import Serve
from  multiprocessing import Process

if __name__ == '__main__':
    server = Serve.TCPServe(8080)
    server.showConnInfo()
    Serve = Process(target=server.ListenConnections)
    Serve.start()