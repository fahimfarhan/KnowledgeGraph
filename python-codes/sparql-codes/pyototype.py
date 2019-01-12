from SPARQLWrapper import SPARQLWrapper, JSON

def get_result(query):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    sparql.setQuery(query)  # the previous query as a literal string

    return sparql.query().convert()


if __name__ == '__main__':
    a = []
    query = "SELECT ?property WHERE { <http://dbpedia.org/resource/Brad_Pitt> dbo:abstract ?property . }"
    a = get_result(query) # unmodified version!
    print(a['results']['bindings'][0]['property']['value'])