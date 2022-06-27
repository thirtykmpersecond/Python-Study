'''
遍历函数map函数是内置函数，用于遍历序列。对序列中每个元素进行操作，最终获取新的序列

input(1,2,3)→map(transform)→output(t1,t2,t3)
'''
li=[11,22,33]
newList = map(lambda a: a+100,li);print(type(newList)) #<class 'map'>
print(list(newList))

li = [11,22,33];si = [1,2,3]
newList = map(lambda a,b: a+b,li,si)
print(list(newList))

'''
筛选函数filter函数是内置函数,用于对序列中的元素进行筛选，最终获取符合条件的序列

input(1,2,3)→filter(predict)→output(符合条件)
'''
li = [11,22,33]
newList = filter(lambda x: x>22,li);print(list(newList))

'''
累计函数reduce函数用于对序列内所有元素进行累计操作

input(1,2)→reduce(binary)→output(sum)

reduce的第一个参数是有两个参数的函数，即函数必须要有两个参数
reduce的第二个参数是将要循环的序列
reduce的第三个参数是初始值
'''
from functools import reduce
li = [11,22,33,44]
x = reduce(lambda arg1,arg2: arg1+arg2,li)# ((((1+2)+3)+4)+5)
print(x)

#reduce还可接受第3个可选参数，作为计算的初始值。若把初始值设为100：
print(reduce(lambda arg1,arg2: arg1+arg2,li,100))