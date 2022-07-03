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

t =  np.arange(1,10,0.05)
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
plt.subplot(2,1,1)
plt.plot(x1, y1, 'yo-')
plt.title('A tale of 2 subplots')
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
plt.plot(x,y,format_string, **kwargs)
```
1. x表示x轴数据，列表或数组，可选
2. y表示y轴数据，列表货属组
3. `format_string`表示控制曲线的格式字符串，可选
4. `**kwargs`表示第二组或更多`(x,y,format_string)`
5. **PS:绘制多条曲线时，各条曲线的参数x不能省略

+ 在`matplotlib`下，一个`Figure`对象可以包含多个`子图(Axes)`，可以使用`subplot()`快速绘制
```python
subplot(numRows, numCols,plotNum)
```
图标的