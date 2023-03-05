# -- coding: utf-8 --
import os
import pandas as pd
import matplotlib.pyplot as plt
print(__file__)
print(os.path.dirname(__file__))
print(os.path.dirname(__file__) + '\\dir\\file_name.file_type')

# 创建一个文件夹
dir_name = 'dir'
if not os.path.exists(os.path.dirname(__file__) + f'\\{dir_name}'):
    os.makedirs(os.path.dirname(__file__) + f'\\{dir_name}')

# pandas打开文件
df = pd.read_csv(os.path.dirname(__file__) + '\\dir\\file_name.file_type')

# pandas保存文件
pd.DataFrame(df).to_csv(os.path.dirname(__file__) + '\\dir\\file_name.file_type')

# matplotlib限制坐标轴范围
plt.xlim(0, 100)
plt.ylim(0, 100)

# matplotlib中文 宋体
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

# matplotlib英文 Times New Roman
plt.rcParams['font.sans-serif'] = ['Times New Roman']

# matplotlib标题与图像距离调远
plt.title('title', pad=20)
plt.subplots_adjust(top=0.9)

# matplotlib子图间距调远
plt.subplots_adjust(wspace=0.3, hspace=0.3)

# matplotlib设置四个子图
fig, ax = plt.subplots(2, 2, figsize=(10, 10))

# matplotlib保存图片
plt.savefig(os.path.dirname(__file__) + '\\dir\\file_name.file_type', dpi=1200, bbox_inches='tight')

# matplotlib显示图片
plt.show()
