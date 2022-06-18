# DataFrame

DataFrame数据框是用于存储多行和多列的数据集合，是Series的容器，类似于Excel的二维表格，对于DataFrame的操作也是“增、删、改、查”

## 创建DataFrame时索引可以省略
```python
from pandas import Series
from pandas import DataFrame

df = DataFrame({
    'age':Series([26,29,24]),'name':Series(['Ken','Jerry','Ben'])
})
print(df)
```

## 获取age列的值

1. 访问列：`变量名[列名]`     如`df['name']` 访问对应的列
2. 访问行：`变量名[n:m]`     如`df[2:3]`   访问n行到m-1行的数据
3. 访问块：`变量名.iloc[n1:n2,m1:m2]` 如`df.iloc[0:3,0:2]` 访问n1到（n2-1）行，m1到（m2-1）列的数据
4. 访问指定位置：`变量名.at[行名，列名]`    访问（行名，列名）位置的数据。如`df.at[1,'name']`

```python
A = df['age'];print(A)
B = df[1:2];print(B) #访问行名时
C = df.iloc[0:2,0:2];print(C)
D = df.at[0,'name'];print(D)
```
## DataFrame的index
+ DataFrame的index可以是任意的，不会像Series报错，也可以自己加序列信息
+ key值作为列名[clomuns]
```python
df1 = DataFrame({'age':[21,22,23], 'name':['Ken','John','Jimi']})
df2 = DataFrame(data = {'age':[21,22,23],'name':['Ken','John','Jimi']},
                index=['first','second','third'])
```

## 访问部分行时，不能仅用index访问
```python
#访问1-99行的数据
df[1:100]
#显示为空
print(df1[2:2])
print(df1[4:1])
print('-----')
```
## 按索引名访问某一行/多行
```python
df2['third':'third']
df2['first':'second']
```

## 访问列
```python
df1['age']
df1[df1.colmns[0:1]]
```

## 访问块
```python
df1.iloc[0:1,0:1]
```

## 访问位置
```python
df1.at[1,'name']
df2.at['second','name']
```
+ 有索引名时再用索引号就会报错

## 修改列名
```python
df1.columns=['age2','name2']
```

## 修改行索引
```python
df1.index = range(1,4)
```

## 根据行索引删除
```python
df1.drop(1,axis=0)
```
+ axis=0表示行轴，可以省略

## 根据列名删除
```python
df1.drop('age2',axis = 1)
#第二种删除列的方法
del df1['name2']
print(df1)
```
+ axis=1表示列轴，不可省略

## 增加列
```python
df1['newColumn'] = [2,4,6]
```

## 增加行
```python
#此方法效率太低
print(len(df2))
df2.loc[len(df2)] = [24,'Keno']
print(df2)
#方法一，合并只是简单地"叠加"成新的数据框，不修改index
print('----')
#此处构造dataframe按照行填入
df3 = DataFrame([[1,2],[3,4]], columns=list('AB'))
df4 = DataFrame([[5,6],[7,8]], columns=list('AB'))
print(pandas.concat([df3,df4]))
#方法二，合并生成一个新的数据框，产生新的index
print(pandas.concat([df3,df4],ignore_index=True))
```