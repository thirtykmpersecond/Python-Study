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
x = np.arange(5)    #在给定的间隔内返回均匀间隔的值。
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
+ density：规范化/均一化`normed＝True`已经不再使用，推荐使用`density=True`。

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

---
# 4.2.2 函数`subplot()`
在代码实现部分我们调用了子区函数`subplot()`，这个函数专门用来绘制几何形状相同的网格区域，子区顾名思义就是将画布分成若干个子画布，这些**子画布就构成了几何形状规则且对称的矩形绘图区域**，然后在这些绘图区域上分别绘制图形。例如，子区函数subplot(211)和子区函数subplot(212)代表首先在画布上分隔出一个2行1列的画布格式，然后在一个2行1列的画布格式上分别绘制图形1和图形2。 

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

### 6.1.2 案例1：在极坐标轴上绘制折线图
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

### 6.1.3 案例2：在极坐标轴上绘制散点图
在极坐标系下，我们可以将极径和极角作为一堆有序数对，实现绘制散点图的可视化目标。
```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

theta = 2*np.pi**np.random.rand(100)
radii = 30*np.random.rand(100)
colors = np.random.rand(100)
size = 50*radii

ax = plt.subplot(111,polar=True)
ax.scatter(theta, radii, s=size, c=colors, cmap=mpl.cm.PuOr, marker='*')

plt.show()
```
通过调用函数`subplot()`获得坐标轴实例`ax`，使用面向对象调用实例方法的技术完成在极坐标轴上绘制散点图的任务。

其中极径和极角作为散点图的有序数对被标记在图中。同时，我们还设置了标记的样式、颜色和大小。

对于标记颜色的设定，我们使用了颜色映射表`PuOr`为标记着色，关于颜色映射表的更多使用细节。

### 6.1.4 案例3：在非等分画布的绘图区域上实现图形展示
通常子区函数`subplot()`用来完成等分画布的绘图展示任务，如果在画布上需要进行非等分画布的图形展示时，我们可以多次调用函数`subplot()`来完成非等分画布的绘图准备任务。
```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
x = np.linspace(0.0, 2*np.pi)
y = np.cos(x)*np.sin(x)

ax1 = fig.add_subplot(121)
ax1.margins(0.03)
ax1.plot(x, y, ls='-', lw=2, color='b')

ax2 = fig.add_subplot(222)
ax2.margins(0.7, 0.7)
ax2.plot(x, y, ls='-', lw=2, color='r')

ax3 = fig.add_subplot(224)
ax3.margins(x=0.1, y=0.3)
ax3.plot(x, y, ls='-', lw=2, color='g')

plt.show()
```
使用实例方法`add_subplot()`绘制了非等分画布的绘图区域的多子区折线图，左侧图形是通过实例方法`add_subplot(121)`完成的。

右侧上下两幅图形是通过实例方法`add_subplot(222)`和`add_subplot(224)`绘制完成的。完成非等分画布的任务的关键是`add_subplot(121)`和`add_subplot(222)`在网格上存在重叠子区域`subplot(122)`。

实例方法`margins(m)`可以设置数据范围的空白区域，也就是说，m倍的数据区间会被添加到原来数据区间的两端，数据范围的空白区域的调整类型既包括x轴也包括y轴的数据区间，**参数m的取值范围是大于-0.5的任意浮点数。**
margins – If a single positional argument is provided, it specifies both margins of the x-axis and y-axis limits.

## 6.2 `subplot2grid()`：让子区跨固定的网格布局
`subplot()`只能绘制等分画布形式的图形样式，要想按照绘图区域的不同展示目的，进行非等分画布形式的图形展示需要使用更高级的方法定制化网格区域。

通过`subplot2grid()`，其中的`rowspan`和`colspan`参数可以让子区跨越固定的网格布局的多个行和列，实现不同的子区布局。

### 6.2.1 函数`subplot2grid()`使用方法
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

# set subplot(23,1-2)
plt.subplot2grid((2,3),(0,0), colspan=2)
x = np.linspace(0.0, 4.0, 100)
y = np.random.randn(100)

plt.scatter(x, y, c='c')
plt.title('散点图')

# set subplot(233)
plt.subplot2grid((2,3),(0,2))
plt.title('空白区域')

# set subplot(23,4-6)
plt.subplot2grid((2,3),(1,0), colspan=3)
x = np.linspace(0.0, 4.0, 100)
y1 = np.sin(x)
plt.plot(x, y1, lw=2, ls='-')

plt.xlim(0,3)
plt.grid(True, ls=':', c='r')
plt.title('折线图')

# set figure title
plt.suptitle('subplot2grid()函数实例展示', fontsize=25)
plt.show()
```
通过调用函数`subplot2grid(shape, loc)`将参数`shape`划定的网格布局作为画图区域，实现在参数`loc`处绘制图形的目的。

参数`shape`设置了一个**2行3列**的网格布局，参数`loc`标示元组的第一个和第二个数字的起点都是0。

以`plt.subplot2grid((2,3),(0,0), colspan=2)`为例，参数`loc(0,0)`标示图形将第一行第一列作为位置起点，`colspan`标示向右延展两列。相应的，`plt.subplot2grid((2,3),(1,0), colspan=3)`标示从第二行第一列开始，向右延展3列。

**注意**：图形位置的索引起点是从0开始的，并不是向`subplot()`子函数中图形位置从1开始。

### 6.2.2 延伸阅读：模块`gridspec`中的`GridSpec`用法
模块`gridspec`是一个可以指定画布中子区域位置或者说是布局的"分区"模块。

在模块`gridspec`中，有一个类`GridSpec`。`GridSpec`可以指定网格的几何形状，也就是说，可以划定一个子区的网格状的几何结构。

我们需要设定网格的**行数和列数**，以此确定子区的划分结构样式。
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

fig = plt.figure()
gs = GridSpec(2,2)
box = dict(facecolor='lightgreen', pad=3, alpha=0.2)
#box = {'facecolor':'lightgreen', 'pad':3, 'alpha':0.2}

# subplot(2,2,1-2)
x1 = np.arange(0, 1e5, 500)
ax1 = fig.add_subplot(gs[0,:], facecolor='yellowgreen')
ax1.plot(x1, 'k--', lw=2)
ax1.set_ylabel('YLabel0,0-1', bbox=box)
ax1.set_xlabel('XLabel0,0-1', bbox=box)
ax1.yaxis.set_label_coords(-0.1, 0.5)

# subplot(2,2,3)
x2 = np.linspace(0, 1000, 10)
y2 = np.arange(1, 11, 1)
ax2 = fig.add_subplot(gs[1,0], facecolor='cornflowerblue')
ax2.scatter(x2, y2, s=20, c='grey', marker='s', lw=2, ec='k')
ax2.set_ylabel('YLabel10', bbox=box)
ax2.set_xlabel('XLabel10', bbox=box)
for ticklabel in ax2.get_xticklabels() :
    ticklabel.set_rotation(45)
ax2.yaxis.set_label_coords(-0.25, 0.5)
ax2.xaxis.set_label_coords(0.5, -0.25)

# subplot(2,2,4)
x3 = np.linspace(0, 10, 100)
y3 = np.exp(-x3)
ax3 = fig.add_subplot(gs[1,1])
ax3.errorbar(x3, y3, fmt='b-', yerr=0.6*y3, ecolor='lightsteelblue', elinewidth=2, capsize=0, errorevery=5)
ax3.set_ylabel('YLabel11', bbox=box)
ax3.set_xlabel('XLabel11', bbox=box)
ax3.xaxis.set_label_coords(0.5, -0.25)
ax3.set_ylim(-0.1, 1.1)
ax3.set_yticks(np.arange(0, 1.1, 0.1))
gs.tight_layout(fig)

plt.show()
```
首先，通过语句`GridSpec(2,2)`生成一个**2行2列**的实例`gs`，将画布划分成2行2列的网格状几何形状。

实例方法`add_subplot()`的参数`gs[0,:]`表示**将第1行、全部列**作为子区，参数gs的索引是从**0开始算起**的，即`gs[1,0]`表示**第2行第1列**的子区位置。类`GridSpec(2,2)`和实例``gs的子区位置索引等特点，与函数`subplot2grid(shape,loc)`是很类似的。 参数`shape`设置了行列的网格布局，参数`loc`所表示的元组的第一个和第二个数字的索引起点都是从0开始的。

因此，根据实例`gs`的子区位置索引的特点，我们分别绘制了`gs[1,0]`和`gs[1,1]`位置的子区`add_subplot()`。在这三个子区里，我们分别绘制了折线图、散点图和误差棒图。

最后，为了使子区`gs[0,:]`和子区`gs[1,0]`的y轴坐标轴标签的位置对齐，调用实例方法`set_label_coords(x,y)`进行位置调整。

`参数x`和`参数y`的默认坐标系统是`Axes坐标系统`。值得注意的是，在`matplotlib2.2.2`中，我们可以直接调用Figure的实例fig的实例方法`fig.align_labels()`，实现坐标轴标签位置的对齐，同理**也可以实现x轴和y轴的坐标轴标签位置的对齐**，即通过`fig.align_xlabels()`和`fig.align_ylabels()`语句实现。

## 6.3 `subplots()`：创建一张画布带有多个子区的绘图模式
`matplotlib.pyplot.subplots()`可以非常便捷地创建**1行1列**的网格布局的子区，而且同时创建一个画布对象。

函数`subplots()`返回值是一个元组对象`(fix, axs)`，其中`fig`是Figure实例，`axs`可以是一个axis对象，如果**多个子区被创建，也可以是一个`axis对象数组`**。

因此使用函数`subplots()`可以创建一张画布带有多个绘图模式的网格布局。

### 6.3.1 案例1：创建一张画布和一个子区的绘图模式
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False
font_style = dict(fontsize=18, weight='black')

# create sample data
x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x)*np.cos(x)

# create just a figure and only one subplot
fig, ax = plt.subplots(1,1, subplot_kw=dict(facecolor='cornflowerblue'))
ax.plot(x, y, 'k--', lw=2)
ax.set_xlabel('时间（秒）', **font_style)
ax.set_ylabel('振幅', **font_style)
ax.set_title('简单折线图', **font_style)
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-0.65, 0.65)
ax.grid(ls=':', lw=1, color='gray', alpha=0.8)

