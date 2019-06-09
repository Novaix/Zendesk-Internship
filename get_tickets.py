import json
import requests

#Connect to API, retrieve tickets
def get_tickets(url,user,pwd):
	#get tickets
	response = requests.get(url+'.json',auth=(user,pwd))

	#todo: handle max retry error

	#quit if error
	handle_response_code(response.status_code)

	#convert tickets from json to string
	tickets=response.json()

	#the response comes in the form of a dict
	#with "next_page" as a key and a url as its value
	#and "tickets" as another key with a list of dicts as its value
	
	#if there is more than one API-side page of tickets
	#append new pages to ticket list and update next page until finished
	while (tickets["next_page"]!=None):
		response = requests.get(tickets["next_page"],auth=(user,pwd))
		more_tickets=response.json()
		tickets["tickets"]+=more_tickets["tickets"]
		tickets["next_page"]=more_tickets["next_page"]
	return tickets

#Handle unavailable API
def handle_response_code(code):
	#Convert status codes to user-friendly output
	error_code_switcher = {
		301: "Redirected.",
		400: "Bad request.",
		401: "Authentication error.",
		403: "Forbidden request.",
		404: "Resource not found."
	}

	#quit on error
	if code!=200:
		print(	'Error connecting to API. Status:',code,
				error_code_switcher.get(code,""))
		exit()
