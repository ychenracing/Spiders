# -*- coding: utf-8 -*-


import re

from scrapy.http import Request
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from onesixnine.items import OnesixnineItem


class OnesixnineSpider(CrawlSpider):
    name = "onesixnine"

    allowed_domains = ['www.169ee.com', '724.169pp.net']

    start_urls = ['http://www.169ee.com']

    album_year_month_day_id_pattern = re.compile(r'http://www\.169ee\.com/[a-z]+/(\d*?)/(\d*?)/(\d*?)\.html')

    image_year_folder_num_id_pattern = re.compile(r'http://724\.169pp\.net/169mm/(\d*?)/(\d*?)/(\d*?)\.[a-z]*?')

    rules = (Rule(SgmlLinkExtractor(allow=(r'^http://www.169ee.com/[a-z]+$',))),
             Rule(SgmlLinkExtractor(
                 allow=(r'^http://www.169ee.com/[a-z]*?/20[0-9]*?/[0-9]*?/[0-9]*?\.html')),
                 callback='parse_album'))

    def parse_album(self, response):
        img_srcs = response.xpath(
            '//div[@id="content"]/div[@class="big-pic"]/div[@class="big_img"]/p/img/@src').extract()
        album_url = response.url
        if not img_srcs:
            return
        year_month_day_id_match = self.album_year_month_day_id_pattern.search(album_url)
        if not year_month_day_id_match:
            return
        year = year_month_day_id_match.group(1)
        month_day = year_month_day_id_match.group(2)
        album_id = year_month_day_id_match.group(3)
        title = response.xpath('/html/head/title/text()').extract_first()
        for img_src in img_srcs:
            item = OnesixnineItem()
            item['title'] = title
            item['year'] = year
            image_year_folder_num_id_match = self.image_year_folder_num_id_pattern.search(img_src)
            if not image_year_folder_num_id_match:
                continue
            item['folder_num'] = image_year_folder_num_id_match.group(2)
            item['_id'] = image_year_folder_num_id_match.group(3)
            item['month_day'] = month_day
            item['album_id'] = album_id
            item['url'] = img_src
            yield item

        next_page_in_album = response.xpath(
            '//div[@id="content"]/div[@class="big-pic"]/div[@class="dede_pages"]/ul/li[last()]/a/@href').extract_first()
        if next_page_in_album and next_page_in_album != '#':
            next_page_url_prefix = album_url[:album_url.rfind('/')+1]
            next_page_url = next_page_url_prefix + next_page_in_album
            yield Request(next_page_url, callback=self.parse_album)
