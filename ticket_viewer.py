import display_ticket
import display_tickets

def main():
	#As per https://develop.zendesk.com/hc/en-us/articles/360001074168-Making-requests-to-the-Zendesk-API
	#we have the basic structure of how requests to the API are formed

	#Get authentication details and base url from file
	authentication=open("authentication.txt","r")
	user = authentication.readline()[:-1]
	pwd = authentication.readline()[:-1]
	#can append '.json' for all tickets, '/{id}.json' for individual ticket
	url = authentication.readline()+'/api/v2/tickets'

	login=(url,user,pwd)

	page=1

	#input loop
	while(True):
		page_max=display_tickets.display_tickets(page,login)
		command=get_command()
		if command=="j":
			page=get_number("Enter the page to jump to: ")
		elif command=="v":
			ticket_id=get_number("Enter the id of the ticket to view: ")
			display_ticket.display_ticket(ticket_id,login)
			raw_input("Press enter to return to the list of tickets.")
		elif command=="n":
			page+=1
			if page>page_max:
				page=1
		elif command=="p":
			page-=1
			if page<1:
				page=page_max


def get_command():
	while(True):
		command=input()
		if command in ["j","v","n","p"]:
			return command
		else:
			continue

def get_number(prompt):
	while(True):
		output=input(prompt)
		try:
			output=int(output)
		except ValueError:
			print(output+" is not a number.")
			continue
		return output

main()