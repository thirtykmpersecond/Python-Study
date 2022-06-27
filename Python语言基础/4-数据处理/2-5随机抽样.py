#逻辑条件切片
import numpy
from pandas import DataFrame
from pandas import read_excel
df = read_excel(r'/Users/pain/Desktop/Python数据及相关的资料.nosync/i_nuc.xls',sheet_name='Sheet4')
print(df[df.电话 >= 18822256753])
print(df[(df.电话>=13422259938)&(df.电话<13822254373)])
"""-------以上方式获取的切片都为DataFrame-------"""
#随机抽取数据
r = numpy.random.randint(0,10,3)
print(r)
#抽取r行数据，也可以直接写成df.loc[r]
print(df.loc[r,:])