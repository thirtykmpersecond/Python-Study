import pandas as pd
#from pandas import DataFrame
#from pandas import read_excel

df = pd.read_excel(r'/Users/pain/Desktop/Python数据及相关的资料.nosync/i_nuc.xls',sheet_name='Sheet4')
print(df)
#更改索引为"学号"
df = df.set_index('学号')
#选取a到b行的数据df.loc['a':'b']
print(df.loc[2308024241:2308024201])
#df.loc第一个参数为行标签，第二个参数为列表签（可选参数）
#两个参数既可以是列表也可以是但个字符
#如果两个参数都为列表，则返回DataFrame，否则为Series
print(df.loc[:,'电话'].head())
"--------"
df = pd.DataFrame({'a':[1,2,3],
                   'b':['a','b','c'],
                   'c':["A","B","C"]})
print(df)
#抽取index=1的行，返回的是Series不是DataFrame
print(df.loc[1])
#抽取index=1和2的两行
#当抽取多行时，行的索引必须为列表形式，不能简单地用逗号分隔
#如df.loc[1,2]，会报错
print(df.loc[[1,2]])