import database 
import menus



def main():
    while True:
        print(menus.MENU)
        option=int(input())

        if option == 1 :
            print ("Borrow Book")
        elif option == 2 :
            print("Return Book")
        elif option ==3:
            print("List of Books")
        elif option == 4:
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
        elif option==5:
            print("list of author")

        elif option ==6:
            while True:
                print(menus.SUB_MENU_MANAGE_AUTHOR)
                option=int(input())
                if option ==1:
                    print("add an author")
                elif option==2:
                    print("add a list of author")
                elif option ==0:
                    break
                else:
                    print("Invalid choice!")
        elif option ==7:
            print("add a new borrower")
        elif option ==8:
            print("List of borrowers")
        elif option==9:
            print("search book")
        elif option==0:
            break 
        else:
            print("Invalid selection!!")
        print('_______________________________________________________________')

main()