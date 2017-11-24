import json
import os

from dotenv import load_dotenv, find_dotenv
from slackclient import SlackClient
load_dotenv(find_dotenv())

slack_token = os.environ['SLACK_API_TOKEN']
sc = SlackClient(slack_token)


def f(uf_data):
	"""
	
	:param dict uf_data:
	:return:
	"""
	return json.dumps(uf_data, indent=4, sort_keys=True)


def get_users():
	u_data = {}
	users = sc.api_call('users.list')
	for user in users['members']:
		if not user['deleted']:
			try:
				name = user['profile']['real_name_normalized']
				title = user['profile']['title']
				u_data[name] = title
			except KeyError:
				pass


def get_user_messages(um_channel_id, latest_timestamp='', um_data=None):
	"""
	
	:param str um_channel_id:
	:param str latest_timestamp:
	:param dict um_data:
	:return:
	"""
	um_data = um_data if um_data else {}

	if not next:
		print '---------------CURRENTLY IN CHANNEL: {}---------------'.format(um_channel_id)
		channel_history = sc.api_call(
			'channels.history', channel=um_channel_id
		)
	else:
		channel_history = sc.api_call(
			'channels.history', channel=um_channel_id, latest=latest_timestamp
		)
		
	try:
		for index, message in enumerate(channel_history['messages']):
			user_info = sc.api_call('users.info', user=message['user'])
			user = user_info['user']['profile']['real_name_normalized']
			text = message['text']
			
			if user in um_data.keys():
				print 'Appending {} with message {}'.format(user, len(text))
				um_data[user].append(text)
			else:
				print 'Adding {} with message {}'.format(user, len(text))
				um_data[user] = [text]
	
		# if channel_history['has_more']:
		# 	last_message = len(channel_history['messages']) - 1
		# 	ts = channel_history['messages'][last_message]['ts']
		# 	return get_user_messages(um_channel_id, latest_timestamp=ts, um_data=um_data)
	except KeyError:
		pass
	
	return um_data

			
if __name__ == '__main__':
	channels = sc.api_call('channels.list')['channels']
	data = {}
	channel_id = os.environ['GP_GENERAL_CHANNEL_ID']
	user_data = get_user_messages(channel_id)
	for k, v in user_data.items():
		if k in data.keys():
			data[k] = data[k] + v
		else:
			data[k] = v

	with open('user_messages.json', 'w') as user_jobs_file:
		json.dump(data, user_jobs_file, indent=4, sort_keys=True)
