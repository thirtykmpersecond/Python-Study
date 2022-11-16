# Python图像处理基础

## PIL库
PIL库在Python3中可以使用`pillow`库替代。

### 读取图片
```python
from PIL import Image

# 读取文件图片
pil_im = Image.open(r'/Users/pain/Desktop/Python数据及相关的资料.nosync/zhouzhou.jpg')

## 转化为灰度图
pil_im_grey = pil_im.convert('L')

pil_im_grey.show()
```

### 创建缩略图
`thumbnail()`方法可以接受一个元组参数，该参数指定生成缩略图的大小，然后将图像转换成符合元组参数指定大小的图像。
```python
pil_im.thumbnail((128,128))

pil_im.show()
```

### 复制和粘贴图像区域
`crop()`方法可以从一幅图像中裁剪指定区域。
```python
from PIL import Image
pil_im = Image.open('/Users/pain/Desktop/Python数据及相关的资料.nosync/zhouzhou.jpg')

box = (150, 350, 400, 600)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_90)
pil_im.paste(region, box)
pil_im.show()
```

### 调整尺寸和旋转
调整尺寸可用`resize()`方法，旋转图像可用`rotate()`方法，该方法参数表示逆时针旋转角度。
```python
from PIL import Image
pil_im = Image.open('/Users/pain/Desktop/Python数据及相关的资料.nosync/zhouzhou.jpg')

out = pil_im.resize((128, 128))

# 旋转图像
out = out.rotate(45)
out.show()
```

### 图像轮廓和直方图
显示图像轮廓和直方图。
```python
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

im = np.array(Image.open(r'/Users/pain/Desktop/Python数据及相关的资料.nosync/zhouzhou.jpg').convert('L'))

print('图片大小', im.shape)

## 图像轮廓
fig = plt.figure()
ax1 = fig.add_subplot(121)

## 不使用颜色信息
plt.gray()

## 在原点左上角显示图像轮廓
ax1.contour(im, origin='image')
ax1.axis('equal')   #设置坐标轴为正方形

## 直方图
ax2 = fig.add_subplot(122)
ax2.hist(im.flatten(), 128)
plt.show()
```

## OpenCV库

### 1. 读取和写入图像
`imread()`返回图像是一个标准的Numpy数组，且该函数能够处理很多不同格式的图像。可以作为PIL模块读取图像的备选方案。
`imwrite()`会根据文件后缀自动转换图像。

```python
import cv2

# 读取图像
im = cv2.imread(r'/Users/pain/Desktop/Python数据及相关的资料.nosync/zhouzhou.jpg')
print(im.shape)

# 保存图像
cv2.imwrite(r'/Users/pain/Desktop/Python数据及相关的资料.nosync/zhouzhou1.jpg', im)
```

### 2. 颜色空间
在OpenCV中，图像不是按照传统的RGB颜色通道，而是按照BGR顺序即RGB倒序存储。读取默认BGR，但是还有一些可用的转换函数。

颜色空间转换函数可用`cvtColor()`实现。例如转换为灰度图像：
```python
import cv2

im = cv2.imread(r'/Users/pain/Desktop/Python数据及相关的资料.nosync/zhouzhou.jpg')

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
print(gray)
print(gray.shape)
```
最有用的一些代码如下： 
+ cv2.COLOR_BGR2GRAY
+ cv2.COLOR_BGR2RGB
+ cv2.COLOR_GRAY2BGR

### 3. 图像显示
可以使用matplotlib来显示OpenCV中的图像
```python
import matplotlib.pyplot as plt
import cv2

## 读取图像
im = cv2.imread('/Users/pain/Desktop/Python数据及相关的资料.nosync/zhouzhou.jpg')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

## 计算图像积分
intim = cv2.integral(gray)

## 归一化并保存
intim = (255*intim)/intim.max()

plt.figure(figsize=(12,6))
plt.subplot(121)
plt.imshow(gray)
plt.title('YTZ picture')
plt.subplot(122)
plt.imshow(intim)
plt.title('YTZ integral')
plt.show()
```