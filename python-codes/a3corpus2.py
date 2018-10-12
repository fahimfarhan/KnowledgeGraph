from mongo_to_py.mongoquery import mongodb_query

tweets = mongodb_query()

count = 0

try:
    filename = 'corpus/file_oo0'+".txt"
    f = open(filename, "w")
    for tw in tweets:
        count = count+1
        f.write((str(tw['username']))+" :\n"+str(tw['text']))
    # f.write(str(tw['text']))
    f.close()
except Exception as x:
    print(x)
