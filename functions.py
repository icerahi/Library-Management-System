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



def update_book(title,genre,author_id,copies,id):
    conn=connect_to_db()
    cursor=conn.cursor()
    try:
        cursor.execute("""UPDATE BOOKS SET 
        title=COALESCE(NULLIF(?,""),title),
        genre=COALESCE(NULLIF(?,""),genre),
        author_id=COALESCE(NULLIF(?,""),author_id),
        copies=COALESCE(NULLIF(?,""),copies)
        WHERE id=?""",(title,genre,author_id,copies,id))

        conn.commit()

        message(f"""ID- '{id}' Book updated!""","Success")

    except Exception as e:
        conn.rollback()
        message(e,"fail")
    conn.close()

def delete_book(id):
    conn=connect_to_db()
    cursor=conn.cursor()

    try:
        cursor.execute("DELETE FROM BOOKS WHERE id=?",(id,))
        conn.commit()
        message(f"""ID- '{id}' Book deleted!""","Success")

    except Exception as e:
        conn.rollback()
        message(e,"fail")
    conn.close()

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




def add_borrower(name,email):
    conn=connect_to_db()
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO BORROWER (name,email) VALUES(?,?)",(name,email))
        conn.commit()
        message(f"ID-{cursor.lastrowid},Name-{name}, Email-{email} added!","success")
    except Exception as e:
        conn.rollback()
        message(e,"fail")
    conn.close()

def list_of_borrowers():
    conn=connect_to_db()
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT * FROM BORROWER")
        borrower_list=cursor.fetchall()
        output_table("List of Borrower",["ID","Name","Email"],borrower_list)
    except Exception as e:
            print(e)
    conn.close()


def search_book():
    pass 





