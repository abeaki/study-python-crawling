
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://ja.dbpedia.org/sparql")
# Subject (主語) が東京都であるもの
sparql.setQuery("""
    select distinct * where { <http://ja.dbpedia.org/resource/東京都> ?p ?o . }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print(results)
for result in results["results"]["bindings"]:
    # p: Predicate (述語)
    # o: Object (目的語)
    print(result["p"]["value"], result["o"]["value"])
