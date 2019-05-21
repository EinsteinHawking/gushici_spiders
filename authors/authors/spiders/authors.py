# -*- coding: utf-8 -*-
import scrapy
from authors.items import AuthorsItem
import time,random

import re   

class TextSpider(scrapy.Spider):
	name = 'authors'
	allowed_domains = ['gushiwen.org']
	start_urls = ['https://so.gushiwen.org/authors/']

	def parse(self, response):
		

		
		informations = response.xpath("//div[@class='left']/div[@class='sonspic']")
		for information in informations:
			item = AuthorsItem()
		
			item['name'] = information.xpath('./div[@class="cont"]/p/a/b/text()').extract_first()
			item['pictureurl'] = information.xpath('div[@class="cont"]/div[@class="divimg"]//img//@src').extract_first()
			item['message'] = information.xpath('div[@class="cont"]//p[2]/text()').extract_first()
			
			print(item['name'])
			print(item['pictureurl'])
			print(item['message'])

			yield item
			page_url = response.xpath('//div[@class="left"]/form[@id="FromPage"]/div[@class="pagesright"]/a[@class="amore"]/@href').get()
			if page_url:
				print("https://so.gushiwen.org" + page_url)
				yield scrapy.Request("https://so.gushiwen.org" + page_url, callback = self.parse)
			

