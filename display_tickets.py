import zendesk_interface

#display list of tickets, with pages
def display_tickets(page,login):
	tickets=get_tickets(*login)
	page_max=1+len(tickets)//25
	#display tickets
	# for ticket in tickets:
		
		#pick what to display
		#the fields are THE SAME FOR BOTH, and are:
		# url
		# id
		# external_id
		# via
		# created_at
		# updated_at
		# type
		# subject
		# raw_subject
		# description
		# priority
		# status
		# recipient
		# requester_id
		# submitter_id
		# assignee_id
		# organization_id
		# group_id
		# collaborator_ids
		# follower_ids
		# email_cc_ids
		# forum_topic_id
		# problem_id
		# has_incidents
		# is_public
		# due_at
		# tags
		# custom_fields
		# satisfaction_rating
		# sharing_agreement_ids
		# fields
		# followup_ids
		# brand_id
		# allow_channelback
		# allow_attachments
	print("'n' for next page, 'p' for previous page, 'j' to jump to a page, 'v' to view a ticket.")
	#this lets the ticket_viewer wrap around correctly
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