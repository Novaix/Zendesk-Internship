import display_ticket, display_ticket_list, zendesk_interface, io_process
import sys

#As per https://develop.zendesk.com/hc/en-us/articles/360001074168-Making-requests-to-the-Zendesk-API
#we have the basic structure of how requests to the API are formed

def main():
	#nested function that prompts a new get request for an updated list
	#as opposed to using the old one
	def refresh_tickets(page):
		nonlocal tickets
		tickets=None
		return page

	login=io_process.get_authentication()
	page=1
	tickets=None

	#this is kept in main to avoid having to pass variables (for readability)
	#
	#implemented as a dict of lambda functions to ensure there will never be
	#a 'legal input' with no corresponding function, or vice-versa
	#
	#all functions can't take more or less than one input
	#(as they're all called with one input)
	#and all functions must return a page number (for the next display)
	commands={
	"j":lambda page: io_process.get_number("Enter the page to jump to: ",page_max),
	"v":lambda page: view_ticket(page,login,len(tickets)),
	"n":lambda page: (page%page_max)+1,
	"p":lambda page: ((page-2)%page_max)+1,
	"q":lambda page: sys.exit(),
	"r":lambda page: refresh_tickets(page)
	}

	#input loop
	while(True):
		#get new list if it needs updating
		if(tickets==None):
			tickets=zendesk_interface.get_ticket_list(*login)

		#display list of tickets
		page_max=display_ticket_list.display_ticket_list(page,tickets)

		#get a command from user
		command=io_process.get_command(commands.keys())
		#execude command AND update page as necessary
		page=commands[command](page)

#display individual ticket details
def view_ticket(return_page,login,ticket_max):
	ticket_id=io_process.get_number("Enter the id of the ticket to view: ",ticket_max)

	ticket=zendesk_interface.get_ticket(*login,str(ticket_id))

	display_ticket.display_ticket(ticket)
	#ignores input, just serves to wait for user
	input("Press enter to return to the list of tickets.")
	return return_page

if __name__ == "__main__":
	main()