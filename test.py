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
        publisher TEXT,
        year_of_publication INTEGER
    )""")
    conn.commit()
    conn.close()

create_table()


#write a function for users to add new books

def add_book(title,author,publisher,year_of_publication):
    conn=connect_to_database()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO books (title,author,publisher,year_of_publication) VALUES (?, ?, ?, ?)",
                    (title,author,publisher,year_of_publication))
    conn.commit()
    conn.close()


def list_books():
    conn=connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books= cursor.fetchall()

    for book in books:
        print(book)
    conn.close()


def menu():
    while True:
        print("\n\t Libaray Management System")
        print("1- Add Book")
        print("2- List Book")
        print("3- Update Book")
        print("4- Delete Book")
        print("5- Exit")

        choice= int(input("ENter your choice: "))

        if choice == 1:
            title =input("New title:")
            author=input("New author:")
            publisher=input("New publisher")
            year_of_publication=input("New year of publication:")
            add_book(title,author,publisher,year_of_publication)
           

        elif choice == 2:
            list_books()

        elif choice == 3:
            id =int(input("ID of the book to update: "))
            title =input("New title:")
            author=input("New author:")
            publisher=input("New publisher")
            year_of_publication=input("New year of publication:")
            update_book(id,title,author,publisher,year_of_publication)

        elif choice== 4:
            id=int(input("ID of the book to delete"))
            delete_book(id)
        
        elif choice== 5:
            break
        else:
            print("Invalid choice")




menu()