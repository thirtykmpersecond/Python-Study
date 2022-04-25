from pandas import DataFrame
from pandas import read_excel
df = read_excel(r'/Users/pain/Desktop/Python数据及相关的资料.nosync/i_nuc.xls',sheet_name='Sheet4')
print(df['IP'].str.strip())