# coding=utf-8
import requests 
import re, json
import math

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer



def getVectorAnalysis(a,b):
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform([str(a),str(b)])
    c = ((tfidf * tfidf.T).A)
    ret = (c[0][1])
    return ret

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


def getRelatednessAB(A,B):
    relatedness_a_b = 0 

    setA = set() 
    setB = set()
    setAnB = set()

    contentA = A # getJson(A)
    contentB = B # getJson(B)

    contentA = str(contentA) 
    contentB = str(contentB)

    setA = getUrlSet(contentA)
    setB = getUrlSet(contentB)

    setAnB = setA.intersection(setB)

    nA = len(setA)
    nB = len(setB)
    nAnB = len(setAnB)
    nW = 369857

    maxA_B = max(nA,nB)
    minA_B = min(nA,nB)

    logMaxA_B = math.log2(maxA_B)
    logMinA_B = math.log2(minA_B)

    logAnB = math.log2(nAnB) 
    logW = math.log2(nW)

    relatedness_a_b = ( logMaxA_B - logAnB )/(logW - logMinA_B )

    return relatedness_a_b

def getEnglishValue(urlRes, jsonData):
    ret = "NOT FOUND"
    ret1=""
    ret2 = ""
    count = 0
    try:
        a = jsonData[str(urlRes)]['http://www.w3.org/2000/01/rdf-schema#comment']
        for i in a:
            if i['lang'] == 'en':
                ret = i['value']
                # return ret1
                break 
    except:
        ret = "NOT FOUND"
        pass
    
    return ret 


def start(line, url1res, url2res, url1data, url2data):
    jsonDataA = getJson(url1data)
    jsonDataB = getJson(url2data)

    relatednessScoreAB = getRelatednessAB(jsonDataA, jsonDataB)
    
    valueA = getEnglishValue(url1res, jsonDataA)
    valueB = getEnglishValue(url2res, jsonDataB)

    vectorScoreAB = getVectorAnalysis(valueA, valueB)

    writeLine = str(relatednessScoreAB)+" ; "+str(vectorScoreAB)+" ; "+str(line)
    fout = open("score.csv", "a") 
    fout.write(writeLine)
    # print(writeLine)
    fout.close()
    pass


def farcry(num):
    #print("DEBUG 1")
    #print("DEBUG ")
    for i in range(num):
        print("DEBUG "+str(i))
        filename = "csv/tuple_"+str(i)+".csv"
        file = open(filename,"r")
        fileContent = file.readlines()

        maximus=-9999
        CorrectLine = ""
        myStopLimit = 0
        for lines in fileContent:
            myStopLimit = myStopLimit+1 
            if(myStopLimit == 40):
                break
            try:
                originalLine = lines
                lines = lines.replace( "\"", "")
                wordListRes =  re.sub(",", " ",  lines).split()
                Ares = wordListRes[0]
                Bres = wordListRes[2]
                lines = lines.replace( "resource", "data")
                # setT.add(lines)
                wordList = re.sub(",", " ",  lines).split()
                A = wordList[0]
                B = wordList[2]
                # print("DEBUG 3 befire start() func")
                try:                
                    start(originalLine, Ares, Bres, A,B)
                except:
                    pass
            except Exception as x:
                print(x)
                pass
        file.close()            
    pass

if __name__ == "__main__":
    farcry(1)