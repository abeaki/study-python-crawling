from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt


def main():
    df_quote = pd.read_csv('quote.csv', header=2, parse_dates=[0], index_col=0)
    #quote.columns.values[0] = 'date'
    #df_quote.rename(columns={'Unnamed: 0': 'date'}, inplace=True)
    #print(df_quote)

    df_exchange = pd.read_csv(
        'nme_R031.9873.20150912204956.01.csv', encoding='cp932',
        header=1, parse_dates=[0], index_col=0,
        names=['date', 'USD', 'rate'], na_values=['      '])

    #df_gold = pd.read_csv('gold.csv', parse_dates=[[0, 1]], index_col=0)

    df_jgbcm = pd.read_csv(
        'jgbcm_all.csv', encoding='cp932', parse_dates=[0],
        index_col=0, date_parser=parse_japanese_date, na_values=['-'])

    s_jobs = pd.read_excel('第3表.xls', skiprows=3, skip_footer=2, parse_cols='W,Y:AJ', index_col=0).stack()
    s_jobs.index = [to_datetime(y, m) for y, m in s_jobs.index]

    #min_date = max(df_exchange.index.min(), df_jgbcm.index.min(), s_jobs.index.min())
    #max_date = max(df_quote.index.max(), df_jgbcm.index.max()) #, s_jobs.index.max())
    min_date = datetime(1973, 1, 1)
    max_date = datetime.now()

    #print(df_jgbcm)
    #df_jgbcm.plot()

    #df_quote.plot()
    plt.subplot(3, 1, 1)
    #fig, ax = plt.subplots()
    plt.xlim(min_date, max_date)
    #ax.xaxis.set_major_locator(YearLocator(5))
    plt.ylim(50, 250)
    plt.plot(df_quote.index, df_quote.USD)
    plt.plot(df_exchange.index, df_exchange.USD)

    plt.subplot(3, 1, 2)
    plt.xlim(min_date, max_date)
    #ax = plt.twinx()
    plt.plot(df_jgbcm.index, df_jgbcm['1'], label='1年国債金利')
    plt.plot(df_jgbcm.index, df_jgbcm['5'], label='5年国債金利')
    plt.plot(df_jgbcm.index, df_jgbcm['10'], label='10年国債金利')
    plt.legend(loc='best')
    #plt.savefig("image2.png")

    plt.subplot(3, 1, 3)
    plt.xlim(min_date, max_date)
    #plt.plot(df_gold.index, df_gold['ドル建価格平均'], label='ドル建価格平均（ドル／トロイオンス）')
    #plt.plot(df_gold.index, df_gold['小売価格平均'], label='小売価格平均 (円/グラム)')
    #df_jobs.plot(ax=ax)
    plt.ylim(0.0, 2.0)
    plt.axhline(y=1, color='gray')
    plt.plot(s_jobs.index, s_jobs, label='有効求人倍率（季節調整値）')
    plt.legend(loc='best')

    plt.show()


def parse_japanese_date(s):
    """
    >>> parse_japanese_date('S49.9.24')
    datetime.datetime(1974, 9, 24, 0, 0)
    >>> parse_japanese_date('H1.3.16')
    datetime.datetime(1989, 3, 16, 0, 0)
    """

    year, month, day = s.split('.')
    base_years = {'S': 1925, 'H': 1988}
    year = base_years[year[0]] + int(year[1:])

    return datetime(year, int(month), int(day))


def to_datetime(year, month):
    year = int(year[:-1])
    month = int(month[:-1])

    if year >= 63:
        year += 1900
    else:
        year += 2000

    return datetime(year, month, 1)

if __name__ == '__main__':
    main()
