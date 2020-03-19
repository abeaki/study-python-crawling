import os
from xml.etree import ElementTree

import amazonproduct

AMAZON_ACCESS_KEY = os.environ['AMAZON_ACCESS_KEY']
AMAZON_SECRET_KEY = os.environ['AMAZON_SECRET_KEY']
AMAZON_ASSOCIATE_TAG = os.environ['AMAZON_ASSOCIATE_TAG']

api = amazonproduct.API(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, 'jp', AMAZON_ASSOCIATE_TAG)

response = api.item_search('All', Keywords='kindle', ResponseGroup='Large')
print(response)

for item in response.Items.Item:
    print(item.ItemAttributes.Title, item.ItemAttributes.FormattedPrice)
