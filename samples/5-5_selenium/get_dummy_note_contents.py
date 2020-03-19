import sys

import feedparser


print('Navigating...', file=sys.stderr)

d = feedparser.parse('recommend_first_page.rss')

for entry in d.entries:
    post = {
        'url': entry.link,
        'title': entry.title,
        'description': entry.description,
    }
    print(post)
