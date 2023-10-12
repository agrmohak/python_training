from dbutils import result_as_dict

def get_all_users(cursor):
    res = cursor.execute('SELECT ID, NAME, EMAIL from USERS')
    return result_as_dict(res)
    
def add_new_user(cursor,name,email, password):
    cursor.execute('INSERT INTO USERS (name,email,password) values (?,?,?)',name,email,password)

def get_user_review(cursor,user_id):
    res = cursor.execute('SELECT * FROM REVIEWS WHERE REVIEWER_ID = ?',user_id)
    return result_as_dict(res)