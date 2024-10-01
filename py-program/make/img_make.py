import numpy as np
import pandas as pd
from mayavi import mlab
import os

# 读取数据
file_path = "F:\\project\\zhouyu\\data\\source\\csv\\南二门xyz.csv"
data = pd.read_csv(file_path)

bs = 1
x = data['X'] * bs
y = data['Y'] * bs
z = data['Z'] * bs

# 创建图形窗口
fig = mlab.figure(size=(3142, 3142), bgcolor=(1, 1, 1))

# 绘制散点图
mlab.points3d(x, y, z, color=(0, 0, 1), scale_factor=0.3)

# 添加一个额外的点
mlab.points3d(0, 0, 0, color=(1, 0, 0), scale_factor=0.3)

# 获取桌面路径
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 创建四个视图并保存 (第一个是测试视图，因为往往第一个无法保存为想要的格式)
for view, angle in zip(['TEXT', 'XY', 'XZ', 'YZ'], [(1, 1), (90, 0), (0, 90), (0, 0)]):
    mlab.view(azimuth=angle[0], elevation=angle[1])
    mlab.savefig(os.path.join(desktop_path, f"{view}.png"), figure=fig, size=(3142, 3142))

# 显示图形（可选，如果要交互查看）
mlab.show()
