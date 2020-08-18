import pymongo
class LocalDatabase:
    def __init__(self, host_name: str, port: int) -> None:
        self.database_connection = pymongo.MongoClient(host_name, port)
    def add_document(self, database: str, collection: str, document: dict) -> None:
        self.database_connection[database][collection].insert_one(document)
    def find_all(self, database: str, collection: str) -> pymongo.cursor.Cursor:
       return self.database_connection[database][collection].find()