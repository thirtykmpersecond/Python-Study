from pandas import DataFrame
from pandas import Series

df = DataFrame(
    {
        'age':Series([26,85,64]),
        'name':Series(["Ben","John","Jerry"])
    }
)
df.to_excel('d:\\01.xlsx')
df.to_excel('d:\\02.xlsx',index=False)