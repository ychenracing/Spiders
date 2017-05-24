# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from haofl.items import HaoflItem


class HaoflSpider(CrawlSpider):
    """爬取haofl"""
    name = 'haofl'  # Spider名，必须唯一，执行爬虫命令时使用

    allowed_domains = ['www.haofl.net']  # 限定允许爬的域名，可设置多个

    start_urls = [
        "http://www.haofl.net/page/1"
    ]
    

    def parse_start_url(self, response):
        """CrawlSpider默认先从start_url获取Request，然后回调parse_start_url方法"""
        li_list = response.xpath('//*[@id="post_container"]/li')
        for li_div in li_list:
            link = li_div.xpath('.//div[@class="thumbnail"]/a/@href').extract_first()
            yield scrapy.Request(link, callback=self.parse_detail_url)

        next_page = response.xpath('//div[@class="pagination"]/a[@class="next"]/@href').extract_first()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse_start_url)


    def parse_detail_url(self, response):
        """获取haofl的详情页"""
        main_div = response.xpath('//*[@id="content"]/div[1]')
        item = HaoflItem()
        item['title'] = main_div.xpath('//h1[1]/text()').extract_first()
        item['text'] = main_div.xpath('//div[@id="post_content"]').extract_first()
        item['download'] = main_div.xpath('//div[@id="post_content"]/blockquote').extract_first()
        item['tag'] = main_div.xpath('//div[@class="article_tags"]/div[@class="tagcloud"]').extract_first()
        item['category'] = main_div.xpath('//div[@class="article_info"]/span[@class="info_category info_ico"]/a').extract_first()
        item['date'] = main_div.xpath('//div[@class="article_info"]/span[@class="info_date info_ico"]/text()').extract_first()
        item['view'] = main_div.xpath('//div[@class="article_info"]/span[@class="info_views info_ico"]/text()').extract_first()
        item['comment'] = main_div.xpath('//div[@class="article_info"]/span[@class="info_comment info_ico"]/a/text()').extract_first()
        item['link'] = response.url
        yield item

