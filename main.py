import menus
from utils import email_validation
from functions import (
    borrow_book,
    add_author,
    list_of_author,
    add_book,
    list_of_books,
    update_book,
    delete_book,
    list_of_borrowers,
    add_borrower,
    borrow_records,
    )


def main():
    while True:
        print(menus.MENU)
        option=int(input())

        if option ==1:
            borrow_records()
            
        elif option == 2 :
            book_id=int(input("Enter the book ID want to Borrow:"))
            borrower_id=int(input("Enter the Borrower ID:"))
            borrow_book(book_id,borrower_id)
        elif option == 3 :
            print("Return Book")
        elif option ==4:
            list_of_books()
        
        elif option==5:
            list_of_author()

        elif option ==6:
            list_of_borrowers()

        elif option==7:
            print("search book")

        elif option == 8:
            while True:
                option=int(input(menus.SUB_MENU_MANAGE_BOOK))
                if option ==1:
                    title=input("Enter Book Title:")
                    genre=input("Enter Book Genre:")
                    author_id=int(input('Enter Author ID:')) 
                    copies=int(input("Enter Number of Copies:"))
                    add_book(title,genre,author_id,copies)
                    
                elif option ==2:
                    id=int(input("Enter ID which book details you want to update:"))
                    print("If you don't want to change leave it Empty!")
                    title=input("Title:")
                    genre=input("Genre:")
                    author_id=input("Author ID:")
                    copies=input("Available Copies:")
                    update_book(title,genre,author_id,copies,id)
                    break

                elif option ==3:
                    id=input("Enter the Book ID which you want to Deleted: ")
                    if id:
                        delete_book(id)
                        
                elif option ==0:
                    break
                else:
                    print("Invalid choice!")
                print("_____________________________")

        elif option ==9:
           
            name= str(input("Enter an Author Name or List:"))
            add_author(name)
               
        elif option ==10:
            name=input("Enter Borrower Name:")
            while True:
                email=input("Enter valid Email:")
                if email_validation(email):
                    add_borrower(name,email)
                    break

        elif option==0:
            break 
        else:
            print("Invalid selection!!")

    

main()