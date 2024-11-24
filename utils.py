from prettytable import PrettyTable 

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


#formatting output as table
def output_table(caption,column_list,data):
    table=PrettyTable()
    table.title=caption
    table.field_names=column_list
    for row in data:
        table.add_row(row)
    print(table)
