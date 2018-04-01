# -*- coding:utf-8 -*-
import datetime

from . import crawler
import requests


class OkexCrawler(crawler.Crawler):
    def fetch(self):
        r = requests.get("https://www.okex.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=this_week",
                         timeout=5)
        json_data = r.json()
        date = int(json_data['date'])
        json_data = json_data['ticker']
        return {
            'exchange': 'okex',
            'date': datetime.datetime.fromtimestamp(date).replace(second=0),
            'high': json_data['high'],
            'vol': json_data['vol'],
            'last': json_data['last'],
            'low': json_data['low']
        }
