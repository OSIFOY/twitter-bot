#!/usr/bin/env python
import sys
import datetime
import memcache
from twython import Twython

def post_tweet(test):
	#Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
	shared = memcache.Client(['127.0.0.1:11211'], debug=0)
	CONSUMER_KEY = str(shared.get('APP_KEY'))
	CONSUMER_SECRET = str(shared.get('APP_SECRET'))
	ACCESS_KEY = str(shared.get('ACCESS_KEY'))
	ACCESS_SECRET = str(shared.get('ACCESS_SECRET'))
	TWEET_ID_TO_REPLY = str(shared.get('TWEET_ID_TO_REPLY'))

	#Create a copy of the Twython object with all our keys and secrets to allow easy commands.
	api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

	#Get current time
	time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

	if test == 0:
		status_string = 'Currently it is ' + time + ', I am replying to the TWEET_ID_TO_REPLY  ' + TWEET_ID_TO_REPLY + ' and I am claiming a free tip of nano. \n@ApolloNano \n!faucet nano_3s17ozbgtgdm6zjk4gkat5ffxhnxzoguu9hfp1dbpyih69e7nfs94gr3rqoo'
		print('tweet posted as reply to: ' + TWEET_ID_TO_REPLY)
		#Using our newly created object, utilize the update_status to send in the text passed in through CMD
		return api.update_status(status = status_string, in_reply_to_status_id = TWEET_ID_TO_REPLY)
	
	else: 
		#Test bot that always replies
		status_string = 'Currently it is ' + time + ' and @tweet_stamp stamp please!'
		#Create a new tweet instead of replying to existing one
		return api.update_status(status=status_string, in_reply_to_status_id = TWEET_ID_TO_REPLY)
