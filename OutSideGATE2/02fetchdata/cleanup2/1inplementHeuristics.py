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


def getRelatednessAB(A,B):
    relatedness_a_b = 0 

    setA = set() 
    setB = set()
    setAnB = set()

    contentA = getJson(A)
    contentB = getJson(B)

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



A = 'http://dbpedia.org/data/The_Abbott'
B = 'http://dbpedia.org/data/Category:Interrogative_words_and_phrases'
print("Relatedness of A, B = "+str(getRelatednessAB(A,B)))
''' 
if __name__ == "__main__":

    i = 1
    filename = "csv/tuple_"+str(i)+".csv"
    file = open(filename,"r")
    fileContent = file.readlines()

    for lines in fileContent:
        maximus=-9999
        CorrectLine = ""
        try:
            lines = lines.replace( "resource", "data")
            lines = lines.replace( "\"", "")
            # setT.add(lines)
            wordList = re.sub(",", " ",  lines).split()
            A = wordList[0]
            B = wordList[2]
    
            score = getRelatednessAB(A,B)

        except:
            pass
'''