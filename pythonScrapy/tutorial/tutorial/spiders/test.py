import scrapy
from scrapy import Selector


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://kenh14.vn/chao-nhe-mua-khai-truong-20220904231539784.chn',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        #title = Selector(response).xpath("//h2[@class='title-page']/text()").extract_first()
        title = response.xpath("//h1[@class='kbwc-title']/text()").extract_first()
        print("aaa", response)
        # content = response.xpath("//div[@class='knc-content']").extract_first().strip()

        print('tieu de', title)
        # print("noi dung", content)
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
#######