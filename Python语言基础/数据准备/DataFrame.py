'''
DataFrame数据框适用于存储多行和多列的数据结合，是Series的容器，类似于Excel的二维表格
'''

from pandas import Series
from pandas import DataFrame

#索引可以省略
df = DataFrame({
    'age':Series([26,29,24]),'name':Series(['Ken','Jerry','Ben'])
})
print(df)
'''
访问列：变量名[列名]     如df['name] 访问对应的列
访问行：变量名[n:m]     如df[2:3]   访问n行到m-1行的数据
访问块：变量名.iloc[n1:n2,m1:m2] 如df.iloc[0:3,0:2] 访问n1到（n2-1）行，m1到（m2-1）列的数据
访问指定位置：变量名.at[行名，列名]    访问（行名，列名）位置的数据。如df.at[1,'name']
'''
#获取age列的值
A = df['age'];print(A)
B = df[1:2];print(B) #访问行名时
C = df.iloc[0:2,0:2];print(C)
D = df.at[0,'name'];print(D)
print('------------')

#dataframe的index是可以任意的，不会像Series报错，也可以自己加序列信息
df1 = DataFrame({'age':[21,22,23], 'name':['Ken','John','Jimi']})
df2 = DataFrame(data = {'age':[21,22,23],'name':['Ken','John','Jimi']},
                index=['first','second','third'])
#print(df1,'\n',df2)
print(df1[1:100])
#显示为空
print(df1[2:2])
print(df1[4:1])
print('-----')
#按索引名访问某一行
print(df2['third':"third"])
#按索引名访问多行
print(df2['first':'second'])
#访问列
print(df1['age'])
print(df1[df1.columns[0:1]])
#访问块
print(df1.iloc[0:1,0:1])
#访问位置
print('----')
print(df1.at[1,'name'])
print(df2.at['second','name'])
print('----')
print(df2)
print('----')
#有索引名时再用索引号就会报错
#print(df2.at[1,'name'])

#修改列名
df1.columns=['age2','name2']
print(df1)
#修改行索引
df1.index = range(1,4)
print(df1)
#根据行索引删除,axis=0表示行轴，可以省略
print(df1.drop(1,axis=0))
#根据列名进行删除,axis=1表示列轴，不可省略
print(df1.drop('age2',axis=1))

#第二种删除列的方法
del df1['name2']
print(df1)

#增加列
df1['newColumn'] = [2,4,6]
print(df1)
#增加行，但此方法效率太低
print(len(df2))
df1.loc[len(df1)] = [24,'Keno']
print(df1)
print('----')
df3 = DataFrame([[1,2],[3,4]], columns=list('AB'))
df4 = DataFrame([[5,6],[7,8]], columns=list('AB'))
print(df3,"\n",df4)
#方法一，合并只是简单地"叠加"成新的数据框，不修改index
print('----')
print(df3.append(df4))
#方法二，合并生成一个新的数据框，产生新的index
print(df3.append(df4,ignore_index=True))