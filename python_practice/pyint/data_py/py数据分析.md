# 1. numpy相关
## 1.1. ndarray对象

### 1.1.1 特点
多维数组对象，每个元素都占有相同大小的内存块，因此ndarray中元素类型相同

### 1.1.2 参数
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

copy参数
```
a=np.array([1,2,3,4,5])
b=np.array(a,copy=true)
```
指定copy=true时，创建b和a，当修改b时，a不会发生改变

### 1.1.3 实践
创建一维数组
```
a=np.array([1,2,3])
```

创建二维数组
```
b=np.array([[1,2,3],[4,5,6]])
```

嵌套序列数量不一样的情况
```
c=np.array([[1,2,3],[4,5]])
c
array([list([1, 2, 3]), list([4, 5])], dtype=object)
```

## 1.2. arange
### 1.2.1 参数
numpy.arange(start, stop, step, dtype)
不包含stop

### 1.2.2 实践
浮点型范围
```
ran1 = np.arange(3.1)
array([0., 1., 2., 3.])
```

np.arange(10,20,2)

200米的校园主干道一侧，从起点开始每隔3米插一面彩旗，由近到远排成一排
彩旗会插到终点处吗
一共需要多少面彩旗
r1=np.arange(0,200,3)
len(r1)

## 1.3. linspace等差数列
### 1.3.1 参数
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

### 1.3.2 实践

ar1=np.linspace(2.0, 3.0, num=5, endpoint=False, retstep=True)
ar1
(array([2. , 2.2, 2.4, 2.6, 2.8]), 0.2)

ar2=np.linspace(2.0, 3.0, num=5)                              
ar2
array([2.  , 2.25, 2.5 , 2.75, 3.  ])

### 1.3.3 用途
等插数列在线性回归经常作为样本集，比如生成x_data，值为[0,100]之间500个等差数列数据集合作为样本特征，
根据目标线性方程y=3*x+2，生成相应的标签集合y_data

## 1.4. logspace等比数列
### 1.4.1 参数
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)

### 1.4.2 实践
序列的起始值为：base ** start
序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中

## 1.5. 数组属性
### 1.5.1 参数
| 属性             | 说明                                        |
| ---------------- | ------------------------------------------- |
| ndarray.ndim     | 秩，即轴的数量或维度的数量                  |
| ndarray.shape    | 数组的维度，对于矩阵，n 行 m 列             |
| ndarray.size     | 数组元素的总个数，相当于 .shape 中 n*m 的值 |
| ndarray.dtype    | ndarray 对象的元素类型                      |
| ndarray.itemsize | ndarray 对象中每个元素的大小，以字节为单位  |

### 1.5.2 shape
一维数组
```
a=np.array([1,2,3,4,5,6])
a.shape
(6,)
```

二维数组
```
a=np.array([[1,2,3],[4,5,6]])
a.shape
(2, 3)
```

三维数组
```

```

### 1.5.3 reshape
a=np.arange(20).reshape((4,5))
a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])

### 1.5.4 resize
np.resize(a, new_shape)如果新数组大于原始数组，则新数组将填充a的重复副本
a=np.array([[0,1],[2,3]])
b=np.resize(a, (2,3))
b
array([[0, 1, 2],
       [3, 0, 1]])
注意：此行为和a.resize(new_shape)不同，后者用0填充，而不是重复的a填充

## 1.6. 切片和索引
### 1.6.1 二维数组
```
a1=np.arange(20).reshape((4,5))
a1[...,1] 所有行第二列
a1[...,1:] 所有行第二列及后的
a1[1,2] == a1[1][2]
a1[...][1] 第二行
```

### 1.6.2 整数数组索引
```
x=np.array([[1,2],[3,4],[5,6]])
y=x[[0,1,2],[0,1,0]]
x是二维数组
y分别获取x中的(0,0),(1,1),(2,0)的数据
```

获取4*3数组中的四个角上元素,它们对应的行索引是[0,0]和[3,3],列索引是[0,2]和[0,2]
b=np.arange(12).reshape((4,3))
y=b[[0,0,3,3],[0,2,0,2]].reshape(2,2)

创建一个8x8的国际象棋棋盘矩阵(黑块为0,白块为1)
1.[0,1,0,1,0,1,0,1]
2.[1,0,1,0,1,0,1,0]
3.[0,1,0,1,0,1,0,1]
4.[1,0,1,0,1,0,1,0]
5.[0,1,0,1,0,1,0,1]
6.[1,0,1,0,1,0,1,0]
7.[0,1,0,1,0,1,0,1]
8.[1,0,1,0,1,0,1,0]
第一步,创建全0的8x8矩阵
a1=np.zeros((8,8),dtype=int)
第二步,特殊位置赋值为1
a1[1::2, 0::2]=1
a1[0::2, 1::2]=1

### 1.6.3 布尔索引
返回所有大于6的数字组成的数组
a1=np.arange(12).reshape(4,3)
a1[a1>6]

提取数组中所有奇数
a1[a1%2!=0]

修改奇数值为-1
a1[a1%2==1] -= 1

筛选指定数据
筛选大于4小于9的数据
a1=np.arange(12).reshape(4,3)
a1[(a1>4) & (a1<9)]

筛选大于4或者小于9的数据
a1[(a1>4) | (a1<9)]

筛选3x4数组的第一行,最后一行的第1,3,4列的数据
a1=np.arange(12).reshape(3,4)
先筛选头尾两行,是个二维数组,再选三列数据
a1[[0,-1],:][:,[0,2,3]]

## 1.7. 广播机制
对形状较小的数组，在横向或者众向上进行一定次数的重复，使其形状与较大的数组拥有相同的维度
```
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([0,1,2])
a+b
```
4x3 的二维数组与长为 3 的一维数组相加，等效于把数组 b 在二维上重复 4 次再运算

广播的规则:
让所有输入数组都向其中形状最长的数组看齐，形状中不足的部分都通过在前面加 1 补齐。
输出数组的形状是输入数组形状的各个维度上的最大值。
如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为 1 时，这个数组能够用来计算，否则出错。
当输入数组的某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值。

简单理解：对两个数组，分别比较他们的每一个维度（若其中一个数组没有当前维度则忽略），满足
数组拥有相同形状。
当前维度的值相等。
当前维度的值有一个是 1。
若条件不满足，抛出 "ValueError: frames are not aligned" 异常。

