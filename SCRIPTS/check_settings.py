import csv
import json
import memcache
from twython import Twython

def func ():
	shared = memcache.Client(['127.0.0.1:11211'], debug=0)
	print ('APP_KEY was set to: ' + str(shared.get('APP_KEY')))
	print ('APP_SECRET was set to: ' + str(shared.get('APP_SECRET')))
	print ('ACCESS_KEY was set to: ' + str(shared.get('ACCESS_KEY')))
	print ('ACCESS_SECRET was set to: ' + str(shared.get('ACCESS_SECRET')))
	print ('LAST_TWEET_FILENAME was set to: ' + str(shared.get('LAST_TWEET_FILENAME')))
   	print ('TWEET_ID_TO_REPLY was set to: ' + str(shared.get('TWEET_ID_TO_REPLY')))

if __name__ == '__main__':
  func()
