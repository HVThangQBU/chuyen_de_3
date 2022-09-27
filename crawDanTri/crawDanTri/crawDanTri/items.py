
import scrapy
from scrapy.item import Item, Field


class CrawBaoDanTri(scrapy.Item):
    danhmuc = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    image = scrapy.Field()
    timeupdate = scrapy.Field()
    url = scrapy.Field()
    pass



