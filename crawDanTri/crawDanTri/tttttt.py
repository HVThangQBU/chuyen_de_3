# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import sys
#
# import mariadb
# # useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
#
# from itemadapter import ItemAdapter
#
#
# class MariadbPipeline:
#     def __init__(self):
#         self.conn = mariadb.connect(
#             user="root",
#             password="2001",
#             host="localhost",
#             port=3307,
#             database="scrapy"
#
#         )
#
#         self.cur = self.conn.cursor()
#
#         ## Create PLDS table if none exists
#         # self.cur.execute("""
#         #  CREATE TABLE IF NOT EXISTS bai_bao(
#         #      title TEXT,
#         #      date_vn TEXT,
#         #      content TEXT,
#         #      url TEXT
#         #  )
#         #  """)
#
#     def process_item(self, item, spider):
#         ## Define insert statement
#         self.cur.execute("select * from scrapydata where title = ?", (item['title'],))
#         # "select * from danhmucdantri where danhmuc = ?", (item['danhmuc'],)
#         result = self.cur.fetchone()
#         ## If it is in DB, create log message
#         if result:
#             spider.logger.warn("Item already in database: %s" % item['titlcd cre'])
#             # spider.logger.warn("Item already in database: %s" % item['danhmuc'])
#
#         ## If text isn't in the DB, insert data
#         else:
#             self.cur.execute("""INSERT INTO scrapydata (title, content, timeupdate, figure, url) VALUES (?,?,?,?,?)
#                      """,
#                              (
#                                  str(item['title']),
#                                  str(item['content']),
#                                  str(item['timeupdate']),
#                                  str(item['figure']),
#                                  str(item['url']),
#                              ),)
#             # """INSERT INTO danhmucdantri (danhmuc) VALUES (?)
#             #                                           """,
#             # (
#             #     str(item['danhmuc']),
#             # )
#             pipelines.pyself.conn.commit()
#         return item
#     def close_spider(self, spider):
#
#         ## Close cursor & connection to database
#         self.cur.close()
#         self.conn.close()