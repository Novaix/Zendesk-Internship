import zendesk_interface

#display list of tickets, with pages
def display_tickets(page,login,tickets):
	#get new list if it needs updating
	if tickets==None:
		tickets=get_tickets(*login)["tickets"]
	page_max=1+len(tickets)//25
	#print column headers; assumed max ID of 1,000,000,000
	#(every other field is bounded automatically except the last)
	print("\n{:11}{:9}{:10}{:8}{:11}{:11}{:11}{}".format(
		"ID:",
		"Type:",
		"Priority:",
		"Status:",
		"Created:",
		"Updated:",
		"Due:",
		"Subject/Tags:"))

	print_tickets(tickets,page)

	#print page marker
	print("Page {}/{}".format(page,page_max))
	print("\n'n' for next page, 'p' for previous page, 'j' to jump to a page,"
		 "'v' to view a ticket, 'r' to refresh list of tickets, 'q' to quit.")
	#returning page_max lets the ticket_viewer wrap around correctly
	#and tickets to prevent bad API requests and prevent needing to constantly
	#make requests
	return (page_max,tickets)

def print_tickets(tickets,page):
	for ticket in tickets[25*(page-1):25*(page-1)+25]:
		subject=ticket.get("subject","")
		if subject=="":
			subject="Missing"
		else:
			subject="\""+subject+"\""

		print("{:11}{:9}{:10}{:8}{:11.10}{:11.10}{:11.10}{}  {}".format(
			str(ticket.get("id","Missing")),
			str(ticket.get("type","Missing")),
			str(ticket.get("priority","Missing")),
			str(ticket.get("status","Missing")),
			str(ticket.get("created_at","Missing")),
			str(ticket.get("updated_at","Missing")),
			str(ticket.get("due_at","Missing")),
			str(subject),
			str(ticket.get("tags","Missing"))))

#get requests the list of all tickets
def get_tickets(url,user,pwd):
	tickets=zendesk_interface.get_json(url+'.json',user,pwd)
	
	#if there is more than one API-side page of tickets
	#append new pages to ticket list and update next page until finished
	while (tickets["next_page"]!=None):
		more_tickets=zendesk_interface.get_json(tickets["next_page"],user,pwd)
		tickets["tickets"]+=more_tickets["tickets"]
		tickets["next_page"]=more_tickets["next_page"]
	return tickets