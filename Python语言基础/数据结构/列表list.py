'''
Python中的列表可作为栈（先进后出表）、队列（先进先出表）等使用。

1、列表定义
只要在[]中添加列表项元素，半角逗号隔开每个元素，即可定义列表。
若要获取列表元素，采用list[index]。
'''
l = [1,2,3,4,5]
print(l[0])
print(l[-1],l[-2])   #倒序取值
print(l[1:3])        #取子列表
print(l[1:],l[:3])   #左闭右开
print(l[:-3])

#list.append(x)     将元素x追加到列表尾部
l.append(0);print(l)

#list.extend(L)     将列表L中所有元素追加到列表尾部形成新的列表
l1 = [6,7,8];l.extend(l1);print(l)

#list.insert(i,x)   在列表的i位置插入x元素
l.insert(1,100);print(l)

#list.remove(x)     将列表中的第一个为x的元素一处。若不存在x将会引发异常。
l.remove(100);print(l)

#list.pop(i)        删除index(序数) 为i的元素，并将删除的元素显示，若不指定i，则默认删除最后一个元素
l.pop(5);print(l)
l.pop();print(l)

#list.split()将字符型转换成list，并以符号切分
s = 'I love Python,and\nyou\t?hehe';print(s)
print(s.split(','));print(s.split('，'));print(s.split())

#list.clear()       清空列表
l.clear();print(l)

#list.index(x)      返回第一个x元素的位置，若不存在x，则报错
l = [1,2,3,4,5];print(l.index(4))
print(l.index(3,1,4),'#后两位参数是范围区间')

#list.count()       统计列表中x元素的个数
print(l.count(4))

#list.reverse()     将列表反向排列    不可用newList = list.reverse()
l.reverse();print(l)

#list.sort()        将列表从小到大排序，若需从大到小，则用list.sort(reverse=True)
l.sort();print(l)
l.sort(reverse=True);print(l)

#list.copy()        返回列表的副本
l1 = l.copy();print(l1)
l1.clear();print(l,l1)
l.clear();print(l,l1)

#list.max(),list.min()  获取最大值最小值

#浅拷贝,相当于给[1，2，3，4，5]贴了两个变量标签，改一个相当于都改了，因为两个变量指向同一内存地址
l2 = [1,2,3,4,5]
l3 = l2
l3[2] = 'x'
print(l3,l2)

#深拷贝，又称内存拷贝
l4 = [1,2,3,4,5]
l5 = l4.copy()
l4.append('y')
print(l4,'\n',l5)

