from pandas import DataFrame
from pandas import read_excel

df = read_excel(r'/Users/pain/Desktop/数据及相关的资料.nosync/rz.xlsx',sheet_name='Sheet2')

print(df.isnull())