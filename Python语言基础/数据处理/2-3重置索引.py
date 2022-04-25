from pandas import DataFrame
from pandas import Series
df = DataFrame({'age':Series([26,85,64,85,85]),
                'name':Series(['Ben','John','Jerry','John','John'])})
#以name为新索引
df1 = df.set_index('name')
#使用ix函数对John用户信息进行提取
print(df1.loc('John'))