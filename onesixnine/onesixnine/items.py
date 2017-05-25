# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OnesixnineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()  # 该图片在该相册中的id
    title = scrapy.Field()  # 该相册的名字
    year = scrapy.Field()  # 该图片上传的年份
    folder_num = scrapy.Field()  # 该图片是该年份的第几个相册
    month_day = scrapy.Field()  # 该相册是该年份的几月几日创建的
    album_id = scrapy.Field()
    url = scrapy.Field()  # 该图片的url
