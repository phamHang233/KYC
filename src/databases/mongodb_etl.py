from pymongo import MongoClient
from config import MongoETLConfig


# from utils.retry_handler import retry_handler

# logger = get_logger("Blockchain ETL")


class MongoDB:
    def __init__(self, connection_url=None, database=None, db_prefix=""):
        self._conn = None
        if not connection_url:
            connection_url = MongoETLConfig.HOST

        _db = MongoETLConfig.DATABASE
        # if databases:
        #     _db = databases
        self.connection = MongoClient(connection_url)
        if db_prefix:
            db_name = db_prefix + "_" + _db
        else:
            db_name = _db

        self.mongo_db = self.connection[db_name]
        self.blocks = self.mongo_db[MongoETLConfig.blocks]

    def get_smart_contracts(self):
        cursor = self.mongo_db.find({""}, batch_size=10000)
        smart_contracts = []
        for smart_contract in cursor:
            smart_contracts.append(smart_contract)

        return smart_contracts



    def get_documents(self, collection, conditions, args=None):
        _collection = self.mongo_db[collection]
        if args:
            result = _collection.find(conditions, args)
        else:
            result = _collection.find( conditions)
        return result

    def get_from_address(self, transaction):

        collection = self.mongo_db["transactions"]
        transaction_lowercase = transaction.lower()
        cursor= collection.find_one({
    '_id': f'transaction_{transaction_lowercase}'
})

        ####
        return cursor["from_address"]
    def get_block_number_from_timestamp(self, condition):
        result= self.blocks.find(condition).sort('number', -1).limit(1)
        return result[0]['number']