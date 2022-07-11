'''SQL Statements related to user management'''

class UserManagerSqlStatements:
    create_user = '''
        INSERT INTO users (username, email, fname, lname, disabled)
        VALUES (?,?,?,?,?)
    '''
    
    get_user = '''
        SELECT *
        FROM users
        WHERE username=?
    '''

    query_users = '''
        SELECT *
        FROM users
        WHERE fname LIKE ?
        AND lname LIKE ?
    '''

    get_user_id = '''
        SELECT id FROM users WHERE username=?
    '''

    register_password = '''
        INSERT INTO passwords (user_id, hashed, salt)
        VALUES ((SELECT id FROM users WHERE username=?), ?, ?)
    '''

    delete_user = '''
        DELETE FROM users
        WHERE username=?
    '''

    check_email = '''
        SELECT id
        FROM users
        WHERE email=?
    '''