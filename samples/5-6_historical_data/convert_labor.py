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

df = pd.read_excel('lt01-a10.xls', skiprows=[0,1,2,3,4,6,7,8,9], skip_footer=3, parse_cols='A:B,E,H,K,N,Q,T') #, index_col=[0,1])
