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
DataFrame的index可以是任意的，不会像Series报错，也可以自己加序列信息
```python

```