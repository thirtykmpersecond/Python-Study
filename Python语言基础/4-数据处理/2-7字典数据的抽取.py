import pandas as pd
#1. 字典的key和value各作为1列
d1={ 'a':'[1,2,3]','b':'[0,1,2]'}
#将字典d1转换为dataframe，且key列作为index
a1 = pd.DataFrame.from_dict(d1,orient='index')
#将index列名改为Key
a1.index.name = 'Key'
#重新设置index列，并将原来的index设为'key'列
b1 = a1.reset_index()
b1.columns=['key','value']
print(b1)

#2.字典中的每个元素作为一列(同长)
#字典的Value长度必须相等
d2 = {'a':[1,2,3],'b':[4,5,6]}
a2 = pd.DataFrame(d2)
print(a2)

#3. 字典中的每个元素作为一列(不同长)
#字典长度不等，通过Series处理
d3 = {'one':pd.Series([1,2,3]),
      'two':pd.Series([4,5,6,7])}
a3 = pd.DataFrame(d3)
print(a3)

#也可以做如下处理
import numpy
d4 = dict(A = numpy.array([1,2]),B = numpy.array([1,2,3,4]))
print(pd.DataFrame(dict([(k,pd.Series(v)) for k,v in d4.items()])))

#还可以做如下处理
d5 = d4.copy()
a5 = pd.DataFrame.from_dict(d5,orient='index').T
print(a5)