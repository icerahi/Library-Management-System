from database import connect_to_db
import datetime
from utils import message, output_table



def borrow_book(book_id,borrower_id):
    conn=connect_to_db()
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO BORROW_RECORD (book_id,borrower_id,borrow_date) VALUES(?,?,?)",(
                book_id,borrower_id,datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            ))
        conn.commit()
    except Exception as e:
        conn.rollback()
        message(f"{e},Book id or borrower id not exist!","fail")
    conn.close()

def return_book():
    pass


#manage book
def add_book(title,genre,author_id,copies):
    conn=connect_to_db()
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO BOOKS (title,genre,author_id,copies) VALUES (?,?,?,?)",(
            title,genre,author_id,copies
        ))
        conn.commit()

        message(f"ID- '{cursor.lastrowid}', Title- '{title}' added!","success")

    except Exception as e:
        conn.rollback()
        message(f"{e}, 'author_id' doesn't exists!",'fail')
    conn.close()

def list_of_books():
    conn=connect_to_db()
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT * FROM BOOKS")
        books_list=cursor.fetchall()
   
        output_table("List of Books",["ID","Title","Genre","Author ID|Name","Available Copies"],
        books_list,cursor)
        

    except Exception as e:
        print(e)
    conn.close()



def update_book():
    pass 

def delete_book():
    pass 


#manage author
def add_author(name):
    conn=connect_to_db()
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO AUTHOR (name) VALUES (?)",(name,))
        conn.commit()
        message(f"ID- '{cursor.lastrowid}', Name- '{name}' added!","success")
    except Exception as e:
        print(e)
    conn.close()
    
def list_of_author():
    conn=connect_to_db()
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT * FROM AUTHOR")
        author_list=cursor.fetchall()
        output_table("List of Author",["ID","Name"],author_list)

    except Exception as e:
        print(e)
    conn.close()



def list_of_borrowers():
    pass 

def search_book():
    pass 





def add_borrower():
    pass
