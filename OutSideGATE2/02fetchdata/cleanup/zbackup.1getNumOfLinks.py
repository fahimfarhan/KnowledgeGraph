import requests 
import re

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
            setT.add(lines)
            wordList = re.sub(",", " ",  lines).split()
            u = wordList[0]
            v = wordList[2]
            setA.add(u);
            setB.add(v);

            for ai in setA: 
                n_ai = getNumberOfLinks(ai)
                mapA[ai] = n_ai;
            
            for bi in setB:
                n_bi = getNumberOfLinks(bi)
                mapB[bi] = n_bi 
            

        except:
            pass
    file.close()
    # print(setA)
    # print(setB)
    return  


if __name__ == "__main__":
    heuristicValue(1)
    nA = getNumberOfLinks("http://dbpedia.org/data/Alice_and_Bob")
    print(nA)
    pass