#!/bin/sh

DB_PATH=out/mongo_data
mkdir -p $DB_PATH
mongod --dbpath=$DB_PATH
