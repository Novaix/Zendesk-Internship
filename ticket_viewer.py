import json
import requests
import display_ticket
import display_tickets
import get_tickets
#As per https://develop.zendesk.com/hc/en-us/articles/360001074168-Making-requests-to-the-Zendesk-API
#we have the basic structure of how requests to the API are formed

#Get authentication details and base url from file
authentication=open("authentication.txt","r")
user = authentication.readline()[:-1]
pwd = authentication.readline()[:-1]
#can append '.json' for all tickets, '/{id}.json' for individual ticket
url = authentication.readline()+'/api/v2/tickets'	

tickets=get_tickets.get_tickets(url,user,pwd)

display_tickets.display_tickets(tickets)

#rudimentary tests (prints) work so far
#todo: input loop