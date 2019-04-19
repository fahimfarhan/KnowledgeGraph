# coding=utf-8
import requests 
import re, json
import math


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

def getUrlSet(my_string):
    listOfIndex = getStartingIndex(my_string)
    ret = set()
    for i in listOfIndex:
        some_url = getSingleUrl(my_string, i)
        ret.add(some_url) # print(getSingleUrl(my_string, i))
    return ret 

def getJson(url):
    url_json = str(url)+".json"
    data = requests.get(url_json).json()
    return data

def getEnglishValue(urlRes, jsonData):
    ret = "NOT FOUND"
    count = 0
    a = jsonData[str(urlRes)]['http://www.w3.org/2000/01/rdf-schema#comment']
    print(a)
    for i in a:
        if count == 10:
            break
        num = str(count)
        if i['lang'] == 'en':
            ret = i['value']
            break 
        else:
            count=count+1
    return ret 



if __name__ == "__main__":
    urlres1 = "http://dbpedia.org/data/Alice_and_Bob"
    urlres2 = "http://dbpedia.org/resource/Brad_Pitt"
    lines = urlres2.replace( "resource", "data")
    lines = lines.replace( "\"", "")
            
    myjsonAlice = getJson(urlres1)
    myjsonJimmy = getJson(lines)

    
    valueAlice =  myjsonAlice['http://dbpedia.org/resource/Alice_and_Bob']['http://www.w3.org/2000/01/rdf-schema#comment'][0] # = getEnglishValue(myjsonAlice)
    valueJimmy  = getEnglishValue(urlres2, myjsonJimmy) # myjsonJimmy['http://dbpedia.org/resource/Brad_Pitt']['http://www.w3.org/2000/01/rdf-schema#comment'][4] # = getEnglishValue(myjsonAlice)

    print(valueAlice)
    print('-----------')
    print(valueJimmy)
    pass