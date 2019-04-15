PREFIX ab: <http://dbpedia.org/resource/> 

SELECT ?s ?o
WHERE
{ ab:Alice  ?s ?o .
ab:Bob ?s ?o .
 } LIMIT 100
