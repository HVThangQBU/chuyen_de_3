# import sys
# import time
# from urllib.parse import urljoin
#
# import mariadb as mariadb
# import scrapy
#
#
#
# from gevent import os
#
#
#
# class ToScrapeSpiderXPath(scrapy.Spider):
#     name = 'webtest'
#     allowed_domains = ['dantri.com.vn']
#     start_urls = ['https://dantri.com.vn/']
#
#     def parse(self, response):
#         item = CrawdantriItem()
#         danhmuc = response.xpath('.//*[@class="menu-wrap"]/li[@class="has-child"]/a/text()').getall()
#         for d in range(len(danhmuc)):
#             print(danhmuc[d])
#             tmp = danhmuc[d]
#
#             item['muc'] = tmp
#             yield item
#         products = response.xpath('//article[@class="article-item"]')
#         for p in products:
#             book_url = self.start_urls[0] + \
#                        p.xpath('.//*[@class="article-title"]/a/@href').extract_first()
#             yield scrapy.Request(book_url, callback=self.parse_product)
#
#     def parse_product(self, response):
#         item = CrawdantriItem()
#
#         title = response.xpath('.//h3[@class="article-title"]/a/text()').get()
#         item['title'] = str(title)
#         content = response.xpath(
#             "//article[@class='singular-container']/h2[@class='singular-sapo'] | //article[@class='singular-container']/div[@class='singular-content']/p/text()").getall(),
#         item['content'] = str(content)
#         time = response.xpath('.//div[@class="author-wrap"]/time[@class="author-time"]/text()').get(),
#         item['timeupdate'] = str(time)
#         figure = response.xpath(
#             './/div[@class="singular-content"]/figure[@class="image align-center"]/img/@src').getall(),
#         item['figure'] = str(figure)
#         item['url'] = response.request.url
#
#         #os.system("pause")
#
#         yield item
#
#
#
#
#
