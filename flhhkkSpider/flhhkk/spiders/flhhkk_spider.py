# -*- coding: utf-8 -*-
import re

from scrapy.spiders import CrawlSpider
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from flhhkk.flhhkk_request import FlhhkkItemPageRequest
from flhhkk.flhhkk_request import FlhhkkIndexPageRequest

from flhhkk.items import FlhhkkItem

chrome_options = Options()
chrome_options.add_argument('--incognito')  # 使用隐身模式打开


# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")

class FlhhkkSpider(CrawlSpider):
    name = 'flhhkk'
    allowed_domains = ['flhhkk.com']
    host = "https://flhhkk.com"

    # 实例化一个浏览器对象
    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def start_requests(self):
        url = "https://flhhkk.com/page/30"
        yield FlhhkkIndexPageRequest(url, callback=self.parse_index)

    # 整个爬虫结束后关闭浏览器
    def close(self, spider):
        self.browser.quit()

    # 访问主页的url, 拿到对应板块的response
    def parse_index(self, response):
        div_list = response.xpath('//div[@class="ajax-load-con content wow fadeInUp"]')
        for div_item in div_list:
            # 对每一个板块进行详细访问并解析, 获取板块内的每条新闻的url
            a = div_item.xpath('.//div/div[1]/h2/a/@href').extract_first()
            yield FlhhkkItemPageRequest(a, callback=self.parse_detail)

        # 继续爬取下一页
        next_page_url = response.xpath(
            '//nav[@class="navigation pagination"]/div[@class="nav-links"]/a[@class="next page-numbers"]/@href').extract_first()
        if next_page_url:
            yield FlhhkkIndexPageRequest(next_page_url, callback=self.parse_index)

    def parse_detail(self, response):
        item = FlhhkkItem()

        content_div = response.xpath('//div[@class="article col-xs-12 col-sm-8 col-md-8"]/div[@class="post"]')

        item["download_content"] = response.xpath('/html/head/meta[3]/@content').extract_first()
        item["title"] = content_div.xpath('.//div[@class="post-title"]/h1/text()').extract_first()
        item["content"] = content_div.xpath('.//div[@class="post-content"]').extract_first()  # 提取div的html内容
        item["url"] = response.request.url
        yield item
