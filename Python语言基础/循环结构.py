#while 循环
n = int(input('请输入结束的数：'))

i = 1
su = 0

while i <= n :
    su += i
    i += 1

print("从1加到%d的结果是：%d"%(n,su)) #格式化输出，%d为整数占位符，%s为字符串占位符，%f为浮点型占位符

'''---------------------------------------'''
print('HIS NAME IS %s，%d years old。'%('Spike',20))

'''---------------------------------------'''

n = int(input('请输入结束时候的数:'))

i = 1
su = 0

for i in range( n+1 ) :
    su += i

print('从1加到%d的结果是：%d'%(n,su))

'''---------------------------------------'''
a = range(-1,10,2)
print(list(a),tuple(a))

