# -*- coding:utf-8 -*-

from pymongo import MongoClient
import os


class CrawlerMongoStore():
    def __init__(self):
        uri = "mongodb://%s:%s@%s:%s/exchange?authSource=exchange" % \
              (os.environ.get('MONGO_USER'), os.environ.get('MONGO_PASSWORD'), os.environ.get('MONGO_IP'),
               os.environ.get('MONGO_PORT'))
        self.client = MongoClient(uri)
        self.db = self.client['exchange']

    def insert_document(self, doc):
        collection = self.db['exchange']
        collection.insert_one(doc)
