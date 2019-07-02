import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='crawl_server.log', level=logging.DEBUG, format=LOG_FORMAT)