#Schuyler Mortimer
from twython import Twython
import sys
import memcache

shared = memcache.Client(['127.0.0.1:11211'], debug=0)
APP_KEY = str(shared.get('APP_KEY'))
APP_SECRET = str(shared.get('APP_SECRET'))
TOKEN_KEY = str(shared.get('ACCESS_KEY'))
TOKEN_SECRET = str(shared.get('ACCESS_SECRET'))

def batch_delete(twitter):

	#ran into a 200 tweet limit, loop gets around this
	while True:

		#get the timeline
		try:
			timeline = twitter.get_user_timeline(count=200)
		except:
			print("You made a mistake.")
			sys.exit()

		if len(timeline) == 0:
			print("No tweets left to delete")
			break

		#delete the timeline
		for tweet in timeline:
			status = int(tweet['id_str'])
			twitter.destroy_status(id=status)
			print('Tweet deleted: ' + str(status))
		print(len(timeline))


def main():
	twitter = Twython(APP_KEY, APP_SECRET, TOKEN_KEY, TOKEN_SECRET)
	batch_delete(twitter)

if __name__ == '__main__':
	main()
