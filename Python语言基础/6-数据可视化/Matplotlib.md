***对于`matplotlib`版本在`2.0.0`以上，只需将代码关键字参数`axis_bgcolor`和`axisbg`更换为`facecolor`。***

# 1 使用函数绘制`matplotlib`的图标组成元素

## 1.1 绘制matplotlib图标组成元素的主要函数
在一个图形输出窗口中，底层是一个`Figure`实例，我们通常称之为「画布」，包含一些**可见**和**不可见**的元素。

在画布上，图形是`Axes`实例, Axes实例几乎包含了我们要介绍的matplotlib组成元素，例如`坐标 轴、刻度、标签、线和标记`等。Axes实例有**x轴**和**y轴**属性，也就是可以使用`Axes.xaxis`和`Axes.yaxis`来控制x轴和y轴的相关组成元素，例如**刻度线、刻度标签、刻度线定位器和刻度标签格式器**。

## 1.2 准备数据
`Numpy`是`matplotlib`库的基础。

```python
# 生成图1
import matplotlib.pyplot as plt
import numpy as np

# 绘图
x = np.linspace(0.5,3.5,100)    #在0.5-3.5之间均匀地取100个数
y = np.sin(x)
y1 = np.random.randn(100)       #在正态分布中随机取100个数
```
## 1.3 绘制matplotlib图表组成元素的函数用法

### 1.3.1 `plot()`  展现变量的趋势变化
```python
plt.plot(x, y, ls="-", lw=2, label="plot figure")
```
参数：
+ x：x轴上的数值。 
+ y：y轴上的数值。 
+ ls/linestyle：折线图的线条风格。 **线条风格：`'-/solid', '--/dashed', '-./dashdot', ':/dotted', 'None', ' ', ''`**
+ lw/lineweight：折线图的线条宽度。 
+ label：标记图形内容的标签文本。

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05,10,1000)   #在指定间隔[0.05,10)内返回均匀间隔的1000个数字，
y = np.cos(x)

plt.plot(x,y,ls='-',lw=2,label='plot figure')
plt.legend()    # 显示标签

plt.show()
```

### 1.3.2 `scatter()` 散点图寻找变量间的关系
```python
plt.scatter(x ,y1 ,c="b", label='scatter figure')
```
参数：
+ x：x轴上的数值
+ y：y轴上的数值
+ c/color：散点图中的标记颜色
+ label：标记图形内容的标签文本

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05,10,1000) 
y = np.random.rand(1000)    #可以返回一个或一组服从“0~1”均匀分布的随机样本值。随机样本取值范围是[0,1)，不包括1。

plt.scatter(x,y,label="scatter figure") 
plt.legend() 

plt.show()
```

### 1.3.3 `xlim()` 设置x轴数值显示范围
```python
plt.xlim(xmin, xmax)
```
参数：
+ xlim：x轴上的最小值
+ xmax：x轴上的最大值
+ 平移性：`ylim()`函数用法与此相同

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.random.rand(1000)    #从[0,1)中返回1000个随机值

plt.scatter(x, y, label='scatter figure')
plt.legend()

plt.xlim(0.05,10)
plt.ylim(0,1)

plt.show()
```

### 1.3.4 `xlabel()`设置x轴的标签文本

```python
plt.xlabel("string")
```
参数：
+ string：标签文本内容
+ 同样可作用于`plt.ylabel()`

调用：
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls='-',c='c', label='plot figure')
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show()
```

### 1.3.5 `grid()` 绘制刻度线的网格线

```python
plt.grid(linestyle=":",color='r')
```

参数：

+ linestyle：网格线的线条风格
+ color：网格线线条颜色

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, linestyle='-',linewidth=2, c='c', label='plot figure')
plt.legend()

plt.grid(linestyle=':', color='r')
plt.show()
```

### 1.3.6 `axhline()` 绘制平行于x轴的水平参考线

***水平：horizontal，垂直：vertical***

```python
plt.axhline(y=0.0, c='r', ls='--', lw=2)
```

参数：

+ y：水平参考线的出发点
+ c：参考线的颜色
+ ls/linestyle：参考线的风格
+ lw/linewidth：参考线的宽度
+ 同样可用于`axvline()`上

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, linestyle='-',linewidth=2, c='c', label='plot figure')
plt.legend()

plt.axhline(y=0.0, c='r', ls='--', lw=2)
plt.axvline(x=0.0, color='r', ls='--', lw=2)

plt.show()
```

### 1.3.7 `axvspan()` 绘制垂直于x轴的参考区域

```python
plt.axvspan(xmin=1.0, xmax=2.0, facecolor='y', alpha=0.3)
```

参数：

+ xmin：参考区域的起始位置
+ xmax：参考区域的种植位置
+ facecolor：参考区域的填充颜色
+ alpha：参考区域的填充颜色透明度
+ 可平移到`axhspan()`

```python
import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0.05,10,1000) 
y = np.sin(x)

plt.plot(x, y, ls='-.', lw=2, c='c', label='plot figure')

plt.axvspan(xmin=4.0, xmax=6.0, facecolor='y', alpha=0.3)
plt.axhspan(ymin=0.0, ymax=0.5, facecolor='y', alpha=0.3)

plt.legend() 
plt.show()
```

### 1.3.8 `annotate()`添加图形内容细节的指向性注释文本

```python
plt.annotate("string", xy=(np.pi/2, 1.0), xytext=((np.pi/2)+0.15, 1.5), weight='bold', color='b', arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='b'))
```

参数：

+ string：图形内容的注释文本
+ xy：被注释图形内容的位置坐标。 
+ xytext：注释文本的位置坐标。 
+ style：注释文本的字体风格 `styles=[normal, italic, oblique]`
+ weight：注释文本的字体粗细风格。 `weights=['ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black']`
+ color：注释文本的字体颜色。 
+ arrowprops：指示被注释内容的箭头的属性字典。

```python
import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0.05,10,1000) 
y = np.sin(x)

plt.plot(x, y, ls='-.', lw=2, c='c', label='plot figure')
plt.legend() 

# connectionstyle = angle , angle3, arc, arc3, bar
plt.annotate("maximum", xy=(np.pi/2, 1.0), xytext=((np.pi/2)+1.0, 0.8),style='italic', weight='bold', color='b', arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='b'))

plt.show()
```

### 1.3.9 `text()`添加图形内容细节的无指向型注释文本

```python
plt.text(x, y, "string", weight='bold', color='b')
```

参数：

+ x：注释文本内容所在位置的横坐标。 
+ y：注释文本内容所在位置的纵坐标。 
+ string：注释文本内容。 
+ weight：注释文本内容的粗细风格。 
+ color：注释文本内容的字体颜色。 

```python
import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0.05,10,1000) 
y = np.sin(x)

plt.plot(x, y, ls='-.', lw=2, c='c', label='plot figure')
plt.legend() 

plt.text(3.10, 0.09, "y=sin(x)", weight='bold', color='b')

plt.show()
```

### 1.3.10 `title()`添加图形内容的标题

```python
plt.title('string')
```

参数：

+ string：图形内容文本

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, linestyle='-',linewidth=2, c='c', label='plot figure')
plt.legend()

plt.axhline(y=0.0, c='r', ls='--', lw=2)
plt.axvline(x=0.0, color='r', ls='--', lw=2)

plt.title('y=sin(x)')

plt.show()
```

### 1.3.11 `legend()` 标示不同图形的文本标签图例

```python
plt.legend(loc='lower left')
```

参数：

+ loc：图例在图中的地理位置

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, linestyle='-',linewidth=2, c='c', label='plot figure')
plt.legend(loc='higher right')

plt.axhline(y=0.0, c='r', ls='--', lw=2)
plt.axvline(x=0.0, color='r', ls='--', lw=2)

plt.title('y=sin(x)')

plt.show()
```

位置：`best upper right upper left lower left lower right right center left center right lower center upper center center`

## 1.4 综合应用

```python
from matplotlib.patches import ConnectionStyle
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm as cm

# 定义数据
x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)
y1 = np.random.randn(100)

# 散点图
plt.scatter(x, y1, c='0.25', label='scatter figure')
plt.plot(x, y, ls='--', lw=2, label='plot figure')

####
# some clean up(remove chartjunk)
# turn the top spine and the right spine off
for spine in plt.gca().spines.keys() :
  if spine == 'top' or spine == 'right' :
    plt.gca().spines[spine].set_color('none')

# turn bottom tick for x-axis on
plt.gca().xaxis.set_ticks_position('bottom')
#set tick_line position of bottom

# leave left ticks for y-axis on
plt.gca().yaxis.set_ticks_position("left")
#set tick_line position of left
####

# 设定xy坐标范围
plt.xlim(0.0, 4.0)
plt.ylim(-3, 3.0)

# 设置坐标轴标签
plt.xlabel('x_axis')
plt.ylabel('y_axis')

# 设定xy网格
plt.grid(True, ls=':', color='r')

# 添加水平参考线
plt.axhline(y=0, c='r', ls='--', lw=2)

# 绘制垂直参考区域
plt.axvspan(xmin=1.0, xmax=2.0, facecolor='y', alpha=.3)

# 添加注释信息
plt.annotate('maxmium', xy=(np.pi/2, 1.0), xytext=((np.pi/2)+0.15, 1.5), weight='bold', c='r', arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='r'))
plt.annotate('spines', xy=(0.75, -3), xytext=(0.35, -2.25), weight='bold', c='b', arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='b'))
plt.annotate('', xy=(0,-2.78), xytext=(0.4, -2.32),arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='b'))
plt.annotate('', xy=(3.5,-2.98), xytext=(3.6, -2.7), arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='b'))

# 设置文本信息
plt.text(3.6,-2.7, "'|' is tickline", weight='bold', color='b')
plt.text(3.6, -2.95, "3.5 is ticklabel", weight='bold', color='b')

# 设置标题
plt.title('structure of matploblib')

# legend
plt.legend(loc='best')

plt.show()
```

# 2 使用统计函数绘制简单图形

## 2.1 `bar()` 于绘制柱状图

在x轴上绘制定型数据的分布特征

