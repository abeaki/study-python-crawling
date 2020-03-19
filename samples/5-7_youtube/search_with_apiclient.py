import os

from apiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=YOUTUBE_API_KEY)

response = youtube.videos().list(
    maxResults=50,
    part='snippet,contentDetails,statistics,status',
    chart='mostPopular',
    regionCode='JP',
).execute()

for item in response.get('items', []):
    print(item['snippet']['title'])
