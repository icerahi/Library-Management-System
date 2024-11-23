import sqlite3
from tables import *

def connect_to_db():
    return sqlite3.connect('data.db')

def create_tables():
    connection=connect_to_db()
    cursor=connection.cursor()

    cursor.execute(CREATE_AUTHOR_TABLE)
    cursor.execute(CREATE_BOOKS_TABLE)
    cursor.execute(CREATE_BORROWER_TABLE)
    cursor.execute(CREATE_BORROW_RECORD_TABLE)

    connection.commit()
    connection.close()

 