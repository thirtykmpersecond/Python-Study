import pandas as pd
from pandas import read_excel
df = pd.read_excel(r'~/Desktop/Python数据及相关的资料.nosync/i_nuc.xls',sheet_name='Sheet3')

#单值替换
df.replace('作弊',0)
#指定列单值替换
#0替换"体育"列中的"作弊"
df.replace({'体育':'作弊'},0)
#0替换"体育"列中的"作弊"以及"军训"列中的"缺考"
df.replace({'体育':'作弊','军训':'缺考'},0)

#多值替换
df.replace(['成龙','周怡'],['陈龙','周毅'])
df.replace({'成龙':'陈龙','周怡':'周毅'})
df.replace({'成龙','周怡'},{'陈龙','周毅'})