from html.parser import HTMLParser
import re


def is_detail_page(url):
    return re.search(r'^http://gihyo\.jp/book/\d+/[\d-]+$', url) is not None


class MyHTMLParser(HTMLParser):

    def __init__(self, *args, **kwargs):
        self.links = []
        self.current_data = []
        self.current_url = None

        super().__init__(*args, **kwargs)

    def handle_starttag(self, tag, attrs):
        #print('Start tag', tag)
        if tag == 'a':
            #print('Start tag', tag, dict(attrs))
            url = dict(attrs).get('href')
            if is_detail_page(url):
                self.current_url = url

    def handle_endtag(self, tag):
        #print('End tag', tag)
        if tag == 'a' and self.current_url:
            title = ''.join(self.current_data)
            if title:
                # ignore links on imgs
                self.links.append({
                    'url': self.current_url,
                    'title': title,
                })
            self.current_data = []
            self.current_url = None

    def handle_data(self, data):
        #print('Data', data)
        if self.current_url:
            self.current_data.append(data)


with open('book.html') as f:
    html = f.read()

parser = MyHTMLParser(convert_charrefs=True)
parser.feed(html)

for link in parser.links:
    print(link['url'], link['title'])
