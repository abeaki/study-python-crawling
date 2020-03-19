import feedparser

# hotentry.rssから読み込む。
d = feedparser.parse('hotentry.rss')

# すべての要素について処理を繰り返す。
for entry in d.entries:
    print(entry.link, entry.title)
