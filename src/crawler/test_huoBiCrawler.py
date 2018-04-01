# -*- coding:utf-8 -*-
import socket
import socks

from unittest import TestCase
from . import huobi_crawler


# -*- coding:utf-8 -*-
class TestHuoBiCrawler(TestCase):
    def test_fetch(self):
        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1086)
        socket.socket = socks.socksocket

        cw = huobi_crawler.HuoBiCrawler()
        print(cw.fetch())
