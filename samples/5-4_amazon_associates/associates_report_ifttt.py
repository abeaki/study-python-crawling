import os

from robobrowser import RoboBrowser
import requests

# 認証の情報は環境変数から読み込む
AMAZON_EMAIL = os.environ['AMAZON_EMAIL']
AMAZON_PASSWORD = os.environ['AMAZON_PASSWORD']
IFTTT_API_KEY = os.environ['IFTTT_API_KEY']


def main():
    # Amazonアソシエイトの売上情報をタプルのリストとして取得する
    report = get_associates_report()
    # 取得した売上情報を表示する
    print(report)
    # タプルのリストからHTMLの文字列を組み立てる
    report_html = '<br>'.join(('{0}: {1}'.format(label, data) for label, data in report))
    # IFTTTを経由して通知する
    notify_ifttt('associates_report_checked', report_html)


def get_associates_report():
    """
    Amazonアソシエイトの売上情報をタプルのリストとして取得する
    """

    # RoboBrowserオブジェクトを作成する
    # AmazonアソシエイトへのログインにはブラウザのUser-Agentを使う必要がある
    browser = RoboBrowser(
        parser='html.parser',
        user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36')

    # Amazonアソシエイトのページを開く
    browser.open('https://affiliate.amazon.co.jp/gp/associates/network/main.html')

    # サインインページにリダイレクトされていることを確認する
    assert 'Amazon.co.jpへのサインイン' in browser.parsed.title.string

    # サインインフォームを埋めて送信する
    signin_form = browser.get_form(id='ap_signin_form')
    signin_form['email'] = AMAZON_EMAIL
    signin_form['password'] = AMAZON_PASSWORD
    browser.submit_form(signin_form)

    # ログインに失敗する場合は、次の行のコメントを外してソースを確認すると良いでしょう
    # print(browser.parsed.prettify())

    # ログイン後の画面が表示されていることを確認する
    assert 'ホーム' in browser.parsed.title.string

    report = []
    # ページの右上に表示されている売上・注文の情報を表示する
    for line_item in browser.select('.line-item, .line-item-total'):
        label = line_item.select_one('.label').string.strip()
        data = line_item.select_one('.data').string.strip()
        report.append((label, data))

    return report


def notify_ifttt(event_name, value1):
    """
    IFTTTを経由して通知する
    """

    # URLを組み立てる
    maker_url = 'https://maker.ifttt.com/trigger/{0}/with/key/{1}'.format(
        event_name, IFTTT_API_KEY)

    # キーワード引数dataでパラメータを指定してPOSTリクエストを送る
    response = requests.post(maker_url, data={'value1': value1})

    # 正しく呼び出せたことを確認する
    assert response.status_code == 200

if __name__ == '__main__':
    main()
