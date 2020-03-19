from bs4 import BeautifulSoup

# HTMLファイルを読み込んでBeautifulSoupオブジェクトを得る。
with open('index.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

# find_all()メソッドでaタグのリストを取得して、個々のaタグに対して処理を行う。
for a in soup.find_all('a'):
    # href属性とリンクのテキストを取得して表示する。
    print(a.get('href'), a.text)
