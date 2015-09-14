# coding: utf-8

# create tables in an empty SQLite database for later use

import sqlite3


def create_tables(con):
    """
    Intializes all necessary tables, run only first time
    :param db_con:
    :return:
    """

    INPUT_TABLES = {
        "PLACES": {"PLACE": "VARCHAR(20)",
                   "USER": "VARCHAR(10)",
                   "VALREGEXP": "VARCHAR(99)",
                   "MIN_LENGTH": "INTEGER",
                   "MAX_LENGTH": "INTEGER"},

        "USERS": {"USER": "VARCHAR(10)",
                  "PW": "VARCHAR(20)",
                  "ISADMIN": "BOOLEAN"},

        "NUMBERS": {"NUMBER": "VARCHAR(30)",
                    "TIME": "TIMESTAMP",
                    "PLACE": "VARCHAR(20)",
                    "USER": "VARCHAR(10)",
                    "FINGERPRINT": "VARCHAR(32)"}

    }

    with con:

        cur = con.cursor()

       # create all tables in loop
        for key in INPUT_TABLES:

            # concat field names and data types for creation string
            sql_string = "CREATE TABLE " + key + "(" + \
                         " ".join(
                             [" ".join([subkey, INPUT_TABLES[key][subkey]])+"," for subkey in INPUT_TABLES[key]]
                         )[:-1]+ \
                         ")"
            # run
            print(sql_string)
            try:
                cur.execute(sql_string)
                print("Success: ", sql_string)
            except sqlite3.OperationalError as e:
                print(e)

        # write initial record for location and user
        LOC_STRING = 'INSERT INTO PLACES(PLACE, USER, VALREGEXP, MIN_LENGTH, MAX_LENGTH) VALUES ("LAGESO", "Helper", "^[a-zA-Z]{1,1}[0-9]+$", 1, 99)'
        USR_STRING = 'INSERT INTO USERS(USER, PW, ISADMIN) VALUES ("Helper", "1234", "-")'
        NUM_STRING = 'INSERT INTO NUMBERS(NUMBER, TIME; PLACE, USER, FINGERPRINT) VALUES ("00000", "-", "DB", "-", "-")'

        for s in [LOC_STRING, NUM_STRING, USR_STRING]:
            try:
                cur.execute(s)
                print("Success: ", s)
            except sqlite3.OperationalError as e:
                print(e)


def initialize_database(path):
    print('Initializing sqlite3 database at {}'.format(path))
    lagesonrdb = sqlite3.connect(path)
    create_tables(lagesonrdb)

    cur = lagesonrdb.cursor()

    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

    rows = cur.fetchall()

    for row in rows:
        print (row[0])

    lagesonrdb.close()
    print('Database initialized.')


if __name__ == '__main__':

    initialize_database('lagesonr.db')
