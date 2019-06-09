import json
import requests

#display individual ticket
def display_ticket(id,url,auth):
	#get new ticket, in case it was updated
	response=requests.get(url+'/'+id+'.json',auth=(user,pwd))
	ticket=response.json()
	
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