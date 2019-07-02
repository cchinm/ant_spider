import socket
import traceback
import pickle
from server import logger
import logging

class CrawlServer:

    def __init__(self, host, port, buffsize=1024*1024):
        self.host = host
        self.port = port
        self.buffsize = buffsize

    def buildup(self):
        """
        建立服务端
        :return:
        """

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            logging.info("socket %s %d" %(self.host, self.port) )
            sock.bind((self.host, self.port))
            sock.listen(5)
        except Exception as e:
            traceback.print_exc()
            logging.error("server error %s" % e)
        else:
            while True:
                try:
                    conn, addr = sock.accept()
                    print(addr)
                    conn.settimeout(15)
                    # 持续接收客户端消息

                    msg = conn.recv(self.buffsize)
                    print(msg)
                    if msg == b"0":
                        logging.info("quit server")
                        conn.send(b"quit")
                        conn.close()
                    elif msg == b"u":
                        urls = self.send_urls()
                        logging.info("send %r" % urls)
                        urls = pickle.dumps(urls)
                        conn.send(urls)
                    else:
                        conn.send(b"welcome to crawl_server")
                except Exception as e:
                    traceback.print_exc()
                    logging.error("server error %s" % e)



    def send_urls(self):
        urls = [
            "https://www.baidu.com",
            "https://www.taobao.com",
            "https://v.qq.com"
        ]
        return urls

    get_urls = send_urls

    def set_urls(self, *urls):
        # TODO:url存入队列文件/数据库
        pass

    def item_pipelines(self, *items):
        # TODO:将数据存入数据库/文件
        pass

if __name__ == '__main__':
    p = CrawlServer("127.0.0.1", 25432)
    p.buildup()