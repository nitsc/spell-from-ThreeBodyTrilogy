import numpy as np
from PIL import Image

width, height = 367,367

def bits_to_img(bits, width, height):
    # 将一维比特串 reshape 成二维数组
    binary_data = np.array(bits).reshape(height, width)
    # 将二值数据转换为灰度图像 (0-255)
    gray_img = binary_data * 255
    return Image.fromarray(gray_img.astype(np.uint8))

# 读取保存的信号
with open("F:\project\zhouyu\data\\result\\recovered\smaller\\recovered_signal.txt", 'r') as f:
    signal_str = f.read()
signal = np.array(list(signal_str), dtype=int)

# 分割信号并还原图像
bits_xy = signal[:width*height]
bits_xz = signal[width*height:2*width*height]
bits_yz = signal[2*width*height:]

img1_recovered = bits_to_img(bits_xy, width, height)
img2_recovered = bits_to_img(bits_xz, width, height)
img3_recovered = bits_to_img(bits_yz, width, height)

# 保存恢复的图像
img1_recovered.save('F:\project\zhouyu\data\\result\\recovered\smaller\\recovered_XY.png')
img2_recovered.save('F:\project\zhouyu\data\\result\\recovered\smaller\\recovered_XZ.png')
img3_recovered.save('F:\project\zhouyu\data\\result\\recovered\smaller\\recovered_YZ.png')