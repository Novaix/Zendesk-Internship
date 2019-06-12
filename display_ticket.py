#display individual ticket
#inelegant, but universal and legible; prints ticket in appropriate format
def display_ticket(ticket):
    #ensure columns are aligned neatly
    longest_field = 0
    for field in ticket.keys():
        if len(field) > longest_field:
            longest_field = len(field)
    #print every valid field in the ticket and its corresponding value
    print("")
    for field,entry in ticket.items():
        print("{0:{2}}: {1}".format(field,str(entry),longest_field+1))