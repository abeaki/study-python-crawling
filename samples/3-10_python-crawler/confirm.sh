#!/bin/sh

mongo scraping --eval 'var c = db.books.find(); while (c.hasNext()) { printjson(c.next()); }'
