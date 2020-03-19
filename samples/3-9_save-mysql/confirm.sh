#!/bin/sh

mysql test_scraping << EOF
SELECT * FROM books;
EOF
