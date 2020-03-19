# See: https://creativeweb.jp/archive/8624/
from sparqlclient import SPARQLClient

client = SPARQLClient('http://statdb.nstac.go.jp/lod/sparql')
# 埼玉県の現在の市町村の一覧
results = client.query('''
SELECT ?s ?name WHERE {
  GRAPH ?g { ?s ?p ?o .
    ?s rdf:type sacs:CurrentStandardAreaCode.
    {{
      ?o dcterms:isPartOf sac:C11000-19700401.
    }UNION{
      ?o dcterms:isPartOf ?district.
      ?district dcterms:isPartOf sac:C11000-19700401.
    }}
    ?o sacs:administrativeClass ?ad.
    ?o rdfs:label ?name.
  }
  FILTER( lang(?name) = "ja")
  FILTER( ?ad = sacs:DesignatedCity || ?ad = sacs:CoreCity || ?ad = sacs:SpecialCity ||
    ?ad = sacs:City || ?ad = sacs:Town || ?ad = sacs:Village )
}
''')

for result in results:
    print(result['name']['value'])
