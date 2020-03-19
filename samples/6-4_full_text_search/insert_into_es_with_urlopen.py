# coding: utf-8

import sys
from urllib2 import urlopen

ELASTICSEARCH_URL = 'http://localhost:9200'

with open(sys.argv[1]) as f:
    for line in f:
        response = urlopen(ELASTICSEARCH_URL + '/blogs/blogpost/', line)
        print(response.read())
