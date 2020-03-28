#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
只是继承一下scrapy.Request，然后pass，好区分哪些Request需要解析下一页链接，相当于改个名
"""
import scrapy

class FlhhkkIndexPageRequest(scrapy.Request):
    """
    selenium专用Request类
    """
    pass

class FlhhkkItemPageRequest(scrapy.Request):
    """
    selenium专用Request类
    """
    pass