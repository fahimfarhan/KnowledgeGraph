from datetime import datetime

from pymongo import MongoClient

MONGO_HOST = 'mongodb://localhost/twitterdb'


def mongodb_query():
    client = None
    inicio = datetime.now()
    my_date = inicio.strftime('%d-%m-%Y')

    query = {
        "my_date": my_date,
        "language": "en"
        # "hashtags":"infinitywar"
    }
    try:
        client = MongoClient(MONGO_HOST)
        db = client.twitterdb

        tweets = db.twitter_search.find({})  # select * from twitter_search
        # tweets = db.twitter_search.find(query)
        for tw in tweets:
            # print(str(tw['tweet_id'])+" "+str(tw.username))
            print(tw['text'])
            # print(tweets)
    except Exception as x:
        print(x)
        pass
    finally:
        client.close()
