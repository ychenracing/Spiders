# -*- coding: utf-8 -*-


import os
import re

from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from onesixnine.items import OnesixnineItem


class OnesixnineSpider(CrawlSpider):
    name = "onesixnine"

    allowed_domains = ['www.169ee.com', '724.169pp.net']

    start_urls = ['http://www.169ee.com']

    year_monthday_albumid_pattern = re.compile(r'http://www\.169ee\.com/[a-z]+/(\d*?)/(\d*?)/(\d*?)\.html')

    image_year_foldernum_imageid_pattern = re.compile(r'http://724\.169pp\.net/169mm/(\d*?)/(\d*?)/(\d*?)\.[a-z]*?')

    rules = (Rule(LinkExtractor(allow=(r'^http://www.169ee.com/[a-z]+$',))),
             Rule(LinkExtractor(
                 allow=(r'^http://www.169ee.com/[a-z]*?/20[0-9]*?/[0-9]*?/[0-9]*?\.html$',
                        r'^http://www.169ee.com/[a-z]*?/20[0-9]*?/[0-9]*?/\d*?_\d*?\.html$')),
                 callback='parse_album'))

    def parse_album(self, response):
        img_srcs = response.xpath(
            '//div[@id="content"]/div[@class="big-pic"]/div[@class="big_img"]/p/img/@src').extract()
        if not img_srcs:
            return
        page_r_index = response.url.rfind('_')
        slash_r_index = response.url.rfind('/')
        if page_r_index > slash_r_index:
            # 当前页面链接中存在分页的部分，去掉当前链接中的分页部分
            album_url_prefix, album_url_suffix = os.path.split(response.url)
            album_url = response.urljoin(re.compile(r'_\d+').sub('', album_url_suffix))
        else:
            album_url = response.url
        # 从当前页面链接中解析出该相册的年、月日、相册id
        year_monthday_albumid_match = self.year_monthday_albumid_pattern.search(album_url)
        if not year_monthday_albumid_match:
            return
        year = year_monthday_albumid_match.group(1)
        month_day = year_monthday_albumid_match.group(2)
        album_id = year_monthday_albumid_match.group(3)
        for img_src in img_srcs:
            item = OnesixnineItem()
            item['title'] = response.xpath('/html/head/title/text()').extract_first()
            item['year'] = year
            image_year_foldernum_imageid_match = self.image_year_foldernum_imageid_pattern.search(img_src)
            if not image_year_foldernum_imageid_match:
                continue
            item['folder_num'] = image_year_foldernum_imageid_match.group(2)
            image_local_id = image_year_foldernum_imageid_match.group(3)
            item['_id'] = year + month_day + album_id + item['folder_num'] + image_local_id
            item['month_day'] = month_day
            item['album_id'] = album_id
            item['album_url'] = album_url
            item['url'] = img_src
            yield item

        next_page_in_album = response.xpath(
            '//div[@id="content"]/div[@class="big-pic"]/div[@class="dede_pages"]/ul/li[last()]/a/@href').extract_first()
        if next_page_in_album and next_page_in_album != '#':
            next_page_url = response.urljoin(next_page_in_album)
            yield Request(next_page_url, callback=self.parse_album)
