from pymongo import MongoClient
class local_database:
    def __init__(self: local_database, database_name: str, port: int) => None:
        self.database_connection = MongoClient(database_name, port)
    def add_document(self: local_database, collection: str, document: dict):
        print(self.database_connection[collection].insert(document))