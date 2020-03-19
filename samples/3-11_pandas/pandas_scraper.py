import pandas

url = 'https://www.nta.go.jp/taxanswer/shotoku/2260.htm'
dataframes = pandas.io.html.read_html(url)

print(dataframes[0])
