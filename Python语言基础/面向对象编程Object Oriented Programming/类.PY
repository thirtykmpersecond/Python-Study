'''
在Python中，所有数据类型都可以被是为对象。

#面向过程
#假设要处理学生通讯录，为了表示学生和电话号码见的联系，面向过程的程序可以用一个dict表示
std1 = {'name':'Yubg','tell':66021}
std2 = {'name':'Jerry','tell':67890}
#通过函数实现查看电话号码
def printTell(std) :
    print("%s,%s"%(std['name'],std['tell']))

printTell(std1)
'''
'''
面向对象首先要创建对象，对象有name和tell两个属性(Property)。
若要打印一个学生电话，首先必须创建出这个学生的相应对象，然后给对象发一个printTell消息，让他自己打印出来
'''
#object:基类，超类所有类的父类，一般没有合适的父类就写object，父类可写可不写

'''
构造函数：__init__()    在使用类创建对象的时候自动调用

注意：如果不显示的写出构造函数，默认会自动添加一个空的构造函数
_init_函数（方法）

1.首先说一下，带有两个下划线开头的函数是声明该属性为私有,不能在类地外部被使用或直接访问。 
2.init函数（方法）支持带参数的类的初始化 ，也可为声明该类的属性 
3.init函数（方法）的第一个参数必须是 self（self为习惯用法，也可以用别的名字），后续参数则可 以自由指定，和定义函数没有任何区别。


'''
class Student(object) :
    #创建方法
    #注意：只要是写在类中的方法，第一个参数必须是self
    #self代表类实例(某个对象)/代表当前调用该方法的对象
    def __init__(self,name,tell) :
        self.name = name
        self.tell = tell
    
    def printTell(self) :
        print('%s,%s'%(self.name,self.tell))

#给对象发消息实际上是调用对象对应的关联函数，我们称之为对象的方法(Method)
big = Student('Bigben',83838);big.printTell()
Ji = Student('Jim',93039);Ji.printTell()
'''
面向对象的思想是抽出Class，根Class创建实例(Instance)
面向对象的抽象程度比函数高，因为一个Class既包含数据，又包含操作数据的方法
'''