from PIL import Image
import numpy as np
import os 

# 读取图片
img1 = Image.open("D:\\temp\\spell-from-ThreeBodyTrilogy-main\\data\\result\\graph\\2D_plot_xy_367.png").convert('L')  # 转换为灰度图
img2 = Image.open("D:\\temp\\spell-from-ThreeBodyTrilogy-main\\data\\result\\graph\\2D_plot_xz._367.png").convert('L')
img3 = Image.open("D:\\temp\\spell-from-ThreeBodyTrilogy-main\\data\\result\\graph\\2D_plot_yz._367.png").convert('L')

# 将图片转换为二值化数据
def img_to_bits(img):
    img_data = np.array(img)
    binary_data = (img_data > 128).astype(int)  # 将像素值大于128的转为1，小于等于128的转为0
    return binary_data.flatten()

# 获取每张图片的比特串
bits_xy = img_to_bits(img1)
bits_xz = img_to_bits(img2)
bits_yz = img_to_bits(img3)

# 将三张图的比特串串联成一个长信号
signal = np.concatenate([bits_xy, bits_xz, bits_yz])

# 输出信号长度和部分内容
print(f"Generated signal with length: {len(signal)}")
print(f"First 100 bits of signal: {signal[:100]}")

# 获取桌面路径
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 你也可以将信号保存为文件
with open(os.path.join(desktop_path,"signal.txt"), 'w') as f:
    f.write(''.join(signal.astype(str)))
    print("Successfully saved signal to signal.txt")
