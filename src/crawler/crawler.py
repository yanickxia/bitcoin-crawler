# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractclassmethod


class Crawler(metaclass=ABCMeta):
    @abstractclassmethod
    def fetch(self):
        pass
