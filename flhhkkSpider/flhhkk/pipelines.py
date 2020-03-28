# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector


class FlhhkkPipeline(object):
    conn = None
    cursor = None

    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='root', database='flhhkk')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if not self.cursor or not self.conn:
            return None
        insert = 'insert into flhhkk_item (title, content, url, download_content) values (%s, %s, %s, %s)'
        try:
            self.cursor.execute(insert, (item["title"], item["content"], item["url"], item["download_content"]))
            self.conn.commit()
            if not self.cursor.rowcount:
                print('插入记录失败！item=', item)
                print('SQL=', insert)
        except Exception as ex:
            print('插入记录出错！item=', item, ", ex=", ex)
            print('SQL=', insert)

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