```python
plt.bar(x,y)
```

参数：

+ x：标示在x轴上的定型数据的类别
+ y：每种定型数据的类别的数量
+ tick_label：横坐标刻度线上的标注
+ hatch：柱状图上的标记
+ bottom：设置y坐标的起点
+ align：bar与刻度对其的方式 `aligns = ['center', 'edge']`

```python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设定使能显示中文
mpl.rcParams['font.sans-serif']=['Arial Unicode MS'] 
# 用来正常显示负号
mpl.rcParams['axes.unicode_minus']=False

# 数据
x = [1,2,3,4,5,6,7,8]
y = [3,1,4,5,8,9,7,2]

# 画图
plt.bar(x, y, align='center', color='c', tick_label=['q','a','c','e','r','j','b','p'], hatch='/') #tick_label 刻度标签

# 设定x、y轴标签
plt.xlabel('箱子编号')
plt.ylabel('箱子重量(kg)')

plt.show()
```

## 2.2 `barh()` 绘制条形图
在y轴上绘制定性数据的分布特征。
```python
plt.barh(x,y)
```
参数：
+ x：表示在y轴上的定性数据的类别
+ y：每种定性数据的类别数量
```python
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

x = [1,2,3,4,5,6,7,8]
y = [3,1,4,5,8,9,7,2]

plt.barh(x, y, align='center', color='c', tick_label=['q','a','c','e','r','j','b','p'], hatch='/')
plt.ylabel('箱子编号')
plt.xlabel('箱子重量(kg)')

plt.show()
```
## 2.3 `hist()` 绘制直方图
```python
plt.hist(x)
```
参数：
+ x：在x轴上绘制箱体的定量数据输入值
+ histtype：要绘制的直方图类型 `histtypes = ['bar', 'barstacked', 'step', 'stepfilled']`
+ align：控制直方图的绘制方式 `aligns = ['left', 'mid', 'right']`

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

boxWeight = np.random.randint(0, 10, 100)
x = boxWeight

bins = range(0, 11, 1)

plt.hist(x, bins=bins, histtype='bar', rwidth=1, alpha=.6)
plt.xlabel('箱子重量(kg)')
plt.ylabel('销售数量')

plt.show()
```

## 2.3 `hist()` 绘制直方图
在x轴上绘制定量数据的分布特征

```python
plt.hist(x)
```
参数：
+ x：在x轴上绘制箱体的定量数据输入值
```python
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

boxWeight = np.random.randint(0, 10, 100)
x = boxWeight

bins = range(0,11,1)
plt.hist(x, bins=bins, color='g', histtype='bar', rwidth=1, alpha=.6)

plt.xlabel('箱子重量(kg)')
plt.ylabel('销售数量')
plt.show()
```
## 2.4 `pie()` 绘制饼图
绘制定型数据的不同类别百分比
```python
plt.pie(x)
```
参数：
+ x：定型数据的不同类别的百分比
```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

kinds = "简易",'保温','行李','密封'
colors = ['#e41a1c','#377eb8','#4daf4a','#984ea3']
soldNums = [0.05, 0.45, 0.15, 0.35]

plt.pie(soldNums, labels=kinds, autopct="%3.1f%%", startangle=60, colors=colors)

plt.title('不同类型箱子的销售数量占比')
plt.show()
```

## 2.5 `polar()` 绘制极线图
```python
plt.polar(theta, r)
```
参数：
+ theta：每个标记所在的射线与极径的夹角
+ r：每个标记到原点的距离
```python
import matplotlib.pyplot as plt
import numpy as np

barSlices = 12
theta = np.linspace(0.0, 2*np.pi, barSlices, endpoint=False)
r = 30*np.random.rand(barSlices)

plt.polar(theta, r, color='chartreuse', lw=2, marker='*', mfc='b', ms=10)

plt.show()
```

## 2.6 `scatter()` 绘制气泡图
而为数据借助气泡大小展示三维数据
```python
plt.scatter(x,y)
```
参数：
+ x：x轴上的数值
+ y：y轴上的数值
+ s：散点标记的大小
+ c：散点标记的颜色
+ cmap：将浮点数映射成颜色的颜色映射表

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

a = np.random.randn(100)
b = np.random.randn(100)

# colormap:RdYlBu
plt.scatter(a, b, s=np.power(10*a+20*b, 2), c=np.random.rand(100), cmap=mpl.cm.RdYlBu, marker='o')
plt.show()
```

## 2.7 `stem()` 绘制棉棒图
绘制离散有序数据
```python
plt.stem(x,y)
```
参数：
+ x：指定棉棒x轴基线上的位置
+ y：绘制棉棒的长度
+ linefmt：棉棒的样式
+ markerfmt：棉棒末端的样式
+ basefmt：指定基线的样式
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5, 2*np.pi, 20)
y = np.random.randn(20)

plt.stem(x, y, linefmt='-.', markerfmt='o', basefmt='-')
plt.show()
```

## 2.8 `boxplot()` 绘制箱线图
绘制箱线图。
```python
plt.boxplot(x)
```
参数：
+ x：绘制箱线图的输入数据
```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

x = np.random.randn(1000)
plt.boxplot(x)

plt.xticks([1], ["随机数生成器AlphaRM"])
plt.ylabel('随机数值')

plt.title('随机数生成器抗干扰能力的稳定性')
plt.grid(axis='y', ls=':', lw=1, c='gray', alpha=.4)
plt.show()
```

## 2.9 `errorbar` 绘制误差棒图
绘制y轴方向或是x轴方向的误差范围
```python
plt.errorbar(x, y, yerr=a, xerr=b)
```
参数：
+ x：数据点的水平位置
+ y：数据点的垂直位置
+ yerr：y轴方向的数据点的误差计算方法
+ xerr：x轴方向的数据点的误差计算方法
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 0.6, 6)
y = np.exp(x)

plt.errorbar(x, y, fmt='bo:', yerr=0.2, xerr=0.02)
plt.xlim(0,0.7)

plt.show()
```

# 3 绘制统计图形

## 3.1 柱状图
是描述统计中使用频率非常高的一种统计图形。它有**垂直样式**和**水平样式**两种效果。
### 3.1.1 应用场景：定型数据的分布展示
柱状图主要是应用在定性数据的可视化场景中，或者是离散型数据的分布展示。
例如，一个本科班级的学生的籍贯分布，出国旅游人士的职业分布以及下载一款App产品的操作系统的分布。
### 3.1.2 绘制原理
重点讲解`bar()`的用法。
```python
import matplotlib as mpl
import matplotlib.pyplot as plt

# 配置字体为 Arial Unicode MS
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# 不实用默认的"Unicode minus"模式来处理坐标轴轴线的刻度标签是负数的情况
mpl.rcParams['axes.unicode_minus'] = False

# Simple data
x = [1, 2, 3, 4, 5]
y = [6, 10, 4, 5, 1]

# Create bar
plt.bar(x, y, align='center', color='b',tick_label=['A', 'B', 'C', 'D', 'E'], alpha=.6)
# 水平方向
#plt.barh(x, y, align='center', color='b',tick_label=['A', 'B', 'C', 'D', 'E'], alpha=.6)


# Set x,y axis label
plt.xlabel('测试难度')
plt.ylabel('试卷份数')

# Set yaxis grid
plt.grid(True, axis='y', ls=':', c='r', alpha=0.3)

plt.show()
```
`plt.bar(x, y, align='center', color='b',tick_label=['A', 'B', 'C', 'D', 'E'], alpha=.6)`
中各个语句含义：
+ x：柱状图中柱体的标签值
+ y：柱状图中柱体的高度
+ align：柱体对其方式，其中`aligns = ['center', 'edge']`
+ color：柱体颜色
+ tick_label：刻度标签值
+ alpha：柱体透明度
+ bottom:柱体在y轴上的起始点，可以是一个数或一组数

## 3.2 条形图
`plt.bar(x, y, align='center', color='b',tick_label=['A', 'B', 'C', 'D', 'E'], alpha=.6)`

## 堆积图
将若干统计图形堆叠起来的统计图形。

### 3.3.1 堆积柱状图
如果将函数`bar()`中的参数`bottom`的取值设定为列表y，列表y1=[2,6,3,8,5]代表另一套试卷的份数，函数`bar(x,y1,bottom=y,color="r")`就会输出堆积柱状图。
```python
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

# some simple date
x = [1, 2, 3, 4, 5]
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]
tick_label = ['A', 'B', 'C', 'D', 'E']

# create bar
plt.bar(x, y, align='center', color='#66c2a5', tick_label=tick_label, label='Class A')
plt.bar(x, y1, align='center', color='#8da0cb', bottom=y, label='Class B')

# set x,y_axis label
plt.xlabel('测试难度')
plt.ylabel('试卷份数')

plt.legend()
plt.show()
```

### 3.3.2 堆积条形图
如果将函数`barh()`中的参数`left`的取值设定为列表y，列表y1=[2,6,3,8,5]代表另一套试卷的份数，函数`barh(x,y1,left=y,color="r")`就会输出堆积条形图。
```python
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

# some simple date
x = [1, 2, 3, 4, 5]
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]
tick_label = ['A', 'B', 'C', 'D', 'E']

# create bar
plt.barh(x, y, align='center', color='#66c2a5', tick_label=tick_label, label='Class A')
plt.barh(x, y1, align='center', color='#8da0cb', left=y, label='Class B')

# set x,y_axis label
plt.xlabel('测试难度')
plt.ylabel('试卷份数')

plt.legend()
plt.show()
```

## 3.4 分块图
如果我们不将多数据以堆积图的形式进行可视化展示，那么就需要借助分块图来对比多数据的分布差异。
同样，分块图可以分为多数据并列柱状图和多数据平行条形图。接下来，我们就结合前面讲过的柱状图和条形图的绘制原理，阐述多数据并列柱状图和多数据平行条形图的绘制方法。

### 3.4.1 多数据并列柱状图
对于堆积柱状图而言，我们也可以选择多数据并列柱状图来改变堆积柱状图的可视化效果。当然，堆积条形图也可以改变可视化效果，呈现多数据平行条形图的图形样式。
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

