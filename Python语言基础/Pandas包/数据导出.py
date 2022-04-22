from pandas import DataFrame
from pandas import Series
df = DataFrame({'age':Series([26,85,64]),
                'name':Series(['Ben','John','Jerry'])
                })
print(df)
df.to_csv('~/Desktop/01.csv')
df.to_csv('~/Desktop/02.csv',index=False)