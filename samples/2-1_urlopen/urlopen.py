from urllib.request import urlopen
import gzip

f = urlopen('http://gihyo.jp/book')
if f.getheader('Content-Encoding') == 'gzip':
    f = gzip.GzipFile(fileobj=f)

print(f.read().decode('utf-8'))
