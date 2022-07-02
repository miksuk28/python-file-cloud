class UserManagerSqlStatements:
    check_if_user_exists = '''
        SELECT if FROM users WHERE username=%s
    '''