# See: http://id.ndl.go.jp/information/about/
from sparqlclient import SPARQLClient

# Accept: */*にしないと406エラーになる。謎実装
#client = SPARQLClient('http://id.ndl.go.jp/auth/ndla', method='GET')
client = SPARQLClient('http://id.ndl.go.jp/auth/ndla', format='xml')
results = client.query('select * where {?s ?p ?o} limit 100')

print(results)
