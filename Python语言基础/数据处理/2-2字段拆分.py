from pandas import DataFrame
from pandas import read_excel
df = read_excel(r'/Users/pain/Desktop/Python数据及相关的资料.nosync/i_nuc.xls',sheet_name='Sheet4')
#IP先转换为str，再删除两侧空格
print(df)
print(df['IP'].str.strip())
#按第一个"."分成两列，1表示新增列数
newDF = df['IP'].str.split('.',1,True)
newDF.columns=['IP','IP2-4']
