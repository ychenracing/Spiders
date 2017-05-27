# -*- coding: utf-8 -*-

import logging
import os
import urllib.request

import pymongo

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from onesixnine import settings


class OnesixninePipeline(object):
    logger = logging.getLogger('OnesixninePipeline')
    connection = pymongo.MongoClient('localhost', 27017)

    def __init__(self):
        self.logger.info('pipeline init')
        self.db = self.connection.scrapy  # 切换到scrapy数据库
        self.collection = self.db.onesixnine  # 获取到onesixnine集合

    def process_item(self, item, spider):
        self.save_image(item)
        return item

    def save_image(self, item):
        if not item:
            return
        if os.path.exists(os.path.dirname(settings.DEFAULT_OUTPUT_FOLDER)):
            save_folder = settings.DEFAULT_OUTPUT_FOLDER
        else:
            save_folder = settings.CANDIDATE_DEFAULT_OUTPUT_FOLDER
        if not os.path.exists(save_folder):
            os.mkdir(save_folder)

        # 获取图片扩展名
        ext = os.path.splitext(item['url'])[1]
        # 得到图片保存的名字
        image_save_path = os.path.join(save_folder,
                                       item['year'] + '_' + item['month_day'] + '_' + item['folder_num'] + '_' + item[
                                           'album_id'] + '_' + item['_id'] + ext)
        urllib.request.urlretrieve(item['url'], image_save_path)
        if not self.connection:
            return item
        self.collection.save(item)

    def __del__(self):
        self.logger.info('pipeline exit!')
