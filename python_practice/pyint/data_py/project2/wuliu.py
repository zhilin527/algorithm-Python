# 数据来源：某企业销售的6种商品对应的送货及用户反馈数据
# 解决问题：
# 1.配送服务是否存在问题
# 2.是否存在尚有潜力的销售区域
# 3.商品是否存在质量问题

# 先放结论：
# 1.货品4->西北，货品2->马来西亚两条线路存在较大问题，急需提升时效
# 2.货品2在华东地区有较大市场空间
# 3.货品1，2，4存在质量问题

# 分析过程如下：
# 一。数据清洗
# 1.重复值，缺失值，格式调整
# 2.异常值处理，如销售金额存在等于0的，属于异常
# 二。数据规整
# 比如，增加一项辅助列：月份
# 三。数据分析并可视化

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'##设置中文显示

# 一.数据清洗
# 1.重复值，缺失值，格式调整
data = pd.read_csv('D:\\workspace\\algorithm-Python\\python_practice\\pyint\\data_py\\project2\\data_wuliu.csv',encoding="gbk")
print(data.info())
# 通过info可以看出，包括10列数据，名字，数据量，格式等，可以得出：
# 1.订单号，货品交货情况，数量：存在缺失值，但是缺失量不大，考虑删除
# 2.订单行，对分析无关紧要，考虑删除
# 3.销售金额格式不对，万元和元，逗号的问题，数据类型需要转换成int、float类型

# 删除重复记录
data.drop_duplicates(keep='first',inplace=True)
# 删除缺失值na,删除带有na的整行
data.dropna(axis=0,how='any',inplace=True)
# 删除订单行这一列
data.drop(axis=1,columns=['订单行'],inplace=True)
# 删除行数据后，索引没有更新
data.reset_index(drop=True,inplace=True)#把原来的index列删除，重置index
# print(data)

# 取出销售金额列，对每一个数据清洗
# 编写自定义过滤函数：
# 如果是万元则删除逗号，转成float,*10000，否则，删除元
def money_map(number):
    if number.find('万元') != -1:#带有万元的
        number_new = float( number[:number.find('万元')].replace(',','') ) * 10000
        pass
    else:#带有元的
        number_new = float( number[:number.find('元')].replace(',','') )
        pass
    return number_new

data['销售金额'] = data['销售金额'].map(money_map)
# print(data)

# print(data.describe())
#数据右偏，均值在中位数偏右
# 销售金额==0，采用删除方法，因为数据量小
data = data[data['销售金额']!=0]
print(data.describe())
# 销售金额和数量存在严重右偏现象，在电商领域2/8法则很正常，无需处理

# 二.数据规整
data['销售时间'] = pd.to_datetime(data['销售时间'])
data['交货时间'] = pd.to_datetime(data['交货时间'])
data['销售月份'] = data['销售时间'].apply(lambda x:x.month)
data['交货月份'] = data['交货时间'].apply(lambda x:x.month)
# print(data)

# 三.数据分析
# 1.配送服务是否存在问题
# 月份维度
data['货品交货状况'] = data['货品交货状况'].str.strip()#去除首尾空格
# 按月份:交货状况两个字段分组
data1 = data.groupby(by=['交货月份','货品交货状况']).size().unstack()
data1['按时交货率'] = data1['按时交货']/(data1['按时交货']+data1['晚交货'])
print(data1.sort_values(by='按时交货率', ascending=False))
# 从按时交货率来看，第四季度低于第三季度，猜测是天气原因

# 销售区域维度
# 按销售区域:交货状况两个字段分组
data1 = data.groupby(by=['销售区域','货品交货状况']).size().unstack()
data1['按时交货率'] = data1['按时交货']/(data1['按时交货']+data1['晚交货'])
print(data1.sort_values(by='按时交货率', ascending=False))
# 西北地区存在突出的延时交货问题，急需解决

# 货品维度
# 按货品:交货状况两个字段分组
data1 = data.groupby(by=['货品','货品交货状况']).size().unstack()
data1['按时交货率'] = data1['按时交货']/(data1['按时交货']+data1['晚交货'])
print(data1.sort_values(by='按时交货率', ascending=False))
# 货品4交货情况严重

# 货品和销售区域结合
# 按货品:销售区域:交货状况三个字段分组
data1 = data.groupby(by=['货品','销售区域','货品交货状况']).size().unstack()
data1['按时交货率'] = data1['按时交货']/(data1['按时交货']+data1['晚交货'])
print(data1.sort_values(by='按时交货率', ascending=False))
# 销售区域：西北最差，货品有1和4
# 货品：最差的是货品2，主要是送往华东和马来西亚

# 2.是否存在尚有潜力的销售区域
# 月份维度
data1 = data.groupby(by=['销售月份','货品'])['数量'].sum().unstack()
print(data1)
data1.plot(kind='line')
# 货品2在10月份和12月份，销量猛增

# 区域维度
data1 = data.groupby(by=['销售区域','货品'])['数量'].sum().unstack()
print(data1)

# 3.商品是否存在质量问题
data['货品用户反馈'] = data['货品用户反馈'].str.strip()
data1 = data.groupby(by=['货品','销售区域'])['货品用户反馈'].value_counts().unstack()
data1.fillna(0,inplace=True)#以0填充na
data1['拒货率'] = data1['拒货']/data1.sum(axis=1)
data1['合格率'] = data1['质量合格']/data1.sum(axis=1)
data1['返修率'] = data1['返修']/data1.sum(axis=1)
print(data1.sort_values(by=['合格率','返修率','拒货率'], ascending=False))

plt.show()