## 1.8. numpy统计函数
### 1.8.1 平均值和中位数
平均数 m1.mean()
m1=np.arange(20).reshape((4,5))
m1
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
m1.mean(axis=0)
array([ 7.5,  8.5,  9.5, 10.5, 11.5])
axis=0表示从上往下计算平均值
m1.mean(axis=1)
array([ 2.,  7., 12., 17.])
axis=0表示从左往右计算平均值

中位数 np.median(ndarray)
np.median(m1)
9.5
a1=np.array([1,2,3,4,100])
np.median(a1)
3.0

### 1.8.2 标准差和方差
方差
((每个数 - 平均数) ** 2次方)总和 // 个数

标准差(平均数分散程度)
方差的算术平方根(开方)
例如,AB两组学生成绩,哪组学生之间差距大
A 95,85,75,65,55,45
B 73,72,71,69,68,67
a1=np.array([95,85,75,65,55,45]) 
b1=np.array([73,72,71,69,68,67]) 
np.std(a1) 
17.07825127659933
np.std(b1) 
2.160246899469287

np.sqrt(np.sum((a1-np.mean(a1))**2)/a1.size)

### 1.8.3 最大和最小
最小从上往下
m1.min(axis=0)
array([0, 1, 2, 3, 4])

最小从左往右
m1.min(axis=1)
array([ 0,  5, 10, 15])

类似 max, sum

### 1.8.4 加权平均数
np.average(a, axis=None, weights=None, returned=False)

权重不指定
a1=np.array([20,30,50])
np.mean(a1)
33.333333333333336
np.average(a1)
33.333333333333336

指定权重
| 姓名 | 平时测验 | 期中考试 | 期末考试 |
| ---- | -------- | -------- | -------- |
| 小明 | 80       | 90       | 95       |
| 小刚 | 95       | 90       | 80       |

权重
| 平时测验占比 | 期中考试占比 | 期末考试占比 |
| ------------ | ------------ | ------------ |
| 20%          | 30           | 50           |

计算综合成绩谁更好
a1=np.array([80,90,95]) 
b1=np.array([95,90,80]) 
w=np.array([0.2,0.3,0.5])
np.average(a1,weights=w)
90.5
np.average(b1,weights=w)
86

## 1.9. 数据类型
### 1.9.1 结构化数据类型
描述一位老师的姓名,年龄,工资的特征,该结构化数据包含以下字段:
str字段 name
int字段 age
float字段 salary
teacher=np.dtype([('name',np.str_,2),('age','i1'),('salary','f4')])
a=np.array([('wl',37,8357.50),('lh',28,7856.80)], dtype=teacher)
a['name']

## 1.10. numpy操作文件
### 1.10.1 参数
numpy.loadtxt(fname, dtype='float', comments='#', delimiter=None, converters=None, skiprows=0, usecols=None,unpack=False, ndmin=0, encoding='bytes')

fname 指定文件名称或路径
dtype 数据类型
comments 字符串或字符串列表，表示注释字符开始的标志
delimiter 字符串，分隔符
converters 字典，将特定列的数据通过字典中对应的函数转换
skiprows 跳过特定行数据
usecols 元组，用来指定要读取的列号
unpack 布尔值，指定是否转置数组
ndmin 整数型，指定返回的数组中至少包含特定维度的数组
encoding 编码

# 2. matplotlib相关
## 2.1 基本绘图
### 2.1.1 绘制正弦图形
xy折线
import matplotlib.pyplot as mp
x=np.arange(1,7)
y=np.array([12,39,36,25,13,41])
mp.plot(x,y)
mp.show()

