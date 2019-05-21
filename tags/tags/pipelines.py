# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class tagsPipeline(object):
		def process_item(self, item, spider):
			with open('标签.txt', "a",encoding="utf-8") as f:
				f.write(item['tags_name']+ '\n')
				f.write(item['tags_url']+ '\n')
				f.write(item['count']+'\n')
				f.write('-----------------------------------------------------------------\n')
			return item

class MongoPipeline(object):

		
    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db['tagsn'].insert(dict(item))
        return item


