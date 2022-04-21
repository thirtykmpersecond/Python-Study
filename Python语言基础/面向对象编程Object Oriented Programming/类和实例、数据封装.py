'''
面向对象变成中最重要的概念就是类Class和实例Instance，
必须牢记类是抽象的模板，而实例是根据类创建出来的一个个具体的“对象”
每个对象都拥有相同的方法，但各自的数据可能不同。

对象一般存储在堆区，变量一般存储在栈区

'''
#Python中是通过class关键字定义类,Class后紧跟类名
#类可以起到模板的作用，因此可以在创建实例的时候把一些我们认为必须绑定的属性强制填进去
#通过定义一个特殊的__init__方法，在创建实例的时候把name，tell等属性绑上去
class Student(object) :
    def __init__(self,name,tell) :
        self.name = name
        self.tell = tell

        #既然Student实例本身就拥有这些数据，要访问这些数据就没必要通过外面的函数去访问
        #直接在内部定义访问数据的函数，将"数据"封装起来，这些封装函数是和类本身关联起来的，称为类的方法
    def printTell(self) :
        print('%s,%s'%(self.name,self.tell))

#定义好类之后可以根据类创造出类的实例，实例是通过类名和()实现的
#实例化对象
#格式： 对象名 = 类名(参数列表)
#注意：没有参数小括号也不能省略
big = Student('Bigben',32323)  #类可以自由的给一个实例绑定变量属性，例如绑定一个name属性
print(big.name);print(big.tell)
print('-----------------------')
big.printTell()