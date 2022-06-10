# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter
from pymongo import MongoClient


class DouBanPipeline(object):
    def __init__(self):
        self.connection = MongoClient("mongodb://localhost:27017/")
        self.db = self.connection.scrapy
        self.collection = self.db.douban

    def process_item(self, item, spider):
        if not self.connection or not item:
            return
        self.db.col.insert_one(item)

    def __del__(self):
        if self.connection:
            self.connection.close()
