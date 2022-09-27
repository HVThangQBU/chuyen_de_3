#
#
# import mariadb
# import requests
# import json
# import base64
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
#
#         # self.cur.execute("""SELECT * from danhmucbaiviet WHERE danhmuc = ?
#         #                          """,
#         #                  (
#         #                      str(item['danhmuc']),
#         #                  ))
#         # myresult = self.cur.fetchmany()
#         #
#         # print("consologday", myresult)
#         # test = dict(myresult)
#         # strdm = str(item['danhmuc'])
#         # bien = test[strdm]
#         # item['iddanhmuc'] = bien
#         # print(bien)
#         self.cur.execute("select * from baivietdantri where title = ?", (item['title'],))
#         result = self.cur.fetchone()
#         # ## If it is in DB, create log message
#         if result:
#             spider.logger.warn("Item already in database: %s" % item['title'])
#         else:
#             self.cur.execute("""INSERT INTO baivietdantri (danhmuc,title, content, image, timeupdate,url) VALUES (?,?,?,?,?,?)
#                                """,
#                              (
#                                 item['danhmuc'],
#                                 item['title'],
#                                 item['content'],
#                                 item['image'],
#                                 item['timeupdate'],
#                                 item['url'],
#                              ))
#             self.conn.commit()
#             self.cur.execute("""SELECT * from baivietdantri WHERE danhmuc = ?
#                                         """,
#                          (
#                              str(item['danhmuc']),
#                          ))
#             records = self.cur.fetchall()
#             for row in records:
#                 url = 'http://localhost/wordpress/wordpress//wp-json/wp/v2'
#                 username = 'admin'
#                 password = 'AX5Z kH3C o9M3 v0Xd NvC8 5hXC'
#                 userpass = username + ':' + password
#                 encoded_u = base64.b64encode(userpass.encode()).decode()
#                 headers = {'Authorization': 'Basic %s' % encoded_u}
#                 post_title = row[2]
#                 post_body = row[3]
#                 post_image = row[4]
#                 post_time = row[4]
#
#                 post = {'title': post_title,
#                         'status': 'publish',
#                         'content': post_body,
#                         'author': '1',
#                         'format': 'standard',
#                         'media': post_image
#                         }
#                 r = requests.post(url + '/posts', headers=headers, json=post)
#                 print(r)
#
#
#
#     def close_spider(self, spider):
#         print(1)
#         #
#         # ## Close cursor & connection to database
#         # self.cur.close()
#         #
#         # self.conn.close()
#
#
#
#
# # class MariadbDanhMucPipeline:
# #     def __init__(self):
# #         self.conn = mariadb.connect(
# #             user="root",
# #             password="2001",
# #             host="localhost",
# #             port=3307,
# #             database="scrapy"
# #
# #         )
# #
# #         self.cur = self.conn.cursor()
# #
# #         ## Create PLDS table if none exists
# #         # self.cur.execute("""
# #         #  CREATE TABLE IF NOT EXISTS bai_bao(
# #         #      title TEXT,
# #         #      date_vn TEXT,
# #         #      content TEXT,
# #         #      url TEXT
# #         #  )
# #         #  """)
# #
# #     def process_item(self, item, spider):
# #         self.cur.execute("select * from danhmucbaiviet where danhmuc = ?", (item['danhmuc'],))
# #         result = self.cur.fetchone()
# #         # ## If it is in DB, create log message
# #         if result:
# #             spider.logger.warn("Item already in database: %s" % item['danhmuc'])
# #         else:
# #             self.cur.execute("""INSERT INTO danhmucbaiviet (danhmuc) VALUES (?)
# #                                """,
# #                              (
# #                                  str(item['danhmuc']),
# #                              ))
# #             self.conn.commit()
# #             # return item
# #
# #     def close_spider(self, spider):
# #
# #         ## Close cursor & connection to database
# #         self.cur.close()
# #
# #         self.conn.close()
# #
# #
#
#
