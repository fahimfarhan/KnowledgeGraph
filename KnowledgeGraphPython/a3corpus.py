from mongo_to_py.mongoquery import mongodb_query

tweets = mongodb_query()

count = 0
for tw in tweets:

    count = count+1
    try:
        filename = 'corpus/file_'+str(tw['_id'])+".txt"
        f = open(filename, "w")
        f.write((str(tw['username']))+" :\n"+str(tw['text']))
        # f.write(str(tw['text']))
        f.close()
    except Exception as x:
        print(x)
