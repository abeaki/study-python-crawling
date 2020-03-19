import os

import requests

# Import.ioのAPIキーを環境変数IMPORT_IO_API_KEYから取得する
IMPORT_IO_API_KEY = os.environ['IMPORT_IO_API_KEY']
# Import.ioで作成したAPIのURL（自分で作成したものに置き換えてください）
API_URL = 'https://api.import.io/store/connector/014ce271-f8ed-4be3-9675-60f736885b21/_query'
# APIに入力として与えるURL
URL_TO_SCRAPE = 'http://www.apple.com/jp/itunes/charts/free-apps/'

# APIを呼び出す
response = requests.get(API_URL, params={
    '_apikey': IMPORT_IO_API_KEY,
    'input': 'webpage/url:' + URL_TO_SCRAPE,
})

# レスポンスのJSONをデコードしてスクレイピング結果のリストを反復処理する
for item in response.json()['results']:
    # アプリの順位とタイトルを表示する
    print(int(item['number']), item['link_2/_text'])
