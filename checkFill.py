from mysql import MySQL
from dataloader import DataLoader
from datetime import datetime
from autoFill import autoFill

db = MySQL()
con = db.connect()

table = []
with con:
    with con.cursor() as cursor:
        sql = "SELECT * FROM afts.OPERATION_HIST where DATE(UPDATE_TIME) = str_to_date('{0}', '%Y-%m-%d');".format(datetime.today().strftime("%Y-%m-%d"))
        cursor.execute(sql)
        result = cursor.fetchall()
        table = list(result)
        for row in table:
            if row[2] != "DONE":
                autoFill(row[1], cursor)
    con.commit()