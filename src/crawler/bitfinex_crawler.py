# -*- coding:utf-8 -*-
import datetime

from . import crawler
import requests


class BitfinexCrawler(crawler.Crawler):
    def fetch(self):
        r = requests.get("https://api.bitfinex.com/v1/pubticker/btcusd", timeout=5)
        json_data = r.json()
        return {
            'exchange': 'bitfinex',
            'date': datetime.datetime.fromtimestamp(round(float(json_data['timestamp']))).replace(second=0),
            'high': json_data['high'],
            'low': json_data['low'],
            'vol': json_data['volume'],
            'last': json_data['last_price'],
        }