# some simple data
x = np.arange(5)
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]

bar_width = 0.35
tick_label = ['A','B','C','D','E']

# create bar
# 可以将"width="省略
plt.bar(x, y, width=bar_width, color='c', align='center', label='Class A', alpha = 0.5)
plt.bar(x+bar_width, y1, width=bar_width, color='b', align='center', label='Class B', alpha=0.5)

# set x,y_axis label
plt.xlabel('测试难度')
plt.ylabel('试卷份数')

# set xaxis ticks and ticklabels
plt.xticks(x+bar_width/2, tick_label)
plt.legend()
plt.show()
```

## 3.4.2 多数据平行条形图
对于堆积条形图而言，我们也同样可以选择多数据平行条形图来改变堆积条形图的可视化效果。多数据平行条形图与多数据并列柱状图的实现方法是类似的，只是调用函数由`bar()`变成`barh()`。
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

# some simple data
x = np.arange(5)
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]

bar_width = 0.35
tick_label = ['A','B','C','D','E']

# create bar
# 可以将"width="省略
plt.barh(x, y, height=bar_width, color='c', align='center', label='Class A', alpha = 0.5)
plt.barh(x+bar_width, y1, height=bar_width, color='b', align='center', label='Class B', alpha=0.5)

# set x,y_axis label
plt.xlabel('试卷份数')
plt.ylabel('测试难度')

# set xaxis ticks and ticklabels
plt.yticks(x+bar_width/2, tick_label)
plt.legend()
plt.show()
```

## 3.5 参数探索
 如果想在柱体上绘制装饰线或装饰图，也就是说，设置柱体的填充样式。 我们可以使用关键字参数`hatch`，关键字参数hatch可以有很多取值，例如，`"/","\\","|","-"`等，每种符号字符串都是一种填充柱体的几何样式。而且，符号字符串的符号数量越多，柱体的几何图形的密集程度越高。下面，我们就通过案例进行实现方法的演示。
 ```python
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

# some simple data
x = [1,2,3,4,5]
y = [6, 10, 4, 5, 1]

# create bar
plt.bar(x, y, align='center', color='c', tick_label=['A','B','C','D','E'], hatch='///')

# set x,y_axis label
plt.xlabel('试卷难度')
plt.ylabel('试卷份数')

plt.show()
 ```

## 3.6 直线堆积图、间断条形图和阶梯图
### 3.6.1 `stackplot()`绘制堆积折线图
“堆积折线图是通过绘制不同数据集的折线图而生成的。堆积折线图是按照垂直方向上彼此堆叠且又不相互覆盖的排列顺序，绘制若干条折线图而形成的组合图形。
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6,1)
y = [0,4,3,5,6]
y1 = [1,3,4,2,7]
y2 = [3,4,1,6,5]

labels = ['BluePlanet', 'BrownPlanet', 'GreenPlanet']
colors = ['#8da0cb', '#fc8d62', '#66c2a5']

plt.legend(loc='upper left')
plt.show()
```
+ 本质是将若干条折线放在同一个坐标轴上，以每条折线下部和下方折线作为填充边界线，用一种颜色填充代表此条折线的数值区域。

### 3.6.2 `broken_barh()` 绘制间断条形图
间断条形图是在条形图的基础上绘制而成的，**主要用来可视化定型数据的相同指标在时间维度上的指标的变化情况。实现定型数据的相同指标的变化情况的有效直观比较。
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

plt.broken_barh([(30,100), (180,50), (260,70)], (20,8), facecolors = '#1f78b4')
plt.broken_barh([(60,90), (190,20), (230,30)], (10,8), facecolors = ('#7fc97f', '#beaed4', '#fdc086', '#ffff99'))

plt.xlim(0,360)
plt.ylim(5,35)
plt.xlabel('演出时间')

plt.xticks(np.arange(0,361,60))
plt.yticks([15,25], ['歌剧院A','歌剧院B'])

plt.grid(ls='-', lw=1, color='gray')
plt.title('不同地区的歌剧院的演出时间比较')

plt.show()
```
以语句`plt.broken_barh([(60,90),(190,20),(230,30), (280,60)],(10,8),facecolors=("#7fc97f","#beaed4","#fdc086","#ffff99"))`为例讲解函数的使用方法。
1. 列表`[(60,90),(190,20),(230,30), (280,60)]`的元组表示**从起点是x轴的数值为60的位置起，沿x轴正方向移动90个单位**，其他类似。
2. `(10,8)`表示**从起点是y轴数值为10的位置起，沿y轴正方向移动8个单位。**，其他类似
3. `facecolors`表示每个柱体的填充颜色，这里使用`HEX`模式的颜色表示方法。
4. 通过使用间断条形图，我们就可以清晰直观地观察和比较两家歌剧院演出时间的不同，从而分析它们的演出时间的特点和规律。

### 3.6.3 `step()` 绘制阶梯图
图形本身而言很像折线图，用来反应数据的趋势变化或周期规律。常用在时间序列数据的可视化任务重，凸显时序数据的波动周期和规律。
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,10,10)
y = np.sin(x)

plt.step(x, y, color='#8dd3c7', where='pre', lw=2)
plt.xlim(0,11)
plt.xticks(np.arange(1,11,1))
plt.ylim(-1.2,1.2)

plt.show()
```

通过语句`plt.step(x,y,color="#8dd3c7",lw=2)`就可以绘制出阶梯图，其中参数的含义和用法与函数`plot()`完全相同。
对于`step()`而言，`where`的默认参数值`pre`，标示x轴上的每个数据点对应的y轴数值向左侧绘制水平线指导x轴上的此数据点的左侧相邻数据点位置。
也就是说**x轴上的相邻数据点的取之是按照左开右闭区间进行数据点选取的**。关键字参数还可以选取`post`，表示示左闭右开。

## 3.7 直方图
直方图是用来展现连续型数据分布特征的统计图形。利用直方图我们可以直观地分析出数据的集中趋势和波动情况。本节我们介绍直方图的应用场景和绘制原理。

### 3.7.1 应用场景：定量数据的分布展示
直方图主要是应用在定量数据的可视化场景中，或者是用来进行连续型数据的可视化展示。比如，公共英语考试分数的区间分布、抽样调查中的人均寿命的分布特征以及居民可支配收入的分布特征。

### 3.7.2 绘制原理
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

# set test scores
scoresT = np.random.randint(0,100,100)
x = scoresT

# plot histogram
bins = range(0,101,10)
plt.hist(x, bins=bins, color='#377eb8', histtype='bar', rwidth=10)

# set x,y_axis label
plt.xlabel('测试成绩')
plt.ylabel('学生人数')

plt.show()
```
`plt.hist(x, bins=bins, color='#377eb8', histtype='bar', rwidth=10)`的含义：
+ x：连续性数据输入值
+ bins：用于确定主题的个数或是柱体边缘范围
+ color：柱体颜色
+ hitstype：柱体类型 `histtypes = ['bar', 'barstacked', 'step', 'stepfilled']`
+ label：图例内容
+ rwidth：柱体宽度
+ edgecolor='black': 柱体边缘的填充颜色

代码中`scoresT`代表人数是100人的班级考试成绩，`bins`用来确定每个柱体包含的数据范围。**除了最后一个柱体的范围是闭区间，其他柱体的数据范围都是左闭右开区间**。
例如第一个柱体的数据范围是[0,10)，最后一个柱体的范围是[90,100]。直方图的颜色是蓝色，直方图类型是柱状类型。

### 3.7.3 直方图和柱状图的关系
一方面，直方图和柱状图在展现效果上是非常类似的，只是直方图描述的是连续型数据的分布，柱状图描述的是离散型数据的分布，也可以讲：一个是描述定量数据；另一个是描述定性数据。
另一方面，从图形展示效果来看，柱状图的柱体之间有空隙，直方图的柱体之间没有空隙。直方图和柱状图的展示效果的差别。

### 3.7.4 堆积直方图
我们可以像前面讲过的绘制堆积柱状图那样绘制堆积直方图，用来比较定量数据的分布差异和分布特征。实现方法也非常简单，只需要添加具体的关键字参数就可以实现堆积直方图的绘制任务。
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

# set test scores
scoresT1 = np.random.randint(0,100,100) #返回[0,100)中的100个随机数
scoresT2 = np.random.randint(0,100,100)
x = [scoresT1, scoresT2]

edgecolors =['#ff0000', '#bebaae']
colors = ['#8dd3c7', '#bebada']
labels = ['Class A', 'Class B']

# plot histogram
bins = range(0,101,10)

plt.hist(x,bins=bins, color=colors, histtype='bar', rwidth=1, edgecolor=edgecolors, stacked=True, label=labels)

#set x,y_axis label
plt.xlabel('测试成绩（分）')
plt.ylabel('学生人数')
plt.title('不同班级的测试成绩直方图')

plt.legend(loc='upper left')
plt.show()
```
通过像函数`hist()`传递关键字参数`stacked`来实现堆积直方图的绘制任务。如果不绘制堆积直方图，可以绘制并排放置的直方图，即`stacked=False`。

### 3.7.5 直方图不同形状
将直方图和阶梯图的特点结合起来即可绘制阶梯形直方图。当然也可以绘制堆积阶梯形直方图。我们只需要向函数`hist()`传递关键参数`histtype`就可以绘制阶梯形直方图。
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

# set test scores
scoresT1 = np.random.randint(0,100,100)
scoresT2 = np.random.randint(0,100,100)
x = [scoresT1, scoresT2]
colors = ['#8dd3c7','#bebada']
labels = ['class A', 'class b']
bins = range(0,101,10)

# plot histogram
plt.hist(x, edgecolor='black', bins=bins, color=colors, label=labels, histtype='stepfilled', rwidth=10, stacked=True)

# set x,y_axis label
plt.xlabel('测试成绩')
plt.ylabel('学生人数')
plt.title('不同班级的测试成绩直方图')
plt.legend()

plt.show()
```

