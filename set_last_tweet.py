import os
import sys
import replies_from_tweet

print 'RECEIVED argv[1]:', str(sys.argv[1])
replies_from_tweet.write_last_tweet_id_to_file(sys.argv[1])

#print(replies_from_tweet.get_last_tweet_id_from_file())