import os
import sys
import json
import time
import twitter
import urllib
import memcache
from datetime import datetime, timedelta
from twython import Twython
from os import environ as e

shared = memcache.Client(['127.0.0.1:11211'], debug=0)
filename = shared.get('LAST_TWEET_FILENAME')
t = twitter.Api(
    consumer_key = str(shared.get('APP_KEY')),
    consumer_secret = str(shared.get('APP_SECRET')),
    access_token_key = str(shared.get('ACCESS_KEY')),
    access_token_secret = str(shared.get('ACCESS_SECRET')),
    sleep_on_rate_limit = True
)

def write_last_tweet_id_to_file(last_tweet_id):
    my_last_tweet = {"user":{"screen_name": "OSIFOY_"},"id": int(last_tweet_id)}
    with open(str(filename), 'w') as json_file:
        json.dump(my_last_tweet, json_file)
    #print('write_last_tweet_id_to_file() wrote last_tweet_id (' + str(last_tweet_id) + ') to the file')

def get_last_tweet_id_from_file():
    for line in open(str(filename)):
        x = json.loads(line)
        #print('get_last_tweet_id_from_file() read from the file: ' + str(x['id']))
        return x['id']

def get_my_last_tweet():
    #print('get_my_last_tweet()')
    for line in open(str(filename)):
        my_last_tweet = twitter.Status.NewFromJsonDict(json.loads(line))
        #print('get_my_last_tweet() returned: ' + str(my_last_tweet))
        yield my_last_tweet

def get_replies(tweet):
    user = tweet.user.screen_name
    tweet_id = tweet.id
    #print(tweet_id)
    max_id = None
    while True:
        q = urllib.urlencode({"q": "to:%s" % user})
        try:
            replies = t.GetSearch(raw_query=q, since_id=tweet_id, max_id=max_id, count=100)
        except twitter.error.TwitterError as e:
            time.sleep(60)
            continue
        for reply in replies:
            if reply.in_reply_to_status_id == tweet_id:
                yield reply
                # recursive magic to also get the replies to this reply
                for reply_to_reply in get_replies(reply):
                    yield reply_to_reply
            max_id = reply.id
        if len(replies) != 100:
            break

def get_last_tweet_time_difference():
    #print('get_last_tweet_time_difference()')
    for tweet in get_my_last_tweet():
        twjdata = t.GetStatus(tweet.id)
    created_at_time_str = datetime.strftime(datetime.strptime(twjdata.created_at,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')
    current_time_str = str(datetime.now()).split(".", 1)[0]
    created_at_time_datetime = datetime.strptime(created_at_time_str, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)
    current_time_datetime = datetime.strptime(current_time_str, '%Y-%m-%d %H:%M:%S') 
    return ((current_time_datetime-created_at_time_datetime).total_seconds())


def get_last_tweet_reply_time_difference():
    #print('get_last_tweet_reply_time_difference()')
    count = 0
    for tweet in get_my_last_tweet():
        #print(tweet)
        for reply in get_replies(tweet):
            count += 1
            twjdata = json.loads(reply.AsJsonString())

    created_at_time_str = datetime.strftime(datetime.strptime(twjdata['created_at'],'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')
    current_time_str = str(datetime.now()).split(".", 1)[0]
    created_at_time_datetime = datetime.strptime(created_at_time_str, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)
    current_time_datetime = datetime.strptime(current_time_str, '%Y-%m-%d %H:%M:%S') 
    #print('get_last_tweet_reply_time_difference: created_at_time_datetime = ' + str(created_at_time_datetime))
    #print('get_last_tweet_reply_time_difference: current_time_datetime = ' + str(current_time_datetime))
    
    return ((current_time_datetime-created_at_time_datetime).total_seconds())


#def get_last_tweet_id():
#    t = Twython(str(shared.get('APP_KEY')),str(shared.get('APP_SECRET')),str(shared.get('ACCESS_KEY')),str(shared.get('ACCESS_SECRET')))
#    result = t.get_user_timeline(screen_name='OSIFOY_', count = 1)
#    for tweet in result:
#        return str(tweet['id'])
