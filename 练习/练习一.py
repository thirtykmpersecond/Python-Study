"""def move(man,step) :
    '''
    将man列表向左移动sep单位，最左边的元素向列表后添加。
    相当于队列顺时针移动
    '''
    for i in range(step) :
        item = man.pop(0)
        man.append(item)
        print(man)

def play(man=41,step=3,rest=2) :
    '''
    man：玩家数
    step：杀死第几个人
    rest：幸存者数量
    '''
    print('总共%d个人，每第%d的人自杀，最后剩余%d个人'%(man,step,rest))
    man = [i for i in range(1,man+1)]  #初始化队列
    print('队列：',man)
    step -= 1                            #数量个数，到第三个人时就自杀
    while len(man) > rest :
        move(man,step)
        print('kill',man.pop(0))
    
    return man
servive = play()
print('最后逃生人的编号是：',servive)
"""

#创建一个1到41的数组
L = [i for i in range(1,42)];print(len(L))
kill = []
count = 0
while len(L) != 2 :
    L.append(L.pop(0))
    count += 1
    if 2 == count :
        kill.append(L.pop(0))
        print("kill %d"%kill[-1])
        count=0
print(L)