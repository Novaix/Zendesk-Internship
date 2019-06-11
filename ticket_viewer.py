import display_ticket
import display_tickets
import sys

def main():
	#As per https://develop.zendesk.com/hc/en-us/articles/360001074168-Making-requests-to-the-Zendesk-API
	#we have the basic structure of how requests to the API are formed
	
	login=get_authentication()

	page=1

	#kept in main to avoid having to pass variables
	#implemented as a dict of lambda functions to ensure there will never be
	#a 'legal input' with no corresponding function, or vice-versa
	commands={
	"j":lambda page: get_number("Enter the page to jump to: ",page_max),
	"v":lambda page: view_ticket(page,login),
	"n":lambda page: (page%page_max)+1,
	"p":lambda page: ((page-2)%page_max)+1,
	"q":lambda page: sys.exit()
	}

	#input loop
	while(True):
		page_max=display_tickets.display_tickets(page,login)
		command=get_command(commands.keys())
		page=commands[command](page)

def view_ticket(return_page,login):
	ticket_id=get_number("Enter the id of the ticket to view: ")
	display_ticket.display_ticket(ticket_id,login)
	input("Press enter to return to the list of tickets.")
	return return_page


def get_command(legal_commands):
	command=""
	while(command not in legal_commands):
		command=input()
	return command


def get_number(prompt,max_=float('inf')):
	while(True):
		output=input(prompt)
		try:
			output=int(output)
			if (output<1) or (output>max_):
				print(str(output)+" is not a valid number (too big or too small).")
				continue
		except ValueError:
			print(str(output)+" is not a number.")
			continue
		return output


#Get authentication details and base url from file
def get_authentication():
	authentication=open("authentication.txt","r")
	user = authentication.readline()[:-1]
	pwd = authentication.readline()[:-1]
	#can append '.json' for all tickets, '/{id}.json' for individual ticket
	url = authentication.readline()+'/api/v2/tickets'

	return (url,user,pwd)


main()