xy正弦
x=np.linspace(-np.pi, np.pi, 1000)
y1=np.sin(x)
y2=np.cos(x)/2
<!-- 创建画布1,默认作为当前画布 -->
f1=mp.figure('f1 Figure')
<!-- 坐标轴范围 -->
mp.xlim(0, np.pi)
mp.ylim(0, 1)
<!-- 坐标轴刻度显示 -->
xvals=[-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
xtexts=['-Π','-Π/2','0','Π/2','Π']
mp.xticks(xvals, xtexts)
mp.yticks([-1.0, -0.5, 0.5, 1.0])
<!-- 修改坐标轴位置 -->
ax=mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
<!-- 画线 -->
mp.plot(x,y1, linestyle='--', linewidth=2, color='orangered', alpha=0.8, label=r'$y=sin(x)$')
mp.plot(x,y2, linestyle='-.', linewidth=2, color='dodgerblue', alpha=0.9, label=r'$y=\frac{1}{2}cos(x)$')
<!-- 绘制特殊点 -->
pointx=[np.pi/2, np.pi/2]
pointy=[1, 0]
mp.scatter(pointx, pointy, marker='o', s=70, color='red', zorder=3, label='simple points')
<!-- 图例 -->
mp.legend(loc='best')
<!-- 创建画布2,切换画布 -->
x2=np.arange(0,50)
y2=x2**2
f2=mp.figure('f2 Figure',facecolor='gray')
mp.plot(x2,y2)

mp.show()

### 2.1.2 绘制直线
mp.hlines(20,1,6)
mp.vlines(4,10,35)
mp.hlines([10,20,30,40],1,6)

### 2.1.3 线条属性
np.plot(xarray, yarray, linestyle='', linewidth=1, color='', alpha=0.5)
1.linestyle: 线型 '-' '--' '-.' ':'
2.linewidth: 线宽 数字
3.color: 颜色 英文颜色单词 或 常见英文颜色单词首字母 或 #495434 或 (1,1,1)
4.alpha: 透明度

### 2.1.4 设置坐标轴范围
mp.xlim()
mp.ylim()

### 2.1.5 设置坐标轴显示
坐标轴刻度显示
mp.xticks(x_val_list, x_text_list)
mp.yticks(y_val_list, y_text_list)
x_val_list x轴刻度值序列
x_text_list x轴刻度标签文本序列[可选]

坐标轴显示设置
ax=mp.gca()
axis=ax.spines['坐标轴名']
axis.set_position((type, val))
type: str, 移动坐标轴的参照类型，一般为'data'
val: 参照值
axis.set_color('color')

### 2.1.6 图例
mp.legend(loc='')

### 2.1.7 特殊点
mp.scatter(xarray, yarray,
       marker='',    # 点型 ~ matplotlib.markers
       s='',         # 大小
       edgecolor='', # 边缘色
       facecolor='', # 填充色
       zorder=3      # 绘制图层编号(编号越大，图层越靠上)
)


## 2.2 图形对象
### 2.2.1 创建图形对象

mp.figure('f1 Figure', facecolor='lightgray')
<!-- 当前画布为f1 -->
x2=np.arange(0,50)
y2=x2**2
f2=mp.figure('f2 Figure', figsize=(4,2),dpi=100,facecolor='gray')
<!-- 当前画布切换为f2 -->
mp.plot(x2,y2)
mp.figure('f1 Figure')
<!-- 当前画布又切换为f1 f1名称已存在-->
### 2.2.2 设置当前窗口参数

<!-- 设置图标标题 显示在图标上方 -->
mp.title(title, fontsize=12)
<!-- 设置水平轴的文本 -->
mp.xlabel(x_label_str, fontsize=12)
<!-- 设置垂直轴的文本 -->
mp.ylabel(y_label_str, fontsize=12)
<!-- 设置刻度参数 labelsize设置刻度字体大小-->
mp.tick_params(..., labelsize=8, ...)
<!-- 设置图标网格线 linestyle设置网格线的样式 -->
#- or solid 粗线
#-- or dashed 虚线
#-. or dashhot 点虚线
#: or dotted 点线
mp.grid(linestyle='')
<!-- 设置紧凑布局,把图标相关参数都显示在窗口中 -->
mp.tight_layout()

### 2.2.3 子图
#### 2.2.3.1 矩阵式布局

画出9x9的矩阵布局子图，每个子图上写对应编号
mp.subplot(3,3,1)
mp.text(0.5, 0.5, '1', ha='center', va='center', size=30, alpha=0.6)

#### 2.2.3.2 网格式布局

import matplotlib.gridspec as mg
mp.figure('Grid Layout', facecolor='lightgray')
<!-- 调用GridSpec方法拆分网格式布局 -->
<!-- rows:行数 -->
<!-- cols:列数 -->
<!-- gs=mg.GridSpec(rows,cols) 拆分成3行3列 -->
gs=mg.GridSpec(3,3)
<!-- 合并0行与0,1列为一个子图标 -->
mp.subplot(gs[0,:2])
mp.text(0.5,0.5,'1',ha='center',va='center',)
mp.show()

#### 2.2.3.3 自由式布局

```python
mp.figure('Flow Layout', facecolor='lightgray')
# 设置图标的位置，给出左下角点坐标与宽高即可
# left_bottom_x: 坐下角点x坐标[比例]
# left_bottom_x: 坐下角点y坐标[比例]
# width:		 宽度[比例]
# height:		 高度[比例]
# mp.axes([left_bottom_x, left_bottom_y, width, height])
mp.axes([0.03, 0.52, 0.94, 0.4])
mp.text(0.5, 0.5, '1', ha='center', va='center', size=36)
mp.axes([0.03, 0.06, 0.54, 0.4])
mp.text(0.5, 0.5, '1', ha='center', va='center', size=36)
mp.show()

```

### 2.2.4 刻度定位器

```python
# 获取当前坐标轴
ax = mp.gca()
# 设置水平坐标轴的主刻度定位器
ax.xaxis.set_major_locator(mp.NullLocator())
# 设置水平坐标轴的次刻度定位器为多点定位器，间隔0.1
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))

```

案例：绘制一个数轴。
```python
# 创建刻度定位器窗口
mp.figure('Locator Layout', facecolor='lightgray')
mp.xlim(1,10)
# 获取当前坐标轴
ax = mp.gca()
# 隐藏除底轴以外的所有坐标轴
ax.spines['top'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data',0.5))
mp.yticks([])
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
mp.text(5, 0.3, 'NullLocator()', ha='center', size=12)

```

常用刻度器如下

```python
# 空定位器：不绘制刻度
mp.NullLocator()
# 最大值定位器：
# 最多绘制nbins+1个刻度
mp.MaxNLocator(nbins=3)
# 定点定位器：根据locs参数中的位置绘制刻度
mp.FixedLocator(locs=[0, 2.5, 5, 7.5, 10])
# 自动定位器：由系统自动选择刻度的绘制位置
mp.AutoLocator()
# 索引定位器：由offset确定起始刻度，由base确定相邻刻度的间隔
mp.IndexLocator(offset=0.5, base=1.5)
# 多点定位器：从0开始，按照参数指定的间隔(缺省1)绘制刻度
mp.MultipleLocator()
# 线性定位器：等分numticks-1份，绘制numticks个刻度
mp.LinearLocator(numticks=21)
# 对数定位器：以base为底，绘制刻度
mp.LogLocator(base=2)

```

### 2.2.5 刻度网格线

绘制刻度网格线的相关API：

```python
ax = mp.gca()
#绘制刻度网格线
ax.grid(
    which='',		# 'major'/'minor' <-> '主刻度'/'次刻度' 
    axis='',		# 'x'/'y'/'both' <-> 绘制x或y轴
    linewidth=1, 	# 线宽
    linestyle='', 	# 线型
    color='',		# 颜色
	alpha=0.5		# 透明度
)

```

案例：绘制曲线 [1, 10, 100, 1000, 100, 10, 1]，然后设置刻度网格线，测试刻度网格线的参数。

```python
y = np.array([1, 10, 100, 1000, 100, 10, 1])
mp.figure('Normal & Log', facecolor='lightgray')
mp.subplot(211)
mp.title('Normal', fontsize=20)
mp.ylabel('y', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))
mp.tick_params(labelsize=10)
ax.grid(which='major', axis='both', linewidth=0.75,
        linestyle='-', color='orange')
ax.grid(which='minor', axis='both', linewidth=0.25,
        linestyle='-', color='orange')
mp.plot(y, 'o-', c='dodgerblue', label='plot')
mp.legend()

```

### 2.2.6 半对数坐标

### 2.2.7 散点图

可以通过每个点的坐标、颜色、大小和形状表示不同的特征值。

| 身高 | 体重 | 性别 | 年龄段 | 种族 |
| ---- | ---- | ---- | ------ | ---- |
| 180  | 80   | 男   | 中年   | 亚洲 |
| 160  | 50   | 女   | 青少   | 美洲 |

绘制散点图的相关API：

```python
mp.scatter(
    x, 			# x轴坐标数组
    y,				# y轴坐标数组
    marker='', 		# 点型
    s=10,			# 大小
    color='',			# 颜色
    edgecolor='', 		# 边缘颜色
    facecolor='',		# 填充色
    zorder=''			# 图层序号
)

```

numpy.random提供了normal函数用于产生符合 正态分布 的随机数 

```python
np.random.normal(loc=0.0, scale=1.0, size=None)
loc：float
此概率分布的期望值(对应着整个分布的中心center)
scale：float
此概率分布的标准差(对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高)
size：int or tuple of ints
输出的shape，默认为None，只输出一个值
n = 100
# 172:	期望值
# 10:	标准差
# n:	数字生成数量
# 身高 体重
height = np.random.normal(172, 20, n)
weight = np.random.normal(60, 10, n)

```

案例：绘制平面散点图。

```python
mp.figure('scatter', facecolor='lightgray')
mp.title('scatter')
mp.scatter(height, weight)
mp.show()

```

设置点的颜色

```python
mp.scatter(height, weight, c='red')			#直接设置颜色
# 样本点与期望值的距离,欧氏距离
d = (height-172)**2 + (weight-60)**2
mp.scatter(height, weight, c=d, cmap='jet')	#以c作为参数，取cmap颜色映射表中的颜色值
# cmap color map 数值越大 颜色越红 数值越小 颜色越蓝

```

### 2.2.8 填充

### 2.2.9 柱状图

绘制柱状图的相关API：

```python
mp.figure('Bar', facecolor='lightgray')
mp.bar(
       x,		# 水平坐标数组
    y,			# 柱状图高度数组
    width,		# 柱子的宽度
    color='', 	# 填充颜色
    label='',		#
    alpha=0.2		#
)

```

案例：先以柱状图绘制苹果12个月的销量，然后再绘制橘子的销量。

```python
apples = np.array([30, 25, 22, 36, 21, 29, 20, 24, 33, 19, 27, 15])
oranges = np.array([24, 33, 19, 27, 35, 20, 15, 27, 20, 32, 20, 22])
mp.figure('Bar'  , facecolor='lightgray')
mp.title('Bar', fontsize=20)
mp.xlabel('Month', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
mp.ylim((0, 40))
x = np.arange(len(apples))
mp.bar(x-0.2, apples, 0.4, color='dodgerblue',label='Apple')
mp.bar(x + 0.2, oranges, 0.4, color='orangered',label='Orange', alpha=0.75)
mp.xticks(x, [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
mp.legend()
mp.show()

```

### 2.2.10 饼图

绘制饼状图的基本API：

```python
mp.pie(
    values, 		# 值列表		
    spaces, 		# 扇形之间的间距列表
    labels, 		# 标签列表
    colors, 		# 颜色列表
    '%d%%',			# 标签所占比例格式
	shadow=True, 	# 是否显示阴影
    startangle=90	# 逆时针绘制饼状图时的起始角度
    radius=1		# 半径
)

```

案例：绘制饼状图显示5门语言的流行程度：

```python
mp.figure('pie', facecolor='lightgray')
#整理数据
values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript',
          'C++', 'Java', 'PHP']
colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold']
mp.figure('Pie', facecolor='lightgray')
mp.title('Pie', fontsize=20)
# 等轴比例
mp.axis('equal')
mp.pie(
    values, 		# 值列表		
    spaces, 		# 扇形之间的间距列表
    labels, 		# 标签列表
    colors, 		# 颜色列表
    '%d%%',			# 标签所占比例格式
	shadow=True, 	# 是否显示阴影
    startanle=90	# 逆时针绘制饼状图时的起始角度
    radius=1		# 半径
)

```

### 2.2.11 等高线图

组成等高线需要网格点坐标矩阵，也需要每个点的高度。所以等高线属于3D数学模型范畴。

绘制等高线的相关API：

```python
cntr = mp.contour(
    x, 			# 网格坐标矩阵的x坐标 （2维数组）
    y, 			# 网格坐标矩阵的y坐标 （2维数组）
    z, 			# 网格坐标矩阵的z坐标 （2维数组）
    8, 			# 把等高线绘制成8部分
    colors='black',		# 等高线的颜色
	linewidths=0.5		# 线宽
)
# 为等高线图添加高度标签
mp.clabel(cntr, inline_spacing=1, fmt='%.1f',
          fontsize=10)

mp.contourf(x, y, z, 8, cmap='jet')
```

案例：生成网格坐标矩阵，并且绘制等高线：

```python
n = 1000
# 生成网格化坐标矩阵
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
mp.figure('Contour', facecolor='lightgray')
mp.title('Contour', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 绘制等高线图
mp.contourf(x, y, z, 8, cmap='jet')
cntr = mp.contour(x, y, z, 8, colors='black',
                  linewidths=0.5)
# 为等高线图添加高度标签
mp.clabel(cntr, inline_spacing=1, fmt='%.1f',
          fontsize=10)
mp.show()
```

### 2.2.12 热成像图

用图形的方式显示矩阵及矩阵中值的大小
1 2 3
4 5 6
7 8 9

绘制热成像图的相关API：

```python
# 把矩阵z图形化，使用cmap表示矩阵中每个元素值的大小
# origin: 坐标轴方向
#    upper: 缺省值，原点在左上角
#    lower: 原点在左下角
mp.imshow(z, cmap='jet', origin='low')
```

使用颜色条显示热度值：

```python
mp.colorbar()
```

### 2.2.13 3D图像绘制

 matplotlib支持绘制三维曲面。若希望绘制三维曲面，需要使用axes3d提供的3d坐标系。

```python
from mpl_toolkits.mplot3d import axes3d
ax3d = mp.gca(projection='3d')   # class axes3d
```

matplotlib支持绘制三维点阵、三维曲面、三维线框图：

```python
ax3d.scatter(..)		# 绘制三维点阵
ax3d.plot_surface(..)	# 绘制三维曲面
ax3d.plot_wireframe(..)	# 绘制三维线框图
```

3d散点图的绘制相关API：

```python
ax3d.scatter(
    x, 		# x轴坐标数组
    y,			# y轴坐标数组
    z,			# z轴坐标数组
    marker='', 	# 点型
    s=10,		# 大小
    zorder='',	# 图层序号
    color='',		# 颜色
    edgecolor='', 	# 边缘颜色
    facecolor='',	# 填充色
    c=v,		# 颜色值 根据cmap映射应用相应颜色
    cmap=''		# 
)
```

案例：随机生成3组坐标，程标准正态分布规则，并且绘制它们。

```python
n = 1000
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)
d = np.sqrt(x ** 2 + y ** 2 + z ** 2)
mp.figure('3D Scatter')
ax = mp.gca(projection='3d')  # 创建三维坐标系
mp.title('3D Scatter', fontsize=20)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
mp.tick_params(labelsize=10)
ax.scatter(x, y, z, s=60, c=d, cmap='jet_r', alpha=0.5)
mp.show()
```

3d平面图的绘制相关API：

```python
ax3d.plot_surface(
    x, 			# 网格坐标矩阵的x坐标 （2维数组）
    y, 			# 网格坐标矩阵的y坐标 （2维数组）
    z, 			# 网格坐标矩阵的z坐标 （2维数组）
    rstride=30,		# 行跨距
    cstride=30, 		# 列跨距
    cmap='jet'		# 颜色映射
)

```

案例：绘制3d平面图

```python
n = 1000
# 生成网格化坐标矩阵
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
mp.figure('3D', facecolor='lightgray')

ax3d = mp.gca(projection='3d')
mp.title('3D', fontsize=20)
ax3d.set_xlabel('x', fontsize=14)
ax3d.set_ylabel('y', fontsize=14)
ax3d.set_zlabel('z', fontsize=14)
mp.tick_params(labelsize=10)
# 绘制3D平面图
# rstride: 行跨距
# cstride: 列跨距 
ax3d.plot_surface(x,y,z,rstride=30,cstride=30, cmap='jet')

```

案例：3d线框图的绘制

```python
# 绘制3D平面图 
# rstride: 行跨距
# cstride: 列跨距 
ax3d.plot_wireframe(x,y,z,rstride=30,cstride=30, 
	linewidth=1, color='dodgerblue')
```

### 2.2.14 简单动画

动画即是在一段时间内快速连续的重新绘制图像的过程。

matplotlib提供了方法用于处理简单动画的绘制。定义update函数用于即时更新图像。

```python
import matplotlib.animation as ma
#定义更新函数行为
def update(number):
    pass
# 每隔10毫秒执行一次update更新函数，作用于mp.gcf()当前窗口对象
# mp.gcf()：	获取当前窗口
# update：	更新函数
# interval：	间隔时间（单位：毫秒）
anim = ma.FuncAnimation(mp.gcf(), update, interval=10)
mp.show()

```

案例：随机生成各种颜色的100个气泡。让他们不断的增大。

```python
#自定义一种可以存放在ndarray里的类型，用于保存一个球
ball_type = np.dtype([
	('position', float, 2),  # 位置(水平和垂直坐标)
    ('size', float, 1),      # 大小
    ('growth', float, 1),    # 生长速度
    ('color', float, 4)])    # 颜色(红、绿、蓝和透明度)

#随机生成100个点对象
n = 100
balls = np.zeros(100, dtype=ball_type)
balls['position']=np.random.uniform(0, 1, (n, 2))
balls['size']=np.random.uniform(40, 70, n)
balls['growth']=np.random.uniform(10, 20, n)
balls['color']=np.random.uniform(0, 1, (n, 4))

mp.figure("Animation", facecolor='lightgray')
mp.title("Animation", fontsize=14)
mp.xticks 
mp.yticks(())

sc = mp.scatter(
	balls['position'][:, 0], 
	balls['position'][:, 1], 
	balls['size'], 
	color=balls['color'], alpha=0.5)
	
#定义更新函数行为
def update(number):
	balls['size'] += balls['growth']
	#每次让一个气泡破裂，随机生成一个新的
	boom_ind = number % n
	balls[boom_ind]['size']=np.random.uniform(40, 70, 1)
	balls[boom_ind]['position']=np.random.uniform(0, 1, (1, 2))
	# 重新设置属性
	sc.set_sizes(balls['size'])
	sc.set_offsets(balls['position'])
	
# 每隔30毫秒执行一次update更新函数，作用于mp.gcf()当前窗口对象
# mp.gcf()：	获取当前窗口
# update：		更新函数
# interval：	间隔时间（单位：毫秒）
anim = ma.FuncAnimation(mp.gcf(), update, interval=30)
mp.show()

```

使用生成器函数提供数据，实现动画绘制

在很多情况下，绘制动画的参数是动态获取的，matplotlib支持定义generator生成器函数，用于生成数据，把生成的数据交给update函数更新图像：

```python
import matplotlib.animation as ma
#定义更新函数行为
def update(data):
    t, v = data
    ...
    pass

def generator():
	yield t, v
        
# 每隔10毫秒将会先调用生成器，获取生成器返回的数据，
# 把生成器返回的数据交给并且调用update函数，执行更新图像函数
anim = ma.FuncAnimation(mp.gcf(), update, generator,interval=10)

```

案例：绘制信号曲线：y=sin(2 * π * t) * exp(sin(0.2 * π * t))，数据通过生成器函数生成，在update函数中绘制曲线。

```python
mp.figure("Signal", facecolor='lightgray')
mp.title("Signal", fontsize=14)
mp.xlim(0, 10)
mp.ylim(-3, 3)
mp.grid(linestyle='--', color='lightgray', alpha=0.5)
pl = mp.plot([], [], color='dodgerblue', label='Signal')[0]
pl.set_data([],[])

x = 0

def update(data):
	t, v = data
	x, y = pl.get_data()
	x.append(t)
	y.append(v)
	#重新设置数据源
	pl.set_data(x, y)
	#移动坐标轴
	if(x[-1]>10):
		mp.xlim(x[-1]-10, x[-1])

def y_generator():
	global x
	y = np.sin(2 * np.pi * x) * np.exp(np.sin(0.2 * np.pi * x))
	yield (x, y)
	x += 0.05

anim = ma.FuncAnimation(mp.gcf(), update, y_generator, interval=20)
mp.tight_layout()
mp.show()

```

# 3. pandas相关
## 3.1 Series相关
Series可以理解为一个一维的数组，只是index名称可以自己改动。类似于定长的有序字典，有Index和 value。

```python
import pandas as pd
import numpy as np

# 创建一个空的系列
s = pd.Series()
# 从ndarray创建一个系列
data = np.array(['a','b','c','d'])
s = pd.Series(data)
s = pd.Series(data,index=[100,101,102,103])
# 从字典创建一个系列	
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
# 从标量创建一个系列
s = pd.Series(5, index=[0, 1, 2, 3])
```

访问Series中的数据：

```python
# 使用索引检索元素
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[0], s[:3], s[-3:])
# 使用标签检索数据
print(s['a'], s[['a','c','d']])
```

## 3.2 日期相关

```python
# pandas识别的日期字符串格式
dates = pd.Series(['2011', '2011-02', '2011-03-01', '2011/04/01', 
                   '2011/05/01 01:01:01', '01 Jun 2011'])
# to_datetime() 转换日期数据类型
dates = pd.to_datetime(dates)
print(dates, dates.dtype, type(dates))
print(dates.dt.day)

# datetime类型数据支持日期运算
delta = dates - pd.to_datetime('1970-01-01')
# 获取天数数值
print(delta.dt.days)

# 日期做差
day2=pd.to_datetime('2011/01/01')
deltadate=dates - day2
print(deltadate)
print(deltadate.dt.days)
```

Series.dt提供了很多日期相关操作，如下：

```python
Series.dt.year	The year of the datetime.
Series.dt.month	The month as January=1, December=12.
Series.dt.day	The days of the datetime.
Series.dt.hour	The hours of the datetime.
Series.dt.minute	The minutes of the datetime.
Series.dt.second	The seconds of the datetime.
Series.dt.microsecond	The microseconds of the datetime.
Series.dt.week	The week ordinal of the year.
Series.dt.weekofyear	The week ordinal of the year.
Series.dt.dayofweek	The day of the week with Monday=0, Sunday=6.
Series.dt.weekday	The day of the week with Monday=0, Sunday=6.
Series.dt.dayofyear	The ordinal day of the year.
Series.dt.quarter	The quarter of the date.
Series.dt.is_month_start	Indicates whether the date is the first day of the month.
Series.dt.is_month_end	Indicates whether the date is the last day of the month.
Series.dt.is_quarter_start	Indicator for whether the date is the first day of a quarter.
Series.dt.is_quarter_end	Indicator for whether the date is the last day of a quarter.
Series.dt.is_year_start	Indicate whether the date is the first day of a year.
Series.dt.is_year_end	Indicate whether the date is the last day of the year.
Series.dt.is_leap_year	Boolean indicator if the date belongs to a leap year.
Series.dt.days_in_month	The number of days in the month.
```

## 3.3 DateTimeIndex

通过指定周期和频率，使用`date_range()`函数就可以创建日期序列。 默认情况下，范围的频率是天。

```python
import pandas as pd
# 以日为频率
# 默认频率是D天
datelist = pd.date_range('2019/08/21', periods=5)
print(datelist)
# 修改频率为月M
datelist = pd.date_range('2019/08/21', periods=5,freq='M')
print(datelist)
# 构建某个区间的时间序列
start = pd.datetime(2017, 11, 1)
end = pd.datetime(2017, 11, 5)
dates = pd.date_range(start, end)
print(dates)
```

`bdate_range()`用来表示商业日期范围，不同于`date_range()`，它不包括星期六和星期天。

```python
import pandas as pd
datelist = pd.bdate_range('2011/11/03', periods=5)
print(datelist)
```

## 3.4 DataFrame

DataFrame是一个类似于表格的数据类型，可以理解为一个二维数组，索引有两个维度，可更改。DataFrame具有以下特点：

- 潜在的列是不同的类型
- 大小可变
- 标记轴(行和列)
- 可以对行和列执行算术运算

```python
import pandas as pd

# 创建一个空的DataFrame
df = pd.DataFrame()
print(df)

# 从列表创建DataFrame
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

# 从字典来创建DataFrame
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['s1','s2','s3','s4'])
print(df)
data = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data)
print(df)
```

## 3.5 核心数据结构操作
### 3.5.1 列访问

DataFrame的单列数据为一个Series。根据DataFrame的定义可以 知晓DataFrame是一个带有标签的二维数组，每个标签相当每一列的列名。

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df['one'])
print(df[['one', 'two']])
```

### 3.5.2 列添加

DataFrame添加一列的方法非常简单，只需要新建一个列索引。并对该索引下的数据进行赋值操作即可。

```python
import pandas as pd

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['s1','s2','s3','s4'])
df['score']=pd.Series([90, 80, 70, 60], index=['s1','s2','s3','s4'])
print(df)
```

### 3.5.3 列删除

删除某列数据需要用到pandas提供的方法pop，pop方法的用法如下：

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
df = pd.DataFrame(d)
print("dataframe is:")
print(df)

# 删除一列： one
del(df['one'])
print(df)

#调用pop方法删除一列
df.pop('two')
print(df)
```