## 3.8 饼图
展示定性数据比例分布特征的统计图形。
### 3.8.1 应用场景：定性数据的比例展示
饼图主要应用在定性数据的可视化场景中，或者是用来进行离散型数据的比例展示。如果需要展示参加硕士研究生考试的性别比例、某市一年中四季使用天然气用量的比重以及家庭生活开支用途的比例分布，这些场景都是使用饼图进行数据可视化的不二之选，通过绘制饼图，就可以直观地反映研究对象定性数据的比例分布情况。
### 绘制原理
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

labels = ['A难度水平', 'B难度水平', 'C难度水平', 'D难度水平']
students = [0.35, 0.15, 0.20, 0.30]
colors = ['#377eb8', '#4daf4a', '#984ea3', '#ff7f00']
explode = [0.1, 0.1, 0.1, 0.1]

# exploded pie chart
plt.pie(students, explode=explode, labels=labels, autopct='%3.1f%%', startangle=45, shadow=True, colors=colors)
plt.title('选择难度不同测试试卷的学生百分比')

plt.show()
```
`plt.pie(students, explode=explode, labels=labels, autopct='#%3.1f%%', startangle=45, shadow=True, colors=colors)`中：
+ students：各部分百分比
+ explode：饼片边缘偏离半径的百分比
+ labels：标记每份冰片的文本标签内容
+ autopct：饼片文本标签内容对应的数值百分比样式
+ startangle：从x轴作为其实位置，第一个饼片逆时针旋转的角度
+ shadow：是否绘制阴影
+ colors：饼片的颜色

变量`labels`分别存储四份不同难度的试卷，变量`students`存储选择每套试卷的学生百分比，元组`explode`存储每份饼片边缘偏离相邻饼片边缘的半径长度比例值，关键字参数`autopct`规定百分比保留一位有效数字，关键字参数`startangle`规定第一个饼片的起始角度是以x轴为起点逆时针旋转45°的，关键字参数`shadow`设定饼图中的每份饼片的投影，关键字参数`colors`设定每份饼片的颜色。

### 3.8.3 非分裂式饼图
只需去掉`explode`参数即可，还可设定参数`pctdistance`和`labeldistance`的具体取值，分别控制百分比数值标签和标签值的显示位置，都以半径长度比例值作为显示位置的依据。
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

labels = ['A难度水平', 'B难度水平', 'C难度水平', 'D难度水平']
students = [0.35, 0.15, 0.20, 0.30]
colors = ['#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

# exploded pie chart
plt.pie(students, labels=labels, autopct='%3.1f%%', startangle=45, colors=colors, pctdistance=0.7, labeldistance=1.2)
plt.title('选择难度不同测试试卷的学生百分比')

plt.show()
```

### 3.8.4 案例：绘制内嵌环形饼图
饼图不仅可以用来描述定型数据的比例分布，还可以将多个饼图进行嵌套，从而实现内嵌环形饼图的可视化效果。
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False
elements = ['面粉','砂糖','奶油','草莓酱','坚果']
weight1 = [40, 15, 20,  10,15]
weight2 = [30, 25, 15, 20, 10]
colormapList = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']
inner_colors = colormapList
outer_colors = colormapList
plt.pie(weight1, autopct='%3.1f%%', radius=1, pctdistance=0.85, colors=outer_colors, textprops=dict(color='w'), wedgeprops=dict(width=0.3, edgecolor='w'))
plt.pie(weight2, autopct='%3.1f%%', radius=0.7, pctdistance=0.75, colors=inner_colors, textprops=dict(color='w'), wedgeprops=dict(width=0.3, edgecolor='w'))
plt.legend(elements, fontsize=12, title='配料表', loc='center left', bbox_to_anchor=(0.91,0,0.3,1))
plt.title('不同果酱面包配料比例表')
plt.show()

```

## 3.9 箱线图
箱线图是由一个箱体和一对箱须所组成的统计图形。箱体是由第一四分位数、中位数（第二四分位数）和第三四分位数所组成的。在箱须的末端之外的数值可以理解成离群值，因此，箱须是对一组数据范围的大致直观描述。
### 3.9.1 应用场景：多组定量数据的分布式比较
箱线图主要应用在一系列测量或观测数据的比较场景中，例如学校间或班级间测试成绩的比较，球队中的队员体能对比，产品优化前后的测试数据比较以及同类产品的各项性能的比较，等等，都可以借助箱线图来完成相关分析或研究任务。因此，箱线图的应用范围非常广泛，而且实现起来也非常简单。
### 3.9.2 绘制原理
```python
plt.boxplot(x, notch=None, sym=None, vert=None, whis=None, 
positions=None, widths=None, patch_artist=None, meanline=None,
 showmeans=None, showcaps=None, showbox=None, showfliers=None, 
 boxprops=None, labels=None, flierprops=None, medianprops=None, 
 meanprops=None, capprops=None, whiskerprops=None)
```
+ x：指定要绘制箱线图的数据；
+ notch：是否是凹口的形式展现箱线图，默认非凹口；
+ sym：指定异常点的形状，默认为+号显示；
+ vert：是否需要将箱线图垂直摆放，默认垂直摆放；
+ whis：指定上下须与上下四分位的距离，默认为1.5倍的四分位差；
+ positions：指定箱线图的位置，默认为[0,1,2…] ；
+ widths：指定箱线图的宽度，默认为0.5；
+ patch_artist：是否填充箱体的颜色（True/False）；
+ meanline：是否用线的形式表示均值，默认用点来表示；
+ showmeans：是否显示均值，默认不显示；
+ showcaps：是否显示箱线图顶端和末端的两条线，默认显示；
+ showbox：是否显示箱线图的箱体，默认显示；
+ showfliers：是否显示异常值，默认显示；
+ boxprops：设置箱体的属性，如边框色，填充色等；
+ labels：为箱线图添加标签，类似于图例的作用；
+ filerprops：设置异常值的属性，如异常点的形状、大小、填充色等；
+ medianprops：设置中位数的属性，如线的类型、粗细等；
+ meanprops：设置均值的属性，如点的大小、颜色等；
+ capprops：设置箱线图顶端和末端线条的属性，如颜色、粗细等；
+ whiskerprops：设置须的属性，如颜色、粗细、线的类型等；
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

testA = np.random.randn(5000)
testB = np.random.randn(5000)

testList = [testA,testB]
labels = ['随机数生成器AlphaRM','随机数生成器BetaRM']
colors = ['#1b9e77', '#d95f02']

whis = 1.6
width = 0.35

bplot = plt.boxplot(testList, whis=whis, widths=width, sym='o', labels=labels, patch_artist=True)
for patch,color in zip(bplot['boxes'],colors) :
    patch.set_facecolor(color)  #bplot含有多个对象，bplot['boxes']可以

plt.ylabel('随机数值')
plt.title('生成器抗干扰能力稳定性比较')

plt.grid(axis='y', ls=':', lw=1, color='gray', alpha=.4)
plt.show()
```
代码`plt.boxplot(testList, whis=whis, widths=width, sym='o', labels=labels, patch_artist=True)`中：
+ testList：绘制箱线图的输入数据
+ whis：四分位间距的倍数
+ widths：设置箱体宽度
+ sym：离群值的标记样式
+ labels：绘制每一个数据集的刻度标签
+ patch_artist：是否给箱体添加颜色

使用`mpl.rcParams["axes.unicode_minus"]=False`语句放弃`unicode_minus`的使用，这样图形中的刻度标签值是负数的情况就可以得到合理解决，即负数可以正确显示。
将需要比较的数据放在列表`testList`中，同时作为函数`boxplot()`的参数进行输入。将关键字参数`whis、widths、sym和labels`传入函数`boxplot()`里，完成箱线图的基本绘制工作。
接下来，我们要对箱线图的返回值进行操作，这个返回值是一个字典数据结构，由于需要对箱体添加颜色，所以使用键`boxes`”`来调出键值`“`bplot["boxes"]`。
最后，使用内置函数`zip()`生成元组列表`zip(bplot["boxes"],colors)`，使用for循环对每个箱体进行颜色填充，从而完成整个箱线图的绘制工作。
如果我们将关键字参数`notch`的参数值设置为`True`，同时其他语句保持不变，那么箱体就变成有V型凹痕的箱体了。
箱线图也可以实现水平方向的可视化效果，箱线图中的离群值也可以不显示，这些视图效果分别通过关键字参数`vert`和`showfliers`实现。

### 3.9.3 箱体、箱须、离群值的含义和计算方法


### 3.9.4 水平方向的箱线图
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

x = np.random.randn(1000)
plt.boxplot(x,vert=False,sym='+')

plt.xlabel('随机数值')
plt.yticks([1], ['随机数生成器AlphaRM'], rotation=90)
plt.title('随机数生成器抗干扰能力的稳定性')

plt.grid(axis='x', ls=':', lw=1, color='gray', alpha=.4)
plt.show()
```

### 3.9.5 不绘制离群之的水平放置的箱线图
也有很多时候，我们只需要绘制数据集的分布结构，也就是说，只需要标记出箱须的长度、上四分位数、下四分位数，中位数的位置，即可满足描绘数据集的分布特征的目标。离群之不是重点要考虑的描述统计对象。
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

x = np.random.randn(1000)
plt.boxplot(x, vert=False, showfliers=False)

plt.xlabel('随机数值')
plt.yticks([1], ["随机数生成器AlphaRM"],rotation=90)

plt.title('随机数生成器抗干扰能力的稳定性')
plt.grid(axis='x', ls=':', lw=1, color='gray', alpha=0.4)
plt.show()
```

## 3.10 误差棒图
在很多科学实验中都存在测量误差或是试验误差，这是无法控制的客观因素。这样，在可视化试验结果的时候，最好可以给试验结果增加观测结果的误差以表示客观存在的测量偏差。误差棒图就是可以运用在这一场景中的很理想的统计图形。

### 3.10.1 应用场景：定量数据的误差范围
通过抽样获得样本，对总体参数进行估计会由于样本的随机性导致参数估计值出现波动，因此需要用误差置信区间来表示对总体参数估计的可靠范围。
误差棒就可以很好地实现充当总体参数估计的置信区间的角色。误差棒的计算方法可以有很多种：单一数值、置信区间、标准差和标准误等。
误差棒的可视化展示效果也有很多种样式：水平误差棒、垂直误差棒、对称误差棒和非对称误差棒等。

