"""
函数的递归是指函数在函数体中直接或间接地调用自身的现象。
递归要有停止条件，否则函数将永远无法跳出递归 ，成了死循环。

斐波那契数列：数列中每一项等于它前面两项的合。
"""

def fib(n):
    if n <= 2:   #不能用if n==1 否则会报错
        return 1
    else:
        return fib(n-1)+fib(n-2)

for i in range(1,10) :
    print('fib(%d)的值为%d'%(i,fib(i)))

"""
函数的嵌套是指在函数中调用另外的函数。这是函数式编程的重要结构，也是我们在编程中最常用的一种程序结构。
"""
#面向对象的编程，在解二元一次方程的过程中，有参数对象，Δ对象，解对象
def argsInput() :
    #定义输入函数
    try :

        A = float(input('请输入A：'))
        B = float(input('请输入B：'))
        C = float(input('请输入C：'))
        #print(type(A),type(B),type(C))
        return A,B,C
    except : #输入出错则重新输入
        print('请重新输入正确的数值类型！')
        return argsInput()             #为了出错时能够重新输入

def getDelta(A,B,C) :      #此处'A,B,C'作为一个整体，并非三个参数
    #计算Δ
    return B**2 - 4*A*C

def slove() :
    A,B,C = argsInput() 
    delta = getDelta(A,B,C)

    if delta<0 :
        print('该方程无解！')
    elif delta == 0 :
        x = -B / 2*A
        print('此方程有一解x = %s'%x)
    else :
        x1 = (B + pow(delta,0.5)) / (-2*A)
        x2 = (B - pow(delta,0.5)) / (-2*A)
        print('此方程有两解x1=%s，x2=%s'%(x1,x2))
#在当前程序下直接执行本程序
def main() :
    slove()
if  __name__ == "__main__":
    main()