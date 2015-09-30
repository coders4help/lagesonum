import datetime
import sqlite3


def reset_all_timestamps_to_now(path):

    db = sqlite3.connect(path)
    cur = db.cursor()

    print("SQLite db contains following columns in table numbers")
    tnames = cur.execute("PRAGMA TABLE_INFO('numbers') ")

    print([ta for _ , ta, _ , _, _, _ in tnames])

    print("++++++ OLD TIMESTAMPS +++++++")
    select_sql_str = 'SELECT * FROM numbers ORDER by time'
    print(select_sql_str)
    old_t = cur.execute(select_sql_str )
    print([t for t in old_t])

    print("replacing...")

    new_time = datetime.datetime.now()
    values = (new_time,)

    sql_str = 'UPDATE numbers SET time = ?'
    print(sql_str[:-1] + str(new_time))
    repl = cur.execute(sql_str, values).fetchall()
    db.commit()

    print("++++++ NEW TIMESTAMPS +++++++")
    print(select_sql_str)
    new_t = cur.execute(select_sql_str )
    print([t for t in new_t])

    print("Done")
    db.close()

if __name__ == '__main__':

    reset_all_timestamps_to_now('lagesonr.db')