### 3.10.2 绘制原理
主要讲解函数`errorbar()`的使用方法和参数使用细节。
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 0.6, 10)
y = np.exp(x)

error = 0.05 + 0.15*x

lower_error = error
upper_error = 0.3*error
error_limit = [lower_error, upper_error]

plt.errorbar(x, y, yerr=error_limit, fmt='o', ecolor='y', elinewidth=4, ms=5, mfc='c', mec='r', capthick=1, capsize=2)
plt.xlim(0,0.7)

plt.show()
```
参数：
+ x，y：数据点的位置
+ yerr：单一数值的非对称形式误差范围
+ fmt：数据点的标记样式和数据点标记的连接线样式。 
+ ecolor：误差棒的线条颜色。 
+ elinewidth：误差棒的线条粗细。 
+ ms：数据点的大小。 
+ mfc：数据点的标记颜色。 
+ mec：数据点的标记边缘颜色。 
+ capthick：误差棒边界横杠的厚度。 
+ capsize：误差棒边界横杠的大小。

函数`errorbar()`里的关键字参数`yerr`使用了误差范围的非对称形式，而且是数据点下方的误差范围大于数据点上方的误差范围。关键字参数`xerr`也可以使用类似的误差范围，关键字参数`fmt`如果取`none`值时，数据点的连线、数据点的标记样式和颜色都不显示。”

### 3.10.3 案例1：带误差棒的柱状图
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

# some sample data
x = np.arange(5)
y = [100, 68, 79, 91, 82]

std_err = [7, 2, 6, 10, 5]
error_attri = dict(elinewidth=2, ecolor='black', capsize=3)

# create bar with errorbar
plt.bar(x, y, color='c', align='center', yerr=std_err, error_kw=error_attri, tick_label=['园区1', '园区2','园区3', '园区4', '园区5'])

# set x,y_axis label
plt.xlabel('芒果种植区')
plt.ylabel('收割量')

# set title of axes
plt.title('不同芒果种植区的单词收割量')

# set yaxis grid
plt.grid(True, axis='y', ls=':', color='gray', alpha=.2)
plt.show()
```
绘制带误差棒的柱状图的关键要点，就是函数`bar()`中关键字参数yerr的使用。同时，误差棒的属性和属性值的控制都由关键字参数`error_kw`实现。
这里我们对误差棒的线宽、颜色和误差横帽的粗细进行了进一步的设置。关于函数bar()中的其他关键字参数含义和用法，我们在前面已经讲过，这里就不再详细阐述了。

### 3.10.4 案例2：代误差棒的条形图
如果试图反应定型数据的分布特征，同时还要反应分布的波动特征，那么这种统计图形就是合适选择。
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

# some sample data
x = np.arange(5)
y = [1200, 2400, 1800, 2200, 1600]
std_err = [150, 100, 180, 130, 80]

bar_width = 0.6
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

# create horizontal bar
plt.barh(x,y, bar_width, color=colors, align='center', xerr=std_err, tick_label=['家庭','小说','心理','科技','儿童'])
# set x,y_axis lebel
plt.xlabel('订购数量')
plt.ylabel('图书种类')

# set title
plt.title('大型图书展销会的不同图书种类的采购情况')
# set xaxis grid
plt.grid(True, axis='x', ls=':', color='gray', alpha=.2)

plt.xlim(0, 2600)
plt.show()
```
带误差棒的条形图的绘制是通过使用函数`barh()`中的关键字参数`xerr`实现的。

### 3.10.5 案例3：带误差棒的多数据并列柱状图。
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

# some simple data
x = np.arange(5)
y1 = [100, 68, 79, 91, 82]
y2 = [120, 75, 70, 78, 85]

std_err1 = [7, 2, 6, 10, 5]
std_err2 = [5, 1, 4, 8, 9]

error_attri = dict(elinewidth=2, ecolor='black', capsize=3)
bar_width = 0.4
tick_label=['园区1', '园区2', '园区3', '园区4', '园区5']

# create bar with errorbar
plt.bar(x, y1,width=bar_width, color='#87c33b', align='center', yerr=std_err1, error_kw=error_attri, label='2010')
plt.bar(x+bar_width, y2, bar_width,color='#cd5c5c', align='center', yerr=std_err2, error_kw=error_attri, label='2013')

# set x,y_axis label
plt.xlabel('芒果种植区')
plt.ylabel('收割量')

# set xaxis tick_label
plt.xticks(x+bar_width/2, tick_label)

# set title of axes
plt.title('不同年份的芒果种植区的单次收割量')

#set yaxis grid
plt.grid(True, axis='y', ls=':', color='gray', alpha=0.2)

plt.legend()
plt.show()
```

# 4 完善统计图形

## 4.1 添加图例和标题
在绘图区域中可能会出现多个图形，而这些图形如果不加以说明，观察者则很难识别出这些图形的主要内容。因此，我们需要给这些图形添加标签说明，用以标记每个图形所代表的内容，方便观察者辨识，这个标签说明就是图例。同样，观察者如果想要清楚地了解绘图区域中的内容，就需要给绘图区域添加文本内容用以说明绘图区域的主要内容，标题就可以让观察者清楚地知道绘图区域的核心信息和图表内容。 

我们通过绘制正弦、余弦曲线来说明添加图例和标题的操作方法。为了让读者充分掌握图例和标题的设置方法和操作细节，分别列举调整图例和标题样式展示效果的应用案例，以供读者练习使用。最后结合前面讲过的饼图，用图例的展示形式来代替饼图中饼片的文本标签，从而使读者理解饼图的多种展现形式和图例的多样化用途。

### 4.1.1 图例和标题的设置方法
讲解`legend()`和`title()`的用法。
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y, label=r'$\sin(x)$')
plt.plot(x, y1, label=r'$\cos(x)$')

plt.legend(loc='lower left')
plt.title('正弦函数和余弦函数的折线图')

plt.show()
```

首先，另一条是余弦曲线，为了添加图例，我们需要在函数`plot()`中添加关键字参数`label`，以使图例可以清楚地显示两条曲线分别代表的图形含义。 

然后，通过函数`legend()`添加图例，同时将图例的展示位置放在左下角。为了更加清晰地说明绘图区域的主要内容，我们又添加了标题，通过调用函数`title()`加以实现。

值得注意的是，这里我们是使用matplotlib自带的`TeX`功能来实现对数学表达式支持的。

用TeX对文本内容进行渲染，通过使用`r"$$"`模式，将表达式`\sin`和`\cos`嵌入一对美元符号之间。一般而言，对于在`r"$text1\text2$"`中的非数学表达式文本text1会以斜体形式输出，并且最终输出时就会呈现印刷级别的文档效果。

需要说明的是，在字符串`r"$text1\text2$"`的开始之处有一个标记“r”，表示该字符串是`raw strings`，字符串按照TeX规范进行解析。

### 4.1.2 案例1：图例的展示样式的调整
说到图例的展示样式，就不得不提到图例的外边框、图例中的文本标签的排列位置和图例的投影效果等方面。这些图例的展示样式都是通过图例函数legend()的关键字参数实现的。
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2.1, 0.1)
y = np.power(x,3)
y1 = np.power(x, 2)
y2 = np.power(x, 1)

plt.plot(x, y, ls='-', lw=2, label='$x^{3}$')
plt.plot(x, y1, ls=':', lw=2, label='$x^{2}$')
plt.plot(x, y2, ls='-.', lw=2, label='$x^{1}$')

plt.legend(loc='upper left', bbox_to_anchor=(0.05, 0.95), ncol=3, title='power function', shadow=True, fancybox=True)
plt.show()
```
图例函数`legend()`关键字参数主要有位置参数`loc`，线框位置参数`bbox_to_anchor`，图例标签内容的标题参数`title`和线框阴影`shadow`、线框圆角处理参数`fancybox`等。

### 4.1.3 案例2：标题的展示样式的调整
通过标题函数`title()`关键字参数得以实现。
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 1000)
y = np.exp(x)

plt.plot(x, y, ls='-', lw=2, color='g')
plt.title('center demo')
plt.title('Left Demo', loc='left', fontdict={'size':'xx-large', 'color':'r', 'family':'Times New Roman'})
plt.title('Right Demo', loc='right',family='Comic Sans MS', size=20, style='oblique', color='c')

plt.show()
```
标题函数`title()`的关键字参数主要集中在标题位置参数和标题文本格式参数，标题位置参数值有`left`、`center`和`right`。
标题文本格式参数主要是字体类别`family`、字体大小`size`、字体颜色`color`、字体风格`style`等.
这些文本格式参数可以放在关键字参数`fontdict`的字典中存储，也可以分别作为标题函数`title()`的关键字参数。

### 4.1.4 案例3：带图例的饼图
通过前面对饼图的绘制原理和实例的讲解，我们对饼图的组成元素和函数`pie()`的参数含义也有了一个透彻掌握。
现在，我们就结合本节讲过的图例的相关内容，讲解为饼图添加图例的方法，从而实现绘图区域的清爽布局。
```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

elements = ['面粉', '砂糖', '奶油', '草莓酱', '坚果']
weight = [40, 15, 20, 10, 15]

colors = ["#1b9e77","#d95f02","#7570b3","#66a61e","#e6ab02"]

wedges, texts, autotexts = plt.pie(weight, autopct='%3.1f%%', textprops=dict(color='w'), colors=colors)

plt.legend(wedges, elements, fontsize=12, title='配料表', loc='center left', bbox_to_anchor=(0.91, 0, 0.3, 1))
plt.setp(autotexts, size=15, weight='bold')
plt.setp(texts, size=12)

