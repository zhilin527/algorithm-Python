# 1.订单表的长度 shape columns
# 2.统计菜名的平均价格 amounts
# 3.什么菜最受欢迎
# 4.哪个订单ID点的菜最多

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
plt.rcParams['font.sans-serif'] = 'SimHei' #设置中文显示

# 1.加载数据
data1 = pd.read_excel('D:\\workspace\\algorithm-Python\\python_practice\\pyint\\data_py\\project1\\meal_order_detail.xlsx',sheet_name='meal_order_detail1')
data2 = pd.read_excel('D:\\workspace\\algorithm-Python\\python_practice\\pyint\\data_py\\project1\\meal_order_detail.xlsx',sheet_name='meal_order_detail2')
data3 = pd.read_excel('D:\\workspace\\algorithm-Python\\python_practice\\pyint\\data_py\\project1\\meal_order_detail.xlsx',sheet_name='meal_order_detail3')
# 2.数据预处理 合并数据 NA处理，分析数据
# print(data1)
# print(data2)
# print(data3)
data = pd.concat([data1, data2, data3], axis=0)#按照行拼接数据
# print(data.head(5))
print(data.dropna(axis=1, inplace=True))#删除na列，并且修改源数据
print(data.info())

# 统计卖出菜品的平均价格
print(round(data['amounts'].mean(), 2))#方法1，pandas自带函数
print(round(np.mean(data['amounts']), 2))#方法2，numpy函数处理

# 什么菜最受欢迎, 对菜名频数统计，取前10名
# print(data.groupby('dishes_id').groups)
dishes_count = data['dishes_name'].value_counts()[:10]
print(dishes_count)
print(dishes_count.shape)

# 哪个订单ID点的菜最多
data_group = data['order_id'].value_counts()[:10]
plt.figure('订单点菜的种类')
plt.title('订单点菜的种类top10')
plt.xlabel('订单ID')
plt.ylabel('点菜种类')
data_group.plot(kind='bar',color=['r','m','b','y','g'])

# 订单点菜数量top10
data['total_amounts'] = data['counts'] * data['amounts']#每道菜消费总额
dataGroup = data[['order_id','counts','amounts','total_amounts']].groupby(by='order_id')
Group_sum = dataGroup.sum()
sort_counts = Group_sum.sort_values(by='counts', ascending=False)
print(sort_counts)

# 消费金额top10
sort_amounts = Group_sum.sort_values(by='total_amounts', ascending=False)
plt.figure('订单消费金额')
plt.title('订单消费金额top10')
plt.xlabel('订单ID')
plt.ylabel('消费金额')
sort_amounts['total_amounts'][:10].plot(kind='bar',color=['r','m','b','y','g'])

data['time'] = pd.to_datetime(data['place_order_time'])
# 一天当中什么时间段 点菜量比较集中 以小时为单位
data['hourcount'] = 1
data['hour'] = data['time'].map(lambda x:x.hour)
group_by_hour = data.groupby(by='hour').count()['hourcount']
plt.figure('点菜数量和小时的关系')
plt.title('点菜数量和小时的关系')
plt.xlabel('小时')
plt.ylabel('点菜数量')
group_by_hour.plot(kind='bar',color=['r','m','b','y','g'])

# 统计每一天点菜数量

data['daycount'] = 1
data['day'] = data['time'].map(lambda x:x.day)
group_by_day = data.groupby(by='day').count()['daycount']
plt.figure('点菜数量和日的关系')
plt.title('点菜数量和日的关系')
plt.xlabel('日')
plt.ylabel('点菜数量')
group_by_day.plot(kind='bar',color=['r','m','b','y','g'])

# 每个星期几点菜数量
data['weekcount'] = 1
data['weekday'] = data['time'].map(lambda x:x.weekday())
group_by_weekday = data.groupby(by='weekday').count()['weekcount']
plt.figure('点菜数量和星期几的关系')
plt.title('点菜数量和星期几的关系')
plt.xlabel('星期')
plt.ylabel('点菜数量')
group_by_weekday.plot(kind='bar',color=['r','m','b','y','g'])

# 3.数据可视化matplotlib
plt.figure('最受欢迎的菜')
plt.title('最受欢迎的菜')
plt.xlabel('菜名')
plt.ylabel('销量')
dishes_count.plot(kind='line',color=['r'])
dishes_count.plot(kind='bar')
for x,y in enumerate(dishes_count):
    plt.text(x,y+2,y,ha='center')
plt.show()