### 3.5.4 行访问

如果只是需要访问DataFrame某几行数据的实现方式则采用数组的选取方式，使用 ":" 即可：

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df[2:4])
```

**loc**方法是针对DataFrame索引名称的切片方法。loc方法使用方法如下：

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df.loc['b'])
print(df.loc[['a', 'b']])
```

**iloc**和loc区别是iloc接收的必须是行索引和列索引的位置。iloc方法的使用方法如下：

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df.iloc[2])
print(df.iloc[[2, 3]])
```

### 3.5.5 行添加

```python
import pandas as pd

df = pd.DataFrame([['zs', 12], ['ls', 4]], columns = ['Name','Age'])
df2 = pd.DataFrame([['ww', 16], ['zl', 8]], columns = ['Name','Age'])

df = df.append(df2)
print(df)
```

### 3.5.6 行删除

使用索引标签从DataFrame中删除或删除行。 如果标签重复，则会删除多行。

```python
import pandas as pd

df = pd.DataFrame([['zs', 12], ['ls', 4]], columns = ['Name','Age'])
df2 = pd.DataFrame([['ww', 16], ['zl', 8]], columns = ['Name','Age'])
df = df.append(df2)
# 删除index为0的行
df = df.drop(0)
print(df)
```

### 3.5.7 修改DataFrame中的数据

更改DataFrame中的数据，原理是将这部分数据提取出来，重新赋值为新的数据。

```python
import pandas as pd

