import sqlite3
import sys
import hashlib
from bcrypt import gensalt
from .exceptions import usermanager_exceptions as exc
from .sql.db import conn
from .sql.users_sql import UserManagerSqlStatements as sql_stmt


class UserManager:
    def __init__(self, token_validity, global_token_block=0, allow_admin_creation=False):
        self._conn = conn
        self._token_valid_for = token_validity
        self._global_token_block = global_token_block
        self._allow_admin_creation = allow_admin_creation
        

    def _exit_program(self, error=None):
        if error is not None:
            print(f"{error}\nA fatal error has occured. Quitting ...")
            sys.exit(1)

        print("Quitting ...")
        sys.exit(0)


    def _check_if_user_exists(self, username):
        user = self._conn.db_execute(sql_stmt.get_user_id, (username,), fetch=1)
        if user is not None:
            return True

        return False


    def _hashed_password(self, password, salt):
        '''Hashes and returns the salted password'''
        hashed = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt.encode("utf-8"),
            100000
        )

        return hashed.hex()


    def _check_if_email_in_use(self, email):
        email_owner = self._conn.db_execute(sql_stmt.check_email, (email,), fetch=1)
        if email_owner is None:
            return False

        return True


    def create_user(self, username, password, email, disabled=False, fname=None, lname=None):
        if self._check_if_user_exists(username):
            raise exc.UserAlreadyExists(username)

        if self._check_if_email_in_use(email):
            raise exc.EmailAlreadyInUse(email)

        self._conn.db_execute(sql_stmt.create_user,
            (username, email, fname, lname, disabled,)
        )

        salt = gensalt().hex()
        hashed_password = self._hashed_password(password, salt)

        self._conn.db_execute(sql_stmt.register_password,
            (username, hashed_password, salt,)
        )


    def get_user(self, username):
        user = self._conn.db_execute(sql_stmt.get_user, (username,), fetch=1)

        if user is None:
            raise exc.UserDoesNotExist(username)

        return user


    def query_users(self, fname, lname, fetch):
        users = self._conn.db_execute(sql_stmt.query_users,
            (f"%{fname}%", f"%{lname}%"), fetch=fetch
        )

        return users


    def delete_user(self, username):
        if not self._check_if_user_exists(username):
            raise exc.UserDoesNotExist(username)

        self._conn.db_execute(sql.delete_user, (username,))