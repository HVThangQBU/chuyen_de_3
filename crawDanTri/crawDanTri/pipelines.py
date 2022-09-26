

import mariadb

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

        self.cur.execute("""SELECT * from danhmucbaiviet WHERE danhmuc = ? 
                                 """,
                         (
                             str(item['danhmuc']),
                         ))
        myresult = self.cur.fetchmany()

        print("consologday", myresult)
        test = dict(myresult)
        strdm = str(item['danhmuc'])
        bien = test[strdm]
        item['iddanhmuc'] = bien
        print(bien)

        self.cur.execute("""INSERT INTO tatcabaiviet (iddanhmuc,title, content, image, timeupdate,url) VALUES (?,?,?,?,?,?)
                           """,
                         (
                            item['iddanhmuc'],
                             str(item['title']),
                             str(item['content']),
                             str(item['image']),
                             str(item['timeupdate']),
                             str(item['url']),
                         ))
        self.conn.commit()

        return item




    def close_spider(self, spider):

        ## Close cursor & connection to database
        self.cur.close()

        self.conn.close()




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


