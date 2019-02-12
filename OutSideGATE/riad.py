#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF, CSV, TSV
import time

def my_geo_describe(location, i):
    try:
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setReturnFormat(JSON)
        query = """PREFIX db: <http://dbpedia.org/resource/>
                    DESCRIBE db:"""+str(location)+ """
                    LIMIT 50"""
        # print(query)
        sparql.setQuery(query)  # the previous query as a literal string

        result =  sparql.query().convert()
        result_str = str(result)
        res_array = result_str.split("\\n")
        # for res in res_array:
        #     print(res)
        
        s = "prototypeOutput/geo_"+str(i)+".json"    
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
    my_geo_describe('dhaka', 0)
    my_geo_describe('Dhaka', 1)
    
    pass