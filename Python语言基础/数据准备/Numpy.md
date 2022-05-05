# Numpy
Numpy的数据结构是`n维的数组对象`，称为`ndarray`。Python中的`List`也可以表示数组，但随着列表数据的增加，效率会降低。

+ 另有reshape、T转置、ufunc、sort等具体函数用法查看相关文档

1. 将列表转换为numpy中的数组
```python
import numpy as np
data1 = [1,2,3,4,5]
array1 = np.array(data1)
print(array1)

data2 = [[1,3,4],[2,5,6]]
array2 = np.array(data2)
print(array2)
```
将一个列表作为元素的嵌套列表可以用np.array()转换为一个多维数组。

2. array数组内部的元素必须为相同类型，如数值型或字符型，可以用dtype查询类型,不用加括号
```python
print(array2.dtype)
```

3. 需要转换数据格式时，可以使用astype函数
```python
array3 = array1.astype('str')
print(array3)
print(array3.astype('int64'))
```

4. 数据计算非常方便，不需要大量循环，可以进行批量运算
```python
print(array1+1)
print(array1 * array1)
print(array1 * 2)
```

5. array数组内的元素访问索引和列表相同，通过方括号与数字进行选择与赋值
```python
print(array1[2])
print(array1[-2:])
array1[1] = 0
print(array1)

print(array2[1])
print(array2[0][1])
```