df = pd.DataFrame([['zs', 12], ['ls', 4]], columns = ['Name','Age'])
df2 = pd.DataFrame([['ww', 16], ['zl', 8]], columns = ['Name','Age'])
df = df.append(df2)
df['Name'][0] = 'Tom'
print(df)
```

### 3.5.8 DataFrame常用属性

| 编号 | 属性或方法 | 描述                                |
| ---- | ---------- | ----------------------------------- |
| 1    | `axes`     | 返回 行/列 标签（index）列表。      |
| 2    | `dtype`    | 返回对象的数据类型(`dtype`)。       |
| 3    | `empty`    | 如果系列为空，则返回`True`。        |
| 4    | `ndim`     | 返回底层数据的维数，默认定义：`1`。 |
| 5    | `size`     | 返回基础数据中的元素数。            |
| 6    | `values`   | 将系列作为`ndarray`返回。           |
| 7    | `head(n)`  | 返回前`n`行。                       |
| 8    | `tail(n)`  | 返回最后`n`行。                     |

实例代码：

```python
import pandas as pd

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['s1','s2','s3','s4'])
df['score']=pd.Series([90, 80, 70, 60], index=['s1','s2','s3','s4'])
print(df)
print(df.axes)
print(df['Age'].dtype)
print(df.empty)
print(df.ndim)
print(df.size)
print(df.values)
print(df.head(3)) # df的前三行
print(df.tail(3)) # df的后三行
```


## 3.6 pandas核心
### 3.6.1 pandas描述性统计

数值型数据的描述性统计主要包括了计算数值型数据的完整情况、最小值、均值、中位 数、最大值、四分位数、极差、标准差、方差、协方差等。在NumPy库中一些常用的统计学函数也可用于对数据框进行描述性统计。

```python
np.min	最小值 
np.max	最大值 
np.mean	均值 
np.ptp	极差 
np.median	中位数 
np.std	标准差 
np.var	方差 
np.cov	协方差
```

实例：

```python
import pandas as pd
import numpy as np

