'''
在Python中，定义一个函数是通过def关键字声明的：

def 函数名(参数) :
    函数体
    return 返回值
'''
def f(x,y) :

    z = x**2 + pow(y,2)
    return z

res = f(2,3)
print(res)