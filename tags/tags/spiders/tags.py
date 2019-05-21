# -*- coding: utf-8 -*-
import scrapy
from tags.items import TagsItem
import time,random

import re   

class TextSpider(scrapy.Spider):
	name = 'tags'
	allowed_domains = ['gushiwen.org']
	start_urls = ['https://www.gushiwen.org/shiwen/']

	def parse(self, response):
		
		informations = response.xpath("//div[@class='right']/")
		for information in informations:
			item = TagsItem()
		
			item['tag_name'] = information.xpath('./div[@class="cont"]/a/text()').extract_first()
			item['tag_url'] = information.xpath('div[@class="cont"]/a//@src').extract_first()
			item['count'] = 0
			
			print(item['tag_name'])
			print(item['tag_url'])
			print(item['count'])

			yield item

#			page_url = response.xpath('//div[@class="left"]/form[@id="FromPage"]/div[@class="pagesright"]/a[@class="amore"]/@href').get()
#			if page_url:
#				print("https://so.gushiwen.org" + page_url)
#				yield scrapy.Request("https://so.gushiwen.org" + page_url, callback = self.parse)
	

