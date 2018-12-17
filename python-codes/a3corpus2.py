from mongo_to_py.mongoquery import mongodb_query

tweets = mongodb_query()

count = 0

try:
    filename = 'corpus/file_oo2'+".txt"
    f = open(filename, "w")
    for tw in tweets:
        # count = count+1
        # f.write((str(tw['username']))+" :\n"+str(tw['text']))
        f.write("{")
        f.write(count)
        count=count+1
        # print(str(tw['hashtags']))
        f.write(str(tw['username']))
        f.write(str(tw['_id'])+" : "+str(tw['text']))
        # f.write(str(tw['text']))
        f.write("}")
    # f.write(str(tw['text']))
    f.close()
except Exception as x:
    print(x)
