# -*- coding:utf-8 -*-
import socket
import socks
import threading
import os
import schedule, time, datetime
from src.crawler.okex_crawler import OkexCrawler
from src.crawler.huobi_crawler import HuoBiCrawler
from src.crawler.bitfinex_crawler import BitfinexCrawler
from src.crawler.bitstamp_crawler import BitstampCrawler
from src.db.mongo_db import CrawlerMongoStore
import logging

logger = logging.getLogger()

mongoStore = CrawlerMongoStore()


def fetch_data(crawler):
    exchange_data = crawler.fetch()
    logger.info(exchange_data)
    mongoStore.insert_document(exchange_data)


def invoke_all_crawlers():
    logger.info("invoke all crawler at " + datetime.datetime.now().strftime("%b %d %Y %H:%M:%S"))

    bit_crawlers = [OkexCrawler(),
                    HuoBiCrawler(),
                    BitfinexCrawler(),
                    BitstampCrawler()]
    thread_list = []
    for bit_crawler in bit_crawlers:
        t = threading.Thread(target=fetch_data, args=(bit_crawler,))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()


if __name__ == '__main__':

    if os.environ.get('SS_PROXY_ENABLE') == 'True':
        socks.set_default_proxy(socks.SOCKS5, os.environ.get('SS_PROXY_IP'), int(os.environ.get('SS_PROXY_PORT')))
        socket.socket = socks.socksocket

    schedule.every(10).minutes.do(invoke_all_crawlers)
    while True:
        schedule.run_pending()
        time.sleep(1)
