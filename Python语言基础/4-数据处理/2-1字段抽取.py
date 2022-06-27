from pandas import DataFrame
from pandas import read_excel

df = read_excel(r'/Users/pain/Desktop/Python数据及相关的资料.nosync/i_nuc.xls',sheet_name='Sheet4')
print(df.head())
#astype()转换类型
df['电话'] = df['电话'].astype(str)
bands = df['电话'].str.slice(0,3)
areas = df['电话'].str.slice(3,7)
tell = df['电话'].str.slice(7,11)
print(bands,areas,tell)