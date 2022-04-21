'''

try/except主要用于处理程序正常执行过程中出现的一些异常情况
try/finally主要用于监控错误的环节。
-------------------------------------------------

try :
    Normal execution block
except A :
    Exception A handle
except B :
    Exception B handle
except :
    Other exception handle
else :
    if no exception , get here    #可无，若有，则必有except x或except块存在，仅在try后无异常时执行
finally :                         #此语句无比放在最后，并且也是必须执行的语句
    print('finally')

----------------------------------------------------------
最简单的异常处理结构:
try :
    处理代码
except Exception as e :        #捕获错误并输出信息。程序捕获错误后并未终止，还在继续执行后面的代码。
    处理代码发生异常，在这里进行异常处理
'''
try :
    1/0
except ZeroDivisionError :
    print('代码出现除0异常，这里进行处理！')
print('我还没停止运行')

try :
    1/0
except Exception as e :
    print('代码出现除0异常，这里进行处理！')
print('我还没停止运行')

'''
try-except-finally结构
常用于无论程序是否发生异常都要执行必须要执行的操作。 如关闭数据库资源、关闭打开的文件资源等，但必须执行的代码需要放在finally模块中。
'''
try :
    1/0
except Exception as e :
    print('除0异常')
finally :
    print('必须执行')

print('---------------------')

try :
    print('这里没有异常')
except Exception as e :
    print('这句话不会输出')
finally :
    print('这里是必须执行的')

'''---------------------------------------

try-except-else结构
程序进入try语句部分，当try语句部分发生异常则进入except语句部分，若不发生异常则进入else语句部分。
'''
try :
    print('正常代码！')
except Exception as e :
    print('将不会输出这句话')
else :
    print('这句话将被输出')
print('---------------------')
try :
    print(1/0)
except ZeroDivisionError :
    print('进入异常处理')
else :
    print('不会输出')

'''----------------------------------------
try-except-else-finally结构
是try-except-else结构升级版，加入了必须执行的部分。
'''

try :
    print('没有异常！')
except Exception as e :
    print('不会输出！')
else :
    print('进入else！')
finally :
    print('必须输出！')

print('------------------------')

try :
    print(1/0)
except Exception as e :
    print('引发异常！')
else :
    print('不会进入else！')
finally :
    print('必须输出！')