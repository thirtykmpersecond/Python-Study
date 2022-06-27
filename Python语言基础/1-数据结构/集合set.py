'''
集合(set)是大多数程序语言都会提供的数据结构。他不能保存重复的数据，即具有过滤重复数据的功能。
对于一个数组或者元组来说，也可以用set出去重复数据

set中的元素位置是无序的，因此不能用set[i]这样的方式获取元素
'''
s = {1,2,3,4,1,2,3,4};print(s)

l = [1,2,3,4,1,2,3,4];print(l)
sl = set(l);print(sl)

t = 1,2,3,4,1,2,3,4 ;print(t)
st = set(t);print(st)

#添加     可以添加重复的，但不会有效果
s4 = set([1,2,3,4,5])
s4.add(6)
#s4.add([7,8,9])   TypeError: unhashable type: 'list',set的元素不能是字典、列表，列表是可变对象
s4.add((7,8,9))
print(s4)

#插入整个list、tuple、str会打碎插入
s5 = set([1,2,3,4,5])
s55 = (9,10)
s5.update([6,7,8])
s5.update(s55)
s5.update("neng")
print(s5)

#删除
s6 = set([1,2,3,4,5])
s6.remove(3)
print(s6)

#遍历
s7 = set([1,2,3,4,5])
for i in s7 :
    print(i)
#set是没有索引的不能执行print(s7[3])
#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

for index,data in enumerate(s7) :
    print(index,data)

s1 = set('abcdefg');print(s1)
s2 = set('defghijkl');print(s2)

#提取s1中不包含s2的部分
a1 = s1-s2;print(a1)
a2 = s2-s1;print(a2)
#s1s2的并集
a3 = s1|s2;print(a3)
#s1s2的交集
a4 = s1&s2;print(a4)
#s1s2对称差集(并集但不包括交集)
a5 = s1^s2;print(a5)

L = [i for i in range(1,11)];print(L)
S=set(L);T=tuple(L)
#zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
D = dict(zip(L,L));print(D)
#print(S+S) TypeError: unsupported operand type(s) for +: 'set' and 'set'
#print(D+D) TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
print(L+L)
