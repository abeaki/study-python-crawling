import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scopes)

gc = gspread.authorize(credentials)

# credentials.jsonのclient_emailに共有したスプレッドシートのみ読み取れる
worksheet = gc.open("QiitaでPythonのタグが付いた投稿").sheet1

records = worksheet.get_all_records(head=4)
for record in records:
    print(record['投稿のタイトル'])
    print(record['投稿のURL'])
