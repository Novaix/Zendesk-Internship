#display list of tickets, with pages
def display_ticket_list(page,tickets):
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

	print_ticket_list(tickets,page)

	#print page marker
	print("Page {}/{}".format(page,page_max))
	print("\n'n' for next page, 'p' for previous page, 'j' to jump to a page,"
		 "'v' to view a ticket, 'r' to refresh list of tickets, 'q' to quit.")
	#returning page_max lets the ticket_viewer wrap around correctly
	#and tickets to prevent bad API requests and prevent needing to constantly
	#make requests
	return page_max

def print_ticket_list(tickets,page):
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