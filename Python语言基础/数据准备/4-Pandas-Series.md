# Pandas
Pandas除了Panel数据结构还有Series和DataFrame两种数据结构，都建立在Numpy的基础上
1. Series:一维数组系列，也称序列，与Numpy 中的一维array 类似。 二者与python 基本的数据结构 list 也很相近。
2. DataFrame:二维的表格型数据结构。可以将 DataFrame 理解为 Series 的容器。以下的内容主要以 DataFrame 为主。
3. Panel：三维数组，可以理解为 DataFrame 的容器。
Series对象本质上是一个NumPy的数组（矩阵），因此Numpy的数组处理函数可以直接对Series进行处理。Series的数据类型没有限制（各种Numpy数据类型）
Series有索引，把索引当作数据的标签Key看待，类似于字典，只是类似，实际上是两组数组。
+ index：从Numpy数组继承的index对象，保存标签信息
+ values：保存值的Numpy数组
+ Series同时具有数组和字典的功能，因此也支持一些字典的方法。

***Python常用的3种数据类型为Logical、Numeric、Character***

## Series
Series用于存储一行或一列数据，以及与之相关的索引集合,如果为指定索引，则默认从0开始。

***访问数据可以根据`索引名`访问也可以根据`索引号`访问***
```python
from pandas import Series
X = Series(['a',2,'螃蟹'], index = [1,2,3])
print(X)
#print(X[0]) 0不在索引内，会报错KeyError
print(X[1])
```

## 字符串对象需要加引号
```python
A = Series([1,2,3])
print(A)
B = Series([1,2,3],index=[1,2,3])
print(B)
C = Series([1,2,3],index=['A','B','C'])
print(C['A'])
```

## 混合定义一个序列
```python
x = Series(['a', True, 1], index=['first', 'second', 'third'])
print(x[1])     #按照索引号访问
print(x['second']) #按索引名访问
```

##
```python
x = x.append(Series(['2']))
print(x)

pd.concat([x,Series(['2'])],ignore_index=True)
pandas.concat([x,Series(['2'],index=[4])])
```

**FutureWarning: The `series.append` method is deprecated and will be removed from pandas in a future version. Use `pandas.concat` instead.
  x = x.append(Series(['2']))**
```python
concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False, 
       keys=None, levels=None, names=None, verify_integrity=False, copy=True)
```
+ objs：需要连接的对象集合，一般是列表或字典；
+ axis：连接轴向； 
+ join：参数为‘outer’或‘inner’； 
+ join_axes=[]：指定自定义的索引； 
+ keys=[]：创建层次化索引； 
+ ignore_index=True：重建索引

## 判断值是否存在，数字型和布尔型时不需要加引号
```python
print(2 in x.values)
print('2' in x.values)
```

## 切片，python中区间为左开右闭，数学中：[1,3)
```python
print(x[1:3])
#按定位获取,经常用于随机抽样
print(x[['third','first']]) //需要对多个索引名加中括号，认为是数组
print(x[[0,1]])
```

## 根据index名称删除
```python
print(x.drop('second'))
print(x)
x = x.drop('second')
print(x)
#print(x.index[0])
#x.index[1]能返回index顺序为1的序列名
print(x.drop(x.index[3]))
```

## 根据值删除
```python
#2!=x.values = array([True, False, True])
print(x[2!=x.values])
#x[2!=x.values] = x[[True, False, True]]
```

## 通过值访问访问系列index
```python
print(x.index[x.values == 'a'])
```

## 修改Series中的index
```python
x.index = [0,1,2,3]
print(x)
```
+ **可以通过赋值更改，也可以通过reindex的方法,个数一定要和值的个数对应**

## 将字典转换为Series
```python
s = Series({'a':1,'b':2,'c':3})
print(s)
```

## reindex重设index
```python
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d','b','a','c'])
print(obj)
obj2 = obj.reindex(['a','b','c','d','e'])
print(obj2)
```