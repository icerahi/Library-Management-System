from prettytable import PrettyTable 
import re

#print message
def message(text,_type):
    symbol="~"
    _type_half_len=len(_type)/2

    border_length=len(text) + 4 #adding extra space
    top_border=f"{symbol * round((border_length/2)-_type_half_len)}{_type}{symbol*round((border_length/2)-_type_half_len)}"
    bottom_border=f"{symbol*border_length}"
    print
    print(top_border)
    print(f"{symbol} {text} {symbol}")
    print(bottom_border)
    print()
    print("``````````````````````````````")


#formatting output as table
def output_table(caption,column_list,data,cursor=None):
    table=PrettyTable()
    table.title=caption
    table.field_names=column_list
    for row in data:
        if cursor:
            cursor.execute("SELECT * FROM AUTHOR WHERE id=?",(row[3],))
            author=cursor.fetchone()
            temp_row=list(row) #not possible to modify tuple to converting to list and again to tuple
            temp_row[3]=f"{author[0]}|{author[1]}"
            modified_row=tuple(temp_row)
            table.add_row(modified_row)
        else:
            table.add_row(row)
    print(table)


def email_validation(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email) is not None
