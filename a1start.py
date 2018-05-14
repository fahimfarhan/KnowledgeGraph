import tweepy
from tweepy import OAuthHandler
from twitter_to_mongo.twimongo import StreamListener
from decouple import config


ckey = config('ckey')
csecret = config('csecret')
atoken = config('atoken')
asecret = config('asecret')

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


WORDS = ["myfirstTweet", "car", "cr7", "messi", "farcry", "Bangladesh", "assassinscreed",
         "infinitywar", "avengersinfinitywar"]

# Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)