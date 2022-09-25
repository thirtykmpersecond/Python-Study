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