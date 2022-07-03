import matplotlib.pyplot as plt
import numpy as np
#设置字体
import pandas as pd
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/System/Library/Fonts/PingFang.ttc', size=14)

'''from ggplot import *
meat_lng = pd.melt(meat[['date','beef','pork','borilers']], id_vars='date')
ggplot(aes(x='date',y='value', color = 'variable'), data=meat_lng)+geom_point(color='red')
'''
t =  np.arange(1,10,0.05)
x = np.sin(t)
y = np.cos(t)

#定义一个图像窗口
a = plt.figure(figsize=(8,5))
#绘制一条直线
a = plt.plot(x,y,"r-*")