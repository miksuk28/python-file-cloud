'''SQL Statements related to user management'''

class UserManagerSqlStatements:
    create_user = '''
        INSERT INTO users (username, fname, lname, disabled)
        VALUES (?,?,?,?)
    '''
    
    get_user_id = '''
        SELECT id FROM users WHERE username=?
    '''

    register_password = '''
        INSERT INTO passwords (user_id, hashed, salt)
        VALUES ((SELECT id FROM users WHERE username=?), ?, ?)
    '''