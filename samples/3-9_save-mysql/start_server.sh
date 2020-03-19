#!/bin/sh -ex

mysql << EOF
CREATE DATABASE test_scraping;
EOF

mysql.server start
