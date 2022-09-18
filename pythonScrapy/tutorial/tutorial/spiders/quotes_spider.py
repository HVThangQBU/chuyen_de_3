import scrapy
from twisted.python.util import println


#
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#
#     def start_requests(self):
#         urls = [
#             'https://quotes.toscrape.com/page/1/',
#             'https://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = f'quotes-{page}.html'
#         # with open(filename, 'wb') as f:
#         #     f.write(response.body)
#         # self.log(f'Saved file {filename}')


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
         #'http://quotes.toscrape.com/',
        'https://dantri.com.vn/the-gioi/xe-cho-linh-cuu-nu-hoang-anh-bat-dau-hanh-trinh-290km-20220911145531934.htm',
    ]

    def parse(self, response):
        title = response.xpath('.//h1[@class="title-page detail"]/text()').extract_first()
        # content = response.xpath('.//div[@class="singular-content"]/p/text()').extract(),
        content = response.xpath("//article[@class='singular-container']/h2[@class='singular-sapo']/text() | //article[@class='singular-container']/div[@class='singular-content']/p/text()").extract(),
        # content = response.xpath("//article[@class='singular-container']/h2[@class='singular-sapo'] | //article[@class='singular-container']/div[@class='singular-content']").extract(),
        time = response.xpath('.//div[@class="author-wrap"]/time[@class="author-time"]/text()').extract_first(),
        figure = response.xpath('.//div[@class="singular-content"]/figure[@class="image align-center"]/img/@src').extract(),
        print('tieu de: ', title)
        println('content: ', content)
        println('time: ', time)
        println('figure: ', figure)
        aa = " avbvhg"
        # for quote in response.xpath('//article[@class="singular-container"]'):
        # #for quote in response.xpath('//div[@class="quote"]'):
        #     yield {
        #         'text': quote.xpath('./h1[@class="title-page detail"]/text()').extract_first(),
        #
        #         # 'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
        #         #'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
        #         'content': quote.xpath('.//div[@class="singular-content"]/p/text()').extract(),
        #         'time': quote.xpath('.//div[@class="author-wrap"]/time[@class="author-time"]/text()').extract_first(),
        #         'figure': quote.xpath('.//div[@class="singular-content"]/figure[@class="image align-center"]/img/@src').extract(),
        #
        #         # 'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
        #         # 'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
        #         # 'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
        #     }
        print('tieu de moidsddddddd=============== ',title)

        with open('readme.txt', 'w', encoding='utf-8') as f:
            f.write("\ntieu de {0}".format(title))
            f.write("\n content \n{0}".format(content))
            f.write("\n time \n{0}".format(time))
            f.write("\n figure \n{0}".format(figure))




        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))