# show figure and subplot(s)
plt.show()
```
调用函数`subplots(1,1)`等同于调用函数`subplots()`，因为`subplots()`的参数`nrows`和`ncols`默认值都是1。

因此调用函数`subplots()`后，返回一个元组`(fig,ax)`，即***生成一个画布对象`fig`和一个坐标轴实例`ax`***。坐标轴实例ax可以绘制折线图，并设置坐标轴标题。函数`subplots()`的关键字参数`subplot_kw`设置坐标轴的背景色。

### 6.3.2 案例2：创建一张画布和两个子区的绘图模式
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False
font_style = dict(fontsize=18, weight='black')

# create sample data
x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x)*np.cos(x)

# create just a figure and two subplot
fig,ax = plt.subplots(1,2,sharey=True)

# subplot(121)
ax1 = ax[0]
ax1.plot(x, y, 'k--', lw=2)
ax1.set_title('折线图')
ax1.grid(ls=':', lw=1, color='gray', alpha=.8)

# subplot(122)
ax2 = ax[1]
ax2.scatter(x, y, s=10, c='skyblue', marker='o')
ax2.set_title('散点图')

# create a figure title
plt.suptitle('创建一张画布和两个子区的绘图模式', **font_style)

# show figure and subplot(s)
plt.show()
```
通过函数`subplots(1,2)`生成一个`画布对象`和一个`坐标轴实例数组`。画布对象和实例数组分别存储在变量`fig`和`ax`中，然后分别在坐标轴`ax1`和`ax2`上绘制折线图和散点图。

为了清楚地说明画布内容，调用了函数`plt.suptitle()`，同时调用实例方法`Axes.title()`解释每个子区的绘图区域内容。

PS：如果我们想要改变**子区边缘相距画布边缘的距离**和**子区边缘之间的高度与宽度的距离**，可以调用函数`subplots_adjust(*agrs,**kwargs)`进行设置。

其中的关键字参数`left`、`right`、`bottom`、`top`、`hspace`和`wspace`都有默认值，而且是使用`Axes坐标轴系统`度量的，即使用闭区间`[0,1]`的浮点数。

关键字参数`left`、`right`、`bottom`、`top`可以调节子区距离画布的距离，关键字参数`wspace`控制子区之间的宽度距离，关键字参数`hspace`控制子区之间的高度距离。

因此，借助函数`subplots_adjust()`可以有效实现子区的画布布局的空间位置的调整。

### 6.3.3 案例3：多种统计图形的组合展示
我们尝试将前面讲过的统计图形进行有效地组合，同时调用前面有关统计图形的操作方法，进而借助函数`subplots()`来创建多种统计图形的组合展示的可视化模式。
```python
import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots(2,3)

# subplot(231)
colors = ['#8dd3c7', '#ffffb3', '#bebada']
ax[0,0].bar([1,2,3], [0.6,0.2,0.8], color=colors, width=.5, hatch='///', align='center')
ax[0,0].errorbar([1,2,3], [0.6,0.2,0.8], yerr=.1, capsize=0, ecolor='#377eb8', fmt='o:')
ax[0,0].set_ylim(0,1.0)

# subplot(232)
ax[0,1].errorbar([1,2,3], [20,30,36], xerr=2, ecolor='#4daf4a', elinewidth=2, fmt='s', label='ETN')
ax[0,1].legend(loc=3, fancybox=True, shadow=True, fontsize=10, borderaxespad=0.4)
ax[0,1].set_ylim(10, 40)
ax[0,1].set_xlim(-2, 6)
ax[0,1].grid(ls=':', lw=1, color='grey', alpha=0.5)

# subplot(233)
x3 = np.arange(1, 10, 0.5)
y3 = np.cos(x3)
ax[0,2].stem(x3, y3, basefmt='r-', linefmt='b-.', markerfmt='bo', label='life signal')
ax[0,2].legend(loc=2, fontsize=8, frameon=False, borderpad=0.0, borderaxespad=0.6)
ax[0,2].set_xlim(0, 11)
ax[0,2].set_ylim(-1.1, 1.1)

# subplot(234)
x4 = np.linspace(0, 2*np.pi, 500)
x4_1 = np.linspace(0, 2*np.pi, 1000)
y4 = np.cos(x4)*np.exp(-x4)
y4_1 = np.sin(2*x4_1)
line1,line2 = ax[1,0].plot(x4, y4, 'k--', x4_1, y4_1, 'r-', lw=2)
ax[1,0].legend((line1,line2), ('energy', 'patience'), loc='upper center', fontsize=8,
               ncol=2, framealpha=0.3, mode='expand', columnspacing=2, borderpad=0.1)
ax[1,0].set_ylim(-2, 2)
ax[1,0].set_xlim(0, 2*np.pi)

# subplot(235)
x5 = np.random.rand(100)
ax[1,1].boxplot(x5, vert=False, showmeans=True, meanprops=dict(color='g'))
ax[1,1].set_yticks([])
ax[1,1].set_xlim(-1,1, 1,1)
ax[1,1].set_ylabel('Micro SD card')
ax[1,1].text(-1.0, 1.2, 'net weight', fontsize=20, style='italic', weight='black', family='monospace')

# subplot(236)
mu = 0.0
sigma = 1.0

x6 = np.random.randn(10000)
n,bins,patches = ax[1,2].hist(x6, bins=30, histtype='stepfilled', cumulative=True,
                              density=True, color='cornflowerblue', label='Test')
y = ((1/(np.sqrt(2*np.pi)*sigma))*np.exp(-0.5*(1/sigma*(bins-mu))**2))
y = y.cumsum()
y/= y[-1]

ax[1,2].plot(bins, y, 'r--', lw=1.5, label='Theory')
ax[1,2].set_ylim(0.0, 1.1)
ax[1,2].grid(ls=':', lw=1, color='grey', alpha=.5)
ax[1,2].legend(loc='upper left', fontsize=8, shadow=True, fancybox=True, framealpha=0.8)

#adjust subplots() layout
plt.subplots_adjust()

plt.show()
```
调用函数`subplots(2,3)`生成一个元组`(fig,ax)`，其中，`fig`是Figure的画布实例，`ax`是一个由axes组成的数组array。数组ax的形状`shape`是2行3列的，数组ax的索引是从0开始计数的。因此，我们先从`ax[0,1]`子区开始讲起，即子区`subplot(2,3,1)`。

在子区`subplot(231)`中，我们绘制了包含误差棒的柱状图，而且柱状图带有“斜线”的几何图案。误差棒的方向是垂直x轴的，误差棒之间使用虚线连接。

在子区`subplot(232)`中，我们绘制了水平方向的误差棒。同时，使用关键字参数`ecolor`和`elinewidth`调整了误差棒的颜色和线宽。我们将图例放在左下角，而且借助关键字参数`borderaxespad`将**图例与坐标轴的空白距离进行调整**。图例的外边框使用圆角形式进行展示。使用实例方法`grid()`调整了线条样式、线宽、线条颜色和网格透明度的网格线，以求凸显误差棒的度量精度。

在子区`subplot(233)`中，我们绘制了棉棒图，同时调整了棉棒图的组成元素的样式属性值。我们将图例放在左上角，而且使用关键字参数`frameon`将图例的边界框去掉。`borderpad`**调整图例内部的空白距离**和`borderaxespad`**图例与坐标轴之间的空白距离**。

在子区`subplot(234)`中，我们使用实例方法`plot()`**同时绘制了两条折线**，而且对折线的颜色、线型和线宽进行了调整。使用变量line1和line2，用来存储实例**Line2D**组成的列表里的实例**Line2D**元素。在图例中，我们将实例line1和实例line2与图例条目文本内容对应放在实例方法`legend()`中，同时使用关键字参数`framealpha`调整了图例背景的透明度，而且使用关键字参数`mode`将图例中的条目文本并排水平放置，`columnspacing`调整列之间的距离。

在子区`subplot(235)`中，我们绘制了水平放置的箱线图，同时向图中添加了文本内容作为注释，文本内容简单地进行了文字样式和字体的调整。

在子区`subplot(236)`中，我们绘制了累积`(cumulative=True)`的阶梯填充型直方图，而且用频率或者称为密度的数值`density=True`进行直方图高度的标示。最后，在直方图的基础上，绘制了正态分布的概率密度曲线。在调用实例方法`grid()`的过程中，为了突出数据的趋势变化，我们借助关键字参数`ls`、`lw`、`color`和`alpha`，调整了网格线的线条样式、线宽、线条颜色和网格透明度的属性值。

# 7 共享绘图区域的坐标轴
在使用matplotlib实践Python数据可视化的过程中，我们都离不开一个重要的呈现载体：画布`(figure)`。我们的所有数据可视化实践都是在画布上进行操作和展示的。因此，画布的有效和正确地使用就成为需要重点研究的方面。

要想实现画布的合理使用，可以借助共享绘图区域的坐标轴实现。因为，坐标轴是图形的重要载体，同时也是划分画布绘图区域的有效展示工具。

## 7.1 共享单一绘图区域的坐标轴
本节主要我们已经探讨了划分画布的主要函数的相关话题，通过使用子区可以在一张画布中创建多个绘图区域，然后在每个绘图区域分别绘制图形。

有时候，我们又想将多张图形放在同一个绘图区域，不想在每个绘图区域只绘制一幅图形。这时候，就可以借助共享坐标轴的方法实现在一个绘图区域绘制多幅图形的目的。

因此，本节我们主要探讨将多张图形放在同一个绘图区域的方法，让读者全面掌握共享坐标轴在一个绘图区域绘制多幅图形的方法，从而应对今后实际的项目和工作任务。

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

fig,ax1 = plt.subplots()
# ax1 = plt.subplot()
t = np.arange(0.05, 10.0, 0.01)
s1 = np.exp(t)

ax1.plot(t, s1, c='b', ls='-')

# set x-axis label
ax1.set_xlabel('x坐标轴')
# make the y-axis label, ticks and tick labels match the line color
ax1.set_ylabel('以e为底指数函数', c='b')
ax1.tick_params('y', colors='b')

