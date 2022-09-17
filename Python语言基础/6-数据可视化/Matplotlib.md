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