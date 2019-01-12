from SPARQLWrapper import SPARQLWrapper, JSON
import time

def get_result(myurl):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)
    query = "SELECT ?property WHERE { <"+str(myurl)+"> dbo:abstract ?property . }"
    sparql.setQuery(query)  # the previous query as a literal string
    q = sparql.query().convert()
    return q['results']['bindings'][0]['property']['value'] 


if __name__ == '__main__':
    '''
    a = []
    query = "SELECT ?property WHERE { <http://dbpedia.org/resource/Brad_Pitt> dbo:abstract ?property . }"
    a = get_result(query) # unmodified version!
    print(a['results']['bindings'][0]['property']['value'])
    '''
    start_time = time.time()
    f = open('graph_link.txt', 'r')
    fout = open("output.txt", "a")
    for i in f:
        # print(i)
        s = i[1:len(i)-2]
        # print(s)
        a = s.split(',')
        '''print(a[2])
        print(a[5])
        print(a[8])'''
        if "u_src=" in a[2]:
            myurl123 = a[2][7:]
            # print(myurl123)
            u_val = "u_val="+get_result(myurl123)
            a.append(u_val)
            # print(val)
            # print("--------------------")
        if "e_src=" in a[5]:
            myurl123 = a[5][7:]
            # print(myurl123)
            e_val = "e_val="+ get_result(myurl123)
            a.append(e_val)
            # print(val)
            # print("--------------------")
        if "v_src=" in a[8]:
            myurl123 = a[8][7:]
            # print(myurl123)
            v_val = "v_val="+get_result(myurl123)
            a.append(v_val)
            # print(val)
            # print("--------------------")
        
        fout.write(str(a))
        fout.write("\n")
        

    f.close()
    fout.close()
    print("--- %s seconds ---" % (time.time() - start_time))