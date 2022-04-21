#-*- coding: utf-8 -*-
'''
遍历list种丢元素
'''

lis = [1,2,3]

for i in lis :
    #i += 1
    print(i)

ageSeries = [26,85,64]
nameSeries = ['A','B','C']     
print(ageSeries,nameSeries)

'''-----------------------------------'''
A = input('输入：')
print('我刚才输入了：',A)

str1 = 'I\'m a boy.'           #转义符'\'
print(str1)
str2 = "I'm a boy."
print(str2)

'''-----------------------------------'''
print(1 is 2);print(1 is not 2)

#定义复数与返回共轭复数
x = complex(4,1)
y = x.conjugate()
print(x,y)

'''-----------------------------------'''
#求解一元二次方程
a = float(input('请输入二次项系数：'))   #将字符转化为浮点型
b = float(input('请输入一次项系数：'))
c = float(input('请输入常数项：'))

#计算delta
delta = pow(b,2) - 4 * a * c

if delta < 0 :

    print('此方程无解')

elif delta == 0 :

    x = -b / ( 2*a )
    print('此方程有一解，x = ',x)

elif delta >0 :

    x1 = (-b + pow(delta,0.5)) / (2 * a)
    x2 = (-b - pow(delta,0.5)) / (2 * a)

    print('此方程有二解，x1 = %f,x2 = %f'%(x1,x2))
