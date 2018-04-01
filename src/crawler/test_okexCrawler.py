# -*- coding:utf-8 -*-
import socket
import socks

from unittest import TestCase
from . import okex_crawler


# -*- coding:utf-8 -*-
class TestOkexCrawler(TestCase):
    def test_fetch(self):
        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1086)
        socket.socket = socks.socksocket

        cw = okex_crawler.OkexCrawler()
        print(cw.fetch())
