# coding=utf-8

import re, json

def getStartingIndex(input_str):
    m = re.finditer("http://", str(input_str))
    ret = set()
    for i in m:
        # print(i.start())
        ret.add(i.start())
    return ret

def getSingleUrl(input_str, startIndex):
    i = startIndex
    while(input_str[i] is not "'"):
        i=i+1
    mystart = startIndex
    myend = i
    ret = input_str[mystart:myend]
    return ret

def getUrlSet(my_string, listOfIndex):
    ret = set()
    for i in listOfIndex:
        some_url = getSingleUrl(my_string, i)
        ret.add(some_url) # print(getSingleUrl(my_string, i))
    return ret 


if __name__ == "__main__":
    filename = "tajmahal.json"
    file = open(filename)
    content = file.readline() 
    # print(content)
    a = getStartingIndex(content)
    print(a)
    # for i in a:
    #    print(getSingleUrl(content, i))
    output = getUrlSet(content, a)
    # print(output)
    for x in output:
        print(x)
    file.close() 