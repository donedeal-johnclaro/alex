import json
import os

from dotenv import load_dotenv, find_dotenv
from slackclient import SlackClient
load_dotenv(find_dotenv())

slack_token = os.environ['SLACK_API_TOKEN']
sc = SlackClient(slack_token)


def f(data):
	return json.dumps(data, indent=4, sort_keys=True)


def get_user_messages(channel_id, next=None, user_data=None):
	data = user_data if user_data else {}
	
	if not next:
		print '--------------------CURRENTLY IN CHANNEL: {}--------------------'.format(channel_id)
		channel_history = sc.api_call(
			'channels.history', channel=channel_id
		)
	else:
		channel_history = sc.api_call(
			'channels.history', channel=channel_id, latest=next
		)
		
	try:
		for index, message in enumerate(channel_history['messages']):
			user_info = sc.api_call('users.info', user=message['user'])
			user = user_info['user']['profile']['real_name_normalized']
			text = message['text']
			
			if user in data.keys():
				print 'Appending {} with message {}'.format(user, len(text))
				data[user].append(text)
			else:
				print 'Adding {} with message {}'.format(user, len(text))
				data[user] = [text]
	
		if channel_history['has_more']:
			last_message = len(channel_history['messages']) - 1
			next = channel_history['messages'][last_message]['ts']
			return get_user_messages(channel_id, next=next, user_data=data)
	except KeyError:
		pass
	
	return data
			
# channels = sc.api_call('channels.list')['channels']
# data = {}
# for channel in channels:
# 	channel_id = channel['id']
# 	user_data = get_user_messages(channel_id)
# 	for k,v in user_data.items():
# 		if k in data.keys():
# 			data[k] = data[k] + v
# 		else:
# 			data[k] = v
data = {}
users = sc.api_call('users.list')
for user in users['members']:
	if not user['deleted']:
		try:
			name = user['profile']['real_name_normalized']
			title = user['profile']['title']
			data[name] = title
		except KeyError:
			pass

with open('user_jobs.json', 'w') as user_jobs_file:
	json.dump(data, user_jobs_file, indent=4, sort_keys=True)
