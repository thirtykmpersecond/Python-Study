import pandas as pd
df = pd.DataFrame({
    'a':[1,2,3],'b':['a','b','c'],'c':["A","B","C"]
})
print(df)
#抽取df的index行，并将此行第一列columns[0]赋值为"--"，第二三列同样
line = pd.DataFrame({df.columns[0]:"--", df.columns[1]:"--", df.columns[2]:"--"}, index=[0])
print(line)
#此处[df.loc[:0]不可写为[df.loc[0]
df0=pd.concat([df.loc[:0],line,df.loc[1:]])
print(df0)