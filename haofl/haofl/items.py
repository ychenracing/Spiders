# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HaoflItem(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
    download = scrapy.Field()
    tag = scrapy.Field()
    category = scrapy.Field()
    date = scrapy.Field()
    view = scrapy.Field()
    comment = scrapy.Field()
    link = scrapy.Field()