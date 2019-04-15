from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF, CSV, TSV
import time

def get_result(input):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)
    #sparql.setReturnFormat(CSV) # RDF , TSV , N# , XML
    # query = "DESCRIBE http://dbpedia.org/resource/"+str(input)+" LIMIT 100"
    query = "DESCRIBE <http://dbpedia.org/resource/"+str(input)+"> LIMIT 5"
    sparql.setQuery(query)  # the previous query as a literal string
    q = sparql.query().convert()
    # return q['results']['bindings'][0]['property']['value'] 
    return q

def get_description():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(CSV)
    query = """PREFIX dbres: <http://dbpedia.org/resource/>
        DESCRIBE dbres:NASA
        LIMIT 10"""
    sparql.setQuery(query)  # the previous query as a literal string

    return sparql.query().convert()


    
    # return result

if __name__ == "__main__":
    try:
        print(get_description() )
        # res = get_result("Alice_and_Bob")
        # print(res)
    except:
        print("Sorry!")
    # get_description()