# consumer key, consumer secret, access token, access secret.
from decouple import config
from tweepy import OAuthHandler, Stream

from prototype.twitter.listener import listener

ckey = config('ckey')
csecret = config('csecret')
atoken = config('atoken')
asecret = config('asecret')

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
# twitterStream.filter(track=["infinitywar"])
twitterStream.filter(track=["myfirstTweet", "car", "messi", "farcry", "Bangladesh", "ronaldo", "assassinscreed",
                            "china", "usa", "infinitywar"])
# twitterStream.all()