# 创建DF
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack', 'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
  'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

df = pd.DataFrame(d)
print(df)
# 测试描述性统计函数
print(df.sum())
print(df.sum(1))
print(df.mean())
print(df.mean(1))
```

pandas提供了统计相关函数：

| 1    | `count()`   | 非空观测数量     |
| ---- | ----------- | ---------------- |
| 2    | `sum()`     | 所有值之和       |
| 3    | `mean()`    | 所有值的平均值   |
| 4    | `median()`  | 所有值的中位数   |
| 5    | `std()`     | 值的标准偏差     |
| 6    | `min()`     | 所有值中的最小值 |
| 7    | `max()`     | 所有值中的最大值 |
| 8    | `abs()`     | 绝对值           |
| 9    | `prod()`    | 数组元素的乘积   |
| 10   | `cumsum()`  | 累计总和         |
| 11   | `cumprod()` | 累计乘积         |

pandas还提供了一个方法叫作describe，能够一次性得出数据框所有数值型特征的非空值数目、均值、标准差等。

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print(df.describe())
print(df.describe(include=['object']))
print(df.describe(include=['number']))
```

### 3.6.2 pandas排序

*Pandas*有两种排序方式，它们分别是按标签与按实际值排序。

```python
import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(np.random.randn(10,2),
                         index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print(unsorted_df)
```

