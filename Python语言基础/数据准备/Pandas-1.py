from pandas import Series
'''
Pandas除了Panel数据结构还有Series和DataFrame两种数据结构，都建立在Numpy的基础上
(1) Series:
一维数组系列，也称序列，与Numpy 中的一维array 类似。
二者与python 基本的数据结构 list 也很相近.
(2) DataFrame:
二维的表格型数据结构。可以将 DataFrame 理解为 Series
的容器。以下的内容主要以 DataFrame 为主
(3）Panel：三维数组，可以理解为 DataFrame 的容器

Series对象本质上是一个NumPy的数组（矩阵），因此Numpy的数组处理函数可以直接对Series进行处理
Series的数据类型没有限制（各种Numpy数据类型）
Series有索引，把索引当作数据的标签Key看待，类似于字典，只是类似，实际上是两组数组
    index：从Numpy数组继承的index对象，保存标签信息
    values：保存值的Numpy数组
Series同时具有数组和字典的功能，因此也支持一些字典的方法
'''

'''
Python常用的3种数据类型为Logical、Numeric、Character
'''

#Series用于存储一行或一列数据，以及与之相关的索引集合,如果为指定索引，则默认从0开始
X = Series(['a',2,'螃蟹'], index = [1,2,3])
print(X)
#print(X[0]) 0不在索引内，会报错KeyError
print(X[1])

#字符串对象需要加引号
A = Series([1,2,3])
print(A)
B = Series([1,2,3],index=[1,2,3])
print(B)
C = Series([1,2,3],index=['A','B','C'])
print(C['A'])

#混合定义一个序列
x = Series(['a', True, 1], index=['first', 'second', 'third'])
print(x[1])     #按照索引号访问
print(x['second']) #按索引名访问

#print(x.append('2'))  不可以追加单个元素，但可以追加系列
x = x.append(Series(['2']))
print(x)

#判断值是否存在，数字型和布尔型时不需要加引号的
print(2 in x.values)
print('2' in x.values)
#切片，python中区间为左开右闭，[1,3)
print(x[1:3])
print('--------------')
#按定位获取,经常用于随机抽样
print(x[[0,'third','first']])
print('----------')

#根据index名称删除，返回一个除x[index]外的序列，真正删除需要一个赋值动作
print(x.drop(0))
print(x)
x = x.drop(0)
print(x)
print('------')
#print(x.index[0])
#x.index[1]能返回index顺序为1的序列名
print(x.drop(x.index[2]))
print('------')
#根据值删除
print(x[2!=x.values])

#通过值访问系列index
print(x.index[x.values == 'a'])

#修改series中的index，可以通过赋值更改，也可以通过reindex的方法,个数一定要和值的个数对应
x.index = [0,1,2]
print(x)

#可以将字典转化为Series
s = Series({'a':1,'b':2,'c':3})
print(s)

#reindex重排序
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d','b','a','c'])
print(obj)
obj2 = obj.reindex(['a','b','c','d','e'])
print(obj2)