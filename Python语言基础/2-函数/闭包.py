'''
所谓闭包其实与回调函数有相通之处。
回调函数是将函数作为参数传递，而闭包是将函数作为返回值返回。
闭包可以延长变量的作用时间与作用域。
'''
def say(word) :
    def name(name) :
        print(word,name)
    return name

hi = say('你好')
hi('小明')

bye = say('再见')
bye('小明')

'''----------------------------------------------'''
#通过此程序更深刻地理解闭包
def func() :  
    res = []

    def put(x) :
        res.append(x)
    
    def get() :
        return res
    return put,get

p,g = func()
p(1);p(2)
print('当前res的值：',g())

p(3);p(4)
print('当前res的值：',g())