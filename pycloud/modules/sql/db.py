import sqlite3
import sys
from sqlite3 import Error

db_file = "pycloud/pycloud.db"

def connect_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row
        
        return conn
    except Error as e:
        print("Unable to connect to database. Quitting...")
        sys.exit(1)


def create_db(conn):
    with open("pycloud/modules/sql/db_schema.sql") as f:
        schema = f.read()

        conn.executescript(schema)


conn = connect_db(db_file)
create_db(conn)


