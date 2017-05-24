# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector


class HaoflPipeline(object):
    conn = None
    cursor = None

    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='root', database='haofl')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if not self.cursor or not self.conn:
            return None
        insert = ('insert into item (title, text, download, tag, category, date, view, comment, link) values '
                  '(%s, %s, %s, %s, %s, %s, %s, %s, %s)')
        try:
            self.cursor.execute(insert, (item['title'], item['text'], item['download'], item['tag'], item['category'],
                                         item['date'], item['view'], item['comment'], item['link']))
            self.conn.commit()
            if not self.cursor.rowcount:
                print 'insert failed! item=', item
        except Exception as ex:
            print 'insert error! ex=', ex, ', item=', item,

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
