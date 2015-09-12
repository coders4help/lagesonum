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

    LOCATIONS = ["LAGESO"]
    USERS = ["Helper"]
    PW = ["1234"]

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

            for key in INPUT_TABLES:

                sql_string = "CREATE TABLE " + key + "(" + \
                             " ".join("") + \
                             ")"
                cur.execute(sql_string)


    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:

        if con:
            con.close()
