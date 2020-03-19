set -ex

curl "https://www.googleapis.com/youtube/v3/search?key=$YOUTUBE_API_KEY&part=snippet&q=手芸&type=video"

curl "https://www.googleapis.com/youtube/v3/videos?key=$YOUTUBE_API_KEY&id=muxH23R0DT0&part=snippet,statistics"

#curl "https://www.googleapis.com/youtube/v3/search?key=$YOUTUBE_API_KEY&part=snippet&order=viewCount&publishedAfter=2015-01-01T00:00:00Z&regionCode=JP&relevanceLanguage=ja&location=35.67966,139.7681&locationRadius=900km&type=video"

#curl "https://www.googleapis.com/youtube/v3/search?key=$YOUTUBE_API_KEY&part=snippet&order=viewCount&publishedAfter=2015-01-01T00:00:00Z&regionCode=JP&relevanceLanguage=ja"

#curl "https://www.googleapis.com/youtube/v3/videos?key=$YOUTUBE_API_KEY&maxResults=50&part=snippet,contentDetails,statistics,status&chart=mostPopular&regionCode=JP"
