import re
import sqlite3
from urllib.request import urlopen
from html import unescape

def main():
    """
    メイン処理。fetch(), scrape(), save()の３つの函数を呼び出す。
    """

    html = fetch('https://sample.scraping-book.com/dp')
    books = scrape(html)
    save('books.db', books)


def fetch(url):
    """
    引数urlで与えられたURLのWebページを取得する。
    WebページのエンコーディングはContent-Typeヘッダーから取得する。
    戻り値：str型のHTML
    """

    f = urlopen(url)
    encoding = f.info().get_content_charset(failobj="utf-8")
    html = f.read().decode(encoding)

    return html


def scrape(html):
    """
    引数htmlで与えられたHTMLから正規表現で書籍の情報を抜き出す。
    戻り値：書籍(dict)のリスト
    """

    books = []
    for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):
        url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
        url = 'https://gihyo.jp' + url

        title = re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)
        title = re.sub(r'<.*?>', '', title)
        title = unescape(title)

        books.append({"url": url, "title": title})

    return books


def save(db_path, books):
    """
    引数booksで与えられた書籍のリストをSQLiteデータベースに保存する。
    データベースのパスは引数db_pathで与えられる。
    戻り値：なし
    """

    conn = sqlite3.connect(db_path)

    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS books')

    c.execute('''
        CREATE TABLE books(
            title text,
            url text
        )
    ''')

    c.executemany('INSERT INTO books VALUES(:title, :url)', books)

    conn.commit()

    conn.close()

if __name__ == '__main__':
    main()