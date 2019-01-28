import tweepy
from tweepy import OAuthHandler
from twitter_to_mongo.twimongo import StreamListener
from decouple import config

count = 0
while (True):
    count = count + 1
    if count == 10:
        break
    try:
        ckey = config('ckey')
        csecret = config('csecret')
        atoken = config('atoken')
        asecret = config('asecret')

        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)

        WORDS = ["bbc", "cnn","physics", "math","biology", "chemistry",
         "thenunmovie ", "QuantaMagazine","ZonePhysics",
        "ChemistryWorld","physorg_com","CompSciFact", "NASA","newscientist",
        "centerofmath","BdMOC","molecular","GenomeBiology","dailystarnews",
         "Bangladesh","uk", "usa","australia",
         "russia","cricket", "football", "tennis", "VictoryDay","prothonalo" ]
        '''
        WORDS = ["fifa", "russia", "fifaworldcup", "football", "brasil", "argentina", "spain", "portugal",
                 "germany", "myfirstTweet", "car", "cr7", "messi", "farcry", "Bangladesh", "assassinscreed",
                 "infinitywar", "avengersinfinitywar",]
        '''
        # Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
        listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
        streamer = tweepy.Stream(auth=auth, listener=listener)
        print("Tracking: " + str(WORDS))
        streamer.filter(track=WORDS)
    except Exception as x:
        print(x)
        pass
