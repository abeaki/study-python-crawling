import requests
import lxml.html

# 月次データの最新のページを取得
r = requests.get('http://gold.tanaka.co.jp/commodity/souba/m-gold.php')
html = lxml.html.fromstring(r.text)

# <option>要素のvalue属性をすべて表示する
for option in html.cssselect('option'):
    print(option.get('value'))
