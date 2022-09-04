***对于`matplotlib`版本在`2.0.0`以上，只需将代码关键字参数`axis_bgcolor`和`axisbg`更换为`facecolor`。
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
+ ls：折线图的线条风格。 
+ lw：折线图的线条宽度。 
+ label：标记图形内容的标签文本。

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05,10,1000)
y = np.cos(x)

plt.plot(x,y,ls='-',lw=2,label='plot figure')
plt.legend()    # 显示标签

plt.show()
```

### 1.3.2 `scatter()` 寻找变量间的关系
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
y = np.random.rand(1000)    

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
y = np.random.rand(1000)

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
plt
```

