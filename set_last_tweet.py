import os
import sys
import replies_from_tweet

replies_from_tweet.write_last_tweet_id_to_file(sys.argv[1])
print 'last tweet set to: ', replies_from_tweet.get_last_tweet_id_from_file()
