# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TagsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	tag_name = scrapy.Field()
	tag_url = scrapy.Field()
	count = scrapy.Field()
