#!/bin/sh

#curl -XGET 'http://localhost:9200/scraping/books/_search?pretty=true&q=%E3%82%BC%E3%83%AD' | jq .
wget -O - 'http://localhost:9200/scraping/books/_search?q=%E3%82%BC%E3%83%AD' | jq .