# ax1 shares x-axis with ax2
ax2 = ax1.twinx()
s2 = np.cos(t**2)
ax2.plot(t,s2,c='r',ls=':')
# make the y-axis label and tick labels match the line color
ax2.set_ylabel('余弦函数',c='r')
ax2.tick_params('y', colors='r')

plt.show()
```
使用函数`subplots()`生成坐标轴实例`ax1`，绘制折线图`ax1.plot()`，用`ax1.set_ylabel('以e为底指数函数', c='b')`和`ax1.tick_params('y', colors='b')`方法将**y轴标签、主刻度线、和刻度标签**都设置成蓝色

调用实例方法`ax1.twinx()`生成实例`ax2`，此时实例`ax2`的x轴与实例`ax1`的轴是共享的，实例`ax2`的刻度线和刻度标签在右侧轴脊处绘制。使用`ax2.set_ylabel('余弦函数',c='r')`和`ax2.tick_params('y', colors='r')`将右侧y轴标签、主刻度线和刻度标签都设置成红色。

这样实现将两幅图形绘制在同一个绘图区域。相应的我们也可以调用`Axes.twiny()`方法满足共享y轴的可视化需求。

## 7.2 共享不同子区绘图区域的坐标轴
很多时候，我们需要共享不同子区的绘图区域的坐标轴，以求强化绘图区域的展示效果，实现精简绘图区域的目的。这时，我们通过调整函数`subplots()`中的参数`sharey`或是参数`sharex`的不同取值情况，从而实现共享不同子区的绘图区域的坐标轴的需求。

下面，就让我们来全面掌握函数`subplots()`在共享不同子区的绘图区域的坐标轴的设置方法，以实现正确和灵活地使用函数`subplots()`。

在6.1节中，介绍函数`subplots()`的使用方法时，调用签名使用了`subplots(1,2,sharey=True)`的形式，其中参数`sharey`表示`子区1`和`子区2`共享y坐标轴。

相对应的，还可以设置参数`sharex`的取值形式。具体而言，参数`sharex`和参数`sharey`的取值形式有四种，分别是`row`、`col`、`all`和`none`，其中`all`和`none`分别等同于`True`和`False`。

下面我们以参数`sharex`为例就四种参数取值形式分别进行讲解，参数`sharey`的取值形式与使用方法和参数`sharex`完全相同。

### 7.2.1 设置方法
下面我们就通过Python代码的形式，来讲解共享绘图区域的坐标轴的具体实现方法。为了增强参数`sharex`取值变化前后的图形展示效果，我们首先绘制没有使用参数`sharex`和`sharey`的调用签名形式的图形。
```python
import matplotlib.pyplot as plt
import numpy as np

# create sample data
x1 = np.linspace(0, 2*np.pi, 400)
y1 = np.cos(x1**2)
x2 = np.linspace(0.01, 10, 100)
y2 = np.sin(x2)
x3 = np.random.rand(100)
y3 = np.linspace(0, 3, 100)
x4 = np.arange(0, 6, 0.5)
y4 = np.power(x4, 3)

# set (2,2) subplots
fig,ax = plt.subplots(2,2)
# set chart of each subplot
ax1 = ax[0,0]
ax1.plot(x1, y1)
ax2 = ax[0,1]
ax2.plot(x2, y2)
ax3 = ax[1,0]
ax3.scatter(x3, y3)
ax4 = ax[1,1]
ax4.scatter(x4, y4)
# show figure and plots
plt.show()
```
通过调用函数`subplots(2,2)`，生成一个2行2列的网格子区布局，可以看到4幅图形的x轴的范围和刻度标签都不相同。下面分为4中情况讨论参数`sharex`的取值情况参数。

1. `sharex='all'`
   + 只需要将语句`plt.subplots(2,2)`改成`plt.subplots(2,2,sharex='all')`，其他语句不变。
   + 等同于`sharex=True`
   + 可以看到4幅图形的x轴取值范围使用了相同的范围，而且是采用了**变量\*2**取值范围作为x轴的共享范围，**变量\*2**的取值范围中的最大值是其他变量的取值范围中上限里的最大值

2. `sharex=none`
   + 与默认值相等，即`sharex=False`

3. `sharex=row`
   + 这种情况是把子区中每一行的图形的x轴取值范围实现共享，而且是**选择每一行中图形的x轴取值范围上限最大的那个取值范围作为共享范围**。

4. `sharex='col'`
   + 这种情况是把子区中每一列的图形的x轴取值范围实现共享，而且是**选择每一行中图形的y轴取值范围上限最大的那个取值范围作为共享范围**。

在以上情形中，展示了参数`sharex`取值为`True`的可以刷效果，4个子区中每列下方的子区会将本列的x轴刻度标签显示出来。

**继续考虑一种情形：**能否将坐标轴的子区之间空隙去掉，变成子区上下边缘是重合的情形？

### 7.2.2 案例：将共享坐标轴的子区之间空隙去掉
前面，我们讲过大量子区的实现方法和相关案例。但是，这些案例的可视化效果都有一个共同点，那就是子区之间存在空隙。

很多时候，为了更好地实现可视化效果，这些空隙是应该去掉的。这样，我们才能实现理想的可视化需求。

接下来我们就介绍将共享坐标轴的子区之间的空隙去掉的操作方法。

```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.0, 10.0, 200)
y = np.cos(x)*np.sin(x)
y2 = np.exp(-x)*np.sin(x)
y3 = 3*np.sin(x)
y4 = np.power(x,0.5)

fig,(ax1,ax2,ax3,ax4) = plt.subplots(4,1,sharex='all')
fig.subplots_adjust(hspace=0)

ax1.plot(x, y, ls='-', lw=2)
ax1.set_yticks(np.arange(-0.6,0.7,0.2))
ax1.set_ylim(-0.7, 0.7)

ax2.plot(x, y2, ls='-', lw=2)
ax2.set_yticks(np.arange(-0.05, 0.36, 0.1))
ax2.set_ylim(-0.1, 0.4)

ax3.plot(x, y3, ls='-', lw=2)
ax3.set_yticks(np.arange(-3, 4, 1))
ax3.set_ylim(-3.5, 3.5)

ax4.plot(x, y4, ls='-', lw=2)
ax4.set_yticks(np.arange(0.0, 3.6, 0.5))
ax4.set_ylim(0.0, 4.0)

plt.show()
```
通过观察图可以看出4幅子图之间的水平方向上没有空隙，4幅子图连接成“一幅”图形。这里的关键语句就是`plt.subplots(4,1,sharex="all")`和`fig.subplots_adjust(hspace=0)`。

第1条语句实现**共享x轴的坐标轴刻度标签**，第2条语句实现**将4幅子图的水平方向的空隙去除**。通过这两条关键语句就成功实现了“拼接子图”的可视化任务。

## 7.3 共享个别子区绘图区域的坐标轴
针对子区的绘图区域的坐标轴范围不同的情形，通过7.2节中介绍的共享不同子区的绘图区域的坐标轴的参数使用方法，我们可以对个别子区做出更加细微的局部调整，以求视图展示效果更加理想和美观。因此，本节内容是7.2节内容的进一步深化探索。

```python
import matplotlib.pyplot as plt
import numpy as np

# create sample data
x1 = np.linspace(0, 2*np.pi, 400)
y1 = np.cos(x1**2)
x2 = np.linspace(0.01, 10, 100)
y2 = np.sin(x2)
x3 = np.random.rand(100)
y3 = np.linspace(0, 3, 100)
x4 = np.arange(0, 6, 0.5)
y4 = np.power(x4, 3)

# set (2,2) subplots
fig,ax = plt.subplots(2, 2)
# set chart of each subplot
ax1 = plt.subplot(221)
ax1.plot(x1, y1)
ax2 = plt.subplot(222)
ax2.plot(x2, y2)
ax3 = plt.subplot(223)
ax3.scatter(x3, y3)
ax4 = plt.subplot(224, sharex=ax1)
ax4.scatter(x4, y4)

plt.show()
```
通过运行结果，我们可以看到子区4的x轴范围已经共享子区1的x轴范围了。

同理，我们也可以使用上面的方法，共享特定子区的y轴范围，如果还以子区4为例，调用签名是`subplot(224,sharey=ax1)`。

### 7.3.2 延伸阅读：`autoscale()`调整坐标范围
如果我们对某一个子区的坐标轴范围和数据范围的搭配比例不是很满意，可以使用函数`autoscale()`进行坐标轴范围的自适应调整，以使图形可以非常紧凑地填充绘图区域。

调用签名是`autoscale(enable=True,axis="both",tight=True)`。调用签名中的具体参数的含义如下所示。

+ enable：进行坐标轴范围的自适应调整
+ axis：使x、y轴都进行自适应调整
+ tight：让坐标轴的范围调整到数据的范围上

例如，我们将子区3的x轴范围调整到数据范围上，我们只需要在子区3的代码部分增加如下代码即可`plt.autoscale(enable=True,axis='both',tight=True)`。

注意观察，子区3的坐标轴范围已经调整到数据本身的范围了。也就是说，x轴范围调整到0至1,y轴范围调整到0至3。这样，图形效果就变得更加紧凑和美观了。


# 8 坐标轴高阶应用

## 8.1 设置坐标轴位置和展示形式
本节我们通过在画布任意区域和位置，讲解设置坐标轴的位置和坐标轴的展示形式的实现方法，让读者掌握坐标轴的位置和展示形式的设置方法，也让读者明白坐标轴的位置和展现形式既可以在子区中进行设置，也可以在画布的任何位置进行设置，从而全面理解坐标轴、子区和画布的关系。

### 8.1.1 案例1：在画布中任意位置添加任意数量的坐标轴
这个做法非常类似于在画布中设置子区，但是子区不能在画布中的任何位置进行设置，添加坐标轴却可以在画布中进行任意结构形式的多图视图布局。通过向画布中添加坐标轴，我们可以实现在一个坐标轴中嵌套多个坐标轴的视图布局。例如，如果需要展示相同数据的不同展现形式或是相同实例的不同属性，那么就需要通过坐标轴生成的多个视图来表达，从而将多个图形放在一张图中。

```python
import numpy as np
import matplotlib.pyplot as plt
# set #1 plot
plt.axes([0.05, 0.7, .3, .3], frameon=True, facecolor='y', aspect='equal')
plt.plot(np.arange(3), [0,1,0], color='b', lw=2, ls='-')

