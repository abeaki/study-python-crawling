# See: http://qiita.com/pika_shi/items/eb56fc205e2d670062ae

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://ja.dbpedia.org/sparql")
# 日本の市区町村一覧
sparql.setQuery("""
select distinct ?prefectureName ?cityName where {
    ?prefecture <http://dbpedia.org/ontology/wikiPageWikiLink> <http://ja.dbpedia.org/resource/Category:日本の都道府県> .
    ?prefecture a <http://schema.org/AdministrativeArea> .
    ?city <http://dbpedia.org/ontology/location> ?prefecture .
    ?prefecture rdfs:label ?prefectureName .
    ?city a <http://dbpedia.org/ontology/City> .
    ?city rdfs:label ?cityName .
}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print(results)
for result in results["results"]["bindings"]:
    print(result["prefectureName"]["value"], result["cityName"]["value"])
