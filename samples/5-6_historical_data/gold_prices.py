import sys
import time
from urllib.parse import urljoin

import requests
import lxml.html


def main():
    # 月次データの最新のページを取得する
    start_url = 'http://gold.tanaka.co.jp/commodity/souba/m-gold.php'
    html = fetch(start_url)

    # CSVのヘッダーを出力する
    print('年,月,ドル建価格最高,ドル建価格最低,ドル建価格平均,為替T.T.S.,平均小売価格最高,小売価格最低,小売価格平均')

    # 最新のページからスクレイピングしてCSVで出力する
    scrape(html)

    # 過去のページのURLについて反復処理する
    for url in past_urls(html, start_url):
        # 1ページ取得するごとに1秒のウェイトを挟む
        time.sleep(1)
        # 過去のページからスクレイピングしてCSVで出力する
        scrape(fetch(url))


def fetch(url):
    """
    引数で指定したURLにアクセスし、HtmlElementオブジェクトを取得する
    """

    print('Fetching {0}'.format(url), file=sys.stderr)
    r = requests.get(url)
    html = lxml.html.fromstring(r.text)
    return html

rows_seen = set()  # 表示済みの行を格納するためのsetオブジェクト


def scrape(html):
    """
    引数で指定したHtmlElementオブジェクトから金の価格推移を取得し、CSV形式で出力する
    """

    # 価格表のtr要素の一覧を反復するが、最初の2つはヘッダー行なので無視する
    for tr in html.cssselect('#price_trends_month table tr')[2:]:
        # trの子要素 (td要素) をリストとして取得し、tdsという変数に代入する
        tds = list(tr)

        # trのclass属性にfirstが含まれている場合 (年が含まれている場合) は、
        # tdsの最初の1つをpop(0)で取り除き、その値をcurrent_yearという変数に代入する
        if 'first' in tr.get('class'):
            current_year = tds.pop(0).text

        # 1列目に年 (current_year) を、2列目以降に残りのtdsの値を格納する。
        # 値に数値の桁区切りを表すカンマ (,) が含まれている場合は、
        # Pythonから扱いにくく、CSVの列区切りのカンマと被るので取り除く
        columns = [current_year] + [td.text.replace(',', '') for td in tds]

        # columnsをカンマで区切って表示する。
        # 最新のページと過去のページで一部の行が重複していることがあるので、
        # rows_seenに含まれていない行のみを表示するようにする
        row = ','.join(columns)
        if row not in rows_seen:
            print(row)
            rows_seen.add(row)  # 表示済みの行をrows_seenに追加する


def past_urls(html, start_url):
    """
    引数で指定したHtmlElementオブジェクトと基準となるURLから
    過去のページのURLのリストを取得する
    """

    urls = []
    # ページ内の1つ目の<select>要素の子孫にあたる<option>要素のうち2つ目以降について反復する
    for option in html.cssselect('select')[0].cssselect('option')[1:]:
        # start_urlと<option>要素のvalue属性をurljoinで結合し、得られた絶対URLを表示する
        url = urljoin(start_url, option.get('value'))
        urls.append(url)

    return urls

if __name__ == '__main__':
    main()
