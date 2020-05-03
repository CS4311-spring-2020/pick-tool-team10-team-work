
import pathlib as pl
import pymongo
from pymongo import MongoClient, collection, cursor, database, errors
from pymongo.results import InsertOneResult, DeleteResult, InsertManyResult


class NavDatabaseInterface:
    db_parent_filepath = str(pl.Path(__file__).parent.absolute()) + '/database_files/'
    db_filepath = str(pl.Path(__file__).parent.absolute()) + '/database_files/database.db'
    client = MongoClient('mongodb://localhost:27017/')

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
            db: database = NavDatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            result: InsertOneResult = log_entries.insert_one(log_entry_item)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def insert_many_log_entries(log_entries_items: list) -> None:
        try:
            db: database = NavDatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            result: InsertManyResult = log_entries.insert_many(log_entries_items)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def find_all_log_entries() -> list:
        try:
            db: database = NavDatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            query_result: cursor = log_entries.find()
            return list(query_result)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def find_log_entries_condition(conditions: list) -> list:
        try:
            db: database = NavDatabaseInterface.client.get_database('pick_database')
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
            db: database = NavDatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            query = {}
            if regex_search is not None and len(regex_search) != 0:
                query = {'event': {'$regex': regex_search}}
            query_result: cursor = log_entries.find(query)
            return list(query_result)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def find_all_log_entries_return_vectors() -> list:
        try:
            db: database = NavDatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            query_result: cursor = log_entries.find({}, {'vector': 1})
            return list(query_result)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def find_all_log_entries_return_locations() -> list:
        try:
            db: database = NavDatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            query_result: cursor = log_entries.find({}, {'location': 1})
            return list(query_result)
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def delete_all_items_log_entries() -> None:
        try:
            db: database = NavDatabaseInterface.client.get_database('pick_database')
            log_entries: collection = db.get_collection('log_entries')
            x: DeleteResult = log_entries.delete_many({})
            print(x.deleted_count, " documents deleted.")
        except pymongo.errors.OperationFailure as e:
            print(e)

    @staticmethod
    def delete_log_entries_collection() -> None:
        try:
            db: database = NavDatabaseInterface.client.get_database('pick_database')
            print(db.list_collection_names)
            db.drop_collection('log_entries')
            print(db.list_collection_names())
        except pymongo.errors.OperationFailure as e:
            print(e)
