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
    name = 'toscrapee'
    start_urls = [
         #'http://quotes.toscrape.com/',
        'https://dantri.com.vn/the-gioi/xe-cho-linh-cuu-nu-hoang-anh-bat-dau-hanh-trinh-290km-20220911145531934.htm',
    ]



    def parse(self, response):
        title = response.xpath('.//h1[@class="title-page detail"]/text()').get()
        #content = response.xpath('.//div[@class="singular-content"]/p/text()').getall(),
        content = response.xpath("//div[@class='singular-content']").getall(),
        time = response.xpath('.//div[@class="author-wrap"]/time[@class="author-time"]/text()').get(),
        figure = response.xpath('.//div[@class="singular-content"]/figure[@class="image align-center"]/img/@src').getall(),
        title2 = str(title)
        content2 = str(content)
        timeupdate = str(time)
        figure2 = str(figure)
        print('tieu de: ', title2.strip().replace(',',''))
        print('content: ', content2.strip().replace(',',''))
        print('time: ', time)
        print('figure: ', figure)
        # sql = "INSERT INTO scrapydata (title, content, timeupdate, figure) VALUES (%s,%s,%s,%s);"
        # data = (title2, content2, timeupdate, figure2)
        # mycursor.execute(sql, data)
        # conn.commit()
        print('tieu de moidsddddddd=============== ',title)
        with open('readme.txt', 'w', encoding='utf-8') as f:
            f.write("\ntieu de {0}".format(title))
            f.write("\n content \n{0}".format(content))
            f.write("\n time \n{0}".format(time))
            f.write("\n figure \n{0}".format(figure))

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))





