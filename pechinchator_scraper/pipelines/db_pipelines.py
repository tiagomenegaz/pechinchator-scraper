from pymongo import MongoClient

from scrapy.conf import settings
from scrapy import log


class MongoDBPipeline(object):

    def __init__(self):
        self.client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = self.client[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def close_spider(self, _spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        log.msg("Thread persisted to DB!", level=log.DEBUG, spider=spider)
        return item
