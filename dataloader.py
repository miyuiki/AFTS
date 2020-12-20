import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class DataLoader:
    def __init__(self):
        cred = credentials.Certificate('./application/serviceAccount.json')

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
        return users

if __name__ == "__main__":
    dt = DataLoader()
    print(dt.get_users())