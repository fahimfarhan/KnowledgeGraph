PREFIX db: <http://dbpedia.org/resource/>
SELECT distinct *
  WHERE 
  { ?s ?o db:Europe . 
    FILTER NOT EXISTS {db:UK ?o ?p }
  }
 LIMIT 50