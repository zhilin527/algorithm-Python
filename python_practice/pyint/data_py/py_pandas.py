import pandas as pd
import numpy as np

# 创建Series对象
s=pd.Series()
print(s, type(s), s.dtype)

# 通过ndarray创建Series对象
ary=np.array([70,80,90,95])
s=pd.Series(ary)
print(s)

# 创建Series对象时 指定index行级索引标签
s=pd.Series(ary, index=['zs','ls','ww','zl'])
print(s, s['zs'])

# 通过字典创建Series
dic1 = {'zs':80, 'ww':75, 'tq':60, 'wb':90}
s=pd.Series(dic1)
print(s)

# 访问Series
print(s[['zs','ww']])

print('-'*30)

# 日期处理
# 构建日期类型的Series
dates=pd.Series(['2011','2011-02','2011-03-01','2011/04/01','2011/05/01 01:01:01','01 Jun 2011'])
dates=pd.to_datetime(dates)
print(dates, dates.dtype, type(dates))
print(dates.dt.day)

# 日期运算
# 把delta转成数字
day2=pd.to_datetime('2011/01/01')
deltadate=dates - day2
print(deltadate)
print(deltadate.dt.days)

# DateTimeIndex
# 默认频率是D天
dates = pd.date_range('2019/10/01', periods=7)
print(dates)
# 修改频率为月M
dates=pd.date_range('2019/10/01',periods=7,freq='M')
print(dates)
# 工作日时间序列
pd.bdate_range('2019/08/01',periods=7)
print(dates)

# DataFrame
# 从列表创建DataFrame
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data=data)
print(df)
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
# 从字典来创建DataFrame
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data=data, index=['s1','s2','s3','s4'])
print(df)
data = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'e']), 'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data=data)
print(df)

# 核心数据结构操作
# 列访问
print(df['one'])
print(df[['one','two']])
# 列添加
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data=data, index=['s1', 's2', 's3', 's4'])
df['score'] = pd.Series([90,80,70,60], index=['s1','s2','s3','s4'])
print(df)
# 列删除
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
# 行访问
data = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df=pd.DataFrame(data=data)
print(df[2:4])
print(df.loc['a'])
print(df.loc[['a','b']])
print(df.iloc[2])
print(df.iloc[[2, 3]])
# 行添加
df = pd.DataFrame([['zs', 12], ['ls', 4]], columns = ['Name','Age'])
df2 = pd.DataFrame([['ww', 16], ['zl', 8]], columns = ['Name','Age'])
df = df.append(df2)
print(df)
# 行删除
df = df.drop(0)
print(df)
# 修改DataFrame中的数据
df['Name'][0] = 'Tom'
# pandas描述性统计
data = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
df = pd.DataFrame(data=data)
print(df.describe())
# pandas排序
unsorted_df = pd.DataFrame(data=np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print(unsorted_df)
# 按行标签排序
# 按照行标进行排序
sorted_df = unsorted_df.sort_index()
print(sorted_df)
# 控制排序顺序
sorted_df = unsorted_df.sort_index(ascending=False)
print (sorted_df)
# 按列标签排序
sorted_df = unsorted_df.sort_index(axis=1)
print(sorted_df)
# 按某列值排序
data = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
unsorted_df = pd.DataFrame(data=data)
# 按照年龄进行排序
sorted_df = unsorted_df.sort_values(by='Age')
print(sorted_df)
# 先按Age进行升序排序，然后按Rating降序排序
sorted_df = unsorted_df.sort_values(by=['Age','Rating'], ascending=[True,False])
print(sorted_df)

# pandas分组
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)
# 按照年份Year字段分组
print(df.groupby('Year'))
# 查看分组结果
print(df.groupby('Year').groups)
# 迭代遍历分组
grouped = df.groupby('Year')
for year,group in grouped:
    print(year)
    print(group)
# 获得一个分组细节
print(grouped.get_group(2014))
# 聚合每一年的平均的分
print(grouped['Points'].agg(np.mean))
# 聚合每一年的分数之和、平均分、标准差
print(grouped['Points'].agg([np.mean, np.sum, np.std]))

# pandas数据表关联操作
# 合并两个DataFrame
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
# 合并两个DataFrame (左连接)
lefts = pd.merge(left, right, how='left')
print(lefts)
# 合并两个DataFrame (左连接)
rs = pd.merge(left,right,on='class_id', how='right')
print(rs)
# 合并两个DataFrame (左连接)
rs = pd.merge(left,right,on='class_id', how='outer')
print(rs)
# 合并两个DataFrame (左连接)
rs = pd.merge(left,right,on='class_id', how='inner')
print(rs)

# pandas透视表与交叉表
print('-'*30)
data = pd.merge(left,right)
print(data)
# 以class_id与gender做分组汇总数据，默认聚合统计所有列
print(data.pivot_table(index=['class_id','gender']))
# 以class_id与gender做分组汇总数据，聚合统计score列
print(data.pivot_table(index=['class_id','gender'], values=['score']))
# 以class_id与gender做分组汇总数据，聚合统计score列，针对age的每个值列级分组统计
print(data.pivot_table(index=['class_id','gender'], values=['score'], columns=['age']))
# 以class_id与gender做分组汇总数据，聚合统计score列，针对age的每个值列级分组统计，添加行、列小计
print(data.pivot_table(index=['class_id','gender'], values=['score'], columns=['age'], margins=True))
# 以class_id与gender做分组汇总数据，聚合统计score列,求最大值，针对age的每个值列级分组统计，添加行、列小计
print(data.pivot_table(index=['class_id', 'gender'], values=['score'], aggfunc=[np.max], columns=['age'], margins=True))

# 交叉表
# 按照class_id分组，针对不同的gender，统计数量
print(pd.crosstab(data.class_id, data.gender, margins=True))


