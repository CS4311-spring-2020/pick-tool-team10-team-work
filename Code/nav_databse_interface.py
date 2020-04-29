import sqlite3
from sqlite3 import Error
import pathlib as pl


class NavDatabaseInterface:

    db_parent_filepath = str(pl.Path(__file__).parent.absolute()) + '/database_files/'
    db_filepath = str(pl.Path(__file__).parent.absolute()) + '/database_files/database.db'

    @staticmethod
    def create_db_conn():
        """

        :return:
        """
        conn = None
        try:
            conn = sqlite3.connect(NavDatabaseInterface.db_filepath)
            return conn
        except Error as e:
            print(e)
        return conn

    @staticmethod
    def create_logentry_col() -> bool:
        """

        :return:
        """
        conn = NavDatabaseInterface.create_db_conn()
        if conn is None:
            return False

        create_logentry_table_string = '''
        CREATE TABLE IF NOT EXISTS logentry_table (
        list_number INTEGER,
        timestamp TEXT,
        event TEXT,
        vector TEXT)
        '''
        try:
            cur = conn.cursor()
            cur.execute(create_logentry_table_string)
            cur.close()
            conn.commit()
            conn.close()
            return True
        except Error as e:
            print(e)
        return False

    @staticmethod
    def create_timefilter_table() -> bool:
        """

        :return:
        """
        conn = NavDatabaseInterface.create_db_conn()
        if conn is None:
            return False

        create_timefilter_table_string = '''
        CREATE TABLE IF NOT EXISTS timefilter_table (
        name TEXT,
        start_time TEXT,
        end_time TEXT,
        uid TEXT)
        '''
        try:
            cur = conn.cursor()
            cur.execute(create_timefilter_table_string)
            cur.close()
            conn.commit()
            conn.close()
            return True
        except Error as e:
            print(e)
        return False

    @staticmethod
    def insert_timefilter_item(uid: str, name: str, start_time: str, end_time: str) -> bool:
        """

        :param uid:
        :param name:
        :param start_time:
        :param end_time:
        :return:
        """
        conn = NavDatabaseInterface.create_db_conn()
        if conn is None:
            return False

        insert_timefilter_data = (name, start_time, end_time, uid)
        insert_timefilter_query = '''
        INSERT INTO timefilter_table 
        (name, start_time, end_time, uid)
        VALUES 
        (?, ?, ?, ?)
        '''

        try:
            cur = conn.cursor()
            cur.execute(insert_timefilter_query, insert_timefilter_data)
            cur.close()
            conn.commit()
            conn.close()
            return True
        except Error as e:
            print(e)
        return False


    @staticmethod
    def update_timefilter_item(uid: str, name: str = None, start_time: str = None, end_time: str = None) -> bool:
        """

        :param uid:
        :param name:
        :param start_time:
        :param end_time:
        :return:
        """
        conn = NavDatabaseInterface.create_db_conn()
        if conn is None:
            return False

        update_timefilter_data = []
        update_timefilter_query = '''UPDATE timefilter_table SET'''

        if name is not None:
            update_timefilter_query += ''' name = ?,'''
            update_timefilter_data.append(name)
        if start_time is not None:
            update_timefilter_query += ''' start_time = ?,'''
            update_timefilter_data.append(start_time)
        if end_time is not None:
            update_timefilter_query += ''' end_time = ?,'''
            update_timefilter_data.append(end_time)

        update_timefilter_query = update_timefilter_query[:-1]
        update_timefilter_query += ''' WHERE uid = ?'''
        update_timefilter_data.append(uid)
        update_timefilter_data = tuple(update_timefilter_data)

        try:
            cur = conn.cursor()
            cur.execute(update_timefilter_query, update_timefilter_data)
            cur.close()
            conn.commit()
            conn.close()
            return True
        except Error as e:
            print(e)
        return False

    @staticmethod
    def select_timefilter_one_item(uid: str) -> tuple:
        conn = NavDatabaseInterface.create_db_conn()
        if conn is None:
            return False

        print("awef")

    @staticmethod
    def select_timefilter_all_items() -> list:
        conn = NavDatabaseInterface.create_db_conn()
        if conn is None:
            return False

        print("awerf")

