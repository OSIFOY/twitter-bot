import os
import re
import replies_from_tweet
import twitter_bot_ApolloNano
from datetime import datetime
from time import sleep

test = 0
waiting_delay = 3600 if test == 0 else 60

print('\n==================================STARTING==================================')
print(str(datetime.now()).split(".", 1)[0])

#replies_from_tweet.write_last_tweet_id_to_file('1394058086948773894')
time_since_last_tweet_reply = replies_from_tweet.get_last_tweet_reply_time_difference()
print('time_since_last_tweet_reply: ' + str(time_since_last_tweet_reply))

while time_since_last_tweet_reply < waiting_delay:
	seconds_left = waiting_delay-time_since_last_tweet_reply
	print('sleeping for ' + str(seconds_left) + ' seconds')
	sleep(seconds_left)
	time_since_last_tweet_reply = replies_from_tweet.get_last_tweet_reply_time_difference()

tweet = twitter_bot_ApolloNano.post_tweet(test)
last_tweet_id = re.search("u'id': (.*)L, u'favorite_count':", str(tweet))
replies_from_tweet.write_last_tweet_id_to_file(last_tweet_id.group(1))
print('==================================FINISHED==================================\n')
