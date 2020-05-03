import sqlite3
from sqlite3 import Error
import pathlib as pl
import csv

null_type = 'null'
integer_type = 'integer'
real_type = 'real'
text_type = 'text'
blob_type = 'blob'
null_check = lambda i, l: -1 if (l[i] == '') else float(l[i])
sm_filepath = str(pl.Path(__file__).parent.absolute()) + '/sm/'


def create_connection(db_filename):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file (string filepath)
    :return: Connection object or None
    """
    db_filepath = sm_filepath + db_filename
    conn = None
    try:
        conn = sqlite3.connect(db_filepath)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, check_exists, table_name, columns_and_types):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    if check_exists is True:
        create_table_string = '''CREATE TABLE IF NOT EXISTS ''' + table_name + ''' ('''
    else:
        create_table_string = '''CREATE TABLE ''' + table_name + ''' ('''

    for cat in columns_and_types:
        create_table_string += cat[0] + sc.space_tq
        create_table_string += cat[1] + sc.comma_tq

    create_table_string = create_table_string[:-1]
    create_table_string += sc.close_parenthesis_tq

    try:
        cur = conn.cursor()
        cur.execute(create_table_string)
        cur.close()
        conn.commit()
        return True
    except Error as e:
        print(e)
    return False


def insert_into_table(cur, table_name, num_columns, insert_data):
    insert_into_table_string = '''INSERT INTO ''' + table_name + ''' VALUES ('''

    for i in range(num_columns):
        insert_into_table_string += sc.question_mark_tq
        insert_into_table_string += sc.comma_tq

    insert_into_table_string = insert_into_table_string[:-1]
    insert_into_table_string += sc.close_parenthesis_tq

    try:
        cur.execute(insert_into_table_string, insert_data)
    except Error as e:
        print(e)
    del insert_data


def sort_table(conn, table_name, column_name):
    cur = conn.cursor()
    sort_table_string = '''SELECT * FROM ''' + table_name + ''' ORDER BY ''' + column_name
    cur.execute(sort_table_string)
    cur.close()
    conn.commit()


def convert_csv_to_table(conn, csv_filenames, table_name):
    cur = conn.cursor()
    for csv_filename in csv_filenames:
        with open(sm_filepath + csv_filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                security_id_sm = -1 if (line[0] == '') else int(line[0])
                ticker_sm = str(line[1])
                figi_sm = str(line[2])
                composite_figi_sm = str(line[3])
                comp_ticker_sm = str(line[4])
                exch_ticker_sm = str(line[5])
                company_cik_sm = str(line[6])
                security_name_sm = str(line[7])
                date_sm = str(line[8])
                type_sm = str(line[9])
                frequency_sm = str(line[10])
                open_sm = null_check(11, line)
                high_sm = null_check(12, line)
                low_sm = null_check(13, line)
                close_sm = null_check(14, line)
                volume_sm = null_check(15, line)
                adj_open_sm = null_check(16, line)
                adj_high_sm = null_check(17, line)
                adj_low_sm = null_check(18, line)
                adj_close_sm = null_check(19, line)
                adj_volume_sm = null_check(20, line)
                adj_factor_sm = null_check(21, line)
                ex_dividend_sm = null_check(22, line)
                split_ratio_sm = null_check(23, line)

                stock_day_info = (security_id_sm, ticker_sm, figi_sm,
                                  composite_figi_sm, comp_ticker_sm, exch_ticker_sm,
                                  company_cik_sm, security_name_sm, date_sm,
                                  type_sm, frequency_sm, open_sm,
                                  high_sm, low_sm, close_sm,
                                  volume_sm, adj_open_sm, adj_high_sm,
                                  adj_low_sm, adj_close_sm, adj_volume_sm,
                                  adj_factor_sm, ex_dividend_sm, split_ratio_sm)

                insert_into_table(cur, table_name, 24, stock_day_info)
                del stock_day_info
    cur.close()
    conn.commit()
