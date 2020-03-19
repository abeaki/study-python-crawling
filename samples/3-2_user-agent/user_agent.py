from urllib.request import urlopen, Request
import gzip

request = Request('http://gihyo.jp/book', headers={
    'User-Agent': 'mybot',
})
f = urlopen(request)
if f.getheader('Content-Encoding') == 'gzip':
    f = gzip.GzipFile(fileobj=f)

print(f.read().decode('utf-8'))
