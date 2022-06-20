# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import pymongo
# useful for handling different eitem types with a single interface
import scrapy
# from itemadapter import ItemAdapter
# from scrapy.exceptions import DropItem
# from scrapy.pipelines.images import ImagesPipeline
from crawler.items import ScrapyItem

# class MongoPipeline:
#     collection_name = "scrapy_djangoitems"

#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db

#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_uri = os.environ.get("MONGO_URI"),
#             mongo_db = os.environ.get("MONGO_DATABASE", 'items')
#         )

#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]

#     def close_spider(self, spider):
#         self.client.close()

#     def process_item(self, item, spider):
#         self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
#         return item

class DjangoPipeline:
    '''This doesn't do much...'''
    def process_item(self, item, spider):
        new = ScrapyItem(**item)
        new.save()
        return item
