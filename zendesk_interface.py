import json
import requests

#Connect to API, retrieve ticket(s)
def get_json(url,user,pwd):
	#get ticket(s)
	try:
		response = requests.get(url,auth=(user,pwd))
	except requests.exceptions.ConnectionError:
		print(
			"Could not connect to API. Try checking your internet connection.")
		exit()

	#quit if error
	handle_response_code(response.status_code)

	#convert ticket(s) from json to string
	output=response.json()
	return output

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
