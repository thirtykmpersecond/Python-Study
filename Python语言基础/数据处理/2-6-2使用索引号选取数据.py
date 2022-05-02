from pandas import read_excel

df = read_excel(r'/Users/pain/Desktop/Python数据及相关的资料.nosync/i_nuc.xls',sheet_name='Sheet4')
df = df.set_index('学号')
print(df)
#选取第二行、第一列的数据
print(df.iloc[1,0])
#选取第1行和第3行的数据
print(df.iloc[[0,2],:])
#选取第1行到第3行（不包含第3行）数据
print(df.iloc[0:2,:])
#选取所有记录第2列第值，返回一个Series
print(df.iloc[:,1])
#选取第2行数据，返回一个Series
print(df.iloc[1,:])