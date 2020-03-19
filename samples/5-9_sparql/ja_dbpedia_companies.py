# See: http://qiita.com/pika_shi/items/eb56fc205e2d670062ae

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://ja.dbpedia.org/sparql")
# 東証一部上場企業一覧
# name: 名前, abstract: 概要
sparql.setQuery("""
select distinct ?name ?abstract where {
    ?company <http://dbpedia.org/ontology/wikiPageWikiLink> <http://ja.dbpedia.org/resource/Category:東証一部上場企業> .
    ?company rdfs:label ?name .
    ?company <http://dbpedia.org/ontology/abstract> ?abstract .
}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print(results)
for result in results["results"]["bindings"]:
    print(result["name"]["value"])
