# -*- coding: UTF-8 -*-from collections import dequefrom algorithm.testlib.instructure import Node,arrtoNodeListimport sysmax_value = sys.maxsizemin_value = -sys.maxsize - 1print('8.进阶3-1-二叉树时间复杂度O(N)，空间O(1)的遍历，Morris遍历')# 1。来到的当前节点计为cur#  如果cur无左孩子，cur向右移动cur=cur.right# 2。如果cur有左孩子，分情况，找到cur左子树最右的节点，计为mostright#     1-如果mostright的右指针right指向空，让其指向cur，然后cur向左移动cur=cur.left#     2-如果mostright的右指针right指向cur，让其指向空，cur向右移动cur=cur.rightdef morrisIn(head):    if head==None:        return    # 当前cur计为head mostright计为None    cur = head    mostright = None    while cur:        mostright = cur.left        #当前cur有左子树        if mostright:            # 获取左子树中最右的节点mostright(不是cur)            while mostright.right and mostright.right != cur:                mostright = mostright.right            # mostright.right 指向空            if not mostright.right:                mostright.right = cur                cur = cur.left                continue            # mostright.right 指向cur            else:                mostright.right = None        #当前cur无左子树        cur = cur.rightprint('9.进阶3-2-二叉树Morris遍历改先序中序')# morrsit改先序def morrisXianXu(head):    if head==None:        return    # 当前cur计为head mostright计为None    cur = head    mostright = None    while cur:        mostright = cur.left        #当前cur有左子树        if mostright:            # 获取左子树中最右的节点mostright(不是cur)            while mostright.right and mostright.right != cur:                mostright = mostright.right            # mostright.right 指向空            if not mostright.right:                mostright.right = cur                # 先序遍历                print(cur.value)                cur = cur.left                continue            # mostright.right 指向cur            else:                mostright.right = None        # 先序遍历        else:            print(cur.value)        #当前cur无左子树        cur = cur.right# morrsit改中序def morrisZhongXu(head):    if head==None:        return    # 当前cur计为head mostright计为None    cur = head    mostright = None    while cur:        mostright = cur.left        #当前cur有左子树        if mostright:            # 获取左子树中最右的节点mostright(不是cur)            while mostright.right and mostright.right != cur:                mostright = mostright.right            # mostright.right 指向空            if not mostright.right:                mostright.right = cur                cur = cur.left                continue            # mostright.right 指向cur            else:                mostright.right = None        #当前cur无左子树        # 中序遍历        print(cur.value)        cur = cur.right# 如果一个节点有左子树，则morrist遍历到达改节点2次，否则一次；# 而且第二次到达该节点的时候，左子树都已遍历# 如果左子树最右节点的right指向空，则是第一次来到当前cur，否则是第二次来到当前curprint('9.进阶3-1-递归遍历二叉树改先序中序后序')# 递归的本质def process(head):    if head == None:        return    print(head.value)    process(head.left)    print(head.value)    process(head.right)    print(head.value)print('10.进阶4-1-搜索二叉树')# 搜索二叉树：任一节点，左子树都比他小，右子树都比他大# 平衡二叉树(AVL树)：左右子树都是平衡二叉树，左右子树高度差不超过1，左右子树都是搜索二叉树# 红黑树：1。头节点必为黑，；#       2。红色不能相临；#       3。一节点出发任意两条链，黑色数量相同，也可理解为最长子树不超过最短子树的两倍长# SBTree Set Balance Tree 任意叔叔节点的子节点数，和侄子节点的子节点数，前者不必后者少# 所有平衡类型的搜索二叉树增删改查时间复杂度都是O(logN)，这些树都想做到的是左右子树某种规模差不多class BinarySearchTree():    # search查找操作    @staticmethod    def search(element,root):        node = root        while node and node.value and node.value != element:            if element<node.value:                node = node.left            else:                node = node.right        return node# delete删除操作，左右子树都有时，取右子树的最左节点顶上去，最左节点的右子树接上去# 平衡二叉树平衡的操作左旋操作，右旋操作，平衡调整无外乎左旋，右旋动作的组合。# AVL树是如何发现不平衡需要调整的：插入新元素时，往上更新节点左右子树最多到第几层，#  6节点左，右子树最多到第三层；往上推，5节点左子树最多到第二层，右子树最多到第三层；往上推#  4节点左子树最多到第一层，右子树最多到第三层，高度差>1，需要调整。# 1。右旋顺时针旋转：# 2。左旋逆时针旋转：# AVL树调整的类型，LL型，RR型，LR型，RL型# LL RR型，只需要做单一的右旋操作，左旋操作即可# LR 型，需要先左旋，再右旋；RL同理，先右旋，再左旋print('11.进阶4-1-大楼轮廓问题，困难1.30分钟处')# 给定一个print('12.进阶4-1-数组累加和等于aim的最长子数组，2.27分钟处')# 给定一个arr，有正有负有零；给一个整数aim，求累加和为aim值的最长子数组# 设定sum累加和从0到i，map记录{key:以i位置结尾的sum，value:第一次出现的位置index}，# map先加一条{0，-1}表示累加和为0出现在-1位置# 遍历数组，计算以i位置结尾的累加和及位置，比较sum-aim结果作为key是否在map中出现，#  若出现，得到value1，则value1+1到i位置累加和一定是aim，则arr[value1+1,i]为一个子数组满足和=aim，长度i-value1#  否则看sum-aim在不在map中，不在则插入；#def MaxZiArrSumtoAim(arr,aim):    if not arr:        return 0,0    res = []    resLen = 0    sum = 0    sumFirstMap = {}    sumFirstMap.update({0:-1})    for i in range(len(arr)):        sum += arr[i]        if sum - aim in sumFirstMap:            FirstSumIndex = sumFirstMap.get(sum - aim)            resLen,res = (i - FirstSumIndex,arr[FirstSumIndex+1:i+1]) if i - FirstSumIndex > resLen else (resLen,res)        if sum not in sumFirstMap:            sumFirstMap.update({sum:i})    return res,resLen# 扩展1。数组arr中整数，要么偶数，要么奇数，求奇偶数量相等的最长子数组# 扩展2。数组arr中，要么0，要么1，求0和1数量相等的最长子数组#  解决，奇数位(1)设为1，偶数位(0)设为-1，转化为求累加和=0的最长子数组print('13.进阶4-1-数组异或和等于0的子数组最多个数，3.00处')# 扩展3，数组异或和表示数组中所有元素异或结果，数组arr随意分成多个子数组，求子数组异或和=0的数量最多的子数组个数# 1。异或运算满足交换律和结合律# 2。0异或N=N；N异或N=0print('13.回调函数')def my_callback(args):    print(*args)def caller(args, f):    f(args)caller((1, 2), my_callback)# 简单来说就是定义一个函数，然后将这个函数的函数名传递给另一个函数做参数，以这个参数命名的函数就是回调函数# my_callback是回调函数，因为它作为参数传递给了callerprint('13-1.带额外状态信息的回调函数')def apply_ascyn(func,args,callback):    result = func(*args)    callback(result)def add(x,y):    return x+ydef print_result(result):    print(result)apply_ascyn(add,(1,2),callback=print_result)# 这里带额外信息的回调函数是print_result# 注意：这里print_result只能接收一个result的参数，不能传入其他信息。#   当想让回调函数访问其他变量或者特定环境的变量值的时候会遇到问题,使用闭包来实现def make_handler():    sequence = 0    def handler(result):        nonlocal sequence        sequence += 1        print("[{}] Got:{}".format(sequence, result))    return handlerhandler = make_handler()apply_ascyn(add,(1,2),handler)print('13-2.nonlocal和global关键字')# nonlocal 关键字用来在函数或其他作用域中使用外层(非全局)变量# global 关键字用来在函数或其他作用域中使用全局变量def dosomething():    a = 25    def add(x):        nonlocal a        a = a + x        return a    return adddef dosomething2():    a = 25    def add(x):        d = a + x        return d    return adda = 10ffff = dosomething()print(ffff(5))  # 30print(ffff(5))  # 35print(ffff(5))  # 40# dosomething函数中，如果没有nonlocal关键字，会报错local variable 'a' referenced before assignment# 因为没有nonlocal关键字，函数体内的变量，python会解释为局部变量a，去局部变量中找a，没有# 如果想要使用全局的a，则需要global关键字# nonlocal关键字它的作用是把变量标记为自由变量print('13-3.闭包')# 闭包是指延伸了作用域的函数，其中包含函数定义体中引用、但是不在定义体中定义的非全局变量# 当一个内嵌函数引用其外部作用域的变量,我们就会得到一个闭包# 创建一个闭包必须满足以下几点:# 1。必须有一个内嵌函数# 2。内嵌函数必须引用外层函数中的变量# 3。外层函数的返回值必须是内嵌函数# 会保留定义函数时存在的自由变量的更改，这样调用函数时虽然定义作用域不可用了，但仍能使用那些更改# 也就是说闭包中修改的外部作用域的变量都生效了，即使闭包作用域没了也生效。def make_averager():    series = [] #自由变量    def averager(new_value):        series.append(new_value)        total = sum(series)        return total/len(series)    return averageravg = make_averager()print(avg(10))print(avg(11))print(avg(12))# averager是一个闭包，闭包中修改了自由变量series，即使闭包作用域没了，修改依然生效。# 那么series是保存在哪里呢？# 自由变量series保存在在返回的avg对象的__closure__属性中# avg.__closure__[0].cell_contents# [10,11,12]print('13-4.classmethod和staticmethod')class A():    C_value = 123    def __init__(self):        A.C_value = A.C_value +1    def f1():        print(A.C_value)    # 可以使用@classmethod装饰器来创建类方法    # 这样的好处是: 不管这个方式是从实例调用还是从类调用，它的第一个参数是类本身    # 实例 和 类名 都可以调用    @classmethod    def f2(cls):        cls.C_value += 1    # 这样也能通过类名直接调用f3，但是不规范，而且不能传递类参数cls    def f3():        A.C_value += 1    # 经常有一些跟类有关系的功能但在运行时又不需要实例和类参与的情况下需要用到静态方法    # 或者仅仅作为维护代码用    # 实例 和 类名 都可以调用    @staticmethod    def f4():        A.C_value += 1print('13-5.max_value和min_value')print('14.进阶5-求二叉树的max，min递归，00:42处')class ReturnData:    def __init__(self,minV,maxV):        self.minV = minV        self.maxV = maxVdef p(head):    if not head:        return ReturnData(max_value,min_value)    leftData = p(head.left)    rightData = p(head.right)    return ReturnData(        min(leftData.minV,rightData.minV,head.value),        max(leftData.maxV,rightData.maxV,head.value)    )def MaxAndMinInHead(head):    resData = p(head)    print(resData.minV,resData.maxV)print('14.进阶5-求最大搜索二叉子树，开始处')# 求整个树的xx东西的思路：求某个(每个)节点的最大搜索二叉子树# 列可能性：以x为头树的最大搜索二叉子树情况：#   1。左子树上的子树；#   2。右子树上的子树；#   3.左右子树均是搜索二叉子树，且左子树max<cur 右子树min>cur,则整个树是搜索二叉树## 整理需要返回的数据类型，从而进行判断#   左搜索二叉树的大小，右搜索二叉树的大小；#   左搜索二叉树的头，右搜索二叉树的头；#   左搜索二叉树max，右搜索二叉树min；#class ReturnData2:    def __init__(self,size,head,minV,maxV):        self.size = size        self.head = head        self.minV = minV        self.maxV = maxVdef p2(head):    if head == None:        return ReturnData2(0,None,max_value,min_value)    left = head.left    leftSubTreeInfo = p2(left)    right = head.right    rightSubTreeInfo = p2(right)    # 对应可能性1或者可能性2    sizeLeft = leftSubTreeInfo.size    sizeRight = rightSubTreeInfo.size    max_size = max(sizeLeft,sizeRight)    max_head = leftSubTreeInfo.head if sizeLeft > sizeRight else rightSubTreeInfo.head    # if max_size == includeItSelf:    #     max_head = head    # 对应可能性3    # includeItSelf = 0    if (leftSubTreeInfo.head == left and rightSubTreeInfo.head == right            and leftSubTreeInfo.maxV < head.value            and rightSubTreeInfo.minV > head.value):        max_size = leftSubTreeInfo.size + 1 + rightSubTreeInfo.size        max_head = head        # includeItSelf = leftSubTreeInfo.size + 1 + rightSubTreeInfo.size    # 需要返回的数据类型    return ReturnData2(        max_size,        max_head,        min(leftSubTreeInfo.minV,rightSubTreeInfo.minV,head.value),        max(leftSubTreeInfo.maxV,rightSubTreeInfo.maxV,head.value)    )print('15.进阶5-求二叉树的最远距离，1:04处')# 可能性：# 1。左子树上# 2。右子树上# 3。左-右，过head节点# 需要返回的数据类型#print('16.进阶5-判断一棵树是否是平衡二叉树，1:44处')class ReturnData3:    def __init__(self,isB,h):        self.isB = isB        self.h = hdef p3(head):    if head == None:        return ReturnData3(True,0)    leftSubTreeData = p3(head.left)    if not leftSubTreeData.isB:        return ReturnData3(False,0)    rightSubTreeData = p3(head.right)    if not rightSubTreeData.isB:        return ReturnData3(False,0)    if abs(leftSubTreeData.h - rightSubTreeData.h) > 1:        return ReturnData3(False,0)    return ReturnData3(True,max(leftSubTreeData.h,rightSubTreeData.h) + 1)print('16.进阶6-判断一棵树是否是完全二叉树，1:50处')# 1。一节点有右孩子，无左孩子，直接False# 2。不违反1的情况下，如果当前节点cur左右孩子不全，则接下来的节点必须都是叶子节点def isCBT(head):    passprint('17.进阶5-设计可以变更的缓存结构LRU，1:56处')class Node2:    def __init__(self,value,key):        self.last = None        self.next = None        self.key = key        self.value = valueclass NodeDoubleLinkedList:    def __init__(self):        self.head = None        self.tail = None    # 双端链表中添加节点    def addNode(self,node):        if node == None:            return        if self.head == None:            self.head = node            self.tail = node        else:            self.tail.next = node            node.last = self.tail            self.tail = node    # 将node节点调至队尾    def moveNodeToTail(self,node):        if self.tail == node:            return        if self.head == node:            self.head = node.next            self.head.last = None        else:            node.next.last = node.last            node.last.next = node.next        self.tail.next = node        node.last = self.tail        self.tail = node        self.tail.next = None    # 删除头节点并返回该节点    def removeHead(self):        if self.head == None:            return None        res = self.head        if self.head == self.tail:            self.head = None            self.tail = None        else:            res.next.last = None            res.next = None            self.head = self.head.next        return resclass MyCache():    def __init__(self,capacity):        if capacity < 1:            raise Exception('should be more than 0')        self.nodeMap = {}        self.nodelist = NodeDoubleLinkedList()        self.capacity = capacity    # 根据key取得value，并将该node优先级升至最高    def get(self,key):        if key in self.nodeMap:            res = self.nodeMap.get(key)            self.nodelist.moveNodeToTail(res)            return res.value        else:            return None    # 更新值    def set(self,key,value):        if key in self.nodeMap:            node = self.nodeMap.get(key)            node.value = value            self.nodelist.moveNodeToTail(node)        else:            node = Node2(key,value)            self.nodeMap.update({key:node})            self.nodelist.addNode(node)            if len(self.nodeMap) == self.capacity + 1:                self.removeMostUnusedCache()    # 删除最近最少使用的节点    def removeMostUnusedCache(self):        removednode = self.nodelist.removeHead()#删除双端链表中的头节点并返回        del self.nodeMap[removednode.key]#删除Map中的节点并返回print('18.进阶6-LFU，开始处')# 实现LFU中的get和set方法，时间复杂度O(1)print('19.进阶6-字符串计算结果，1:12处')# 给定一个字符串str，str是一个公式，公式里可能有整数，加减乘除号，括号，返回公式的计算结果# str="3 + 1 * 4" 返回7# 说明：# 1。可以认为公式一定是正确的公式# 2。如果负数，则需要括号扩起来，负数开头则不用# 3。不用考虑溢出print('20.进阶6-跳表，02:08:00处')# Redis使用跳表实现有序集合#print('21.进阶7-子数组的最大异或和，开始处')# 给定一个数组，求子数组的最大异或和# 一个数组的异或行为，数组中所有的数异或起来的结果。print('22.进阶7-换钱的方法数，动态规划，01:00:25处')# 给一个arr[100,50,20,10] 面值这些的钱，给一个aim，目标钱# arr中每种钱随意用一张，凑成aim数值的钱，有几种凑法。# 详细说明了 暴力递归改动态规划 过程def process1(arr,index,aim):    '''    :param arr:    :param index: 可以任意使用index及其之后的钱    :param aim:剩余目标钱数    :return: 方法数    '''    res = 0    if index == len(arr):        res =  1 if aim == 0 else 0    else:        for zhang in range(aim//arr[index] + 1):            res += process1(arr,index + 1,aim - zhang * arr[index])    return res# 递归到达一个状态时，后面子问题的解的返回值是确定的，这叫无后效性问题。# 用map记录此时后面子问题的解的返回值,复用numOfFunMap ={}# key:'index_aim'# value:返回值#def process_map(arr,index,aim):    '''    '''    res = 0    if index == len(arr):        res =  1 if aim == 0 else 0    else:        for zhang in range(aim//arr[index] + 1):            nextAim = aim - zhang * arr[index]            key = str(index+1) + '_'+str(nextAim)            if key in numOfFunMap:                res += numOfFunMap.get(key)            else:                res += process_map(arr,index + 1,aim - zhang * arr[index])    # 返回之前，用map记录此时问题的解的返回值,以备复用    process_map[str(index) + '_' + str(aim)] = res    return res## 转DP过程：# 两个参数index，aim记录之前问题的解，用二位数组记录解# 画表：index：0-N，aim：0-1000# 找最终解在哪里：这张二维表能记录所有的解，最终目标是求index=0，aim=1000处的解# 看基础解在哪里：由baseCase确定哪些解能确定，index=N的时候能确定，即最后一行，且index=N，aim=0时，解为1# 看位置依赖：怎么调递归的#def coins3(arr,aim):    if not arr or len(arr)==0 or aim < 0 :        return 0    dp = [[0 for j in range(aim+1)]for i in range(len(arr))]    for i in range(len(arr)):        dp[i][0] = 1    for j in range(1,aim+1):        if arr[0]*j <= aim:            dp[0][arr[0]*j] = 1    num = 0    for i in range(1,len(arr)):        for j in range(1,aim+1):            num = 0            for k in range(0,j):                if j - arr[i]*k >= 0:                    num += dp[i-1][j - arr[i]*k]            dp[i][j] = num    #    for i in range(len(arr)):        print(dp[i])    return dp[len(arr)-1][aim]def coins4(arr, aim):    if not arr or len(arr) == 0 or aim < 0:        return 0    dp = [[0 for j in range(aim + 1)] for i in range(len(arr))]    for i in range(len(arr)):        dp[i][0] = 1    for j in range(1, aim + 1):        if arr[0] * j <= aim:            dp[0][arr[0] * j] = 1    for i in range(1, len(arr)):        for j in range(1, aim + 1):            dp[i][j] = dp[i-1][j]            dp[i][j] += (dp[i][j-arr[i]] if j-arr[i] >= 0 else 0)    #    for i in range(len(arr)):        print(dp[i])    return dp[len(arr) - 1][aim]print('23.进阶7-排成一条线的纸牌博弈问题，动态规划，01:51:25处')## arr=[1,100,1]# 给一堆牌arr，两人选，每次只能从两边选，每人选到的牌点数加起来大的人赢，求赢的人点数# 先选ff，后选ss，返回点数较大的# dp两张表，ff表和ss表def win1(arr):    if not arr or len(arr) == 0:        return 0    return max(ff(arr,0,len(arr)-1),ss(arr,0,len(arr)-1))def ff(arr,i,j):    if i==j:        return arr[i]    return max(arr[i]+ss(arr,i+1,j),arr[j]+ss(arr,i,j-1))def ss(arr,i,j):    if i==j:        return 0    return min(ff(arr,i+1,j),ff(arr,i,j-1))print('24.进阶7-，1-N位置，机器人走P步刚好在K位置情况，动态规划，02:14:00处')# 机器人初始停留在M位置上，机器人可以左走或右走，机器人走P步后，正好停在K位置情况有多少种#def ways(N,curPosition,restSteps,K):    if N<2 or curPosition<1 or curPosition>N or restSteps<0 or K<1 or K>N:        return 0    if restSteps==0:#P剩余步数        if curPosition == K:            return 1        else:            return 0    res = 0    if curPosition == 1:        res = ways(N,curPosition+1,restSteps-1,K)    elif curPosition == N:        res = ways(N,curPosition-1,restSteps-1,K)    else:        res = ways(N,curPosition+1,restSteps-1,K) + ways(N,curPosition-1,restSteps-1,K)    return resdef ways2(N,M,P,K):    if N<2 or M<1 or M>N or P<0 or K<1 or K>N:        return 0    dp = [[0 for _ in range(N+1)] for _ in range(P+1)]    for i in range(1,N+1):        if i == K:            dp[0][i] = 1        else:            dp[0][i] = 0    for i in range(1,P+1):        for j in range(1,N+1):            if j == 1:                dp[i][j] = dp[i - 1][j + 1]            elif j == N:                dp[i][j] = dp[i - 1][j - 1]            else:                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]    for i in range(P+1):        print(dp[i])    return dp[P][M]#从M出发走P步到达K位置print('25.进阶8-arr整数，累加和等于aim最长子数组，开始处')# 给定一个arr，全是正数，一个整数aim，求累加和等于aim的，最长子数组，额外空间o(1),时间o(n)# arr有正有负，不能用LR指针，只能用map记录，因为有正有负会回## 1。LR两个指针，sum记录，sum<aim,R++;sum>aim,L++def maxSubArr(arr,aim):    resLen = 0    L,R = 0,0    sum = arr[0]    while R < len(arr):        if sum == aim:            resLen = max(resLen,R-L+1)            R += 1            if R == len(arr):                break            sum += arr[R]        elif sum < aim:            R += 1            if R == len(arr):                break            sum += arr[R]        else:            sum -= arr[L]            L += 1    return resLenprint('25.进阶8-arr可正可负可0，求累加和sum<=aim 最长子数组，00:22:00处')# min_Sum=[] (sums):表示以当前位置i开头，的最小sum子数组# min_Sum_index=[] (ends):表示上面sums子数组的右边界def maxLenAwesome(arr,k):    if not arr or len(arr) == 0:        return 0    min_sums = []    min_sums_ends = []    min_sums[len(arr)-1] = arr[-1]    min_sums_ends[len()-1] = len(arr)-1    # 求min_Sum数组    # 从后往前求，最后一个min_Sum肯定为元素本身    # i位置的min_Sum求法：i+1位置的min_Sum<0说明可以加进来，min_Sum=arr[i]+min_Sum[i+1];否则不能加进来    for i in range(len(arr)-2,-1,-1):        if min_sums[i+1] < 0:            min_sums[i] =arr[i] + min_sums[i+1]            min_sums_ends[i] = min_sums_ends[i+1]        else:            min_sums[i] = arr[i]            min_sums_ends[i] = i    # R是下一个将要扩进来的块的开头    # 每次是从start扩到R-1这些元素    R,sum,resLen = 0,0,0    for start in range(len(arr)):        while R < len(arr) and sum + min_sums[start] < k:            sum += min_sums[start]            R = min_sums_ends[R] + 1        sum -= arr[start] if R > start else 0        resLen = max(resLen,R-start)        R = max(R,start+1)    return resLenprint('26.进阶8-环形单链表的约瑟夫问题，01:28:00')# n个节点围成环，报数1-k，报到k的人自杀，问最后剩的节点，时间复杂度o(n)# y=x%i函数# 编号 = (报数-1) % i + 1 当长度为i的时候print('27.进阶8-字符串匹配问题，动态规划，02:20:00')# 给定字符串str，不含有.和*；再给定字符串exp 其中可以含有.和*,*不能是exp的首字符，并且任意两个*字符不相邻，# exp中，.代表任何一个字符，exp中的*表示*前一个字符可以有0个或者多个# 请写一个函数，判断str是否能被exp匹配# f(i,j) str 从 i 及其开始，exp 从 j 及其开始，能否匹配# 1。j+1位置有字符，但不是*# i# |# a a a a# a b x x# |# j#   则 j 位置必须和 i 位置一样，若不一样，则返回False#   若i，j一样，则返回f(i+1,j+1)# 2。j+1位置有字符，是*#     1.j位置不是.#     # i#     # |#     # a a a a#     # c * x x#     # |#     # j#   此时有可能匹配上，依赖于f(i,j+2)#     2.j位置是.#     # i#     # |#     # a a a a#     # . * x x#     # |#     # j#if __name__ == '__main__':    # arr = [1, 2, 3, None, 5, 6, None]    # head = arrtoNodeList(arr)    # # morrisIn(head)    # node = BinarySearchTree.search(2,head)    # print(node.value)    # arr = [7,3,2,1,1,7,-6,-1,7]    # aim = 7    # res,resLen = MaxZiArrSumtoAim(arr,aim)    # print('res: '+str(res) + ' resLen: '+str(resLen))    # arr = [6,4,7,2,5,None,None,1]    # head = arrtoNodeList(arr)    # res = p2(head)    # print(res.size,res.head.value,res.minV,res.maxV)    # res = p3(head)    # print(res.isB)    # arr=[5,3,2]    # print(coins3(arr,10))    # print(coins4(arr,10))    # arr = [1,100,1]    # print(win1(arr))    # print(ways2(4,2,2,1))#ways2(N,M,P,K)    arr=[1,2,3,1,1,1,5]    print(maxSubArr(arr,6))    pass