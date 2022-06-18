import pandas as pd
df = pd.DataFrame({
    'a':[1,2,3],'b':['a','b','c'],'c':["A","B","C"]
})
print(df)
#抽取df的index行，并将此行第一列columns[0]赋值为"--"，第二三列同样
line = pd.DataFrame({df.columns[0]:"--", df.columns[1]:"--", df.columns[2]:"--"}, index=[0])
print(line)
#此处根据索引名来选取数据，不是索引号
#所以此处不是左开右闭
#此处[df.loc[:0]不可写为[df.loc[0]
df0=pd.concat([df.loc[:0],line,df.loc[1:]])
print(df0)
#等价于
df0=pd.concat([df.loc[0:0],line,df.loc[1:]])
print(df0)
#等价于
df1 = pd.concat([df.iloc[0:1],line,df.loc[1:]])
print(df1)

##重置df0的索引
#`df0`的索引没有重新给出新的索引，需要进行重新设定.

# 方法一：利用`reset_index()`函数给出新的索引，但是原索引将作为新增加的index列，在对新增加的列利用drop函数，删除新增的index列。
df1 = df0.reset_index()
df2 = df1.drop('index', axis=1)
# 方法二：直接对`reset_index()`添加`drop=True`参数，即删除原索引并给出新的索引
df2 = pd.concat([df.loc[:0],line,df.loc[1:]]).reset_index(drop=True)
# 方法三：先找出`df0`对索引长度，`lenth=len(df0.index)`，再利用整数学列函数生成索引：`range(lenth)`，然后把生成的索引赋值给`df0.index`
df0.index=range(len(df0.index))