import menus
from functions import (
    borrow_book,
    add_author,
    list_of_author,)


def main():
    while True:
        print(menus.MENU)
        option=int(input())

        if option == 1 :
            book_id=int(input())
            borrow_book(1,1)
            print ("Borrow Book")
        elif option == 2 :
            print("Return Book")
        elif option ==3:
            print("List of Books")
        
        elif option==4:
            list_of_author()

        elif option ==5:
            print("List of borrowers")

        elif option==6:
            print("search book")

        elif option == 7:
            while True:
                option=int(input(menus.SUB_MENU_MANAGE_BOOK))
                if option ==1:
                    print("add a single book")
                elif option==2:
                    print("add a list of book")
                elif option ==3:
                    print('Update a book')
                elif option ==4:
                    print("delete a book")
                elif option ==0:
                    break
                else:
                    print("Invalid choice!")
                print("_____________________________")

        elif option ==8:
           
            name= str(input("Enter an Author Name or List:"))
            add_author(name)
               
            print("_____________________________")

        elif option ==9:
            print("add a new borrower")

        elif option==0:
            break 
        else:
            print("Invalid selection!!")
        print('_______________________________________________________________')

main()