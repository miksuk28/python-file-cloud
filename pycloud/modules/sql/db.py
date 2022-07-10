import sys
import sqlite3
from sqlite3 import Error


class DatabaseWrapper:
    def __init__(self, db_file, schema_location):
        self._db_file = db_file
        self._schema = schema_location
        self.conn = self._connect_to_db()

        # Make sure database schema is correct
        self._create_db()


    def _connect_to_db(self):
        try:
            conn = sqlite3.connect(self._db_file, check_same_thread=False)
            conn.row_factory = sqlite3.Row

            return conn
        except Error as e:
            print(f"{e}\n\nFatal Error occured: Unable to connect to database. Quitting ...")
            sys.exit(1)


    def _create_db(self):
        with open(self._schema, "r") as f:
            schema = f.read()
            self.conn.executescript(schema)


    def list_and_dictify(self, list):
        new_list = []
        for row in list:
            new_list.append(dict(row))

        return new_list


    def db_execute(self, sql, params=(), commit=True, fetch=None):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        if commit:
            self.conn.commit()


        if fetch == "all":
            result = cur.fetchall()
            if result is not None:
                return self.list_and_dictify(result)

            return
        elif fetch == 1:
            result = cur.fetchone()
            if result is not None:
                return dict(result)
            
            return
        elif not fetch:
            return 

        return self.list_and_dictify(cur.fetchmany(fetch))


# To be imported by other modules that need DB access
conn = DatabaseWrapper("pycloud.db", "modules/sql/db_schema.sql")