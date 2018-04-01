# -*- coding:utf-8 -*-

from . import crawler
import requests
import datetime


class BitstampCrawler(crawler.Crawler):
    def fetch(self):
        r = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd/", timeout=5)
        json_data = r.json()

        return {
            'exchange': 'bitstamp',
            'date': datetime.datetime.fromtimestamp(int(json_data['timestamp'])).replace(second=0),
            'high': json_data['high'],
            'low': json_data['low'],
            'last': json_data['last'],
            'open': json_data['open'],
            'vol': json_data['volume']
        }
