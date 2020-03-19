import os

import requests

YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']

response = requests.get('https://www.googleapis.com/youtube/v3/videos',
                        params=dict(
                            key=YOUTUBE_API_KEY,
                            maxResults=50,
                            part='snippet,contentDetails,statistics,status',
                            chart='mostPopular',
                            regionCode='JP',
                        ))

for item in response.json().get('items', []):
    print(item['snippet']['title'])
