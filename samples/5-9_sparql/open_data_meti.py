# See: http://datameti.go.jp/sparql
from sparqlclient import SPARQLClient

client = SPARQLClient('http://datameti.go.jp/sparql')
results = client.query('select * where {?s ?p ?o} limit 100')

for result in results:
    print(result)
