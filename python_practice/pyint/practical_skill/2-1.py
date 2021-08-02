# -*- coding: UTF-8 -*-import heapqimport refrom random import randint,sample,shufflefrom collections import Counter,OrderedDict,namedtuple,dequefrom functools import reducefrom itertools import isliceimport pickleif __name__ == '__main__':    print('============1.过滤列表字典==============')    #过滤列表中的一些属性，列表推导；字典推导    #1。用循环的方式；    # 2。列表/字典推导的方式；    # 3。filter函数的形式，推荐列表/字典推导，效率更高    #随机生成-10-10之间的10个整数    rdlist = [randint(-10,10) for _ in range(10)]    print(rdlist)    print([val for val in rdlist if val >= 0])    print(list(filter(lambda x:x>0, rdlist)))    #字典推导    stuScores = {'student{0}'.format(i): randint(50,100) for i in range(1,21)}    print(stuScores)    #过滤90分以上的学生    stuSc = {k:v for k,v in stuScores.items() if v >= 90}    print(stuSc)    #    print(dict(filter(lambda x:x[1]>=90,stuScores.items())))    #集合过滤    rdSet = {randint(0,20) for _ in range(20)}    print(rdSet)    #    print({v for v in rdSet if v%3 == 0})    print('============2.为元组元素命名=============')    #学生信息格式固定，元组存储，索引访问时，可读性差    #1。定义一系列数值常量或枚举类型    #2。namedtuple    stu1Info = ('Jim', 16, 'male', 'Jim8721@gmail.com')    NAME,AGE,SEX,EMAIL = range(4)    print(stu1Info[NAME],stu1Info[AGE])    #枚举,有命名空间，不是全局变量    from enum import IntEnum#枚举类型    class StudentEnum(IntEnum):        NAME =0        AGE =1        SEX =2        EMAIL =3    print(stu1Info[StudentEnum.NAME],stu1Info[StudentEnum.AGE])    print(isinstance(StudentEnum.NAME,int))    #namedtuple    student = namedtuple('Student',['name','age','sex','email'])    s2 = student('Jim', 16, 'male', 'Jim8721@gmail.com')    print(s2.name,s2.age)    print('============3.为字典项排序=============')    #将字典的各项转换为元祖，用sorted排序    d = {k:randint(60,100) for k in 'abcdefgh'}    l = [(v,k) for k, v in d.items()]    sorted(l,reverse=True)    #或者zip    sorted(list(zip(d.values(),d.keys())))    #或者key=    p = sorted(d.items(), key=lambda item: item[1])    for i,item in enumerate(p,1):        if item[1]>90:            print(i,item)    h = {k:(v,i)for i,(k,v) in enumerate(p,1)}    print('============4.统计序列元素频度=============')    #1.转化成字典，然后排序    data = [randint(0,20) for _ in range(30)]    d = dict.fromkeys(data,0)    for x in data:        d[x] += 1    dd = sorted(d.items(),key=lambda x:x[1],reverse=True)    #heapq.nlargest    heapq.nlargest(3,((v,k) for k,v in d.items()))    #2.collections.Counter    c = Counter(data)    print(c.most_common(3))    print('============5.找到多个字典中的公共键=============')    d1 = {k: randint(1, 4) for k in sample('abcdefg', randint(3, 6))}    d2 = {k: randint(1, 4) for k in sample('abcdefg', randint(3, 6))}    d3 = {k: randint(1, 4) for k in sample('abcdefg', randint(3, 6))}    print([k for k in d1 if k in d2 and k in d3])    #利用map映射    dl = [d1,d2,d3]    print([k for k in d1 if all(map(lambda x: k in x,dl[1:]))])    #利用set的交集操作    reduce(lambda x, y: x & y, map(dict.keys, dl))    print('============6.让字典保持有序=============')    players = list('abcdefgh')    shuffle(players)    od = OrderedDict()    for i,player in enumerate(players,1):        od[player]=i    print('============7.实现用户历史记录功能=============')    #deque双端队列，可以设置长度    #q = deque([],5)    def guess(n,k):        if n==k:            print('猜对了，这个数字是%d'%k)            return True        if n<k:            print('猜大了，比%d小'%k)        elif n>k:            print('猜小了，比%d大'%k)        return False    def main():        n = randint(1,100)        i = 1        q = deque([],5)        while True:            line = input('[%d] Please Input a Number: '%i)            if line.isdigit():                k = int(line)                q.append(k)                pickle.dump(q,open('save.pkl','wb'))                i += 1                if guess(n,k):                    break            elif line == 'quit':                break            elif line == 'h?':                i += 1                q2 = pickle.load(open('save.pkl','rb'))                print(list(q2))            else:                i += 1                print('请输入数字！')    # main()    print('============9.=============')