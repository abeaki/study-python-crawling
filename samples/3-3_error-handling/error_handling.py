from urllib.request import urlopen
from urllib.error import HTTPError
import gzip

try:
    f = urlopen('http://gihyo.jp/boook')  # Invalid URL
    if f.getheader('Content-Encoding') == 'gzip':
        f = gzip.GzipFile(fileobj=f)

    print(f.read().decode('utf-8'))
except HTTPError as ex:
    print('Error! code: {0}, reason: {1}'.format(ex.code, ex.reason))
