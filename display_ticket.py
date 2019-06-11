import zendesk_interface

#display individual ticket
def display_ticket(id,login):
	#get new ticket, in case it was updated
	ticket=get_ticket(id,*login)["ticket"]
	print("\n")
	print_ticket(ticket)

#inelegant, but universal and legible; prints ticket in appropriate format
def print_ticket(ticket):
	#ensure columns are aligned neatly
	longest_field=0
	for field in ticket.keys():
		if len(field)>longest_field:
			longest_field=len(field)
	#print every valid field in the ticket and its corresponding value
	for field,entry in ticket.items():
		print("{0:{2}}: {1}".format(field,str(entry),longest_field+1))

#get requests an individual ticket
def get_ticket(id,url,user,pwd):
	return zendesk_interface.get_json(url+'/'+str(id)+'.json',user,pwd)