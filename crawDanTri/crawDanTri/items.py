# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class CrawdantriItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    iddanhmuc = Field()
    danhmuc = Field()
    title = Field()
    content = Field()
    image = Field()
    timeupdate = Field()
    url = Field()
# class CrawdanhmucItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     danhmuc = Field()



