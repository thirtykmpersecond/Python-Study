from pandas import DataFrame
from pandas import read_excel
df = read_excel(r'/Users/pain/Desktop/Python数据及相关的资料.nosync/i_nuc.xls',sheet_name='Sheet4')
print(df[df.电话 == 13322252452])
print(df[df.电话>13500000000])
print(df[df.电话.between(13300000000,19900000000)])
print(df[df.IP.isnull()])
#na=False：不包括NaN值，True为包括
print(df[df.IP.str.contains('222',na=False)])