import zendesk_interface

#display list of tickets, with pages
def display_tickets(page,login):
	tickets=get_tickets(*login)["tickets"]
	page_max=1+len(tickets)//25
	# display tickets; assumed max ID of 1,000,000,000
	print("\n{:11}{:9}{:9}{:8}{:11}{:11}{:11}{}".format("ID:","Type:",
		"Priority:","Status:","Created:","Updated:","Due:","Subject/Tags:"))
	for ticket in tickets[25*(page-1):25*(page-1)+25]:
		print("{:11}{:9}{:9}{:8}{:11.10}{:11.10}{:11.10}\"{}\"; {}".format(str(ticket["id"]),
			str(ticket["type"]),str(ticket["priority"]),str(ticket["status"]),
			str(ticket["created_at"]),str(ticket["updated_at"]),
			str(ticket["due_at"]),str(ticket["subject"]),str(ticket["tags"])))
	print("Page {}/{}".format(page,page_max))
	print("\n'n' for next page, 'p' for previous page, 'j' to jump to a page,"
		 "'v' to view a ticket, 'q' to quit.")
	#returning this lets the ticket_viewer wrap around correctly
	return page_max

def get_tickets(url,user,pwd):
	#get tickets
	tickets=zendesk_interface.get_json(url+'.json',user,pwd)

	#the response comes in the form of a dict
	#with "next_page" as a key and a url as its value
	#and "tickets" as another key with a list of dicts as its value
	
	#if there is more than one API-side page of tickets
	#append new pages to ticket list and update next page until finished
	while (tickets["next_page"]!=None):
		more_tickets=zendesk_interface.get_json(tickets["next_page"],user,pwd)
		tickets["tickets"]+=more_tickets["tickets"]
		tickets["next_page"]=more_tickets["next_page"]
	return tickets