from unittest import TestCase
from . import bitstamp_crawler


# -*- coding:utf-8 -*-
class TestBitstampCrawler(TestCase):
    def test_fetch(self):
        bitCrawler = bitstamp_crawler.BitstampCrawler()
        print(bitCrawler.fetch())
