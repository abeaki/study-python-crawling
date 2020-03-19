import feedparser

d = feedparser.parse('rss1.xml')
print(d.feed.title)

for entry in d.entries:
    print(entry.link, entry.title)
