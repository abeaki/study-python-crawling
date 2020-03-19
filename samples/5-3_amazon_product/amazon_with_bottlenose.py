import os
from xml.etree import ElementTree

import bottlenose

AMAZON_ACCESS_KEY = os.environ['AMAZON_ACCESS_KEY']
AMAZON_SECRET_KEY = os.environ['AMAZON_SECRET_KEY']
AMAZON_ASSOCIATE_TAG = os.environ['AMAZON_ASSOCIATE_TAG']

amazon = bottlenose.Amazon(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOCIATE_TAG,
                           Region='JP')
response = amazon.ItemSearch(Keywords='kindle', SearchIndex='All', ResponseGroup='Large')
response = response.replace(b'xmlns="http://webservices.amazon.com/AWSECommerceService/2011-08-01"', b'')
print(response)

root = ElementTree.fromstring(response)
for item in root.findall('.//Item'):
    print(item.find('.//Title').text, item.find('.//FormattedPrice').text)
