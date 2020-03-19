from datetime import datetime

import pandas as pd
import matplotlib
# 描画のバックエンドとしてデスクトップ環境が不要なAggを使う
matplotlib.use('Agg')
# 日本語を描画できるようフォントを指定する
matplotlib.rcParams['font.sans-serif'] = 'Hiragino Kaku Gothic Pro, MigMix 1P, IPA Gothic'
import matplotlib.pyplot as plt

# 為替データの読み込み
df_exchange = pd.read_csv(
    'exchange.csv', encoding='cp932', header=1,
    names=['date', 'USD', 'rate'], index_col=0,
    parse_dates=True, skipinitialspace=True)

min_date = datetime(1973, 1, 1)
max_date = datetime.now()

fig = plt.figure()  # figはFigureクラスのオブジェクト
ax1 = fig.add_subplot(3, 1, 1)  # ax1はAxesクラスのオブジェクト
ax1.plot(df_exchange.index, df_exchange.USD, label='ドル・円')
ax1.set_xlim(min_date, max_date)
ax1.set_ylim(50, 250)
ax1.legend(loc='best')
fig.savefig('historical_data.png', dpi=300)