**按行标签排序**

使用`sort_index()`方法，通过传递`axis`参数和排序顺序，可以对`DataFrame`进行排序。 默认情况下，按照升序对行标签进行排序。

```python
import pandas as pd
import numpy as np

# 按照行标进行排序
sorted_df=unsorted_df.sort_index()
print (sorted_df)
# 控制排序顺序
sorted_df = unsorted_df.sort_index(ascending=False)
print (sorted_df)
```

**按列标签排序**

```python
import numpy as np

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
unsorted_df = pd.DataFrame(d)
# 按照列标签进行排序
sorted_df=unsorted_df.sort_index(axis=1)
print (sorted_df)
```

**按某列值排序**

像索引排序一样，`sort_values()`是按值排序的方法。它接受一个`by`参数，它将使用要与其排序值的`DataFrame`的列名称。

```python
import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
unsorted_df = pd.DataFrame(d)
# 按照年龄进行排序
sorted_df = unsorted_df.sort_values(by='Age')
print (sorted_df)
# 先按Age进行升序排序，然后按Rating降序排序
sorted_df = unsorted_df.sort_values(by=['Age', 'Rating'], ascending=[True, False])
print (sorted_df)
```

### 3.6.3 pandas分组

在许多情况下，我们将数据分成多个集合，并在每个子集上应用一些函数。在应用函数中，可以执行以下操作 :

- *聚合* - 计算汇总统计
- *转换* - 执行一些特定于组的操作
- *过滤* - 在某些情况下丢弃数据

```python
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)
```

#### 3.6.3.1 将数据拆分成组

```python
# 按照年份Year字段分组
print (df.groupby('Year'))
# 查看分组结果
print (df.groupby('Year').groups)
```

#### 3.6.3.2 迭代遍历分组

groupby返回可迭代对象，可以使用for循环遍历：

```python
grouped = df.groupby('Year')
# 遍历每个分组
for year,group in grouped:
    print (year)
    print (group)
```

#### 3.6.3.3 获得一个分组细节

```python
grouped = df.groupby('Year')
print (grouped.get_group(2014))
```

#### 3.6.3.4 分组聚合

聚合函数为每个组返回聚合值。当创建了分组(*group by*)对象，就可以对每个分组数据执行求和、求标准差等操作。

```python
# 聚合每一年的平均的分
grouped = df.groupby('Year')
print (grouped['Points'].agg(np.mean))
# 聚合每一年的分数之和、平均分、标准差
grouped = df.groupby('Year')
agg = grouped['Points'].agg([np.sum, np.mean, np.std])
print (agg)
```

### 3.6.4 pandas数据表关联操作

Pandas具有功能全面的高性能内存中连接操作，与SQL等关系数据库非常相似。
Pandas提供了一个单独的`merge()`函数，作为DataFrame对象之间所有标准数据库连接操作的入口。

**合并两个DataFrame：**

