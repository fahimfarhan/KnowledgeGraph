#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF, CSV, TSV
import time

def start(u,e,v,i):
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
        # for res in res_array:
        #     print(res)
        
        s = "prototypeOutput/smartOutput_"+str(i)+".csv"    
        fout = open(s, "w")
        for res in res_array:
            fout.write(str(res))
            fout.write("\n")
        # fout.write(str(result))
        fout.close()
    except Exception as x:
        print('sorry '+str(x))
    return 0


if __name__ == "__main__":
    #start('God', 'gave', 'Bible', 0)
    #start('Barnes', 'calls', 'Australia', 1)
    '''
    start('hydrogen', 'trains', 'future', 2)
    start('Brexit', 'giving', 'liars', 3)
    start('GrandPrix', 'trains', 'Maxico', 4)
    '''
    start('concept', 'depicts', 'NASA', 5)
    start('client', 'trains', 'search', 6)
    start('Hennessy', 'accuses', 'Nicki', 7)
    pass