PREFIX db: <http://dbpedia.org/resource/>
select distinct * where {
 ?s ?o db:Europe . 
 db:UK ?o ?p .
}
 LIMIT 50