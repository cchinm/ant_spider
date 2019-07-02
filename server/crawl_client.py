import socket
import pickle
class CrawlClient:

    def __init__(self, host, port, buffsize=1024):
        self.host = host
        self.port = port
        self.buffsize = buffsize

    def buildup_client(self, tpe=b"0"):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        sock.send(tpe)
        msg = sock.recv(1024)
        print(msg)
        try:
            msg = pickle.loads(msg)
            print(msg, type(msg))
            sock.close()
        except:
            pass


if __name__ == '__main__':
    p = CrawlClient("127.0.0.1", 25432)
    p.buildup_client(b"u")
    p.buildup_client(b"0")