# 使用Python对数据进行可视化处理
## 准备工作
```bash
#安装ggplot
pip install ggplot
```


+ `Jupyter`设置图像显示方式如下：

```Python
%matplotlib inline #jupyter中嵌入显示
%config InlineBackend.figure_format = 'retina'	#呈现分辨率较高图像
```



> ```python
> %matplotlib inline	#在Jupyter中嵌入显示
> import pandas as pd
> from ggplot import *	#安装ggplot库
> meat_lng = pd.melt(meat[['date','beef','pork','broilers']], id_vars='date')
> ggplot(aes(x='date',y='value',colour='variable'), data=meat_lng) + geom_point(color='red')
>  
>  #修改配置:
>  #~/opt/anaconda3/envs/python38/lib/python3.8/site-packages/ggplot/utils.py
>  #pd.tslib.Timestamp --> pd.Timestamp
>  
> # ~/opt/anaconda3/envs/python38/lib/python3.8/site-#packages/ggplot/stats/smoothers.py
> # pd.tslib.Timestamp --> pd.Timestamp
> # from pandas.lib import Timestamp --> from pandas import Timestamp
> ```



+ Matplotlib显示中文方式如下

```python
import matplotlib.pyplot as plt
import numpy as np
#设置字体
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/System/Library/Fonts/PingFang.ttc', size=14)
matplotlib.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号

t = np.arange(1,10,0.05)
x = np.sin(t)
y = np.cos(t)

# 定义一个图像窗口
plt.figure(figsize=(8,5))
#绘制一条线
plt.plot(x,y,"r-*")
#使坐标轴相等
plt.axis("equal")
plt.xlabel("正弦", fontproperties = font)
plt.ylabel('余弦', fontproperties = font)
plt.title('A Circle', fontproperties = font)
#显示图像
plt.show()
```

## Matplotlib绘图示例

### 点图和线图

点图和线可以表示二位数据之间的关系，是查看两个变量之间关系的最直观的方法，可以通过`plot()`得到。

使用`subplot`可以绘制多个子图图像，并且可以添加`X`、`Y`坐标轴名称以及标题。
```python
##subplot()绘制多个子图
import numpy as np
import matplotlib.pyplot as plt

#生成X
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
#生成Y
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

#绘制第一个子图
plt.subplot(2,1,1)  #subplot(numRows, numCols,plotNum)
plt.plot(x1, y1, 'yo-') # x1,y1分别为横纵坐标
plt.title('A tale of 2 subplots')   # 
plt.ylabel('Damped oscillation')
#绘制第二个子图
plt.subplot(2,1,2)
plt.plot(x2,y2,'r.-')
plt.xlabel('time(s)')
plt.ylabel('Undamped')
#生成结果
plt.show()
```
+ 绘图可以调用`matplotlib.pyplot`库来进行，方式如下：
```python
plt.plot(x, y, format_string, **kwargs)
```
1. x表示x轴数据，列表或数组，可选
2. y表示y轴数据，列表或数组。
3. `format_string`表示控制曲线的格式字符串，可选
4. `**kwargs`表示第二组或更多`(x, y, format_string)`
5. **PS:绘制多条曲线时，各条曲线的参数x不能省略**

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

## 直方图

统计学中，`直方图(Histogram)`是一种对数据分布情况对图形表示，是一种二位统计图标，他的两个坐标分别是**统计样本**和**该样本对应的某个属性**的度量。

我们使用`hist()`函数来绘制向量的直方图，计算出直方图的概率密度，并绘制出概率密度曲线，在标注中使用数学表达式。代码如下：
```python
## 直方图
import numpy as np
#import matplotlib.mlab as mlab     #用不上
import matplotlib.pyplot as plt
from scipy.stats import norm    #不添加的话mlab.normpdf会报错，
# 示例数据
mu = 100    #分布均值
sigma = 15  #分布标准差
x = mu + sigma*np.random.randn(10000)   #从正态分布返回一组数据
print("x:", x.shape)

# 直方图的条数
num_bins = 50
#绘制直方图
#n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
#Change normed attribute in the code to density
#then also add an attribute stacked = True
n, bins, patches = plt.hist(x, num_bins, density = True, facecolor='green', alpha=0.5, stacked=True)
#添加一个最佳拟合曲线
#原先写法,报错
#y = mlab.normpdf(bins, mu, sigma)
y = norm.pdf(bins, mu, sigma)   #返回关于数据的pdf数值（概率密度函数）
plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')
## 在图中添加共识需要使用 latex 语法
plt.title('Histogram of IQ: $\mu=100$, $\sigma=15$')
#调整图像间距，防止y轴数值与label重合
plt.subplots_adjust(left=0.15)
plt.show()
print('bind:\n', bins)
```

+ `hist()`函数格式如下
```python
import matplotlib.pyplot as plt
n, bins, patches = plt.hist(arr, bins=10, density=True,stacked=True, facecolor='black', edgecolor='black', alpha=1 )
```
***计算并绘制x的直方图。如果输入包含多个数据，则返回值为元组（n，bins，补丁）或（[n0，n1，...]，bins，[patches0，patches1，...]）。***
+ arr: 直方图的一维数组`x`
+ bins: 直方图的柱数，默认为10
+ density: 是否将得到的直方图向量归一化
+ facecolor: 直方图颜色
+ edgecolor: 直方图边框颜色
+ alpha: 透明度
+ histtype: 直方图类型,有`bar`,`barstacked`,`step`,`stepfilled`几种类型
返回值：
+ n:直方图向量，是否归一化由参数density决定
+ bins:返回各个bin的区间范围
+ patches:返回每个bin里面包含的数据，是一个list

