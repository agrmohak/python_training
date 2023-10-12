import pyodbc as db
import dbutils
def add_author(cursor:db.Cursor, name, bio ):
    query = 'INSERT INTO AUTHORS(name, bio) VALUES(?,?)'
    cursor.execute(query, name, bio)

def remove_author(cursor:db.Cursor, author_id):
    query = 'DELETE FROM AUTHORS WHERE id = ?'
    res = cursor.execute(query, author_id)
    return dbutils.result_as_dict(res)

def get_all_authors(cursor:db.Cursor): 
    query = 'SELECT * FROM AUTHORS'
    res = cursor.execute(query)
    return dbutils.result_as_dict(res)
def get_author_by_id(cursor:db.Cursor, id):
    query = 'SELECT * FROM AUTHORS WHERE ID=?'
    res = cursor.execute(query, id)
    return dbutils.result_as_dict(res)

# def update_author():
#     pass 

# def get_author_reviews():
#     query = '''SELECT * FROM '''
#     pass 