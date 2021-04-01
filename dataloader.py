import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import logging
from datetime import datetime

FORMAT = '%(asctime)s |%(levelname)s| %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, filename='./log/' + datetime.now().strftime('AFTS_%Y%m%d.log'))


class DataLoader:
    def __init__(self):
        cred = credentials.Certificate('/home/kslab/workspace/Jay/AFTS/serviceAccount.json')

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

if __name__ == "__main__":
    dt = DataLoader()
    dt.get_users()

