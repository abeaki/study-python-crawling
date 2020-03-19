import os
import sys
import json

from requests_oauthlib import OAuth1Session

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

terms = sys.argv[1:]
if not terms:
    print('Usage: stream_api_with_tweepy.py SEARCH_TERM [SEARCH_TERM]...')
    exit(1)

twitter = OAuth1Session(CONSUMER_KEY,
                        client_secret=CONSUMER_SECRET,
                        resource_owner_key=ACCESS_TOKEN,
                        resource_owner_secret=ACCESS_TOKEN_SECRET)

response = twitter.get('https://stream.twitter.com/1.1/statuses/filter.json',
                       params={'track': ','.join(terms)},
                       stream=True)

for line in response.iter_lines(delimiter=b'\r\n'):
    if line == b'':
        continue

    status = json.loads(line.decode('utf-8'))

    if 'limit' in status:
        continue  # Ignore limit message

    try:
        print('@' + status['user']['screen_name'], status['text'])
    except TypeError:
        print(status)
        exit(1)
