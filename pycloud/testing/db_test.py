import sqlite3
from sqlite3 import Error
import os

print(f"Current Working Dir: {os.getcwd()}")

def connect_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row

        return conn
    except Error as e:
        print(e)
        print("\nUnable to connect to database. Quitting...")
        sys.exit(1)


def create_db(conn):
    with open("../modules/sql/db_schema.sql") as f:
        schema = f.read()

        conn.executescript(schema)


conn = connect_db("test.db")
create_db(conn)


def list_and_dictify(list):
    new_list = []
    for row in list:
        new_list.append(dict(row))

    return new_list


def db_execute(sql, params=(), commit=True, fetch=None, return_dict=True):
    cur = conn.cursor()
    cur.execute(sql, params)
    if commit:
        conn.commit()

    if fetch == "all":
        return list_and_dictify(cur.fetchall())
    elif fetch == 1:
        return dict(cur.fetchone())
    elif not fetch:
        return

    return list_and_dictify(cur.fetchmany(fetch))
