import json
from urllib.request import urlopen
from urllib.parse import urlencode

from sparqlclient import SPARQLClient

client = SPARQLClient("http://ja.dbpedia.org/sparql")
# results = client.query("""
#     SELECT DISTINCT * WHERE {
#         ?s rdf:type schema:Museum .
#     } ORDER BY ?s
# """)
#
# for result in results:
#     print(*[value['value'] for key, value in result.items()])
# print(len(results))

results = client.query("""
SELECT ?s, ?label, SAMPLE(?address) AS ?address, ?lon_degree, ?lon_minute, ?lon_second, ?lat_degree, ?lat_minute, ?lat_second WHERE {
    ?s rdf:type schema:Museum ;
       dbpedia-owl:location ?location .
    ?location dbpedia-owl:country dbpedia-ja:日本 .
    OPTIONAL { ?s rdfs:label ?label } .
    OPTIONAL { ?s prop-ja:所在地 ?address } .
    OPTIONAL {
       ?s prop-ja:経度度 ?lon_degree ;
          prop-ja:経度分 ?lon_minute ;
          prop-ja:経度秒 ?lon_second ;
          prop-ja:緯度度 ?lat_degree ;
          prop-ja:緯度分 ?lat_minute ;
          prop-ja:緯度秒 ?lat_second .
    } .
} ORDER BY ?s
""")

geojson = {
    'type': 'FeatureCollection',
    'features': [],
}

import dbm
import os
import sys
geocoding_cache = dbm.open('geocoding.db', 'c')


def geocode(address):
    if address not in geocoding_cache:
        print('Geocoding {0}...'.format(address), file=sys.stderr)
        url = 'http://geo.search.olp.yahooapis.jp/OpenLocalPlatform/V1/geoCoder?' + urlencode({
            'appid': os.environ['YAHOOJAPAN_APP_ID'],
            'output': 'json',
            'query': address,
        })

        response = json.loads(urlopen(url).read().decode('utf-8'))
        if 'Feature' not in response:
            return None, None
        coordinates = response['Feature'][0]['Geometry']['Coordinates']
        print('Geocoded: {0}'.format(coordinates), file=sys.stderr)
        geocoding_cache[address] = coordinates

    return [float(value) for value in geocoding_cache[address].decode().split(',')]


for result in results:
    values = {key: value['value'] for key, value in result.items()}
    if 'lon_degree' in values:
        lon = float(values['lon_degree']) + float(values['lon_minute']) / 60 + float(values['lon_second']) / 3600
        lat = float(values['lat_degree']) + float(values['lat_minute']) / 60 + float(values['lat_second']) / 3600
    elif 'address' in values:
        lon, lat = geocode(values['address'])
    else:
        lon = None
        lat = None

    label = values.get('label', values['s'])
    address = values.get('address')
    print(lon, lat, label, address)

    if lon is None:
        continue

    geojson['features'].append({
        'type': 'Feature',
        'geometry': {'type': 'Point', 'coordinates': [lon, lat]},
        'properties': {'label': label, 'address': address},
    })

print(len(results))

with open('museums.geojson', 'w') as f:
    json.dump(geojson, f)
