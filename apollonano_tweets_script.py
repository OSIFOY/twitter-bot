import os
import re
import replies_from_tweet
import twitter_bot_ApolloNano
from datetime import datetime
from time import sleep

test = 0
tweet_all_3610_seconds = True
waiting_delay = 3600 if test == 0 else 20

print('\n==================================STARTING==================================')
print(str(datetime.now()).split(".", 1)[0])

#if tweet_all_3610_seconds:
#	get_last_tweet_time_difference = replies_from_tweet.get_last_tweet_reply_time_difference()	
#	while get_last_tweet_time_difference < waiting_delay:
#		seconds_left = waiting_delay-get_last_tweet_time_difference
#		print('sleeping for ' + str(seconds_left) + ' seconds')
#		sleep(seconds_left)
#		get_last_tweet_time_difference = replies_from_tweet.get_last_tweet_reply_time_difference()
#else: 
try:
	#replies_from_tweet.write_last_tweet_id_to_file('1395385135361572864')
	time_since_last_tweet_reply = replies_from_tweet.get_last_tweet_reply_time_difference()
	print('time_since_last_tweet_reply: ' + str(time_since_last_tweet_reply))

	while time_since_last_tweet_reply < waiting_delay:
		seconds_left = waiting_delay-time_since_last_tweet_reply
		print('sleeping for ' + str(seconds_left) + ' seconds')
		sleep(seconds_left)
		time_since_last_tweet_reply = replies_from_tweet.get_last_tweet_reply_time_difference()
except:
	print('exception catched and handled')

tweet = twitter_bot_ApolloNano.post_tweet(test)
last_tweet_id = re.search("u'id': (.*)L, u'favorite_count':", str(tweet))
replies_from_tweet.write_last_tweet_id_to_file(last_tweet_id.group(1))
print('==================================FINISHED==================================\n')