```python
import pandas as pd
left = pd.DataFrame({
         'student_id':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
         'student_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung', 'Billy', 'Brian', 'Bran', 'Bryce', 'Betty', 'Emma', 'Marry', 'Allen', 'Jean', 'Rose', 'David', 'Tom', 'Jack', 'Daniel', 'Andrew'],
         'class_id':[1,1,1,2,2,2,3,3,3,4,1,1,1,2,2,2,3,3,3,2], 
         'gender':['M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F'], 
         'age':[20,21,22,20,21,22,23,20,21,22,20,21,22,23,20,21,22,20,21,22], 
         'score':[98,74,67,38,65,29,32,34,85,64,52,38,26,89,68,46,32,78,79,87]})
right = pd.DataFrame(
         {'class_id':[1,2,3,5],
         'class_name': ['ClassA', 'ClassB', 'ClassC', 'ClassE']})
# 合并两个DataFrame
data = pd.merge(left,right)
print(data)
```

**使用“how”参数合并DataFrame：**

```python
# 合并两个DataFrame (左连接)
rs = pd.merge(left, right, how='left')
print(rs)
```

其他合并方法同数据库相同：

| 合并方法 | SQL等效            | 描述             |
| -------- | ------------------ | ---------------- |
| `left`   | `LEFT OUTER JOIN`  | 使用左侧对象的键 |
| `right`  | `RIGHT OUTER JOIN` | 使用右侧对象的键 |
| `outer`  | `FULL OUTER JOIN`  | 使用键的联合     |
| `inner`  | `INNER JOIN`       | 使用键的交集     |

试验：

```python
# 合并两个DataFrame (左连接)
rs = pd.merge(left,right,on='subject_id', how='right')
print(rs)
# 合并两个DataFrame (左连接)
rs = pd.merge(left,right,on='subject_id', how='outer')
print(rs)
# 合并两个DataFrame (左连接)
rs = pd.merge(left,right,on='subject_id', how='inner')
print(rs)
```

### 3.6.5 pandas透视表与交叉表

有如下数据：

```python
import pandas as pd
left = pd.DataFrame({
         'student_id':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
         'student_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung', 'Billy', 'Brian', 'Bran', 'Bryce', 'Betty', 'Emma', 'Marry', 'Allen', 'Jean', 'Rose', 'David', 'Tom', 'Jack', 'Daniel', 'Andrew'],
         'class_id':[1,1,1,2,2,2,3,3,3,4,1,1,1,2,2,2,3,3,3,2], 
         'gender':['M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F'], 
         'age':[20,21,22,20,21,22,23,20,21,22,20,21,22,23,20,21,22,20,21,22], 
         'score':[98,74,67,38,65,29,32,34,85,64,52,38,26,89,68,46,32,78,79,87]})
right = pd.DataFrame(
         {'class_id':[1,2,3,5],
         'class_name': ['ClassA', 'ClassB', 'ClassC', 'ClassE']})
# 合并两个DataFrame
data = pd.merge(left,right)
print(data)
```

**透视表**

透视表(pivot table)是各种电子表格程序和其他数据分析软件中一种常见的数据汇总工具。**它根据一个或多个键对数据进行分组聚合，并根据每个分组进行数据汇总**。

```python
# 以class_id与gender做分组汇总数据，默认聚合统计所有列
print(data.pivot_table(index=['class_id', 'gender']))

# 以class_id与gender做分组汇总数据，聚合统计score列
print(data.pivot_table(index=['class_id', 'gender'], values=['score']))

# 以class_id与gender做分组汇总数据，聚合统计score列，针对age的每个值列级分组统计
print(data.pivot_table(index=['class_id', 'gender'], values=['score'], columns=['age']))

# 以class_id与gender做分组汇总数据，聚合统计score列，针对age的每个值列级分组统计，添加行、列小计
print(data.pivot_table(index=['class_id', 'gender'], values=['score'], 
                       columns=['age'], margins=True))

# 以class_id与gender做分组汇总数据，聚合统计score列，针对age的每个值列级分组统计，添加行、列小计
print(data.pivot_table(index=['class_id', 'gender'], values=['score'], columns=['age'], margins=True, aggfunc='max'))
```

**交叉表**

交叉表(cross-tabulation, 简称crosstab)是一种用于**计算分组频率的特殊透视表**：

```python
# 按照class_id分组，针对不同的gender，统计数量
print(pd.crosstab(data.class_id, data.gender, margins=True))
```

### 3.6.6 pandas可视化
#### 3.6.6.1 数据读取与存储

**读取与存储csv：**

```python
# filepath 文件路径。该字符串可以是一个URL。有效的URL方案包括http，ftp和file 
# sep 分隔符。read_csv默认为“,”，read_table默认为制表符“[Tab]”。
# header 接收int或sequence。表示将某行数据作为列名。默认为infer，表示自动识别。
# names 接收array。表示列名。
# index_col 表示索引列的位置，取值为sequence则代表多重索引。 
# dtype 代表写入的数据类型（列名为key，数据格式为values）。
# engine 接收c或者python。代表数据解析引擎。默认为c。
# nrows 接收int。表示读取前n行。

pd.read_table(
    filepath_or_buffer, sep='\t', header='infer', names=None, 
    index_col=None, dtype=None, engine=None, nrows=None) 
pd.read_csv(
    filepath_or_buffer, sep=',', header='infer', names=None, 
    index_col=None, dtype=None, engine=None, nrows=None)
```

```python
DataFrame.to_csv(excel_writer=None, sheetname=None, header=True, index=True, index_label=None, mode=’w’, encoding=None) 
```

**读取与存储excel：**

```python
# io 表示文件路径。
# sheetname 代表excel表内数据的分表位置。默认为0。 
# header 接收int或sequence。表示将某行数据作为列名。默认为infer，表示自动识别。
# names 表示索引列的位置，取值为sequence则代表多重索引。
# index_col 表示索引列的位置，取值为sequence则代表多重索引。
# dtype 接收dict。数据类型。
pandas.read_excel(io, sheetname=0, header=0, index_col=None, names=None, dtype=None)
```

```python
DataFrame.to_excel(excel_writer=None, sheetname=None, header=True, index=True, index_label=None, mode=’w’, encoding=None) 
```

**读取与存储JSON：**

```python
# 通过json模块转换为字典，再转换为DataFrame
pd.read_json('../ratings.json')
```

# 4. 实践项目相关
## 4.1 餐厅订单数据分析
