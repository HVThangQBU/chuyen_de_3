
import base64, requests
import urllib
from tempfile import NamedTemporaryFile
import mariadb
import requests
import json
import base64
import random
import urllib.request

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc import Client
import base64, requests
from tempfile import NamedTemporaryFile

class MariadbPipeline:
    def __init__(self):
        self.conn = mariadb.connect(
            user="root",
            password="2001",
            host="localhost",
            port=3307,
            database="scrapy"

        )

        self.cur = self.conn.cursor()

        ## Create PLDS table if none exists
        # self.cur.execute("""
        #  CREATE TABLE IF NOT EXISTS bai_bao(
        #      title TEXT,
        #      date_vn TEXT,
        #      content TEXT,
        #      url TEXT
        #  )
        #  """)

    def process_item(self, item, spider):

        # self.cur.execute("""SELECT * from danhmucbaiviet WHERE danhmuc = ?
        #                          """,
        #                  (
        #                      str(item['danhmuc']),
        #                  ))
        # myresult = self.cur.fetchmany()
        #
        # print("consologday", myresult)
        # test = dict(myresult)
        # strdm = str(item['danhmuc'])
        # bien = test[strdm]
        # item['iddanhmuc'] = bien
        # print(bien)
        self.cur.execute("select * from baivietdantri where title = ?", (item['title'],))
        result = self.cur.fetchone()
        # ## If it is in DB, create log message
        if result:
            spider.logger.warn("Item already in database: %s" % item['title'])
        else:
            self.cur.execute("""INSERT INTO baivietdantri (danhmuc,title, content, image, timeupdate,url) VALUES (?,?,?,?,?,?)
                               """,
                             (
                                item['danhmuc'],
                                item['title'],
                                item['content'],
                                item['image'],
                                item['timeupdate'],
                                item['url'],
                             ))
            self.conn.commit()
            client = Client('http://localhost/wordpress/wordpress/xmlrpc.php',
                            'admin', 'AX5Z kH3C o9M3 v0Xd NvC8 5hXC')
            self.cur.execute("""SELECT * from baivietdantri WHERE danhmuc = ?
                                        """,
                         (
                             str(item['danhmuc']),
                         ))
            records = self.cur.fetchall()
            for row in records:
                #goi uploading.py -> post_id
                post_danhmuc = row[1]
                post_title = row[2]
                post_body = row[3]
                post_time = row[5]
                url_img = row[4]
                name = random.randrange(10000000, 100000000)
                fullname = str(name) + ".jpg"
                urllib.request.urlretrieve(url_img, fullname)
                raw = requests.get(url_img).content
                with NamedTemporaryFile(delete=False, mode="wb", suffix=".jpg") as img:
                    img.write(raw)
                    # print(f.file())
                    c = open(img.name, "rb")
                    filename = img.name
                    data = {
                        'name': filename,
                        'type': 'image/jpeg',  # mimetype
                    }

                    # read the binary file and let the XMLRPC library encode it into base64
                    with open(filename, 'rb') as img:
                        data['bits'] = xmlrpc_client.Binary(img.read())

                    response = client.call(media.UploadFile(data))
                attachment_id = response['id']
                post = WordPressPost()
                post.title =   post_title
                post.content =  post_body
                post.post_status = 'publish'
                post.terms_names = {
                    'post_tag': ['Báo Dân Trí', 'Hoàng Thắng'],
                    'category': [post_danhmuc,'THANG HOANG'],
                }
                post.thumbnail = attachment_id
                post.id = client.call(posts.NewPost(post))


    def close_spider(self, spider):
        print(1)
        #
        # ## Close cursor & connection to database
        # self.cur.close()
        #
        # self.conn.close()




# class MariadbDanhMucPipeline:
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
#         self.cur.execute("select * from danhmucbaiviet where danhmuc = ?", (item['danhmuc'],))
#         result = self.cur.fetchone()
#         # ## If it is in DB, create log message
#         if result:
#             spider.logger.warn("Item already in database: %s" % item['danhmuc'])
#         else:
#             self.cur.execute("""INSERT INTO danhmucbaiviet (danhmuc) VALUES (?)
#                                """,
#                              (
#                                  str(item['danhmuc']),
#                              ))
#             self.conn.commit()
#             # return item
#
#     def close_spider(self, spider):
#
#         ## Close cursor & connection to database
#         self.cur.close()
#
#         self.conn.close()
#
#


