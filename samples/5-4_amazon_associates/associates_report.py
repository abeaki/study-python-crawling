import os

from robobrowser import RoboBrowser

# 認証の情報は環境変数から読み込む。
AMAZON_EMAIL = os.environ['AMAZON_EMAIL']
AMAZON_PASSWORD = os.environ['AMAZON_PASSWORD']

# RoboBrowserオブジェクトを作成する。
browser = RoboBrowser(
    # Beautiful Soupで使用するパーサーを指定する。
    parser='html.parser',
    # AmazonアソシエイトへのログインにはブラウザーのUser-Agentを使わないと
    # Cookieが使用できないと表示されてログインできない。
    # ここではFirefoxのUser-Agentを指定している。
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0')

# Amazonアソシエイトのページを開く。
browser.open('https://affiliate.amazon.co.jp/gp/associates/network/main.html')

# サインインページにリダイレクトされていることを確認する。
assert 'Amazon.co.jpへのサインイン' in browser.parsed.title.string

# サインインフォームを埋めて送信する。
# フォームのidはブラウザーの開発者ツールで確認できる。
signin_form = browser.get_form(id='ap_signin_form')
signin_form['email'] = AMAZON_EMAIL  # name="email" という入力ボックスを埋める。
signin_form['password'] = AMAZON_PASSWORD  # name="password" という入力ボックスを埋める。
browser.submit_form(signin_form)

# ログインに失敗する場合は、次の行のコメントを外してHTMLのソースを確認すると良い。
# print(browser.parsed.prettify())

# ログイン後の画面が表示されていることを確認する。
assert 'ホーム' in browser.parsed.title.string

# ページの右上に表示されている売上・注文の情報を表示する。
# ブラウザーの開発者ツールでclass属性の値を確認できる。
# CSSセレクターを,で区切るとOR条件を意味する。
for line_item in browser.select('.line-item, .line-item-total'):
    label = line_item.select_one('.label').string.strip()
    data = line_item.select_one('.data').string.strip()
    print(label, data)
