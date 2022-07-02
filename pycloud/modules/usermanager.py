import sqlite3
import sys
from .exceptions import usermanager_exceptions as exc
from .sql.db import conn
from .sql.users_sql import UserManagerSqlStatements as sql_stmt


class UserManager:
    def __init__(self):
        self._conn = conn
        

    def _exit_program(self, error=None):
        if error is not None:
            print(f"{error}\nA fatal error has occured. Quitting ...")
            sys.exit(1)

        print("Quitting ...")
        sys.exit(0)


    def _check_if_user_exists(self, username):
        cur = self._conn.cursor()
        cur.execute("SELECT id FROM users WHERE username=%s", username)
        result = cur.fetchone()

        if result is None:
            return False

        return True


    def _db_execute(self, sql, params, commit=True, fetch=1):
        cur = self._conn.cursor()
        cur.execute(sql, params)
        if commit:
            self._conn.commit()

        if fetch == 1:
            return cur.fetchone()
        elif not fetch:
            return 
        
        return cur.fetchmany(fetch)


    def create_user(self, username, password=None, disabled=False, fname=None, lname=None):
        if self._check_if_user_exists(username):
            raise exc.UserAlreadyExists(username)

        self._db_execute("INSERT INTO users (", params)