# set #2 plot
plt.axes([0.3, 0.4, .3, .3], frameon=True, fc='y', aspect='equal')
plt.plot(2+np.arange(3), [0,1,0], color='blue', lw=2, ls='-')

# set #3 plot
plt.axes([0.55, 0.1, .3, .3], frameon=True, fc='y', aspect='equal')
plt.plot(4+np.arange(3), [0,1,0], c='b', lw=2, ls=':')

plt.show()
```
上述代码试图通过多幅视图来展示函数plot()中的参数linestyle的不同属性值的图形效果。 不同于使用子区函数subplot()、subplot2grid()和模块matplotlib.gridspec构建子区的方法，这些方法都只能在规则网格内进行视图布局。也就是说，只能在横纵交错的网格区域绘制子区模式，无法完成子区的交错、覆盖和重叠等视图组合模式。
函数`plt.axes(rect, frameon=True, fc='y', aspect='equal')`参数含义如下：
+ rect：`[left,bottom,width,height]`，列表`rect`中的`left`和`bottom`两个元素分别表示坐标轴的左侧边缘和底部边缘距离画布边缘的距离，`width`和`height`两个元素分别表示坐标轴的宽度和高度，`left`和`width`两个元素的数值都是画布宽度的归一化距离， `bottom`和`height`两个元素的数值都是画布高度的归一化距离。
+ frameon：如果`frameon=True`，则绘制坐标轴四条轴脊，否则不绘制。
+ fc：同`facecolor`，背景颜色

### 8.1.2 案例2：调整已经确定的坐标轴的显示、隐藏与刻度范围问题
```python
import numpy as np
import matplotlib.pyplot as plt

# set #1 plot
plt.axes([0.05, 0.7, .3, .3], frameon=True, facecolor='y', aspect='equal')
plt.plot(np.arange(3), [0,1,0], color='b', lw=2, ls='--')
plt.ylim(0, 1.5)
plt.axis('image')

# set #2 plot
plt.axes([0.3, 0.4, .3, .3], frameon=True, fc='y', aspect='equal')
plt.plot(2+np.arange(3), [0,1,0], color='blue', lw=2, ls='-')
plt.ylim(0, 15)
plt.axis([2.1, 3.9, 0.5, 1.9])

# set #3 plot
plt.axes([0.55, 0.1, .3, .3], frameon=True, fc='y', aspect='equal')
plt.plot(4+np.arange(3), [0,1,0], c='b', lw=2, ls=':')
plt.ylim(0, 1.5)
plt.axis('off')

plt.show()
```
上述代码中，我们除了调用函数`ylim()`和函数`axis()`，其他部分与向画布中任意位置添加任意数量的坐标轴的代码相同，通过调用函数`axis()`，分别实现了将图形变得紧凑、调整坐标轴的刻度范围和隐藏坐标轴的显示。

具体而言，左上角的图形通过调用`plt.axis("image")`语句使画面紧凑，中间图形利用函数`axis([xmin,xmax,ymin,ymax])`的参数，实现重新改变坐标轴范围的需求，右下角的视图使用`plt.axis(“off”)`语句将坐标轴完全隐藏而只显示函数`plot()`的绘制图形。

### 8.1.3 使用`axis()`绘制坐标轴。
上述两个案例的绘制原理，基本上都是首先调用函数`axes()`绘制坐标轴，然后调用函数`axis()`在原来坐标轴的基础上调整坐标轴的视图显示情况，包括可见性、范围和比例协调性等。 

我们也可以通过调用函数`axis()`实现绘制坐标轴，再绘制图形的可视化需求。
```python
import matplotlib.pyplot as plt
import numpy as np

plt.axis([3, 7, -0.5, 3])
plt.plot(4+np.arange(3), [0,1,0], c='b', lw=4, ls='-')

plt.show()
```

## 8.2 使用两种方法控制坐标轴刻度的显示
面对不同Python数据可视化的应用场景的定制化需求，我们需要对坐标轴刻度的显示进行有效的控制，以满足视图展示效果的要求。前面讲过使用模块pyplot的API方法和调用matplotlib的面向对象的方法，并对比了两种操作模式的特点。

接下来，就给大家讲解一下关于matplotlib中的控制坐标轴刻度显示的两种方法：一种方法是利用matploblib的面向对象的`Axes.set_xticks()`和`Axes.set_yticks()`实例方法，实现不画坐标轴刻度的需求；另一种方法是调用模块pyplot的API，使用函数`setp()`设置刻度元素`(ticklabel和tickline)`，更新显示属性的属性值为`False`。

### 8.2.1 方法1：调用`Axes.set_xticks()`和`Axes.set_yticks()`方法
```python
import matplotlib.pyplot as plt
import numpy as np

ax1 = plt.subplot(1,2,1)
ax1.set_xticks(np.arange(0,251,50))
plt.grid(True, axis='x')

ax2 = plt.subplot(122)
ax2.set_xticks([])
plt.grid(True, axis='x')

plt.show()
```
上述左图是有刻度元素的图，右图是没有刻度元素的图。值得注意的是，如果不设置坐标轴刻度，那么网格线也不会被设置。

设置刻度，包括设置刻度标签和刻度线。刻度标签可以通过`Axes.set_xticklabels()`和`Axes.set_yticklabels()`实例方法进行有效的设置。

### 8.2.2 方法2：调用函数`step()`
```python
import matplotlib.pyplot as plt
ax1 = plt.subplot(221)
plt.setp(ax1.get_xticklabels(), visible=True)
plt.setp(ax1.get_xticklines(), visible=True)
plt.grid(True, axis='x')

ax2 = plt.subplot(222)
plt.setp(ax2.get_xticklabels(), visible=True)
plt.setp(ax2.get_xticklines(), visible=False)
plt.grid(True, axis='x')

ax3 = plt.subplot(223)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_xticklines(), visible=True)
plt.grid(True, axis='x')

ax4 = plt.subplot(224)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_xticklines(), visible=False)
plt.grid(True, axis='x')

plt.show()
```
首先，讲解一下pyplot.setp()的使用方法。例如，设置一条折线图的线型风格为破折线，你可以敲入以下代码：
```python
import matplotlib.pyplot as plt
line, = plt.plot([1,2,3])
plt.setp(line, ls='--')
plt.show()
```
其中`setp()`中非关键字参数`line`代表`matplotlib.lines.Line2D`实例，关键字参数`linestyle`是`Line2D`的属性，参数为`--`，当然也可以用`plt.setp(line, 'linestyle', '--')`语句改变线条风格。

回到代码本身，通过调用函数`setp()`可以分别设置刻度标签`ticklabel`和刻度线`tickline`的显示情况，通过将`Line2D`实例的属性`visible`的属性值设置为`True`或`False`，可以控制刻度元素的显示与隐藏。

值得注意的是，最后一张图是将刻度标签和刻度线都设置为隐藏，但是，隐藏并不同于方法1中的操作，方法1中的操作是**不画刻度元素**，而方法2中的操作是**首先画出刻度元素，然后将其隐藏**。这从x轴上的参考线的隐藏和显示就可以看出两者的区别。也就是说，***不画刻度元素自然就没有参考线，但是画刻度元素后，又将其隐藏，参考线并不会消失***。

本节我们探讨了坐标轴刻度显示设置的两种简易操作方法，虽然从可视化效果上来看，二者基本上可以实现相同的展示效果。但是，从运行机制上来看，二者还是有本质区别

***PS***:8.2.2节中我们看到改变Line2D实例属性的方法是通过函数`setp()`来实现的。下面补充一下改变`matplotlib.lines.Line2D`实例的属性值的方法，还是以上面的代码`line,=plt.plot([1,2,3])`为例，我们可以通过`Line2D`实例的方法`set_attr(attrValue)`实现改变实例属性值的目标，其中，`attr`代表Line2D实例的属性，`attrValue`代表Line2D实例的`attr`属性的属性值。例如，`line.set_linestyle("-")`就将线条风格变为实线，`line.set_linewidth(2.5)`就将线条宽度变为2.5。前面已经讲过棉棒图的绘制原理和应用展示。下面，我们就结合本节中的相关知识进一步探索改变棉棒图的组成要素的属性值的方法。

### 8.2.3 案例1：棉棒图的定制化展示
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5, 2*np.pi, 20)
y = np.random.randn(20)
markerline, stemlines, baseline = plt.stem(x,y)

plt.setp(markerline, c='chartreuse', marker='D') # markerline.set_marker('D'),markerline.set_color('chartreuse')
plt.setp(stemlines, ls='-.')# stemlines.set_linestyle('-.')
baseline.set_linewidth(2)   # plt.setp(baseline, lw=2)

plt.show()
```
通过调用函数`stem()`获得实例`markerline`、`stemlines`和`baseline`。我们可以应用本节所讲的改变实例属性值的方法对这些实例的属性值进行定制化设置，以求呈现更好的可视化效果。需要补充的是，`stemlines`是实例列表，改变实例属性值应该使用函数`setp()`来进行设置。

