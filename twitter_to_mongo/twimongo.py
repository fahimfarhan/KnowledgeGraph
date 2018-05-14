from __future__ import print_function
import tweepy
import json
import datetime
from pymongo import MongoClient
from datetime import date

MONGO_HOST = 'mongodb://localhost/twitterdb'  # assuming you have mongoDB installed locally


# and a database called 'twitterdb'


class StreamListener(tweepy.StreamListener):
    # This is a class provided by tweepy to access the Twitter Streaming API.

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        # This is the meat of the script...it connects to your mongoDB and stores the tweet
        client = None
        try:
            client = MongoClient(MONGO_HOST)

            # Use twitterdb database. If it doesn't exist, it will be created.
            db = client.twitterdb

            # Decode the JSON from Twitter
            datajson = json.loads(data)

            # Pull important data from the tweet to store in the database.
            tweet_id = datajson['id_str']  # The Tweet ID from Twitter in string format
            username = datajson['user']['screen_name']  # The username of the Tweet author
            followers = datajson['user']['followers_count']  # The number of followers the Tweet author has
            text = datajson['text']  # The entire body of the Tweet
            hashtags = datajson['entities']['hashtags']  # Any hashtags used in the Tweet
            dt = datajson['created_at']  # The timestamp of when the Tweet was created
            language = datajson['lang']  # The language of the Tweet

            # Convert the timestamp string given by Twitter to a date object called "created". This is more easily
            # manipulated in MongoDB.
            created = datetime.datetime.strptime(dt, '%a %b %d %H:%M:%S +0000 %Y')
            # created = datetime.datetime.strptime(dt, '%d-%m-%Y')
            inicio = datetime.datetime.now()
            my_date = inicio.strftime('%d-%m-%Y')

            # Load all of the extracted Tweet data into the variable "tweet" that will be stored into the database
            tweet = {'id': tweet_id, 'username': username, 'followers': followers, 'text': text, 'hashtags': hashtags,
                     'language': language, 'created': created,'my_date': my_date}

            # grab the 'created_at' data from the Tweet to use for display
            # created_at = datajson['created_at']

            # print out a message to the screen that we have collected a tweet
            print("Tweet collected : " + str(tweet))

            # insert the data into the mongoDB into a collection called twitter_search
            # if twitter_search doesn't exist, it will be created.
            db.twitter_search.insert(tweet)
        except Exception as e:
            print(e)
        finally:
            client.close()
