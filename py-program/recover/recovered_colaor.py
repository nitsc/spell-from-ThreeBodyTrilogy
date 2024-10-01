import cv2
import numpy as np

def process_image(image_path):
    """
    将图像的黑色像素转换为蓝色，中心点改为红色

    Args:
        image_path: 图像路径

    Returns:
        处理后的图像
    """

    # 读取图像
    img = cv2.imread(image_path)

    # 获取图像高度和宽度
    height, width = img.shape[:2]

    # 定义黑色阈值（可以根据实际情况调整）
    black_threshold = 10

    # 找到黑色像素并转换为蓝色
    mask = np.all(img <= black_threshold, axis=2)
    img[mask] = [255, 0, 0]  # 蓝色

    # 将中心点改为红色
    center_x, center_y = width // 2, height // 2
    img[center_y, center_x] = [0, 0, 255]  # 红色

    return img

# 图像路径列表
image_paths = ["F:\project\zhouyu\data\\result\\recovered\smaller\\recovered_XY.png", 
               "F:\project\zhouyu\data\\result\\recovered\smaller\\recovered_XZ.png", 
               "F:\project\zhouyu\data\\result\\recovered\smaller\\recovered_YZ.png"]

paths = ['F:\project\zhouyu\data\\result\\recovered\smaller\\recovered_XY_color.png', 
               'F:\project\zhouyu\data\\result\\recovered\smaller\\recovered_XZ_color.png', 
               'F:\project\zhouyu\data\\result\\recovered\smaller\\recovered_YZ_color.png']

# 遍历图像列表并处理
for image_path in image_paths:
    processed_img = process_image(image_path)
    for path in paths:
        # 保存处理后的图像
        cv2.imwrite(path, processed_img)

print("图像处理完成！")