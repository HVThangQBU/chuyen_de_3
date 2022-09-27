from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

from crawDanTri.items import CrawBaoDanTri


def strip_value(value):
    m = re.search("http[^\s]+(\s)*h?(http[^\s>]+)(\s)*", value)
    if m:
        # print m.group(2).encode('UTF-8')
        return m.group(2)
    else:
        # print value.encode('UTF-8')
        return value

class ToScrapeSpiderXPath(CrawlSpider):

    name = 'crawbaibao'
    allowed_domains = ['dantri.com.vn']
    f = open("readme.csv")
    start_urls = [url.strip() for url in f.readlines()]
    # print(start_urls)
    f.close()
    rules = (

        Rule(LinkExtractor(allow='',
                           deny=['/abc/'],
                           process_value=strip_value,
                           restrict_xpaths=["//div[@class='pagination']"]), follow=True,
             process_links=None),
        Rule(LinkExtractor(allow='',
                           deny=['/abc/'],
                           process_value=strip_value,
                           restrict_xpaths=["//article[@class='article-item']"]), follow=False, callback='parse_item',
             process_links=None)
    )
    def parse_item(self, response):
        item = CrawBaoDanTri()
        danhmuc = response.xpath("//*[@class='breadcrumbs']/li/a/text()").get()
        item['danhmuc'] = danhmuc
        title = response.xpath("//*[@class='title-page detail']/text()").get()
        item['title'] = title
        # list_p = response.xpath("//h2[@class='singular-sapo']/text() |div[@class='singular-content']/p/strong/text() | //div[@class='singular-content']/p/text()").getall()
        list_p = response.xpath(
            "//h2[@class='singular-sapo']/text() | //div[@class='singular-content']/p/text()").extract()
        content = str(list_p)
        item['content'] = content.strip(", ['']").replace(',','')
        image = response.xpath(
            ".//div[@class='singular-content']/figure[@class='image align-center']/img/@src | //figure[@class='image']/img/@src").get()
        item['image'] = str(image)
        timeupdate = response.xpath(".//time[@class='author-time']/text()").get()
        item['timeupdate'] = timeupdate
        url = response.request.url
        item['url'] = str(url)
        yield item

