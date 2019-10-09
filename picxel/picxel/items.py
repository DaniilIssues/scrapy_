# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PicxelItem(scrapy.Item):
    category = scrapy.Field()
    tags = scrapy.Field()
    author = scrapy.Field()
    license = scrapy.Field()
    source = scrapy.Field()
    size = scrapy.Field()
    pic_url = scrapy.Field()
    pic_result = scrapy.Field()
