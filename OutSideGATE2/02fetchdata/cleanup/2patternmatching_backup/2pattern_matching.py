# coding=utf-8
import re  
import json


# Driver Code 
string1 = "[{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]{'type': 'uri', 'value': 'http://dbpedia.org/class/yago/TopographicPoint108664443'}"




def getUrlSet(input):
    myset = set()
    for m in re.finditer("http://", str(input)):
    # print(m)
        i = m.start()
        while(input[i] is not "'"):
            i=i+1
        # print(input[m.start():i])
        myset.add(input[m.start():i])
        return myset

def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)

l = getUrlSet(string1)
for i in l:
    print(i)

'''
file = open("tajmahal.json","r")
fileContent = file.read()
print(fileContent)

l2 = getUrlSet(str(fileContent))
print(l2)
for j in l2:
    print(j)
'''

'''
with open('tajmahal.json') as json_data:
    d = json.load(json_data)
    print(d)
'''

file = open("tajmahal.json")
fileContent = file.readline()
fileContent1 = str(file) 
fileContent1 = fileContent1.replace("\'", "\"")
d = json.loads(fileContent1)
out = item_generator(d, "value")
for i in out:
    print(i)
''' 
'''