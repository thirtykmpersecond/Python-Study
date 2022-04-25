from pandas import DataFrame
from pandas import Series
from pandas import read_excel

df = read_excel(r'~/Desktop/Python数据及相关的资料.nosync/rz.xlsx',sheet_name='Sheet2')
print(df)
#1.缺失数据识别
print(df.isnull())
print(df.notnull())
#2.1 丢弃缺失数据处理
newDF = df.dropna(how = 'all',axis = 1)
print(newDF)
newDF = df.dropna()
print((newDF))
#2.2 替换NaN
print(df.fillna('?'))
#用前一个数值替代缺失值
print(df.fillna(method='pad'))
#用后一个数值替代缺失值
print(df.fillna(method='bfill'))
#用平均数或其他描述性统计量替代
#print(df.fillna(df.mean()))
#为不同列填充不同的值来填补数据
print(df.fillna({'数分':100,'高代':0}))
#清除字符串左、右或首、尾指定的字符
df = DataFrame({'age':Series([26,85,64,85,85]),
                'name':Series(['Ben','John','Jerry','John','John'])})
#默认为空格，中间的不清除
print(df['name'].str.strip('J'))
#删除左/右
print(df['name'].str.lstrip('B'))
print(df['name'].str.rstrip('n'))