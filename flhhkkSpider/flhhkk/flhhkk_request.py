#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
只是继承一下scrapy.Request，然后pass，好区分哪些Request需要处理，相当于改个名
"""
import scrapy

class FlhhkkRequest(scrapy.Request):
    """
    flhhkkSpider专用Request类
    """
    pass