### 8.2.4 案例2：坐标轴样式和位置的定制化展示
通过这个案例，我们将掌握有关**设置刻度标签**和**刻度线样式**的实现方法，以及**调整轴脊的相对位置**的方法。这些方法既是前面讲过的技巧的运用，也是操作细节的延伸。而且，这些方面的展示效果都是基于面向对象的操作方法实现的。
```python
import matplotlib.pyplot as plt
import numpy as np
from calendar import day_name
from matplotlib.ticker import FormatStrFormatter

fig = plt.figure()
ax = fig.add_axes([0.2,0.2, 0.7,0.7])  # left, bottom, width, height

ax.spines['bottom'].set_position(('outward', 10))
ax.spines['left'].set_position(('outward', 10))
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

x = np.arange(1, 8, 1)
y = 2*x + 1

ax.scatter(x, y, c='orange', s=50, ec='orange') #size=50, edgecolor='orange'

for tickline in ax.xaxis.get_ticklines() :  # 设定tickline中的细节
    tickline.set_color('blue')  # 不能显示
    tickline.set_markersize(8)
    tickline.set_markeredgewidth(5)
for ticklabel in ax.get_xmajorticklabels() : # 设定ticklabel中的细节
    ticklabel.set_color('slateblue')
    ticklabel.set_fontsize(15)
    ticklabel.set_rotation(20)

ax.yaxis.set_major_formatter(FormatStrFormatter(r"$\yen%1.1f$"))

plt.xticks(x, day_name[0:7], rotation=20)
ax.yaxis.set_ticks_position('left')       # 'left', 'right', 'both', 'default', 'none'
ax.xaxis.set_ticks_position('bottom')   # 'top', 'bottom', 'both', 'default', 'none'

for tickline in ax.yaxis.get_ticklines() :
    tickline.set_color('lightgreen')    # 不能显示
    tickline.set_markersize(8)
    tickline.set_markeredgewidth(5)
for ticklabel in ax.get_ymajorticklabels() :
    ticklabel.set_color('green')
    ticklabel.set_fontsize(18)

ax.grid(ls=':', lw=1, c='gray', alpha=.5)

plt.show()
```
为了突出刻度标签的视觉效果，我们将刻度线的颜色设置成与刻度标签同样的颜色，而且刻度线的大小和宽度也都做了调整。更为重要的是，我们将左侧轴脊和底部轴脊分别向左和向下移动10个点的距离，即向数据区域之外移动一些距离，以突显数据本身的变化趋势和规律，如果移动距离是负数，则向数据区域内部移动负数绝对值个数的点的距离。

## 8.3 控制坐标轴的显示
控制坐标轴显示主要是通过控制坐标轴的载体`轴脊`的显示来实现的，在轴脊上有`刻度标签`和`刻度线`，它们共同组成了坐标轴。因此，控制坐标轴显示是综合通过控制轴脊和刻度线的显示来完成的。这样，进行轴脊和刻度线的显示方法的学习，就可以掌握坐标轴显示的方法。 

在一个绘图区域中，有4条轴脊，分别是`顶边框`、`右边框`、`底边框`和`左边框`，这4条轴脊是4条坐标轴的载体，起到显示刻度标签和刻度线的作用。下面我们就通过Python代码的形式来讲解控制轴脊和坐标轴显示的方法。
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.sin(x)

ax1 = plt.subplot(221)
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.set_xlim(-2*np.pi, 2*np.pi)
ax1.set_ylim(-1.0, 1.0)
plt.title(r'$a$')
plt.scatter(x, y, marker='+', c='b')

ax2 = plt.subplot(222)
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.xaxis.set_ticks_position('bottom')
ax2.set_xlim(-2*np.pi, 2*np.pi)
ax2.set_ylim(-1.0, 1.0)
plt.scatter(x, y, marker='+', c='b')
plt.title(r'$b$')

ax3 = plt.subplot(223)
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.yaxis.set_ticks_position('left')
ax3.set_xlim(-2*np.pi, 2*np.pi)
ax3.set_ylim(-1.0, 1.0)
plt.title(r'$c$')
plt.scatter(x, y, marker='+', c='b')

ax4 = plt.subplot(224)
ax4.spines['right'].set_color('none')
ax4.spines['top'].set_color('none')
ax4.xaxis.set_ticks_position('bottom')
ax4.yaxis.set_ticks_position('left')
ax4.set_xlim(-2*np.pi, 2*np.pi)
ax4.set_ylim(-1.0, 1.0)
plt.title(r'$d$')
plt.scatter(x, y, marker='+', c='b')

plt.show()
```
通过`ax2.spines['right'].set_color('none')`和`ax2.spines['top'].set_color('none')`语句将顶边框和有边框去掉，但刻度线还是被保留。

通过`ax2.xaxis.set_ticks_position('bottom')`语句，将顶边框上的刻度线去掉。同理`ax3.yaxis.set_ticks_position('left')`将有边框的刻度线去掉展示效果。

`ax1 = plt.subplot(221)`和`plt.setp(ax1.get_xticklabels(), visible=True)`和`plt.setp(ax1.get_xticklines(),visible=True)`语句也可以实现刻度标签和刻度线的显示需求，但是却不能改变刻度标签和刻度线的显示位置。

## 8.4 移动坐标轴的位置
在学习了控制坐标轴显示的方法之后，我们就可以对坐标轴显示进行进一步操作，即移动坐标轴的位置。 移动坐标轴的位置的操作是以控制坐标轴显示作为方法和知识基础的。

所谓移动坐标轴的位置就是移动坐标轴的载体（轴脊）的位置，进而设置刻度线的位置，从而完成移动坐标轴的位置的任务。前面讲过调整刻度范围和刻度标签、控制坐标轴显示的方法。

如果可以将左侧和底端的坐标轴移动位置，变成可以清楚地显示出曲线周期的特点和数值变化的规律的图形，那就更完美了。接下来，我们就讲解如何移动坐标轴的位置。 

下面就通过Python代码的形式，结合前面调整刻度范围和刻度标签、控制坐标轴显示的方法的代码部分，移动坐标轴位置。
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)
y1 = np.cos(x)

ax = plt.subplot(111)
ax.plot(x, y, ls='-', lw=2, label=r'$\sin(x)$')
ax.plot(x, y1, ls='-', lw=2, label=r'$\cos(x)$')
ax.legend(loc='lower left')
plt.title('$\sin(x)$'+"和"+"$\cos(x)$"+'函数')

# set xlimit
ax.set_xlim(-2*np.pi, 2*np.pi)
# set ticks
plt.xticks([-2*np.pi, -3*np.pi/2, -1*np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], [r"$-2\pi$", r'$-3\pi/2$', r'$-\pi$',r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.show()
```
代码的主体部分基础上，添加了两条关键代码：
+ `ax.spines['bottom'].set_position(('data', 0))`
+ `ax.spines['left'].set_position(('data', 0))`

`as.spines`会调用轴脊字典，其中的`key`是`轴脊位置`，`top`、`right`、`bottom`、`left`键值是`matplotlib.spines.Spine`对象，实例方法`set_position`就是就是对轴脊位置的控制方法。其中参数`data`说明控制轴脊的`坐标值`与`折线图`的坐标系统一致。因此`参数0`就表示将**底端轴脊移动到左侧轴脊的零点处，同理将左侧轴脊移动到底端轴脊的零点处**。

在`matplotlib`元素组成结构中，已经说明轴脊是刻度线和坐标轴标签的载体。这样当左侧和低端轴脊移动位置时，刻度线和刻度标签也会相应地移动位置。

我们将x轴刻度线放在底端轴脊上，将y轴刻度线放在左侧轴脊上。从而，完成移动坐标轴位置的工作。

# 9 设置线条类型和标及类型的显示样式
在matplotlib的大量实践中，会频繁地进行折线图的线条类型和标记类型的设置工作。更加重要的是，线条类型和标记类型的显示样式的美观与否会极大地影响Python数据可视化的效果。因此，我们需要重点进行这方面的操作技巧和设置方法的讲解。这部分会涉及字典数据结构作为关键字参数的使用方法、线条类型的设置方法和标记类型的设置方法。

这部分会涉及字典数据结构作为关键字参数的使用方法、线条类型的设置方法和标记类型的设置方法。

## 9.1 不同签名形式的字典使用方法
在Python数据可视化的代码实现中，大量运用了字典数据结构。在函数或是实例方法的调用签名中，字典数据结构经常作为关键字参数值进行调用而传入代码块中。

通过使用字典设置相应属性的属性值，大大提高了代码的简洁程度，并减少了重复设置的烦琐工作。这里以文本属性和相应的属性值为例，构造字典font存储文本属性和属性值，同时使用关键字参数`fontdict`作为设置方法的代表参数。

### 9.1.1 调用签名中的关键字参数的设置形式`fontdict=font`
```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
font = {'family':'monospace', 'color':'maroon', 'weight':'bold', 'size':16}

x = np.linspace(0.0, 2*np.pi, 500)
y = np.cos(x)*np.sin(x)

ax.plot(x, y, c='k', ls='-', lw=2)
ax.set_title("keyword mode is 'fontdict=font'", fontdict=font)
ax.text(1.5, 0.4, 'cos(x)*sin(x)', fontdict=font)
ax.set_xlabel('time(h)', **font)
ax.set_ylabel(r'$\Delta$height(cm)', **font)
ax.set_xlim(0, 2*np.pi)

plt.show()
```
首先将文本属性和属性值都放在字典`font`中，然后分别在实例方法`plot()`,`set_title()`,`set_xlabel()`,`set_ylabel()`,`set_xlim()`中，作为关键字参数`fontdict`的参数值传递到实例方法的调用签名中。

### 9.1.2 方法2：关键字参数的设置形式`**font`
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 2*np.pi, 500)
y = np.cos(2*x)*np.sin(2*x)
font = {'family':'monospace', 'color':'maroon', 'weight':'bold', 'size':16}

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, y, color='k', lw=2, ls='-')
ax.set_title("keyword mode is '**font'", **font)
ax.text(1.5, 0.52, 'cos(2*x)*sin(2*x)', **font)
ax.set_xlabel('time(h)', **font)
ax.set_ylabel(r'$\Delta$height(cm)', **font)
ax.set_xlim(0, 2*np.pi)

plt.show()
```
这里我们将字典`font`直接作为关键字参数传入实例方法的调用签名中。在调用签名中，我们使用`**font`方法将字典变为关键字参数，使调用签名形式变得非常简洁。

值得注意的是，字典`font`的定义方法还可以是：`font=dict(family="serif",color="navy",weight="black",size=16)`

## 9.2 线条类型的显示样式设置方法
在折线图中，我们通过函数或是实例方法`plot()`的关键字参数`linestyle(ls)`设置线条类型的显示样式。不同的线条类型可以产生不同的视图效果，同时也有各自更为适用的应用领域和场景。
```python
import matplotlib.pyplot as plt
import numpy as np
font = dict(family='serif', c='navy', weight='black', size=16)
color = 'skyblue'
linewidth = 3
linestyleList = ['-', '--', '-.', ':']

fig = plt.figure()
ax = fig.add_subplot(111)

x = np.arange(1, 11, 1)
y = np.linspace(1, 1, 10)

