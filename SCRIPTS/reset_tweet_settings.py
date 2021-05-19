import os
import memcache

shared = memcache.Client(['127.0.0.1:11211'], debug=0)

#get from developer twitter site
shared.set('APP_KEY', 'YhKV2ygb0GVcAZQL62d6QGXP0')
print ('APP_KEY was set to: ' + str(shared.get('APP_KEY')))

shared.set('APP_SECRET', 'WavXgvEITPDSRBUZl8akB10O5CMeIQsaTDSB51zNZBAOuFi1yt')
print ('APP_SECRET was set to: ' + str(shared.get('APP_SECRET')))

shared.set('ACCESS_KEY', '1262692838-tR5UlggkQY1BJ8gC9Y3wozisNOcGa8s6ICPGkSN')
print ('ACCESS_KEY was set to: ' + str(shared.get('ACCESS_KEY')))

shared.set('ACCESS_SECRET', 'yahapnHzbfaE1adZTzIBEx0wEN7VpqeP5vssHlSrKm4Xr')
print ('ACCESS_SECRET was set to: ' + str(shared.get('ACCESS_SECRET')))

#name of the file where last_tweet_id is saved
shared.set('LAST_TWEET_FILENAME', '/home/pi/twitterbot/last_tweet_info.json')
print ('LAST_TWEET_FILENAME was set to: ' + str(shared.get('LAST_TWEET_FILENAME')))

#id of the tweet to reply to
shared.set('TWEET_ID_TO_REPLY', '1390000237348106247')
print ('TWEET_ID_TO_REPLY was set to: ' + str(shared.get('TWEET_ID_TO_REPLY')))
