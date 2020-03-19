from urllib.request import urlopen
from html.parser import HTMLParser
import os
import time


class MyHTMLParser(HTMLParser):

    def __init__(self, *args, **kwargs):
        self.img_urls = set()
        super().__init__(*args, **kwargs)

    def handle_starttag(self, tag, attrs):
        #print('Start tag', tag)
        if tag == 'img':
            #print('Start tag', tag, dict(attrs))
            attrs_dict = dict(attrs)
            url = attrs_dict.get('src')
            if url:
                self.img_urls.add(url)


os.makedirs('out', exist_ok=True)

with open('book.html') as f:
    html = f.read()

parser = MyHTMLParser(convert_charrefs=True)
parser.feed(html)

for img_url in parser.img_urls:
    print('Downloading', img_url)
    f = urlopen(img_url)
    with open('out/{0}'.format(os.path.basename(img_url)), 'bw') as out_file:
        out_file.write(f.read())

    time.sleep(1)
