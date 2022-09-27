# import os
#
# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
#
# import re
#
# from twisted.python.util import println
#
#
# def strip_value(value):
#     m = re.search("http[^\s]+(\s)*h?(http[^\s>]+)(\s)*", value)
#     if m:
#         # print m.group(2).encode('UTF-8')
#         return m.group(2)
#     else:
#         # print value.encode('UTF-8')
#         return value
#
# class QuotesSpider(CrawlSpider):
#     name = "baodautu"
#     allowed_domains = ['baodautu.vn']
#     start_urls = [
#             'https://baodautu.vn/batdongsan/',
#             'https://baodautu.vn/quoc-te-d54/',
#     ]
#     rules = (
#
#         Rule(LinkExtractor(allow='',
#                            deny=['/abc/'],
#                            process_value=strip_value,
#                            restrict_xpaths=["//nav[@class='d-flex pagation align-items-center']"]), follow=False, callback='parse_item', process_links=None),
#         Rule(LinkExtractor(allow='',
#                            deny=['/abc/'],
#                            process_value=strip_value,
#                            restrict_xpaths=["//a[@class='fs22 fbold']"]), follow=False, callback='parse_item',
#              process_links=None)
#     )
#     def parse_item(self, response):
#         print('Parse Item>>>>>>>>>>>>>>>>>>>>>')
#         category = response.xpath("//div[@class='fs16 text-uppercase ']/a/text()").get().strip()
#         title = response.xpath("//div[@class='title-detail']/text()").get().strip()
#         image = response.xpath("//div[@id='content_detail_news']//img/@src").get().strip()
#         list_p = response.xpath("//div[@id='content_detail_news']//p//text()").getall()
#         content = str(list_p)
#         date = response.xpath("//span[@class='post-time']/text()").get().strip().replace("-", "")
#         url = response.request.url
#         print(category)
#         println(title)
