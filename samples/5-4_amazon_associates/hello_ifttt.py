import requests

event_name = 'associates_report_checked'
IFTTT_API_KEY = '************'

# URLを組み立てる
maker_url = 'https://maker.ifttt.com/trigger/{0}/with/key/{1}'.format(
    event_name, IFTTT_API_KEY)

# キーワード引数dataでパラメータを指定してPOSTリクエストを送る
response = requests.post(maker_url, data={'value1': 'Hello IFTTT from Python!'})

# 正しく呼び出せたことを確認する
assert response.status_code == 200
