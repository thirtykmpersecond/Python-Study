"""
可迭代对象(Iterable)：可以直接作用于for循环的对象统称为可迭代对象。
可以用isinstance()去判断一个对象是否是iterable对象

可以直接作用于for的数据类型一般分两种：
1、集合数据类型，如list、tuple、dict、set、string
2、是generator，包括生成器和带yield的generator function

迭代器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后跑出一个stopIteration错误
       表示无法继续返回下一个值。

可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator对象)
迭代器一定是迭代对象，但迭代对象不一定是迭代器

可以使用isinstance()函数判断是否是Iterator
"""
from collections import Iterable   #判断是否是可迭代对象
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance("",Iterable))
print(isinstance((x for x in range(10)),Iterable))
#print(isinstance(a,Iterable))  报错

from collections import Iterator    #判断是否是迭代器
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance("",Iterator))
print(isinstance((x for x in range(10)),Iterator))

l = (x for x in [22,3,4,2,4,77])
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))

#转成Iterator对象,list对象不是迭代器，直接被next调用会报错
a = iter([1,2,3,4,5,6])
print(next(a))
print(next(a))

print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter(()),Iterator))
print(isinstance(iter(""),Iterator))