## 等线值图
又称为等量线图，是以相等数值点的连线表示连续分布且逐渐变化的数量特征的一种图型，是用数值相等各点连成的曲线（即等值线）在平面上的投影来表示被摄物体的外形和大小的图

使用`contour()`函数将三维图像在二维空间上表示，并且使用`clabel()`在每条线上显示数据值的大小。
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# 生成数据
delta = 0.2
x = np.arange(-3, 3, delta) #np.arange()返回给定区间内均匀的值
y = np.arange(-3, 3, delta)
X, Y = np.meshgrid(x,y)     #从坐标向量返回坐标矩阵
Z = X**2 + Y**2
x = X.flatten()     #返回一维的数组，但该函数只能适用于numpy对象（array或mat）
y = Y.flatten()
z = Z.flatten()

# 定义一个图像窗口
fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(121,projection='3d')
# 绘制三角形曲面，cmap指颜色，默认绘制为RGB(A)颜色空间，jet表示“蓝-青-黄-红”颜色
ax1.plot_trisurf(x,y,z, cmap=cm.jet, linewidth=0.01)
plt.title("3D")
ax2 = fig.add_subplot(122)
# 大写的XYZ。 15代表的是显示等高线的密集程度，数值越大，画的等高线数就越多。
#`contour()`函数将三维图像在二维空间上表示
cs = ax2.contour(X,Y,Z, 15,cmap='jet', )    
# clabel()在每条线上显示数据值的大小。
ax2.clabel(cs, inline=True, fontsize=10, fmt='%1.1f')
plt.title("Contour")
plt.show()
```

## 三维曲面图
通常用来描绘三维空间的数值分布和形状。可以通过`plot_surface()`函数来得到想要的图像。
```python
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

# 三维图像+各个轴的投影等高线
fig = plt.figure(figsize=(8,6))
ax = fig.gca(projection='3d')

# 生成三维测试数据
X,Y,Z = axes3d.get_test_data(0.05)
ax.plot_surface(X,Y,Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contour(X,Y,Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contour(X,Y,Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contour(X,Y,Z, zdir='y', offset=40, cmap=cm.coolwarm)
ax.set_xlabel('X')
ax.set_xlim(-40,40)
ax.set_ylabel('Y')
ax.set_ylim(-40,40)
ax.set_zlabel('Z')
ax.set_zlim(-100,100)
plt.show()
```

## 条形图
条形图(Bar Chart)是一种以长方形为变量的统计图表。**用来比较两个或两个以上的数值（不同时间按或不同条件），只有一个变量，通常利用较小的数据集分析**。

亦可横向排列或多维表达。
```python
"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
n_groups = 5 # 组数
# 平均分和标准差
means_men = (20, 35, 30, 35, 37)
std_men = (2, 3, 4, 1, 2)

means_women = (25, 32, 34, 20 ,25)
std_women = (3, 5, 2, 3, 3)
# 条形图
fig, ax = plt.subplots()
# 生成0， 1， 2， 3，……
index = np.arange(n_groups)
bar_width = 0.35 #条的宽度

opacity = 0.4
error_config = {'ecolor': '0.3'}
# 图形中的第一类条
rects1 = plt.bar(index, means_men, bar_width, alpha=opacity, color='b', yerr=std_men, error_kw = error_config, label='Men')
# 图形中的第二类条
rects2 = plt.bar(index+bar_width, means_women, bar_width, alpha = opacity, color='r', yerr=std_women, error_kw=error_config, label='Women')
plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(index + bar_width, tuple(list('ABCDE')))
plt.legend()
## 自动调整subplot参数给指定填充区
plt.tight_layout()
plt.show()
```

## 饼图
可以使用`pie()`函数绘制饼图.
```python
import matplotlib.pyplot as plt
## 切片按照顺时针方向排列并绘制

# 每块饼的标签
labels = 'Forgs', 'Hogs', 'Dogs', 'Logs'
# 每块饼的大小
size = [15, 30, 45, 10]
# 颜色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
#偏移值
explode = (0, 0.1, 0, 0)
# autopct: 保留小数值
# startangle: 图型起始点偏移量
plt.pie(size, explode=explode, labels=labels, colors=colors, autopct = '%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
```

## 气泡图/散点图
通过每个点面积大小，反映第三维数。气泡图可以表示多维数据。

`scatter()`函数绘制散点图
```python
import matplotlib.pyplot as plt
import pandas as pd
df_data = pd.read_csv('https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv')

# 作图
fig, ax = plt.subplots()
# 设置气泡图颜色
color = ['#99CC01','#FFFF01','#0000FE','#FE0000','#A6A6A6','#D9E021','#FFF16E','#0D8ECF','#FA4D3D','#D2D2D2','#FFDE445','#9b59b6']
# 创建气泡图 sepal.length 为x， sepal.width为y ,同时设置petal.length为气泡大小，并设置颜色透明度
ax.scatter(df_data['sepal.length'], df_data['sepal.width'], s=df_data['petal.length']*100, c=color, alpha=0.6)

```