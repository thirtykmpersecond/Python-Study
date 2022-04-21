'''
类可以拥有共有变量和公有方法，也可以有私有变量和私有方法。
公有部分的对象可以从外部访问，私有部分的对象只有在类的内部才可访问。
在普通变量名前加两个'_",即可变成私有变量或方法
'''
class pubAndPri(object) :
    pub = "此pub为共有变量"
    __pri = '此pri为私有变量'

    def __init__(self) :
        self.other = '公有变量other也可以这样定义'
    
    def outPub(self) :
        print('公有方法',self.pub,self.__pri)
    
    def __outPri(self) :
        print('私有方法',self.pub,self.__pri)

pp = pubAndPri()
pp.outPub()         #访问公有方法
print(pp.pub,pp.other)    #访问公有变量

#不能直接调用私有属性
try :
    pp.__outPri()
except Exception as e :
    print('调用私有方法发生错误')

try:
    print(pp.__pri)
except Exception as e:
    print('访问私有变量发生错误！')

'''----------------------------------------------'''
class Person(object) :

    def run(self) :
        print('run')
        print(self.__money)
    def eat(self,food) :
        print('eat ' + food)
    
    def __init__(self,name,age,height,weight,money) :
        print(name,age,height,weight,money)
        #定义属性，self代表当前创造的对象
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__money = money

    #通过内部的方法，修改私有属性
    #通过自定义的方法实现对私有属性的赋值与取值
    def setMoney(self,money) :
        #还可以做数据的过滤
        if money < 0 :
            money = 0
        self.__money = money
    
    def getMoney(self) :
        return self.__money

per = Person('Neng',20,172,60.5,1000000)

#内部属性可以在外部直接赋值
per.age = 10
print(per.age)

#如果要让程序内部的属性不被外部直接访问,在属性前加两个下划线'__'
#在Python中，如果在属性前，加两个下划线，那么这个属性就变成了私有属性(private)/限制访问
#per.__money = 0
#print(per.__money)   #若注释掉per.__money = 0,则会报错'Person' object has no attribute '__money'

#动态语言的添加属性，动态语言的优点之一，
per.a = 100
print(per.a)

#但内部可以使用
#per.run()

per.setMoney(-10)
print(per.getMoney())

#不能直接访问per.__money是因为Python解释器把__money变成了_Person__money
#仍然可以用_Person__money去访问(不建议)，不同版本的编译器解释出的名字不一样
per._Person__money = 1
print(per._Person__money)
print(per.getMoney())

#在Python中 __XXX__属于特殊变量。可以直接访问
#在Python中 _X 的变量，外部是可以直接访问的，但是按照约定的规则，意思是‘虽然我可以被访问，但是请把我视为私有变量，不要直接访问我’
