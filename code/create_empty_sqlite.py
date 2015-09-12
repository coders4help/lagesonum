__author__ = 'f.zesch'

# create tables in an empty SQLite database for later use

import sqlite3
import MySQLdb as mdb
import sys

def create_tables(db_con):
    """
    Intializes all necessary tables, run only first time
    :param db_con:
    :return:
    """

    PLACE_INIT_DATA = ("LAGESO", "Helper", "^[a-zA-Z]{1,1}[0-9]+$", 1, 99)
    USER_INIT_DATA = ("Helper", "1234", 0)



    INPUT_TABLES = {
    "PLACES" : {"PLACE": "VARCHAR(20)",
                "USER": "VARCHAR(10)",
                "VALREGEXP": "VARCHAR(99)",
                "MIN_LENGTH": "INTEGER",
                "MAX_LENGTH": "INTEGER"}


    "USERS" : { "USER": "VARCHAR(10)",
                "PW": "VARCHAR(20)",
                "ISADMIN": "BOOLEAN"}

    "NUMBERS" : {"NUMBER": "VARCHAR(30)",
                "TIME": "TIMESTAMP",
                "PLACE": "VARCHAR(20)",
                "USER": "VARCHAR(10)"}

    }


    try:
        con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

        with con:

            cur = con.cursor()

            # create all tables in loop
            for key in INPUT_TABLES:

                # concat field names and data types for creation string
                sql_string = "CREATE TABLE " + key + "(" + \
                             " ".join(
                                 [" ".join([subkey, INPUT_TABLES[key][subkey]])+"," for subkey in INPUT_TABLES[key]]
                             )[:-2]+ \
                             ")"
                # run
                cur.execute(sql_string)

            # initial record for location and user
            cur.execute("INSERT INTO PLACES(PLACE, USER, VALREGEXP, MIN_LENGTH, MAX_LENGTH) VALUES (PLACE_INIT_DATA)")
            cur.execute("INSERT INTO USERS(USER, PW, ISADMIN) VALUES (USER_INIT_DATA)")

    except mdb.Error as e:
        print("Error %d: %s" % (e.args[0],e.args[1]))
        sys.exit(1)

    finally:

        if con:
            con.close()
