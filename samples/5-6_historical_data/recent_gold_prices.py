import requests
import lxml.html

# 月次データの最新のページを取得
r = requests.get('http://gold.tanaka.co.jp/commodity/souba/m-gold.php')
html = lxml.html.fromstring(r.text)

# CSVのヘッダーを出力
print('年,月,ドル建価格最高,ドル建価格最低,ドル建価格平均,為替T.T.S.,平均小売価格最高,小売価格最低,小売価格平均')

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

    # columnsをカンマで区切って表示する
    row = ','.join(columns)
    print(row)
