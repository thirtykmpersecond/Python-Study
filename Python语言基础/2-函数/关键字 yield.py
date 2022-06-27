'''
yield关键字可以将函数执行的中间结果返回值，但不结束程序。
1）可迭代对象包含迭代器。
2）如果一个对象拥有__iter__方法，其是可迭代对象；如果一个对象拥有next方法，其是迭代器。
3）定义可迭代对象，必须实现__iter__方法；定义迭代器，必须实现__iter__和next方法。

下面模仿range()函数写一个自己的range。
'''
def func(n) :
    i = 0
    while i<n :
        yield i         #为什么不是print(i)
        i += 1

for i in func(10) :
    print(i)

'''
yield 关键字的作用就是把一个函数变成一个generator(生成器)。
带有yield的函数不再是一个普通函数，Python解释器会将其视为一个generator。
上面的代码中，若把yield i改为print(i),就获取不到可迭代(iterable)的效果。
'''
#代码1 简单输出斐波那契数列的前N个数
def fab(max) :
    n, x, y = 0, 0, 1
    while n < max :
        print(y)
        x,y = y, x + y       #a = b,b = a+b
        n = n + 1
fab(5)
'''
直接在fab函数中用print函数打印该函数会导致fab函数可复用性较差。
因为fab函数没有返回值(返回None)，其他函数无法获得该函数生成的数列。
若要提高fab函数的复用性，最好不要直接打印数列，而是返回一个列表list。
'''
#代码2 斐波那契数列第二个代码
def fab2(max) :
    n, x, y = 0, 0, 1
    L = []
    while n < max :
        L.append(y)
        x,y = y, x+y
        n += 1
    return L

for n in fab2(5) :
    print(n)

'''
改写后的fab函数通过返回列表能满足复用性的要求，但是该函数在运行中占用的内存会随着参数max的增大而增大。
若要控制内存占用，最好不要用列表来保存中间结果，而是通过可迭代(Iterable)对象来迭代。
'''
def fab3(max) :
    n, x, y = 0, 0, 1
    while n < max :
        yield y    #代替print(y)
        x, y = y, x+y
        n += 1

for i in fab3(5) :
    print(i)

'''
总结：
yield的作用就是把一个函数变成一个generator，带有yield的函数不再是一个普通函数，Python解释器会将其视为一个generator。
调用fab(5)不会执行fab函数，而是返回一个可迭代(Iterable)对象。
在执行for循环时，每次循环都会执行fab函数内部的代码。执行到 'yield b' 时，fab函数就会返回一个迭代值。
下次迭代时，代码从'yield b'的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到遇到yield。
'''