plt.title('果酱面包配料比例表')
plt.show()
```
通过调用图例函数`plt.legend(wedges,elements)`，我们就可以将**饼片外部的文本标签放在图例中**，而饼片的数值标签仍然放在饼片内部。
函数legend()的参数`wedges`和`elements`分别表示`饼片实例列表`和`文本标签列表`，而且**这两个参数要一起配合使用才可以将饼片外部的文本标签放置在图例内部的任务中。**

`plt.pie()`的返回值是`patches`、`texts`、`autotexts`，都为列表，分别是：
1. `matplotlib.patches.Wedge`实例序列
2. 标签文本实例的列表
3. 数字标签的文本实例列表。只有当参数`autopct`不是`None`时，才会返回。

## 4.2 调整刻度范围和刻度标签
刻度范围是绘图区域中坐标轴的取值区间，包括x轴和y轴的取值区间。刻度范围是否合适直接决定绘图区域中图形展示效果的优劣。

因此，调整刻度范围对可视化效果的影响非常明显。同理，刻度标签的样式也同样影响可视化效果的优劣。 如果我们可以根据具体的数据结构和数据形式采用合适的刻度标签样式，那么不仅可以将数据本身的特点很好地展示出来，也可以让可视化效果变得更加理想。 

通过观察图4.1，细心的读者可能会发现两个可以改进的地方：
1. x轴范围可以缩小，因为图中左右两侧各有一部分空白区域
2. x轴上的刻度标签可以改成以圆周率为单位的刻度标签，这就是本节要探讨的刻度范围和刻度标签的内容。

### 4.2.1 调整刻度范围和刻度标签的方法
通过函数`xlim()`和函数`xticks()`
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)

# set subplot(211)
plt.subplot(211)

# plot figure
plt.plot(x, y)

# set subplot(212)
plt.subplot(212)

# set xlimit
plt.xlim(-2*np.pi, 2*np.pi)

# set xticks
plt.xticks([-2*np.pi, -3*np.pi/2, -1*np.pi, -1*(np.pi)/2, 0, (np.pi)/2, np.pi, 3*np.pi/2, 2*np.pi], 
           [r"$-2\pi$", r'$-3\pi/2$', r'$-\pi$',r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])

# plot figure
plt.plot(x, y)

plt.show()
```
为了加强调整刻度范围和刻度标签前后变化的对比效果，我们将图中的正弦曲线保留，去掉余弦曲线。

同时，我们调用子区函数`subplot()`，关于子区函数`subplot()`的具体用法，在[4.2.2](#4.2.2 函数`subplot()`)节里进行学习。图中上面的一幅图是正弦函数曲线，下面一幅图是改进后的正弦曲线。

具体来讲，我们通过调用`xlim()`函数来改变x轴的刻度范围，使得绘图区域中的图形变得更加紧凑。

我们又通过函数`xticks()`来改变刻度标签。具体而言，就是将刻度标签变成以圆周率为单位的刻度标签，使得图形内容更加便于理解和观察。

同样，我们利用matplotlib的自带`TeX`的功能实现渲染文本内容的需要，通过使用`r"$$"`模式，将`LaTeX`的表达式`\pi`嵌入`r"$$"`中的美元符号之间。

一般而言，对于在`r"$text\pi$"`中的非数学表达式文本text会以斜体形式输出，并且最终输出时就会呈现印刷级别的文档效果。

在字符串`r"$text\pi$"`的开始之处有一个标记r，表示该字符串是`raw strings`，字符串按照`TeX规范`进行解析，通常情况下不可以省略。

# 4.2.2 函数`subplot()`
在代码实现部分我们调用了子区函数`subplot()`，这个函数专门用来绘制几何形状相同的网格区域，子区顾名思义就是将画布分成若干个子画布，这些子画布就构成了几何形状规则且对称的矩形绘图区域，然后在这些绘图区域上分别绘制图形。例如，子区函数subplot(211)和子区函数subplot(212)代表首先在画布上分隔出一个2行1列的画布格式，然后在一个2行1列的画布格式上分别绘制图形1和图形2。 

在一般情况下，刻度标签的数值范围都是升序排列的，也就是说坐标轴的交点是(0,0)原点。但是，在很多科学实验或科学试验的情况中，收集到的原始数据进行可视化展示时，需要将刻度范围调整成降序排列，方便科研人员观测数据的规律和特征。接下来，我们就通过案例加以说明。

+ 在`matplotlib`下，一个`Figure`对象可以包含多个`子图(Axes)`，可以使用`subplot()`快速绘制
```python
subplot(numRows, numCols,plotNum)
```
图标的整个其绘图区域被分为`numRows行`和`numCols列`，然后按照**从左到右、从上到下**的顺序对每个区域进行编号。

|       表格       |       分区       |       演示       |
|:--------------:|:--------------:|:--------------:|
| subplot(2,3,1) | subplot(2,3,2) | subplot(2,3,3) |
| subplot(2,3,4) | subplot(2,3,5) | subplot(2,3,6) |

**如果`numRows`、`numCols`、`plotNum`这三个数都小于10的话，可以把它们缩写为一个整数。例如`subplot(323)`与`subplot(3,2,3)`相同
。**

`subplot`在`plotNum`指定的区域中创建一个轴对象。如果新创建的轴和之前创建的轴重叠，之前的轴将被删除。

在一般情况下，刻度标签的数值范围都是升序排列的，**也就是说坐标轴的交点是(0,0)原点**。但是，在很多科学实验或科学试验的情况中，收集到的原始数据进行可视化展示时，需要将刻度范围调整成降序排列，方便科研人员观测数据的规律和特征。接下来，我们就通过案例加以说明。

### 4.2.3 案例：逆序设置坐标轴刻度标签
通过调整函数`xlim()`参数内容来实现逆序展示刻度标签的可视化需求。

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

time = np.arange(1, 11, 0.5)
machinePower = np.power(time, 2) + 0.7
plt.plot(time, machinePower, ls='-', lw=2, color='r')

plt.xlim(10, 1)
plt.xlabel('使用年限')
plt.ylabel('机器功率')
plt.title('机器损耗曲线')

plt.grid(ls=':', lw=1, color='gray', alpha=.5)
plt.show()
```

通过使用函数`xlim()`实现将`使用年限`的刻度标签值降序排列，其中的关键是将函数`xlim(xmin,xmax)`的参数`xmin`和`xmax`调换顺序，进而变成`xlim(xmax,xmin)`实现的可视化效果。

这样，就可以直观清晰地反映出机器的性能随着使用年限的推移而产生的下降情况。

## 4.3 向统计图形添加表格
通过使用matplotlib可以绘制精美的统计图形，数据可视化的主要作用就是直观地解释数据，以使观察者可以发现数据背后的规律或是趋势变化。但是，有时候为了更加全面地凸显数据的规律和特点，需要将统计图形和数据表格结合使用。例如，在第3章中，我们介绍了饼图的相关知识，但是饼图只是从数据的比例分布角度进行数据可视化展示，如果结合原始数据综合分析数据的特点和规律，那么对数据的可视化展示效果会更加使人印象深刻。这样，我们就从相对角度和绝对角度两方面来全面展示数据的内在特点和意义。 

我们以前面讲过的饼图为例，进一步地向饼图中添加数据表格来全面展示数据的规律特征。 

同时，从多元化分析的角度来看，通过添加数据表格可以借助其他统计图形来揭示数据的深层含义。从而更好地把握数据本身的结构特点、内在规律，进而更加客观地观察和理解数据。

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

labels = ['A难度水平', 'B难度水平', 'C难度水平', 'D难度水平']
students = [0.35, 0.15, 0.20, 0.30]
colors = ['#377eb8', '#4daf4a', '#984ea3', '#ff7f00']
explode = [0.1, 0.1, 0.1, 0.1]

# exploded pie chart
plt.pie(students, explode=explode, labels=labels, autopct='%3.1f%%', startangle=45, shadow=True, colors=colors)
plt.title('选择难度不同测试试卷的学生百分比')

# add tabel to pie figure
colLabels = labels
rowLabels = ['学生选择试卷人数']
studentValues = [[350, 150, 200, 300]]
colColors = colors

plt.table(cellText = studentValues, cellLoc='center', colLabels=colLabels, colColours=colColors, rowLabels=rowLabels, rowLoc='center', loc='bottom')
plt.show()
```
`tabel()`函数参数如下：
+ cellText：表格的数值，将源数据**按行分组**，每组数据放在列表里存储，所有组数据再放在列表里储存。
+ cellLoc：表格中数据对齐位置，可以左对齐、居中、右对齐
+ colWidth：表格的宽度
+ colColours：表格中每列列名称单元格的颜色
+ rowLabels：表格每行的行名称。 
+ rowLoc：表格每行的行名称对齐位置，可以左对齐、居中和右对齐。 
+ loc：表格在画布中的位置。 
 
通过上面的表格，我们就可以清楚地知道学生选择不同难度试卷的实际人数，从相对和绝对角度分别考察试卷的难易程度对学生选择试卷的影响情况，使得后续的分析结论能够更加客观和全面地反映试卷的难度对学生考试的影响。

---------

# 5 统计图形绘制进阶：图形样式
`刻度`作为统计图形的一部分，由`刻度标签`和`刻度线`组成。如果需要进一步设置刻度样式，需要知道`定位器(locator)`和`刻度格式器(formatter)`两个概念。

+ 刻度定位器用来设置刻度线的位置
+ 刻度格式器用来设置刻度标签的显示样式

### 5.1.1 刻度定位器和刻度格式器的使用方法
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter

x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# set x,y-major_tick_locator
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.yaxis.set_major_locator(MultipleLocator(1.0))

# set x,y-minor_tick_locator
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))

# set x-minor_tick_formatter
def minor_tick(x, pos):
    if not x % 1.0 :
        return "%.2f" % x
ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

# change athe appearance of ticks and tick labels
ax.tick_params('y', which='major', length=15, width=2.0, colors='r')
ax.tick_params(which='minor', length=5, width=1.0, labelsize=10, labelcolor='0.25')

# set x,y_axis_limit
ax.set_xlim(0, 4)
ax.set_ylim(0, 2)

# plot subplot
ax.plot(x, y, c=(0.25, 0.25, 1.00), lw=2, zorder=10)    #pair 0
ax.plot(x, y, c=(0.25, 0.25, 0.25), lw=2, zorder=0)     #pair 1

