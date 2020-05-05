
import pathlib as pl
import pymongo
from pymongo import MongoClient, collection, cursor, database, errors
from pymongo.results import InsertOneResult, DeleteResult, InsertManyResult, UpdateResult
from bson.objectid import ObjectId


class DatabaseInterface:
    db_parent_filepath = str(pl.Path(__file__).parent.absolute()) + '/database_files/'
    db_filepath = str(pl.Path(__file__).parent.absolute()) + '/database_files/database.db'
    client = MongoClient('mongodb://localhost:27017/')

    @staticmethod
    def create_vectors_item(name: str, description: str) -> dict:
        vector_item: dict = {
            'name': name,
            'description': description,
            'log_entries': []
        }
        return vector_item

    @staticmethod
    def insert_one_vectors(vectors_item: dict) -> InsertOneResult:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            vectors: collection = db.get_collection('vectors')
            result: InsertOneResult = vectors.insert_one(vectors_item)
            return result
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def insert_many_vectors(vectors_items: list) -> InsertManyResult:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('vectors')
            result: InsertManyResult = log_entries.insert_many(vectors_items)
            return result
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def find_vectors_all() -> list:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            vectors: collection = db.get_collection('vectors')
            result: cursor = vectors.find({})
            return list(result)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def find_vectors_condition(conditions: list) -> list:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('vectors')
            query: dict = {}
            if conditions is not None and len(conditions) != 0:
                query = {'$or': conditions}
            result: cursor = log_entries.find(query)
            return list(result)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def find_one_vectors_by_id(vector_id: str) -> dict:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('vectors')
            result: cursor = log_entries.find(filter={'_id': ObjectId(vector_id)})
            return dict(result)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def update_one_vectors_by_id(vectors_item_id: str, update_fields: dict) -> UpdateResult:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('vectors')
            filter_query: dict = {'_id': ObjectId(vectors_item_id)}
            update: dict = {'$set': update_fields}
            result: UpdateResult = log_entries.update_one(filter=filter_query, update=update)
            return result
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def create_log_entries_item(list_number: int, timestamp: str, event: str,
                                vector: str, location: str, creator: str) -> dict:
        logentry_item: dict = {
            'list_number': list_number,
            'timestamp': timestamp,
            'event': event,
            'vector': vector,
            'location': location,
            'creator': creator
        }
        return logentry_item

    @staticmethod
    def insert_one_log_entries(log_entry_item: dict) -> None:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            result: InsertOneResult = log_entries.insert_one(log_entry_item)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def insert_many_log_entries(log_entries_items: list) -> None:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            result: InsertManyResult = log_entries.insert_many(log_entries_items)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def find_log_entries_all() -> list:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            query_result: cursor = log_entries.find()
            return list(query_result)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def find_log_entries_condition(conditions: list) -> list:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            query = {}
            if conditions is not None and len(conditions) != 0:
                query = {'$or': conditions}
            query_result: cursor = log_entries.find(query)
            return list(query_result)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def find_log_entries_regex(regex_search: str) -> list:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            query = {}
            if regex_search is not None and len(regex_search) != 0:
                query = {'event': {'$regex': regex_search}}
            query_result: cursor = log_entries.find(query)
            return list(query_result)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def find_all_log_entries_return_locations() -> list:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            query_result: cursor = log_entries.find({}, {'location': 1})
            return list(query_result)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def delete_vectors_all() -> DeleteResult:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            vectors: collection = db.get_collection('vectors')
            result: DeleteResult = vectors.delete_many({})
            #print(result.deleted_count, " documents deleted.")
            return result
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def delete_one_vectors_by_id(vector_id: str) -> DeleteResult:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            vectors: collection = db.get_collection('vectors')
            result: DeleteResult = vectors.delete_one({'_id': ObjectId(vector_id)})
            #print(result.deleted_count, " documents deleted.")
            return result
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def delete_vectors_collection() -> None:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            #print(db.list_collection_names)
            db.drop_collection('vectors')
            #print(db.list_collection_names())
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def delete_log_entries_all() -> DeleteResult:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            result: DeleteResult = log_entries.delete_many({})
            #print(result.deleted_count, " documents deleted.")
            return result
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def delete_log_entries_collection() -> None:
        try:
            db: database = DatabaseInterface.client.get_database('pick_database')
            #print(db.list_collection_names)
            db.drop_collection('log_entries')
            #print(db.list_collection_names())
        except pymongo.errors.OperationFailure as e:
            print(e)
