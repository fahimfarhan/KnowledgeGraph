import requests 
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



#data = requests.get('http://dbpedia.org/data/Alice_and_Bob.json').json()
#print(data)

def getNumberOfLinks(url):
    ret = 0
    try:
        url_json = str(url)+".json"
        data = requests.get(url_json).json()
        datastr = str(data);
        # print(datastr)
        ret = datastr.count("uri") 
        return ret
    except:
        pass
    return ret

def getJson(url):
    url_json = str(url)+".json"
    data = requests.get(url_json).json()
    return data

def  heuristicValue(i):
    # 1. open ith file
    filename = "csv/tuple_"+str(i)+".csv"
    file = open(filename,"r")
    fileContent = file.readlines()

    setA = set() 
    setB = set()
    setT = set()
    mapA = [] 
    mapB = []

    for lines in fileContent:
        try:
            lines = lines.replace( "resource", "data")
            lines = lines.replace( "\"", "")
            # setT.add(lines)
            wordList = re.sub(",", " ",  lines).split()
            A = wordList[0]
            B = wordList[2]
            

        except:
            pass
    file.close()
    # print(setA)
    # print(setB)
    return  


if __name__ == "__main__":
    # heuristicValue(1)
    testSetA = set()
    testSetA = getJson("http://dbpedia.org/data/Taj_Mahal")
    linkcount = 0
    print(testSetA)
    pass