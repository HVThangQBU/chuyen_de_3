import sys

import mariadb as mariadb
import scrapy
try:
    conn = mariadb.connect(
        user="root",
        password="2001",
        host="localhost",
        port=3307,
        database="scrapy"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
mycursor = conn.cursor()

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'testAll'
    allowed_domains = ['dantri.com.vn']
    start_urls = ['https://dantri.com.vn/']

    def parse(self, response):
        quotes = response.xpath('//*[@class="article-content"]')
        for q in quotes:

            title = q.xpath('.//*[@class="article-title"]').get()
            content = q.xpath('.//*[@class="article-excerpt"]/a/text()').getall(),
        # content = response.xpath("//article[@class='singular-container']/h2[@class='singular-sapo'] | //article[@class='singular-container']/div[@class='singular-content']").getall(),
            time = response.xpath('.//div[@class="author-wrap"]/time[@class="author-time"]/text()').get(),
            figure = q.xpath('.//*[@class="article-item"]/*[@class="article-thumb"]/img/@src').getall(),
            yield {"Quote Text ": title, "content": content,"time": time,"a":figure}
        # print('tieu de: ', title)
        # print('content: ', content)
        # print('time: ', time)
        # print('figure: ', f
        # igure)
        # title2 = str(title)
        # content2 = str(content)
        # timeupdate = str(time)
        # figure2 = str(figure)
        # sql = "INSERT INTO scrapydata (title, content, timeupdate, figure) VALUES (%s,%s,%s,%s);"
        # data = (title2, content2, timeupdate, figure2)
        # mycursor.execute(sql, data)
        # conn.commit()
        # print('tieu de moidsddddddd=============== ',title)
        # with open('readme.txt', 'w', encoding='utf-8') as f:
        #     f.write("\ntieu de {0}".format(title))
        #     f.write("\n content \n{0}".format(content))
        #     f.write("\n time \n{0}".format(time))
        #     f.write("\n figure \n{0}".format(figure))
        #
        # next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))