ax.text(4,4.0, 'line styles', **font)

for i,ls in enumerate(linestyleList) :
    ax.text(0, i+0.5, "'{}'".format(ls), **font)
    ax.plot(x, (i+0.5)*y, linestyle=ls, color=color, linewidth=linewidth)

ax.set_xlim(-1, 11)
ax.set_ylim(0, 4.5)
ax.margins(0.2)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
```
我们对列表`linestyleList`中的线条样式元素进行了循环显示，每种线条样式的视图效果都有各自的特点。

值得注意的是，我们对在for循环中调用的实例方法`text()`的显示文本的字符串做了格式化处理，有关格式化字符串的内容和语法，读者可以参考Python书籍的有关字符串的章节。

## 9.3 标及类型的显示样式设置方法

### 9.3.1 方法1：单一字符模式
```python
import matplotlib.pyplot as plt
import numpy as np

font_style = dict(family='serif', color='navy', weight='black', size=12)
line_marker_style = dict(linestyle=':', linewidth=2, color='maroon', markersize=10)

fig = plt.figure()
ax = fig.add_subplot(111)
msNameList = ["'.'--point marker","','--pixel marker", "'o'--circle marker", "'v'--triangle_down marker", "'^'--triangle_up marker","'<'--triangle_left marker", "'>'--triangle_right marker", "'1'--tri_down marker", "'2'--tri_up marker", "'3'--tri_left marker", "'4'--tri_right marker", "'s'--square marker", "'p'--pentagon marker", "'*'--star marker", "'h'--hexagon1 marker", "'H'--hexagon2 marker", "'+'--plus marker", "'x'--x marker", "'D'--diamond marker", "'d'--thin_diamond marker", "'|'--vline marker", "'_'--hline marker"]
markerstyleList = ['.',',','o','v','^','<','>','1','2','3','4','s','p', '*','h','H','+','x','D','d','|','_']

x = np.arange(5, 11, 1)
y = np.linspace(1, 1, 6)

ax.text(4,23, "marker styles", **font_style)
for i,ms in enumerate(markerstyleList) :
    ax.text(0, i+0.5, msNameList[i], **font_style)
    ax.plot(x, (i+0.5)*y, marker=ms, **line_marker_style)

ax.set_xlim(-1, 11)
ax.set_ylim(0, 24)
ax.margins(0.3)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
```
我们将全部标记类型的样式都展示出来了，同时，每种标记类型的英文注释也附加在标记类型之后，方便读者对标记类型的样式进行理解和掌握。

标记样式不仅可以使用上面介绍的标记样式，还可以使用`mathtext`模式的标记样式，即关键字参数`marker`取值是原始字符串（raw strings）`r"$text\text$"`模式。

### 9.3.3 方法2：`mathtext`模式
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

x = np.arange(1, 13, 1)
y = np.array([12,34,22,30,18,13,15,19,24,28,23,27])

fig, ax = plt.subplots(2,2)

# subplot(221)
ax[0,0].scatter(x, y*1.5, marker=r'$\clubsuit$', c='#fb8072', s=500)
ax[0,0].locator_params(axis='x', tight=True, nbins=11)
ax[0,0].set_xlim(0, 13)
ax[0,0].set_xticks(x)
ax[0,0].set_title('显示样式"%s"的散点图' % r'$\clubsuit$')

# subplot(222)
ax[0,1].scatter(x, y-2, marker=r'$\heartsuit$', s=500)
ax[0,1].locator_params(axis='x', tight=True, nbins=11)
ax[0,1].set_xlim(0, 13)
ax[0,1].set_xticks(x)
ax[0,1].set_title('显示样式"%s"的散点图'% r'$\heartsuit$')

# subplot(223) 
ax[1,0].scatter(x, y+7, marker=r'$\diamondsuit$', s=500)
ax[1,0].locator_params(axis='x', tight=True, nbins=11)
ax[1,0].set_xlim(0, 13)
ax[1,0].set_xticks(x)
ax[1,0].set_title('显示样式"%s"的散点图'% r'$\diamondsuit$')

# subplot(224)
ax[1,1].scatter(x, y-9, marker=r'$\spadesuit$', s=500)
ax[1,1].locator_params(axis='x', tight=True, nbins=11)
ax[1,1].set_xlim(0, 13)
ax[1,1].set_xticks(x)
ax[1,1].set_title('显示样式"%s"的散点图'% r'$\spadesuit$')

plt.suptitle('不同原始字符串作为标及类型的展示效果', fontsize=16, weight='black')
```
我们使用原始字符串（raw strings）作为标记类型，即关键字参数`marker`的取值是`r"$\text$"`模式的原始字符串，通过使用2行2列的子区进行不同标记类型的显示样式的效果展示，这些标记类型是常规字符串的标记类型无法实现的样式。

因此，标记类型使用原始字符串模式极大地拓展了我们的标记类型的种类和样式，同时也使可视化效果给人以审美般的视觉享受。

## 9.4 延伸阅读
### 9.4.1 案例1：破折号样式的不同展现形式的设置方法
```python
import matplotlib.pyplot as plt
import numpy as np
font_style = dict(family='serif', weight='black', size=12)
line_marker_style1 = dict(linestyle='--', lw=2, color='maroon', markersize=10)
line_marker_style2 = dict(linestyle='--', lw=2, color='cornflowerblue', markersize=10)
line_marker_style3 = dict(linestyle='--', lw=2, color='turquoise', markersize=10)

fig = plt.figure()
ax = fig.add_subplot(111, facecolor='honeydew')
x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x)*np.cos(x)
ax.plot(x, y, dashes=[10,2], label='dashes=[10,2]', **line_marker_style1)
ax.plot(x, y+0.2, dashes=[3,1], label='dashes=[3,1]', **line_marker_style2)
ax.plot(x, y+0.4, dashes=[2,2,8,2], label='dashes=[2,2,8,2]', **line_marker_sytle3)

ax.axis([0, 2*np.pi, -0.7, 1.2])
ax.legend(ncol=3, bbox_to_anchor=(0, 0.95, 1, 0.05), mode='expand', fancybox=True, shadow=True, prop=font_style)

plt.show()
```
线条类型是“破折号”样式的折线呈现多种展现形式，实现多种展现形式的关键是关键字参数`dashes`的使用。折线是由若干个数据点所组成的，如果我们将这些数据点中的一些数据点有规律地抹掉，就会出现“破折号”样式的折线。因此，控制数据点的抹去模式就可以实现“破折号”样式的折线的多种展现形式。

+ `ax.plot(x, y, dashes=[10,2], label='dashes=[10,2]', **line_marker_style1)`中参数`dashes`的取值含义：折线组成单元是由线段长度为10个数据点、线段之间间隔2个数据点的单元样式组成。
+ `ax.plot(x, y+0.2, dashes=[3,1], label='dashes=[3,1]', **line_marker_style2)`中参数`dashes`的取值含义：折线组成单元是由线段长度为10个数据点、线段之间间隔1个数据点的单元样式组成。
+ `line_marker_style3 = dict(linestyle='--', lw=2, color='turquoise', markersize=10)`中`dashes`的取值含义：折线组成单元是由线段长度为2个数据点、线段之间间隔2个数据点的单元样式、折线组成单元是由线段长度为8个数据点、线段之间间隔2个数据点的单元样式组成。

这样，通过使用关键字参数`dashes`我们实现了“破折号”样式的线条类型的定制化展示的需求。借助关键字参数`dashes`的丰富组合模式，我们可以极大地丰富线条类型`--`的展现形式，让折线图的可视化效果呈现出多样性和定制化的特点。

### 9.4.2 案例2：标记填充样式的设置方法
前面已经介绍过有关标记类型的显示样式的相关内容。现在，再进一步考虑标记样式能否通过标记填充样式得以展现，也就是说，借助标记填充样式的选择也可以同样实现标记显示样式的设置需求，而且同种标记类型会由于标记填充样式的不同而呈现出更加丰富的展示效果，这就极大地丰富了标记展示样式的内容。
```python
import matplotlib.pyplot as plt
import numpy as np
font_style = dict(family='Arial Unicode MS', color='saddlebrown', weight='semibold', size=16)
line_marker_style = dict(linestyle=':', lw=2, color='cornflowerblue', markerfacecoloralt='lightgrey', marker='o', markersize=18)

fig = plt.figure()
ax = fig.add_subplot(111)
fillstyleList = ['full', 'left', 'right', 'bottom', 'top', 'none']
x = np.arange(3, 11, 1)
y = np.linspace(1, 1, 8)
ax.text(4, 6.5, 'fill style', **font_style)
for i,fs in enumerate(fillstyleList) :
    ax.text(0, i+0.4, "'{}'".format(fs), **font_style)
    ax.plot(x, (i+0.5)*y, fillstyle=fs, **line_marker_style)

ax.set_xlim(-1, 11)
ax.set_ylim(0, 7)
ax.margins(0.3)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
```
通过上面的代码和运行结果，可以知道标记填充样式的实现是借助关键字参数`fillstyle`实现的，关键字参数`fillstyle`的取值共有6种标记填充样式。我们现在也已经明白这6种标记填充样式，正如填充名称本身所定义的内容一样，填充名称用来指示填充颜色在标记类型中的位置，例如，关键字参数`fillstyle`取值是`left`，那么标记类型`o`的填充颜色就覆盖在标记类型`o`的左半边中，其他取值的含义与`left`的含义相类似，这里就不再介绍了。值得注意的是，标记颜色的关键字参数`markerfacecolor`用关键字参数`markerfacecoloralt`代替了，只有这样才能将***填充名称***`none`的展现形式有效地表现出来。

### 9.4.3 案例3：`plot()`的设置方法
函数plot()用来绘制有序数对的折线和标记的绘图函数。典型调用如下：

```python
plot([x], y, [fmt], **kwargs)

plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
```
参数`x`和`y`是输入值，然而参数`x`是选择输入值，如果省略`x`输入值，`x`输入值就是列表`[0,1,…,N-1]`，其中`N`是输入值`y`的**元素个数**。**_一般x和y输入值是长度N的数组，也可以是常数值组成的列表_**。

