'''
概述：
使用键-值(key-value)存储，具有极快的查找速度

注意：字典是无序的

存储的数据不是key，但是与key有关。value是数据，key是钥匙
key的特性：
1、字典中的key必须唯一
2、key必须是不可变的对象
3、字符串、整数等都是不可变的，可以作为Key
4、list是可变的，不能作为key

dict
1、查找和插入的速度极快，不会随着key-value的增加而变慢
2、需要占用大量的内存，内存浪费多
list
1、查找和插入的速度会随着数据量的增多而减慢
2、占用空间小，浪费内存少
'''
d = {1:10,2:20,'a':12,5:'hello'};print(d,type(d))
d1 = dict(a=1,b=2,c=3);print(d1)

#将二元列表作为元素的列表转换为字典
d2 = dict([['a',12],[6,'a4'],['hel','rt']]);print(d2)

#字典的取值,若没有则会报错
print(d[1]);print(d.get(5))

#字典的复制
dc = d.copy();print(d)

#字典清除
dc.clear();print(dc)

#获取字典的项列表
print(d.items())

#获取字典的key列表,value列表
print(d.keys(),'\n',d.values())

#弹出key = 1项
print(d);print(d.pop(1));print(d)

#字典的遍历
for i in d :
    print(i,d[i])

#取迭代器，tuple和set都可以
iterable = iter(d)
k=next(iterable);print(k,d[k])