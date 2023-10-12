import pyodbc as db
from dbutils import result_as_dict

def get_all_books(cursor:db.Cursor):
    query = 'SELECT * FROM BOOKS'
    cursor.execute(query)
    return result_as_dict(cursor)

def get_books_by_id(cursor:db.Cursor,id):
    query = 'SELECT * FROM BOOKS WHERE ID=?'
    cursor.execute(query, id)
    return result_as_dict(cursor)

def get_books_by_authorid(cursor:db.Cursor,a_id):
    query = 'select * from Books where author=?'
    cursor.execute(query,a_id)
    return result_as_dict(cursor)

def add_book(cursor:db.Cursor,isbn,title,a_id):
    query = 'INSERT INTO BOOKS (isbn, title,author) VALUES (?,?,?,?)'
    cursor.execute(query ,isbn,title,a_id)

def remove_book(cursor:db.Cursor,b_id):
    query = 'DELETE from Books where id=?'
    res = cursor.execute(query,b_id)
    return result_as_dict(res)

def get_book_review(cursor:db.Cursor,b_id):
    query = 'SELECT * FROM REVIEWS AS R JOIN BOOKS AS B ON R.BOOK_ID=B.ID WHERE B.ID=?'
    cursor.execute(query,b_id)
    return result_as_dict(cursor)

def add_book_review(cursor:db.Cursor,b_id,u_id,u_pass, rating,review_text):
    res = cursor.execute('SELECT * FROM USERS WHERE id=? and passord=?',u_id, u_pass)
    res = result_as_dict(res)
    if res:
        query = 'INSERT INTO REVIEWS(REVIEWER_ID, BOOK, DESCRIPTION, RATING) VALUES (?,?,?,?) '
        cursor.execute(query,u_id,b_id,review_text,rating)
    