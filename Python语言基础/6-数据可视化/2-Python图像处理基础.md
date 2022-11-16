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

pil_im_grey
```

### 创建缩略图
