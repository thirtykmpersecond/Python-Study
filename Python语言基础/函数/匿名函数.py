'''
python中允许使用lambda关键字定义一个匿名函数。属于‘一次性’函数。
'''
#求两数的合，定义函数f(x,y) = x+y
f = lambda x,y : x+y
print(f(2,3))

#求两数的平方和
print((lambda x,y: x**2 + pow(y,2))(3,4))