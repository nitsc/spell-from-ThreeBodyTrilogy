import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread("F:/project/zhouyu/data/GRAPH/bigest/XY.png")

# 将图像转换为灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用128作为阈值进行二值化
_, binary_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)

# 将蓝色和红色像素分离
# 在原图上处理，区分蓝色和红色
red_mask = (img[:,:,2] > 128) & (img[:,:,0] < 128)  # 红色通道大于128，且蓝色通道小于128
blue_mask = (img[:,:,0] > 128) & (img[:,:,2] < 128)  # 蓝色通道大于128，且红色通道小于128

# 将红色和蓝色的掩码应用到二值化图像上
red_points = np.zeros_like(binary_img)
blue_points = np.zeros_like(binary_img)
red_points[red_mask] = 255
blue_points[blue_mask] = 255

# 显示结果
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Red Points')
plt.imshow(red_points, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Blue Points')
plt.imshow(blue_points, cmap='gray')
plt.axis('off')

plt.show()