from pandas import DataFrame
from pandas import Series

df = DataFrame({'age':Series([26,85,64]),
                'name':Series(['Ben','John','Jerry'])
                })

df.to_excel('~/Desktop/01.xlsx')
df.to_excel('~/Desktop/02.xlsx')