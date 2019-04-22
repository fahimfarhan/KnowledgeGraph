#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF, CSV, TSV
import time
import re


def getIntersectionTuples(u,e,v,i):
    input_str = str(u) + " , "+str(e) +" , " +str(v)
    try:
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setReturnFormat(CSV)
        query = """PREFIX db: <http://dbpedia.org/resource/>
                    select distinct * where {
                    ?s ?o db:"""+str(u)+""" . 
                    db:"""+str(v)+ """ ?o ?p .
                    }
                    LIMIT 50"""
        # print(query)
        sparql.setQuery(query)  # the previous query as a literal string

        result =  sparql.query().convert()
        result_str = str(result)
        res_array = result_str.split("\\n")
        
        s = "csv/tuple_"+str(i)+".csv"    
        fout = open(s, "w")
        for res in res_array:
            fout.write(str(res)+" , "+str(input_str))
            fout.write("\n")
        fout.close()
    except Exception as x:
        print('sorry '+str(x))
        pass
    return 0


if __name__ == "__main__":
    file = open("SmallInput.txt","r")
    fileContent = file.readlines()
     
    lineCount=0
    for lines in fileContent:
        print(lineCount)
        try:
            wordList = re.sub("[^\w]", " ",  lines).split()
            u = wordList[0]
            e = wordList[1]
            v = wordList[2]
            getIntersectionTuples(u,e,v,lineCount)
            # print(u+" "+v)
        except:
            pass 
        finally:
            lineCount=lineCount+1
    file.close()
    pass
