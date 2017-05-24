# -*- coding: utf-8 -*-
import re

from scrapy.spiders import CrawlSpider
from scrapy.spiders import Request

from qiubai.items import QiubaiItem


class QiubaiSpider(CrawlSpider):
    name = 'qiubai'

    allowed_domains = ['www.qiushibaike.com']

    start_urls = ['http://www.qiushibaike.com/8hr/page/1/?s=4984271']

    host = "http://www.qiushibaike.com"

    gender_strip_pattern = re.compile('articleGender |Icon')

    def parse_start_url(self, response):
        content_left_div = response.xpath('//div[@id="content-left"]')
        content_div_list = content_left_div.xpath('./div[@class="article block untagged mb15"]')
        for content_div in content_div_list:
            item = QiubaiItem()
            author_div = content_div.xpath('./div[@class="author clearfix"]')
            test_anonymous = author_div.xpath('./a').extract()
            if test_anonymous:
                item['profile_link'] = author_div.xpath('./a/@href').extract_first()
                item['avatar'] = author_div.xpath('./a[@rel]/img/@src').extract_first()
                item['name'] = author_div.xpath('./a[@title]/h2/text()').extract_first()
                gender_text = author_div.xpath('./div[contains(@class, "articleGender")]/@class').extract_first()
                item['gender'] = self.gender_strip_pattern.sub('', gender_text)
                item['age'] = author_div.xpath('./div[contains(@class, "articleGender")]/text()').extract_first()
            id = content_div.xpath('./a[@class="contentHerf"]/@href').extract()[0]
            item['_id'] = id[id.rfind('/') + 1:]
            content_href_div = content_div.xpath('./a[@class="contentHerf"]')
            item['content'] = content_href_div.xpath('./div[@class="content"]').extract_first()
            item['content_link'] = content_href_div.xpath('./@href').extract_first()
            stat_div = content_div.xpath('./div[@class="stats"]')
            item['up'] = stat_div.xpath('./span[@class="stats-vote"]/i[@class="number"]/text()').extract_first()
            comment_href = stat_div.xpath('./span[@class="stats-comments"]/a[@class="qiushi_comments"]')
            item['comment_num'] = comment_href.xpath('./i[@class="number"]/text()').extract_first()
            yield item

        next_page = content_left_div.xpath('./ul[@class="pagination"]/li[last()]/a/@href').extract_first()
        if next_page:
            yield Request(self.host + next_page, callback=self.parse_start_url)