# set grid
ax.grid(ls='-', lw=.5, color='r', zorder=0)     #pair 0
#ax.grid(ls='-', lw=0.5, color='r', zorder=10)   #pair 1
#ax.grid(ls='--', lw=.5, color='.25', zorder=0)  #only one

plt.show()
```
我们需要先从模块`ticker`导入类`AutoMinorLocator`、`MultipleLocator`和`FuncFormatter`。

接下来构建一个`Figure`画布对象，向画布中添加一个1行1列的子区，从而生成一个`Axes`实例`ax`，再分别设置x轴和y轴的主刻度线的位置，其中`ax.xaxis`和`ax.yaxis`分别获得x轴实例和y轴实例。 我们以x轴为例，讲一下主刻度线位置的设置。

`ax.xaxis.set_major_locator(MultipleLocator(1.0))`语句会**在x轴的一倍处分别设置主刻度线**，其中参数`MultipleLocator(1.0)`就是设置主刻度线的显示位置。

以x轴为例，设置次要刻度线的显示位置。`ax.xaxis.set_minor_locator(AutoMinorLocator(4))`语句中，`AutoMinorLocator(4)`语句标示**将每一份主刻度线区间等分为4份**。

设置好刻度线的显示位置后要设置次要刻度线显示位置的精度，这个通过实例方法`set_minor_formatter()`完成，其中参数`FuncFormatter()`是用来控制**位置精度**的。

这样我们就完成了刻度线的显示位置以及位置精度的设置，下面我们来讲解一下`刻度线`和`刻度标签样式`的设置方法。

**主刻度样式**的设置主要通过`tick_param()`完成。`ax.tick_params('y', which='major', length=15, width=2.0, colors='r')
`中参数：
+ which：设置主刻度样式
+ length：设置主刻度线长度
+ width：设置主刻度线宽度
+ colors：设置主刻度线和主刻度标签的颜色

**次要刻度样式**设置主要通过`ax.tick_params(which='minor', length=5, width=1.0, labelsize=10, labelcolor='0.25')`，参数意义如下：
+ which：设置次要刻度样式
+ length：设置次要刻度线的长度
+ width：设置次要刻度线的宽度
+ labelsize：设置次要刻度标签的大小
+ labelcolor：设置次要刻度标签的颜色

### 5.1.2 调用模块pyplot中的函数实现刻度样式设置
语句`ax.tick_params()`是通过调用实例ax的实例方法进行刻度样式设置的。同时，通过调用模块`pyplot`中的函数也可以实现刻度样式的设置工作。

具体而言，模块`pyplot`中的刻度样式的设置是通过函数`tick_params()`实现的，即可以执行语句`plt.tick_params()`来进行刻度样式的设置。

前者是matplotlib的面向对象的操作方法，后者是调用模块pyplot的API的操作方法，这是两种不同思想的操作模式，虽然使用pyplot模块绘制图表非常方便，但是要想使图表有更多的调整和定制化展示，还是应该使用matplotlib的面向对象的操作方法。

### 5.1.3 案例1：刻度标签和刻度线样式的定制化
结合具体案例，分别通过调整x轴的刻度标签和y轴的刻度线样式，来讲解面向对象的操作方法。
```python
import matplotlib.pyplot as plt
import numpy as np

# 新建一个画布对象，设置背景颜色
fig = plt.figure(facecolor=(1, 1, 0.9412))
# 第一个左右移动，第二个上下移动，第三个左右缩放，第四个上下缩放
ax = fig.add_axes([0.1, 0.4, 0.5, 0.5])

# 对每个ticklabel更改参数
for ticklabel in ax.xaxis.get_ticklabels() :
    ticklabel.set_color('slateblue')    # 字体颜色
    ticklabel.set_fontsize(18)  # 字体大小
    ticklabel.set_rotation(30)  # 角度

for tickline in ax.yaxis.get_ticklines() :
    tickline.set_color('lightgreen')    
    tickline.set_markersize(20) # 刻度标记长度
    tickline.set_markeredgewidth(2) #刻度标记宽度

plt.show()
```
首先生成`Figure`实例`fig`，然后向**画布添加坐标轴生成实例**`ax`，其中`add_axes()`的参数是一个坐标轴位置和大小的四元列表。

通过`ax.xaxis`实例获得x轴实例，调用方法`get_ticklabels()`获得`Text`实例列表，**使用for循环对实例元素`Text`进行不同属性的属性值设置**。

同理通过`ax.yaxis`获得y轴实例，从而借助方法`get_ticklines()`获得`Line2D`实例表，也用for循环对其不同属性进行设置。最终完成设置。

### 5.1.4 案例2：货币和时间序列样式的刻度标签
通常时间序列数据是通过复杂的代码和方法实现的。然而，对于初学者而言，这种实现途径是有难度的。因此，我们介绍一种简便的展示时间序列数据的方法，以满足读者相应数据集的展示需求。同时，如果读者需要展示财务方面的数据，就需要标示数据的计量单位，这种实践需求也是可以通过调整刻度标签的样式获得实现的。下面我们来讲解货币和时间序列样式的刻度标签的设置方法。
```python
import matplotlib.pyplot as plt
import numpy as np
from calendar import month_name, day_name
from matplotlib.ticker import FormatStrFormatter

fig = plt.figure()
ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
x = np.arange(1, 8, 1)
y = 2*x

ax.plot(x, y, ls='-', lw=2, color='orange', marker='o', ms=20, mfc='c', mec='c')

# RMB ticklabel
ax.yaxis.set_major_formatter(FormatStrFormatter(r'$\yen%1.1f$'))

# dayName ticklabel
plt.xticks(x, day_name[0:7], rotation=20) # 位置、名称、角度
ax.set_xlim(0, 8)
ax.set_ylim(0, 18)

plt.show()
```
例子中，将x轴、y轴的刻度标签分别换为日期标签和货币标签。对于日期标签，通过导入标准库`calendar`中的`day_name`实例获得日期形式的刻度标签。

对于货币标签，我们通过模块`ticker`中导入类`FormatStrFormatter`，将实例`FormatStrFormatter(r'$\yen%1.1f$')`作为参数带入实例方法`ax.yaxis.set_major_formatter()`实现格式化坐标轴标签。

其中`r'$\yen%1.1f$'`生成保留两位有效数字的人民币计量的刻度标签。

+ ms：marker size
+ mfc：marker face color
+ mec：marker edge color

## 5.2 添加有指示注解和无指示注解
当我们想对图形做出一些注释和说明时，可以使用注解`annotate`，相对应的面向对象的实例方法是`Axes.annotate()`。注解本身也有作用对象之分，有对细节做出标志的有指示注解和对整体做出说明的无指示注解两类。接下来，我们就逐一加以说明。

`有指示注解`是通过箭头指示的方法对绘图区域中的内容进行解释的标注方法。`无指示注解`是单纯使用文本进行内容解释或是说明的标注方法。为了清楚地说明这两种注解的使用方法和应用场景，我们通过具体代码来讲解有指示注解和无指示注解的设置方法。
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

# set subplot
ax.plot(x, y, c='b', ls='--', lw=2)

# annotate the point xy with text with the 'arrowsytle'
ax.annotate('maximum', xy=(np.pi/2, 1.0), xycoords='data', xytext=((np.pi/2)+0.15, 0.8), textcoords='data', weight='bold', color='r', arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='r'))

# annotate the whole points with text without the 'arrowstyle'
# add text to axes
ax.text(2.8, 0.4, r'$y=\sin(x)$', fontsize=20, color='b', bbox=dict(facecolor='y', alpha=0.5))

plt.show()
```
首先生成实例ax，然后`ax.plot()`绘制图形。借助`ax.annotate(s,(x,y),xycoords,xytext,textcoords,weight,color,arrowprops)`来指示指定位点。
+ s：注解内容
+ (x,y)：被解释内容的位置
+ xycoords：xy的坐标系统，参数值`data`标示与折线图使用相同的坐标系统
+ xytext：注释内容所在位置，如果把注释内容想象为一个矩形，`xytext`标记的是左上角顶点的位置
+ textcoords：xytext的坐标系统
+ weight：注解内容的风格
+ color：注解内容的颜色
+ arrowprops：指示箭头的风格

对折线图的顶点进行详细的解释后，我们需要对折线图本身加以说明，告诉读者这是一条正弦函数曲线的局部，这时候就需要添加无指示注解。通过调用`ax.text(x,y,s,**kw)`实例方法来完成，其参数的含义如下所示。
+ x，y：注解的横纵坐标，如果把注释内容想象为一个矩形，标记的是左上角顶点的位置
+ s：注解内容
值得注意的是，有指示注解和无指示注解的主要区别是有无箭头显示，也就是对被解释内容的精确定位。

### 5.2.2 案例1：圆角文本框的设置
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.0, 10, 40)
y = np.random.randn(40)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0,10)
ax.set_ylim(-1.5,2.5)
ax.plot(x, y, ls='-', lw=2, marker='o', ms=20, mfc='orange', alpha=.6)
ax.grid(ls=':', color='gray', alpha=.5)
ax.text(6,0, 'Matplotlib', size=30, rotation=30, bbox=dict(boxstyle='round', ec='#8968cd', fc='#ffe1ff'))
plt.show()
```
圆角文本框的效果是通过`Rectangle`属性字典`bbox`实现的，具体是使用关键字参数`bbox`的字典参数值中的键值对`boxstyle="round"`实现的，其中的键值`round`还可以改成`square`，进而形成直角线框的效果。

### 5.2.3 案例2：文本的水印效果
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,40)
y = np.random.randn(40)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, y, lw=2, ls='-', marker='o', ms=20, mfc='orange', mec='b', alpha=0.6)
ax.grid(ls=':', color='gray', alpha=0.5)
ax.text(1,2, 'matplotlib', fontsize=50, color='gray', alpha=.5)
ax.set_xlim(0,10)
ax.set_ylim(-2,3)

plt.show()
```
文本的水印效果是通过函数`text()`中的关键字参数`alpha`的设定来实现的，关键字参数`alpha`的取值越小，文本的水印效果越明显。

为了凸显文本的水印效果，最好也将图形的透明度调高，即将关键字参数`alpha`的数值调小。

