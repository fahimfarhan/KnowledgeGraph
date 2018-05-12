from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# import MySQLdb
import time
import json


# import tweepy

class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]

        username = all_data["user"]["screen_name"]

        mydata = username + " : " + tweet + "\n"
        '''
        c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

        conn.commit()
        '''

        f = open('output/tweepy.txt', 'a')
        f.write(mydata)
        f.close()
        print((username, tweet))
        return True

    def on_error(self, status):
        print("error 1 here: " + str(status))
