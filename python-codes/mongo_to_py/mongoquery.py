from datetime import datetime

from pymongo import MongoClient

MONGO_HOST = 'mongodb://localhost/twitterdb'


def mongodb_query():
    client = None
    inicio = datetime.now()
    my_date = inicio.strftime('%d-%m-%Y')

    query = {
        # "my_date": my_date,
        "language": "en"
        # "hashtags":"infinitywar"
    }
    try:
        client = MongoClient(MONGO_HOST)
        db = client.twitterdb

        # tweets = db.twitter_search.find({})  # select * from twitter_search
        count = 0
        tweets = db.twitter_search.find(query)
        for tw in tweets:
            print("{")
            print(count)
            count=count+1
            print("hashtags: ", end='')
            for j in tw['hashtags']:
                print(""+str(j['text']) +" , ", end='')
            print('')
            # print(str(tw['hashtags']))
            # print("username: "+str(tw['username']))
            print(str(tw['_id'])+" : "+str(tw['text']))
            # print(str(tw['text']))
            print("}")
            # print(tweets)
    except Exception as x:
        print(x)
        pass
    finally:
        client.close()
        return tweets
