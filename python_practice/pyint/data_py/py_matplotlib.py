import numpy as np
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

# # 创建画布f1,默认f1作为当前画布
# f1=mp.figure('f1 Figure')
# # xy正弦
# x1=np.linspace(-np.pi, np.pi, 1000)
# y1=np.sin(x1)
# y2=np.cos(x1)/2
# # <!-- 坐标轴范围 -->
# # mp.xlim(0, np.pi)
# # mp.ylim(0, 1)
# # <!-- 坐标轴刻度显示 -->
# xvals=[-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
# xtexts=['-Π','-Π/2','0','Π/2','Π']
# mp.xticks(xvals, xtexts)
# mp.yticks([-1.0, -0.5, 0.5, 1.0])
# # <!-- 修改坐标轴位置 -->
# ax=mp.gca()
# ax.spines['top'].set_color('none')
# ax.spines['right'].set_color('none')
# ax.spines['left'].set_position(('data', 0))
# ax.spines['bottom'].set_position(('data', 0))
# # <!-- 画线 -->
# mp.plot(x1,y1, linestyle='--', linewidth=2, color='orangered', alpha=0.8, label=r'$y=sin(x)$')
# mp.plot(x1,y2, linestyle='-.', linewidth=2, color='dodgerblue', alpha=0.9, label=r'$y=\frac{1}{2}cos(x)$')
# # <!-- 绘制特殊点 -->
# pointx=[np.pi/2, np.pi/2]
# pointy=[1, 0]
# mp.scatter(pointx, pointy, marker='o', s=70, color='red', zorder=3, label='simple points')
# # <!-- 图例 -->
# mp.legend(loc='best')

# # <!-- 创建画布f2,切换画布f2 -->
# x2=np.arange(0,50)
# y2=x2**2
# f2=mp.figure('f2 Figure',facecolor='gray')
# # 设置窗口f2的参数
# mp.title('f2 f2', fontsize=18)
# mp.xlabel('time', fontsize=14)
# mp.ylabel('price', fontsize=14)
# mp.tick_params(labelsize=10)
# mp.grid(linestyle=':')
# # 画f2
# mp.plot(x2,y2)

# # 创建f3窗口
# f2=mp.figure('f3 subplot Figure')
# for i in range(1,10):
#     mp.subplot(3,3,i)#子图行数,子图列数,子图编号
#     mp.text(0.5, 0.5, i, ha='center', va='center', size=36, alpha=0.6)
#     mp.xticks([])#x轴刻度设置为空
#     mp.yticks([])#y轴刻度设置为空
#     mp.tight_layout()#紧凑布局

# mp.figure('Grid Layout', facecolor='lightgray')
# # <!-- 调用GridSpec方法拆分网格式布局 -->
# # <!-- rows:行数 -->
# # <!-- cols:列数 -->
# # <!-- gs=mg.GridSpec(rows,cols) 拆分成3行3列 -->
# gs=mg.GridSpec(3,3)
# # <!-- 合并0行与0,1列为一个子图标 -->
# mp.subplot(gs[0,:2])
# mp.text(0.5,0.5,'1',ha='center',va='center',size=36,alpha=0.6)
# mp.xticks([])
# mp.yticks([])
# mp.tight_layout()
# # 第二个子图
# mp.subplot(gs[:2,-1])
# mp.text(0.5,0.5,'2',ha='center',va='center',size=36,alpha=0.6)
# mp.xticks([])
# mp.yticks([])
# mp.tight_layout()
# # 第三个子图
# mp.subplot(gs[1,1])
# mp.text(0.5,0.5,'3',ha='center',va='center',size=36,alpha=0.6)
# mp.xticks([])
# mp.yticks([])
# mp.tight_layout()
# # 第四个子图
# mp.subplot(gs[1:,0])
# mp.text(0.5,0.5,'4',ha='center',va='center',size=36,alpha=0.6)
# mp.xticks([])
# mp.yticks([])
# mp.tight_layout()
# # 第五个子图
# mp.subplot(gs[2,1:])
# mp.text(0.5,0.5,'5',ha='center',va='center',size=36,alpha=0.6)
# mp.xticks([])
# mp.yticks([])
# mp.tight_layout()

# mp.figure('Flow Layout', facecolor='lightgray')
# mp.axes([0.03, 0.52, 0.94, 0.4])
# mp.text(0.5, 0.5, '1', ha='center', va='center', size=36)
# mp.axes([0.03, 0.06, 0.54, 0.4])
# mp.text(0.5, 0.5, '1', ha='center', va='center', size=36)

# 刻度定位器
# mp.figure('Locator Layout', facecolor='lightgray')
# mp.xlim(1,10)
# # 获取当前坐标轴
# ax = mp.gca()
# # 隐藏除底轴以外的所有坐标轴
# ax.spines['top'].set_color('none')
# ax.spines['left'].set_color('none')
# ax.spines['right'].set_color('none')
# ax.spines['bottom'].set_position(('data',0.5))
# mp.yticks([])
# ax.xaxis.set_major_locator(mp.MultipleLocator(1))
# ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
# mp.text(5, 0.3, 'NullLocator()', ha='center', size=12)

# # 散点图
# n = 300
# height = np.random.normal(175, 10, n)
# weight = np.random.normal(70, 7, n)
# mp.figure('scatter', facecolor='lightgray')
# mp.title('scatter')
# mp.xlabel('height', fontsize=14)
# mp.ylabel('weight', fontsize=14)
# mp.grid(linestyle=':')
# # 样本点与期望值的距离,欧氏距离
# d = (height-172)**2 + (weight-60)**2
# # mp.scatter(height, weight, marker='o',s=70,label='person',color='dodgerblue')
# mp.scatter(height, weight, marker='o',s=70,label='person',c=d,cmap='jet')
# # cmap color map 数值越大 颜色越红 数值越小 颜色越蓝
# mp.legend()

# 柱状图
apples = np.array([30, 25, 22, 36, 21, 29, 20, 24, 33, 19, 27, 15])
oranges = np.array([24, 33, 19, 27, 35, 20, 15, 27, 20, 32, 20, 22])
x = np.arange(apples.size)
mp.figure('Bar'  , facecolor='lightgray')
mp.title('Bar Chart')
mp.bar(x+0.2,apples,width=0.4,color='dodgerblue',label='Apples',alpha=0.8)
mp.bar(x-0.2,oranges,width=0.4,color='orangered',label='Oranges',alpha=0.8)
mp.xlabel('Month',fontsize=12)
mp.ylabel('Sales',fontsize=12)
mp.xticks(x,[
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
mp.ylim((0, 40))
mp.legend()

mp.show()