import numpy as np  #as命名为别名表示为调用
'''
还有reshape、T转置、ufunc、sort等函数具体使用方法查阅相关文档
'''
#将列表转换为numpy中的数组，将一个列表作为元素的嵌套列表可以用np.array()转换为一个多维数组
data1 = [1,2,3,4,5]
array1 = np.array(data1)
print(array1)

data2 = [[1,3,4],[2,5,6]]
array2 = np.array(data2)
print(array2)

#array数组内部的元素必须为相同类型，如数值型或字符型，可以用dtype查询类型,不用加括号
print(array2.dtype)

#需要转换数据格式时，可以使用astype函数
array3 = array1.astype('str')
print(array3)
print(array3.astype('int64'))

#数据计算非常方便，不需要大量循环，可以进行批量运算
print(array1+1)
print(array1 * array1)
print(array1 * 2)

#array数组内的元素访问索引和列表相同，通过方括号与数字进行选择与赋值
print(array1[2])
print(array1[-2:])
array1[1] = 0
print(array1)

print(array2[1])
print(array2[0][1])