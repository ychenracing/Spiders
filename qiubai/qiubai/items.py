# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    avatar = scrapy.Field()
    profile_link = scrapy.Field()
    name = scrapy.Field()
    gender = scrapy.Field()
    age = scrapy.Field()
    content = scrapy.Field()
    content_link = scrapy.Field()
    up = scrapy.Field()
    comment_num = scrapy.Field()