对于参数`fmt`，我们可以使用参数`fmt`控制线条颜色、标记样式和线条风格，也就是说， `fmt=[color][marker][linestyle]`。对于参数`fmt`的使用而言，这是格式化折线图的基本方式。对于线条颜色、标记样式和线条风格而言，我们可以选择其中的一种格式化方式或是多种格式化方式。因此，参数`fmt`是**一种便捷的字符串式注释**。例如，下面几种调用签名格式：
```python
plot(x, y)
plot(x, y, 'k') # black markers with default shape
plot(y)
plot(y, 'ro')   # red circles
```

折线图`plot()`的关键参数是`(keyword arguments)`，是`Line2D`实例。`Line2D`的属性可以作为关键字参数用来控制折线图的展现样式。例如，线条`label`、线条宽度`linewidth`、标记样式`linestyle`、标记颜色`markerfacecolor`等。

实例具有的属性是生成实例的类、函数或方法的关键字参数。因此，查找实例具有的属性工作就可以通过遍历实例对应的类、函数或方法的关键字参数来完成。而且实例`Line2D`的属性作为关键字参数经常和参数`fmt`混合使用，共同完成控制折线图的展示效果任务。

+ 实例`Line2D`可以通过下面的方法获得：
```python
line, = plt.plot(x, y, label='circles')
```
+ 对实例`Line2D`的属性(折线图的关键参数)控制就可以通过下面的语句实现：
```python
line.set_linewidth(2)
line.set_linestyle('--')
line.set_dashes([10, 2, 5, 2])
```
使用下面的调用签名所绘制的折线图是相同的：
```python
plot(x, y, 'ro:', linewidth=3, markersize=16, label='example1')
plot(x, y, color='r', linestyle=':', marker='o', linewidth=3, markersize=16, label='example1')
```
值的注意的是，在参数`fmt`和关键字参数存在冲突时，关键字参数优先执行绘图样式。我们在同一个坐标轴内可以绘制多条折线图，实现这一绘图模式的语句有以下两种做法。
```python
plot(x1, y1, 'ro');plot(x2, y2, 'b--')

plot(x1, y1, 'ro', x2, y2, 'b--')
```
如果`x`和`y`是`(N,M)`形状的数组，那么对于以上的实现语句就可以写成以下形式：
```python
plot(x[a], y[a], 'ro', x[b], y[b], 'b--')   # x, y is a (N,M) shaped array.
```
在`5.1.4`节中，我们讲过设置时间格式的刻度线标签的方法，这是设置时间序列图的简便方法。时间序列图可以理解成折线图的一种变形或是特例。也就是说，时间序列图是将x轴或是y轴用日期`date`标示，反映数据随时间延伸的趋势变化或是规律。在matplotlib中，时间序列图是包含日期的折线图，实现函数是`plot_date()`，函数`plot_date()`的参数和函数`plot()`的参数类似，只是坐标轴的刻度标签被格式化为日期数据。实例Line2D的属性依然可以作为函数`plot_date()`中的关键字参数`kwargs`，绘图格式化参数`fmt`依然可以使用，如果关键字参数`xdate`或是`ydate`取值是`True`，那么`参数x`和`参数y`的取值就会被理解成`matplotlib`中的日期。使用函数`plot_date()`实现的时间跨度可以任意设定，应用范围远远大于`5.1.4`节中所介绍的方法，但是，代码实现的复杂程度也较高。


# 10 `matplotlib`的配置
修改matplotlib的配置，可以满足定制化的展示需求，通过修改配置中的相关属性值可以使得可视化效果更理想，从而满足展示或印刷的质量要求。修改matplotlib的配置有两种途径：

+ 通过代码进行修改
+ 通过修改配置文件`matplotlibrc`实现

这两种设置方法可以分别理解成：一种是局部调整；另一种是全局修改。会在10.1节和10.2节分别讲解这两种实现方法的配置要点和相关技巧。

## 10.1 修改代码层面的`matplotlib`的配置
在本节中，我们讲解在代码层面进行matplotlib配置的实现方法。进行代码层面的属性值的设置，主要是解决个性化的项目需求，从而完成定制化的展示工作。通过代码层面的配置，我们可以按照具体项目的需求，灵活地进行matplotlib的相关属性值的设置，从而不必拘泥于系统默认的相关属性值的配置内容。这样，我们就可以非常方便地实现定制化的局部的matplotlib配置的设置需求。

绘图库matplotlib提供了很好的绘图功能，是Python中使用最多的数据可视化包。本节会介绍通过修改运行脚本的代码实现改变`matplotlib`的相关属性值的目的。

在代码实现方面，有两种方法实现改变`matplotlib`的相关属性值：
+ 调用属性字典`matplotlib.rcParams`或是属性字典`matplotlib.pyplot.rcParams`
+ 调用函数`matplotlib.rc()`或是函数`matplotlib.pyplot.rc()`。

如果需要恢复标准的`matplotlib`默认设置，则可以调用函数`matplotlib.rcdefaults()`或是函数`matplotlib.pyplot.rcdefaults()`。

分别以`matplotlib.rcParams`和`matplotlib.rc()`为例对两种设置方法进行讲解，`matplotlib.pyplot.rcParams`和`matplotlib.pyplot.rc()`的参数的设置方法与此完全相同。

### 10.1.1 方法1：调用函数`matplotlib.rc()`
```python
import matplotlib as mpl

# usage of package matplotlib
## method1 of setting attribution
mpl.rc('lines', linewidth=2, color='c', linestyle='--')

## method2 of setting attribution
line = {'linewidth':2, 'color':'c', 'linestyle':'--'}
mpl.rc('lines', **line)
```
通过调用函数`matplotlib.rc()`，我们可以将`lines`的相关属性以关键字参数的形式进行赋值，从而改变`matplotlib`的相关属性值。

也可以将属性和属性值放在一个字典中，将字典作为关键字参数，以`**line`形式进行参数调用，最终改变`matplotlib`的相关属性值。

### 10.1.2 方法2：调用属性字典`matplotlib.rcParams`
```python
import matplotlib as mpl

# usage of package matplotlib
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.color'] = c
mpl.rcParams['lines.linestyle'] = '--'
```
通过调用属性字典`matplotlib.rcParams`，利用属性字典的属性名、属性值的对应关系与更新字典键值的方法，就可以改变`matplotlib`的相关属性值。

## 10.2 修改项目层面的`matplotlib`配置
通过修改配置文件`matplotlibrc`，完成修改matplotlib的相关属性值的工作。通过这种方法，我们可以在没有其他定制化需求的情况下，始终使用我们配置好的`matplotlibrc`文件中的相关属性值，而不必每次在具体项目中进行相关属性值的设置。

### 10.2.1 配置文件路径
在`10.1`节中，我们讲解的关于修改matplotlib配置的设置方法是基于**代码层面**展开的。如果在每次编写新的代码时，都进行同样的matplotlib配置的设置，就显得没有必要，而且极大地降低了项目执行进度。例如，在一个项目中，通常会由很多个子项目组成，如果在每个子项目中都进行相同的matplotlib配置的设置，则会严重影响项目的进展速度和项目之间的协同配合。这时就可以在项目中使用一个独立于项目本身的matplotlib配置的设置方法，也就是在项目中使用matplotlibrc文件进行matplotlib配置的设置。这种设置方式可以使得matplotlib配置与代码分离，从而使代码更加简洁，很容易在项目间分享配置模板，提高协同工作的效率。

在项目层面修改matplotlib配置时，主要基于配置文件`matplotlibrc`所在的位置。配置文件主要存在于以下三种路径中，不同的路径决定了配置文件的调用顺序，下面就是配置文件`matplotlibrc`的使用先后顺序。

1. 项目所在路径：`matplotlibrc`文件在当前运行代码所在的目录中。
2. 配置文件的默认路径：
   + Windows：`$HOME/.matplotlib/`
   + Linux：如果`$HOME/.matplotlib/`存在，则在其中；若`$XDG_CONFIG_HOME`被定义，则在其中；或在`$HOME/.config`中。
   + 通过`matplotlib.get_configdir()`寻找

每次重新安装matplotlib时，matplotlibrc配置文件都会被覆盖。因此，当需要matplotlibrc配置文件被持久有效保存时，就需要将matplotlibrc配置文件移动到配置文件的默认目录中。

通过调用函数`matplotlib.matplotlib_fname()`，可以输出系统在项目本身包含配置文件matplotlibrc之外的调用配置文件的搜索路径。简单来讲，如果项目包含配置文件，那么就优先使用项目中的配置文件。

```python
import matplotlib.pyplot as plt
import numpy as np

# normal plot
plt.axes([0.1, 0.7, .3, .3], frameon=True, facecolor='y', aspect='equal')
plt.plot(np.arange(3), [0,1,0])
plt.cla()
plt.plot(np.arange(3), [0,1,0])

# no-plot
plt.axes([0.4, 0.4, .3, .3], frameon=True, facecolor='y', aspect='equal')
plt.plot(2+np.arange(3), [0,1,0])

# no-axes
plt.axes([0.7, 0.1, .3, .3], frameon=True, facecolor='y', aspect='equal')
plt.plot(4+np.arange(3), [0,1,0])
plt.axes('off')

plt.show()
```

# 11 文本属性设置
第10章讲解了配置文件`matplotlibrc`的配置要素的设置方法，其中配置要素`font`主要是控制字体属性的字体类别`family`、字体风格`style`、字体粗细`weight`、字体大小`size`、字体拉伸`stretch`和字体变体`variant`。接下来，我们就探讨字体属性的设置方法。

字体属性支持`matplotlib.text.Text`实例的属性，也支持函数`matplotlib.pyplot.text()`和实例方法`matplotlib.axes._axes.Axes.text()`的关键字参数。

| matplotlib.pyplot API  |     Matplotlib Object Oriented API      | 
|:----------------------:|:---------------------------------------:|
|         text()         |    matplotlib.axes._axes.Axes.text()    |
|        xlabel()        | matplotlib.axes._axes.Axes.set_xlabel() |
|        ylabel()        | matplotlib.axes._axes.Axes.set_ylabel() |
|         title()| matplotlib.axes._axes.Axes.set_title()  |
|suptitle()|matplotlib.figure.Figure.suptitle()|

