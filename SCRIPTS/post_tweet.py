#!/usr/bin/env python
import sys
import datetime
from time import sleep
import memcache
from twython import Twython

shared = memcache.Client(['127.0.0.1:11211'], debug=0)
CONSUMER_KEY = str(shared.get('APP_KEY'))
CONSUMER_SECRET = str(shared.get('APP_SECRET'))
ACCESS_KEY = str(shared.get('ACCESS_KEY'))
ACCESS_SECRET = str(shared.get('ACCESS_SECRET'))

print('STARTING:')

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

status_string = 'Currently it is ' + time

api.update_status(status=status_string)
print('FINISHED: ' + time)