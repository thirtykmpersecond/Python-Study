from pandas import DataFrame
from pandas import Series
df = DataFrame({'age':Series([26,85,64,85,85]),
                'name':Series(['Ben','John','Jerry','John','John'])})
#以name为新索引
df1 = df.set_index('name')
#使用loc函数对John用户信息进行提取行数据,ix函数已弃用
#iloc函数是根据索引号提取行数据
print(df1.iloc[1])
print(df1.loc['John'])