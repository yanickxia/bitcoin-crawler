# -*- coding:utf-8 -*-

from . import crawler
import requests
import datetime


class HuoBiCrawler(crawler.Crawler):
    def fetch(self):
        r = requests.get("https://api.huobi.pro/market/history/kline?period=1day&size=1&symbol=btcusdt", timeout=5)
        json_data = r.json()
        date = int(json_data['ts'] / 1000)
        json_data = json_data['data'][0]
        return {
            'exchange': 'huobi',
            'date': datetime.datetime.fromtimestamp(date).replace(second=0),
            'high': json_data['high'],
            'vol': json_data['vol'],
            'last': json_data['close'],
            'low': json_data['low'],
            'open': json_data['open']
        }
