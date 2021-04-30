import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import logging
from datetime import datetime
from mysql import MySQL

FORMAT = '%(asctime)s |%(levelname)s| %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, filename='./log/' + datetime.now().strftime('AFTS_%Y%m%d.log'))


class DataLoader:
    def __init__(self):
        cred = credentials.Certificate('./serviceAccount.json')

        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://autoapply-ee19b.firebaseio.com/'
        })
        

    def get_users(self):
        ref = db.reference()
        data = ref.get()
        users = []
        for v in data.values():
            users.append(v['tsmc_id'])
            logging.info('user ' + v['tsmc_id'] + ' is loaded.')
        return users
    
    def update_load_status(self, users):
        db = MySQL()
        con = db.connect()
        with con:
            with con.cursor() as cursor:
                for user in users:
                    sql = "INSERT INTO afts.OPERATION_HIST (context_id, emp_id, update_time, status) VALUES ('{0}-{1}', '{2}', '{3}','LOADED');"\
                        .format(user, datetime.today().strftime("%y%m%d"), user, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    logging.info("Excute SQL: " + sql)
                    cursor.execute(sql)
            con.commit()


if __name__ == "__main__":
    dt = DataLoader()
    users = dt.get_users()
    

