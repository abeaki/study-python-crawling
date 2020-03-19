from urllib.parse import urljoin

import requests
import lxml.html

# 月次データの最新のページを取得
start_url = 'http://gold.tanaka.co.jp/commodity/souba/m-gold.php'
r = requests.get(start_url)
html = lxml.html.fromstring(r.text)

# ページ内の1つ目の<select>要素の子孫にあたる<option>要素のうち2つ目以降について反復する
for option in html.cssselect('select')[0].cssselect('option')[1:]:
    # start_urlと<option>要素のvalue属性をurljoinで結合し、得られた絶対URLを表示する
    url = urljoin(start_url, option.get('value'))
    print(url)
