'''
指的是将函数作为参数传递到另外的函数中执行。例如将A函数作为参数传递到B函数。
然后在B函数中执行A函数。这种好处的做法就是在函数被定义之前就可以使用函数。或对其他程序提供的API进行调用
'''
def func(fun,args) :
    fun(args)

def f1(x) :
    print('这是f1函数',x)

def f2(x) :
    print('这是f2函数',x)

func(f1,1)
func(f2,'hello')