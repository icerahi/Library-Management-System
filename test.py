import sqlite3

def connect_to_database():
    conn=sqlite3.connect('test.db')
    return conn 


def create_table():
    conn=connect_to_database()
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        publisher TEXT
        year_of_publication INTEGER
    )""")
    conn.commit()
    conn.close()

create_table()


#write a function for users to add new books

def add_book(title,author,publisher,year_of_publication):
    conn=connect_to_database()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO books (title,author,publisher,year_of_publication) VALUES(?,?,?,?)",
                    title,author,publisher,year_of_publication)
    conn.commit()
    conn.close()


