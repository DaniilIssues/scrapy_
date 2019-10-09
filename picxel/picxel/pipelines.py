import pymongo
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.exceptions import DropItem


# class PicxelPipeline(object):
#
#     def open_spider(self, spider):
#         self.file = open('items.json', 'w', encoding='utf-8')
#
#     def close_spider(self, spider):
#         self.file.close()
#
#     def process_item(self, item, spider):
#         item['size'] = item['size'].split(" ")[-1]
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         return item


class MongoPipeline(object):

    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = 'mongodb+srv://daniil:WaD9090997658@profile-qfvg4.gcp.mongodb.net/test?retryWrites=true&w=majority'
        self.mongo_db = 'picxel'

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        item['size'] = item['size'].split(" ")[-1]
        self.db[self.collection_name].insert_one(dict(item))
        return item
