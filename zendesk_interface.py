import json
import requests
import sys

#Connect to API, retrieve ticket(s)
def get_json(url,user,pwd):
	#get ticket(s)
	try:
		response = requests.get(url,auth=(user,pwd))
	except requests.exceptions.ConnectionError:
		sys.exit(
			"Could not connect to API. Try checking your internet connection.")

	#quit if error
	handle_response_code(response.status_code)

	#convert ticket(s) from json to string
	output=response.json()
	return output

#Handle unavailable API
def handle_response_code(code):
	#Convert status codes to user-friendly output
	error_code_switcher = {
		301: " Redirected.",
		400: " Bad request.",
		401: " Authentication error.",
		403: " Forbidden request.",
		404: " Resource not found.",
		500: " Internal server error.",
		503: " Service unavailable.",
		504: " Gateway timeout."
	}

	#quit on error
	if code!=200:
		sys.exit(	'Error connecting to API. Status: '+str(code)+
				error_code_switcher.get(code,""))