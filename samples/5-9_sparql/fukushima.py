# See: http://qiita.com/HirofumiYashima/items/6d6fd5cc203f414917d8
from sparqlclient import SPARQLClient

# エンドポイントに?を含めることができない
client = SPARQLClient('https://fukushima.archive-disasters.jp/api/sparql/G0000004lodf?operation=search')
results = client.query('select * where {?s ?p ?o} limit 100')

print(results)
for result in results:
    print(result['s']['value'], result['p']['value'], result['o']['value'])
