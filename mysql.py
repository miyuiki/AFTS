import pymysql.cursors

class MySQL:
    def connect(self):
        connection = pymysql.connect(host='tsmc-afts.ddns.net', database='afts', user='cichangg', password='miyuiki0712')
        return connection

    # def execute(self, con, query):
    #     with con:
    #         with con.cursor() as cursor:
    #             cursor.execute(query)
    #         con.commit()
