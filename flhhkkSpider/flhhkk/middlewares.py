# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from flhhkk.flhhkk_request import FlhhkkIndexPageRequest
from flhhkk.flhhkk_request import FlhhkkItemPageRequest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class FlhhkkSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # 如果spider为SeleniumSpider的实例，并且request为SeleniumRequest的实例
        # 那么该Request就认定为需要启用selenium来进行渲染html
        # 控制浏览器打开目标链接
        spider.browser.get(request.url)

        # 在构造渲染后的HtmlResponse之前，做一些事情
        # 1.比如等待浏览器页面中的某个元素出现后，再返回渲染后的html；
        # 2.比如将页面切换进iframe中的页面；
        if isinstance(request, FlhhkkIndexPageRequest):
            # 等待下一页出现
            WebDriverWait(spider.browser, 600).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, '//nav[@class="navigation pagination"]/div[@class="nav-links"]')))
        elif isinstance(request, FlhhkkItemPageRequest):
            # 等待要爬取的item出现
            WebDriverWait(spider.browser, 600).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, '//div[@class="article col-xs-12 col-sm-8 col-md-8"]')))

        # 获取浏览器渲染后的html
        html = spider.browser.page_source

        # 构造Response
        # 这个Response将会被你的爬虫进一步处理
        return HtmlResponse(url=spider.browser.current_url, request=request, body=html.encode(), encoding="utf-8")

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
