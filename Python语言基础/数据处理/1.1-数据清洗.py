from pandas import DataFrame
from pandas import Series
df = DataFrame({'age':Series([26,85,64,85,85]),
                'name':Series(['Ben','John','Jerry','John','John'])})
print(df)
#去重
print(df.duplicated())
print(df.duplicated('name'))
print(df.drop_duplicates('age'))