如表所示为配置要素font的字体属性和对应的字体属性值。值得注意的是，字体属性`weight`中的属性值`a numeric value in range 0-1000`和字体属性`size`中的属性值`size in points`都表示实际数值，因此，在代码中作为参数值使用时**不需要添加双引号**，而其他的字体属性值也包括其他字体属性对应的字体属性值，在代码中以参数值形式使用时都需要添加双引号，如`family="serif"`。

|字体属性|字体属性值|
|:---:|:---:|
|family|serif</br>sans-serif</br>cursive</br>fantasy</br>monospace|
|style|normal</br>italic</br>oblique|
|weight|a numeric value in range 0-1000</br>ultralight</br>light</br>normal</br>regular</br>book</br>medium</br>roman</br>semibold</br>demibold</br>demi</br>bold</br>heavy</br>extra bold</br>black|
|size|size in points</br>xx-small</br>x-small</br>small</br>medium</br>large</br>x-large</br>xxlarge|
|variant|normal</br>small-caps|

下面就通过3种方法来探索改变这些配置要素值的视图效果，这3种方法分别是:
+ 改变配置文件matplotlibrc的字体属性值
+ 改变配置文件matplotlibrc的字体文本属性值
+ 调用属性字典rcParams及通过关键字参数进行设置。

**_值得注意的是_**，字体库`fonts`中应该包括需要配置的字体，例如字体库中应该包含`New Century Schoolbook`字体。

### 11.1.1 方法1：改变配置文件`matplotlibrc`的字体属性值和文本属性值

配置文件`matplotlibrc`：
```editorconfig
font.family         : serif
font.serif          : New Century Schoolbook
font.style          : normal
font.variant        : small-caps
font.weight         : black
#font.stretch        :normal
# note that font.size controls default text sizes. To configure
# special text sizes tick labels, axes, labels, title, etc, see the rc
# settings for axes and ticks. Special text sizes can be defined
# relative to font.size, using the following values: xx-small, x-small,
# small, medium, large, x-large, xx-large, larger, or smaller
font.size           : 12.0
#font.serif          : Bitstream Vera Serif, New Century Schoolbook, Century Schoolbook L, Utopia, 
text.color          : blue
```

### 11.1.2 方法2：通过属性字典`rcParams`调整字体属性值和文本属性值
```python
import matplotlib.pyplot as plt
import numpy as np
# line properties in change
plt.rcParams['lines.linewidth'] = 8.0
plt.rcParams['lines.linestyle'] = '--'
# font properties in change
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Arial Unicode MS'
plt.rcParams['font.style'] = 'normal'
plt.rcParams['font.variant'] = 'small-caps'
plt.rcParams['font.weight'] = 'black'
plt.rcParams['font.size'] = 12.0
# text properties in change
plt.rcParams['text.color'] = 'blue'
plt.axes([0.1, 0.1, .8, .8], frameon=True, facecolor='y', aspect='equal')
plt.plot(2+np.arange(3), [0,1,0])
plt.title("Line Chart")
# Add text in string 'Text instance' to axis at location 'x', 'y', data
# coordinates
plt.text(2.25, .8, 'FONT')
plt.show()
```
通过使用属性字典`rcParams`，同样完成了对`font`的字体属性值和`text`的文本属性值的设置，视图效果与方法1中的视图效果完全一致。`rcParams["font.serif"]`的键值以已经添加的字体文件在打开字体文件后出现的字体名称作为选择依据，键值`New Century Schoolbook`就是按照这一原则获取到的，而且尽量清除`matplotlib`文件夹中的文件`fontlist.cache`和文件夹`tex.cache`。

### 11.1.3 方法3：通过设置函数的关键字参数
```python
import matplotlib.pyplot as plt
import numpy as np
plt.axes([0.1, 0.1, .8, .8], frameon=True, facecolor='y', aspect='equal')
# line properties in change 
plt.plot(2+np.arange(3), [0,1,0], linewidth=8.0, linestyle='--')
plt.title('Line Chart', color='red', family='New Century Schoolbook', style='normal', variant='small-caps', weight='black', size=18)
# Add text in string 'Text isntance' to axis at locathyion 'x', 'y' data
# coordinates
# font properties and text properties in change
plt.text(2.25, .8, 'FONT', color='blue', fontdict={'family':'New Century Schoolbook', 'style':'normal', 'variant':'small-caps', 'weight':'black', 'size':2})

plt.show()
```
通过在函数`matplotlib.pyplot.text()`和`matplotlib.pyplot.title()`中设置关键字参数，实现控制配置要素`font`的字体属性值和配置要素`text`的文本属性值。

这里将标题`title()`的文本颜色设置为红色，注释文本`text()`的文本颜色设置为蓝色。这与上面的两种情况将文本颜色统一设置为蓝色有所区别。

## 11.2 手动添加字体

## 11.3 案例：字体主要属性可视化展示
我们在11.1节介绍了配置要素`font`的字体属性和对应的字体属性值，以及支持字体属性的函数`text()`。下面我们就看看通过函数`text()`展示配置要素`font`的字体属性和对应的字体属性值的实际效果，方便读者对配置要素font的字体属性和对应的字体属性值的内容进行深入理解。 

字体属性主要包括`family`（字体类别）、`style`（字体风格）、`size`（字体大小）、`variant`（字体变体）以及`weight`（字体粗细）等属性。这些字体属性是实例Text的属性，这些属性可以作为函数text()的关键字参数，这些属性对应的属性值可以作为参数值。因此，我们可以通过函数text()展示每种属性的属性值。

```python
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# viewing family options
families = ['serif', 'sans-serif', 'fantasy', 'monospace']

ax.text(-1,1, 'family', fontsize=18, horizontalalignment='center')

pi = [.9, .8, .7, .6, .5, .4, .3, .2, .1]

for i,family in enumerate(families) :
    ax.text(-1, pi[i], family, family=family, horizontalalignment='center')

# viewing size options
sizes = ['xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']
ax.text(-0.5, 1, 'size', fontsize=18, horizontalalignment='center')

for i,size in enumerate(sizes) :
    ax.text(-0.5, pi[i], size, size=size, horizontalalignment='center')

# viewing style options
styles = ['normal', 'italic', 'oblique']
ax.text(0,1, 'style', fontsize=18, horizontalalignment='center')

for i,style in enumerate(styles) :
    ax.text(0, pi[i], style, family='sans-serif', style=style, horizontalalignment='center')

# viewing variant options
variants = ['normal', 'small-caps']

ax.text(0.5,1, 'variant', fontsize=18, horizontalalignment='center')
for i, variant in enumerate(variants) :
    ax.text(0.5, pi[i], variant, family='serif', variant=variant, horizontalalignment='center')

# viewing weight options
weights = ['light', 'normal', 'semibold', 'bold', 'black']
ax.text(1,1, 'weight', fontsize=18, horizontalalignment='center')

for i,weight in enumerate(weights) :
    ax.text(1, pi[i], weight,weight=weight, horizontalalignment='center')

ax.axis([-1.5, 1.5, 0.1, 1.1])
ax.set_xticks([])
ax.set_yticks([])

plt.show()
```
我们对配置要素`font`的字体属性和对应的字体属性值进行了**迭代输出**，输出效果清晰直观地以`family`、`size`、`style`、`variant`和`weight`的顺序进行排列，对应的属性值也相应地展示出来，方便根据具体项目需要采用合适的字体属性和对应的字体属性值。

其中反复使用语句`for i,j in enumerate()`，内置函数`enumerate()`是将列表中的元素和元素所对应的索引分别赋给变量`j`和`i`,从而使for循环将索引和元素通过调用`Axes`的实例方法`text()`逐一进行输出展示。

# 12 颜色使用
## 12.1 使用颜色参数和颜色映射表
### 12.1.1 颜色参数的使用
在需要使用颜色参数的方法或是函数中，例如函数title(),`title(" a color map and color model",color="colorName")`，颜色参数color有以下几种使用模式。
+ 模式一：英文缩写模式的基本颜色

|缩写|颜色|缩写| 颜色  | 缩写  | 颜色  | 缩写  | 颜色  |
|---|---|---|-----|-----|-----|-----|-----|
|b|蓝色|g| 绿色  | r   | 红色  | c   | 青色  |
|m|泽红|y| 黄色  | k   | 黑色  | w   | 白色  |

+ 模式二：`Hex`模式的`#RRGGBB`字符串
```python
color = '#E0FFFF'
color = '#4682B4'
```
+ 模式三：`HTML/CSS`模式的颜色名
```python
color = 'lightgreen'
color = 'burlywood'
color = 'skyblue'
```
+ 模式四：`Decimal`模式的归一化到[0,1]的`(R,G,B)`元组
```python
color = (0.5294, 0.8078, 0.9216)
```
通过在极坐标系统下绘制柱状图的探索，展示颜色关键字参数的不同模式的参数值的使用方法。在极坐标轴上绘制的柱状图称为极区图，因为它既有饼图的样式又是借助函数bar()实现的。极区图由若干饼图中的饼片呈放射状投射在极坐标轴上，每一个饼片都是有一定角度的，同时饼片的半径类似于柱状图中柱体的高度，这也就解释了为什么可以通过函数bar()绘制极区图的原因。每一个饼片的颜色可以使用一种颜色来填充，颜色值可以使用模式1、模式2和模式3中的颜色定义方法来确定。

```python
import matplotlib.pyplot as plt
import numpy as np
barSlices = 12
theta = np.linspace(0, 2*np.pi, barSlices, endpoint=False)
radii = 30*np.random.rand(barSlices)
width = 2*np.pi/barSlices
colors = np.array(['c','m','y','b','#C67171', '#c1cdcd', '#ffec8b', '#a0522d', 'red', 'burlywood', 'chartreuse', 'green'])
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
bars = ax.bar(theta, radii, width=width, color=colors, bottom=0.0)
plt.show()
```
在关键字参数`color`中，我们使用`模式1`、`模式2`和`模式3`中的颜色定义方法进行饼片颜色的设定。

在函数`bar()`中，参数`theta`和参数`radii`分别用来确定饼片的角度和半径，饼片颜色由关键字参数`color`确定，全部饼片的半径起点是极径`0.0`，即由关键字参数`bottom`确定。