### 5.2.4 圆角线框的有弧度指示注解
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,2000)
y = np.sin(x)*np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, ls='-', lw=2)

bbox = dict(boxstyle='round', fc='#7ec0ee', ec='#9b30ff')
arrowprops = dict(arrowstyle='-|>', connectionstyle='angle, angleA=0, angleB=90,rad=10', color='r')

ax.annotate('single point', (5, np.sin(5)*np.cos(5)), xytext=(2, np.sin(2)*np.cos(2)), fontsize=12, color='r', bbox=bbox, arrowprops=arrowprops)
ax.grid(ls=':', color='gray', alpha=0.6)

plt.show()
```
有弧度指示的注解主要是借助Axes的实例方法`annotate()`的关键字参数`arrowprops`中的键值对`connectionstyle="angle,angleA=0,angleB=90,rad=10"`来完成的

圆角线框是通过关键字参数`bbox`的字典参数值`bbox = dict(boxstyle="round",fc="#7EC0EE",ec="#9B30FF")`来实现的，其中的键`boxstyle`的键值还可以选择`square`。

### 5.2.5 案例4：有箭头指示的趋势线
一方面，我们可以单一地展示指示箭头而将注解隐藏，从而产生只有指示箭头的展示效果，进而用这种没有文本的指示箭头作为趋势线来反映折线的趋势变化和周期规律。

另一方面，我们也可以使用其他方法实现有指示箭头作为趋势线的可视化需求。下面，我们就分别讲解这两种趋势线的实现方法和样式特征。
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 2000)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, y, ls='-', lw=2)
ax.set_ylim(-1.5, 1.5)
arrowprops = dict(arrowstyle='-|>', color='r')
ax.annotate('', xy=(3*np.pi/2, np.sin(3*np.pi/2)), xytext=(np.pi/2, np.sin(np.pi/2)+0.05), color='r', arrowprops=arrowprops)
ax.arrow(0.0, -0.4, np.pi/2, 1.2, head_width=0.05, head_length=.1, fc='g', ec='g')
ax.grid(ls=':', color='gray', alpha=.6)

plt.show()
```
借助Axes的实例方法`arrow()`绘制出绿色箭头，但是箭头**不是**正三角形。

借助Axes的实例方法`annotate()`可以绘制出没有注解的指示箭头，而且箭头是正三角形的。

实例方法`arrow(x,y,dx,dy)`中的参数`dx`是参数`x`的`水平增量`，对应的参数`dy`是参数`y`的`垂直增量`。

### 5.2.6 案例5：桑基图
有指示注解不仅可以用来作为图形内容的注释，还可以抽象为一种图形。这种图形就是桑基图，桑基图是一种特定类型的流量图。

在流量图中，指示箭头的宽度是与流量的大小成比例的。流量图的典型应用场景是可视化呈现能量、物质或是成本在流动过程中的转移情况。
```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.sankey import Sankey

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

flows = [0.2, 0.1, 0.4, 0.3, -0.6, -0.05, -0.15, -0.2]
labels = ['', '', '', '', 'family', 'trip', 'education', 'sport']

orientations = [1, 1, 0, -1, 1, -1, 1, 0]
sankey = Sankey()
sankey.add(flows=flows, labels=labels, orientations=orientations, color='c', fc='lightgreen', patchlabel='Life Cost', alpha=.7)

digrams = sankey.finish()
digrams[0].texts[4].set_color('r')
digrams[0].texts[4].set_weight('bold')
digrams[0].text.set_fontsize(20)
digrams[0].text.set_fontweight('bold')
plt.title('日常生活中成本开支的流量图')
plt.show()
```
首先，通过使用语句`from matplotlib.sankey import Sankey`，从matplotlib中的模块`sankey`导入类`Sankey`，调用语句`Sankey()`生成实例`sankey`。然后分别调用实例方法`add()`和`finish()`完成桑基图的基础绘制工作。

列表`flows`中的负值表示**流出量**，正值表示**流入量**。

列表`orientations`中的-1、0和1分别表示流量的显示位置在下方、水平和上方。最后调整流量图`diagrams[0]`的文本`List Cost`和`family`的显示样式、颜色等属性的属性值。

## 5.3 实现标题和坐标轴标签的投影效果
标题和坐标轴标签都是对绘图区域中的图形进行注释的文本内容，既然是文本内容，我们就可以对文本内容的样式进行设置。

设置标题和坐标轴的投影效果就是调整文本内容样式的有力探索。下面，我们就分别完成设置标题和坐标轴标签的投影效果的工作。

### 5.3.1 实现标题和坐标轴标签的投影效果的操作方法
这里不能简单地通过调用函数来实现。需要引入一个新类`patheffects(路径效果)`从而完成后续的操作。
```python
import matplotlib.pyplot as plt
import matplotlib.patheffects as pes
import numpy as np

x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)

fontsize = 23

# plot a sin(x) func
plt.plot(x, y, ls='--', lw=2)

# set text contents
title = '$y=\sin({x})$'
xaxis_label = '$x\_axis$'
yaxis_label = '$y\_axis$'

# get text instance
title_text_obj = plt.title(title, fontsize=fontsize, va = 'bottom')
xaxis_label_text_obj = plt.xlabel(xaxis_label, fontsize=fontsize-3, alpha=1)
yaxis_label_text_obj = plt.ylabel(yaxis_label, fontsize=fontsize-3, alpha=1)

# set shadow
title_text_obj.set_path_effects([pes.withSimplePatchShadow()])
pe = pes.withSimplePatchShadow(offset=(1,-1), shadow_rgbFace='r', alpha=.3)
xaxis_label_text_obj.set_path_effects([pe])
yaxis_label_text_obj.set_path_effects([pe])

plt.show()
```
1. 引入一个新类`pathefects`路径效果,对标题和坐标轴内容进行添加，放入变量`title_text_obj`、`xaxis_label_text_obj`、`yaxis_label_text_obj`中。
2. 设置文本内容投影：，这里主要通过调用`Artist.set_path_effetcs(path_effects)`来实现，其中`path_effects`是实例列表，列表中的实例就是调用`pes`类中`withSimplePatchShadow`类。
3. 初始化函数`withSimplePatchShadow()`主要参数：
   + offset：文本内容投影相对文本内容本身的偏移距离
   + shadow_rgbFace：投影的颜色
   + alpha：投影的透明度，范围是*0.0~1.0*，数字越大透明度越小

通过上面的操作实现了文本内容的投影效果，通过前面所讲的坐标轴位置和样式的操作方法和本节介绍的操作方法，读者基本可以掌握对图画细节和定制化的操作方法，这些方法是具有泛化性的，读者可以根据自身的实际需求灵活地运用书中所讲的操作方法，从而满足自己的具体研究、工作和学习的需要。 

除了可以给坐标轴标签添加投影效果，还可以给坐标轴标签添加文本框，以及调整文本框的位置，同样会实现强调文本内容的目的。

### 5.3.2 案例：给坐标轴标签添加文本框
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
box = dict(facecolor='#6959cd', pad=2, alpha=.4)
ax.plot(x, y, c='b', ls='--', lw=2)

# set text contents
title = '$y=\sin({x})$'
xaxis_label = '$x\_axis$'
yaxis_label = '$y\_axis$'
ax.set_xlabel(xaxis_label, fontsize=18, bbox=box)
ax.set_ylabel(yaxis_label, fontsize=18, bbox=box)
ax.set_title(title, fontsize=23, va='bottom')

# axes coords
ax.yaxis.set_label_coords(-0.08, 0.5)
ax.xaxis.set_label_coords(1.0, -0.05)

ax.grid(ls='-.', lw=1, color='gray', alpha=0.5)
plt.show()
```
通过调用`Axes`的实例方法`set_xlabel()`和`set_ylabel()`，关键字参数`bbox`是实现坐标轴标签文本框的关键，参数值是`dict`数据结构。

实例方法`set_label_coords()`是确定文本位置的关键，这个参数采用`Axes`坐标轴系统，即取值范围为`[0.0-1.0]`，数值取负数标示与坐标轴方向相反的距离，**(-0.5, 0.1)**表示左边坐标轴的左侧和底部坐标轴上方的距离交点。

因此，有序数对`(a,b)`标示坐标轴移动至x轴长度a倍的距离，y轴的b倍距离。

# 6 划分画布的主要函数
本章我们专门讨论划分画布的相关函数。这里就需要引入一个概念：`子区`。子区顾名思义就是将画布分成若干子画布，这些子画布构成绘图区域，在这些绘图区域上分别绘制图形。因此，子区的本质就是在纵横交错的行列网格中，添加绘图坐标轴。这样就实现了一张画布多张图形分区域展示的效果。

这也是组织子区相关代码的逻辑顺序。接下来，我们先来讲解子区相关函数。

## 6.1 `subplot()`：绘制网格区域中的几何形状相同的子区布局
这个函数专门用来绘制**网格区域中的几何形状相同**的子区布局。

子区函数的调用签名可以是`subplot(numRows,numCols,plotNum)`，也可以是`subplot(CRN)`.

### 6.1.1 函数`subplot()`的使用方法
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)
y1 = np.cos(x)

# set figure#1
plt.subplot(121)
plt.plot(x, y)

# set figure#2
plt.subplot(122)
plt.plot(x, y1)

plt.show()
```
函数`subplot(121)`和函数`subplot(122)`代表在画布上分隔出一个1行2列的画布格式，实现在画布上绘制“1行2列”的图形1“正弦曲线”和图形2“余弦曲线”的绘图布局。

### 6.1.2 案例1：在即坐标轴上绘制折线图
在**极坐标**下也可以绘制折线图。
```python
import matplotlib.pyplot as plt
import numpy as np
radii = np.linspace(0, 1, 100)
theta = 2*np.pi*radii

ax = plt.subplot(111, polar=True)
ax.plot(theta, radii, color='r', linestyle='-', lw=2)
plt.show()
```
通过调用函数`subplot()`获得坐标轴实例`ax`，使用面向对象调用实例方法。

其中极径和极角作为折线图的数量参数，同时依然可以设置折线图的线形、颜色和线宽等属性。