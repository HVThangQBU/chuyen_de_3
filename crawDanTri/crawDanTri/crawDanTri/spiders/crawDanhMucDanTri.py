import sys
import time
from urllib.parse import urljoin

import mariadb as mariadb
import scrapy
import requests
from bs4 import BeautifulSoup
class DanhMuc(scrapy.Spider):
    name = 'danhmucdantri'
    allowed_domains = ['dantri.com.vn']
    start_urls = ['https://dantri.com.vn']

    def parse(self, response):
        listDanhmuc = []
        f = open('readme.csv', 'w', encoding='utf-8')
        start_urls = 'https://dantri.com.vn'
        for href in response.xpath('//li[@class="has-child"]/a/@href').extract():
            linkDanhMuc = start_urls+href
            # listDanhmuc.append(linkDanhMuc)
            f.write("{0}".format(linkDanhMuc))
            f.write("\n")
        f.close()
