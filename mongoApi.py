
import pymongo


class Mongo():
    def __init__(self, db_name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]

    def insert(self, collection_name, data):
        collection = self.db[collection_name]
        collection.insert_one(data)

    def find(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)
    
    def find_all(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find(query)
    
    def update(self, collection_name, query, data):
        collection = self.db[collection_name]
        return collection.update_one(query, data)

    def delete(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query)
    
