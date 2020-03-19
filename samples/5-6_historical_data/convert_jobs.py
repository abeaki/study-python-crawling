from datetime import datetime

import pandas as pd


def to_datetime(year, month):
    year = int(year[:-1])
    month = int(month[:-1])

    if year >= 63:
        year += 1900
    else:
        year += 2000

    return datetime(year, month, 1)

df = pd.read_excel('第3表.xls', skiprows=3, skip_footer=2, parse_cols='W,Y:AJ', index_col=0)
series = df.stack()
series.index = [to_datetime(y, m) for y, m in series.index]
print(series)


series2 = pd.read_excel('第3表.xls', skiprows=3, skip_footer=2, parse_cols='B,D:O', index_col=0).stack()
series2.index = [to_datetime(y, m) for y, m in series2.index]

import matplotlib.pyplot as plt

series.plot(label='有効求人倍率（季節調整値）')
#pd.DataFrame(series, columns=['有効求人倍率（季節調整値）']).plot()
#plt.ylim(0, 2)
#plt.plot(series2.index, series2, label='有効求人倍率（実値）')
#plt.plot(series.index, series, label='有効求人倍率（季節調整値）')
plt.show()
