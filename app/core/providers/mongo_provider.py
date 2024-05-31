import pymongo


class MongoProvider:
    def __init__(self, config):
        database_url = config['MONGO_CONNECTION_STRING']
        self.client = pymongo.MongoClient(database_url)
        db = self.client.test
        self.session = db.my_collection

    def get_session(self):
        return self.session
