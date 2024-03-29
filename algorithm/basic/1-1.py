# -*- coding: UTF-8 -*-
import random
from algorithm.testlib.instructure import Node,arrtoNodeList
from collections import deque
import sys
max_value = sys.maxsize
min_value = -sys.maxsize - 1

def print_str(a=None,b=None):
    if a is not None and b is not None:
        print(str(a)+str(b))
    elif b is None:
        print(a)


print_str('========堆排序=========')
def heap_sort_use_heapq(iterable):
    from heapq import heappush,heappop
    items = []
    for value in iterable:
        heappush(items,value)
    return [heappop(items) for i in range(len(items))]

def exe_heap_sort_use_heapq():
    ll = list(range(12))
    random.shuffle(ll)
    print_str('ll->', ll)
    lled = heap_sort_use_heapq(ll)
    print_str('lled->', lled)



print_str('========二分查找=========')
def binary_search(sorted_arr,target):
    if not sorted_arr:
        return -1
    beg,end = 0,len(sorted_arr)-1
    while beg <= end:
        mid = beg+(end-beg)//2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid]<target:
            beg = mid+1
        else:
            end = mid-1
    if beg >= end:
        return -1

# 二分查找 找第一个等于target的元素，返回其下标
def find_first_position(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        # mid=(i+j)//2
        mid = i + (j - i) // 2
        if target > arr[mid]:
            i = mid + 1
        elif target == arr[mid]:
            j = mid
        else:
            j = mid - 1
    if arr[i] == target:
        return i
    else:
        return -1

# 二分查找 找最后一个等于target的元素，返回其下标
def find_second_position(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        mid = (i + j + 1) // 2
        if target > arr[mid]:
            i = mid + 1
        elif target == arr[mid]:
            i = mid
        else:
            j = mid - 1
    if arr[j] == target:
        return j
    else:
        return -1

print_str('========二分查找递归实现=========')
def binary_search_recursive(sorted_arr,beg,end,target):
    if not sorted_arr:
        return -1
    if beg >= end:
        return -1
    # mid = int(beg+(end-beg)//2)
    mid = beg+end//2
    if target == sorted_arr[mid]:
        return mid
    elif sorted_arr[mid]>target:
        return binary_search_recursive(sorted_arr,beg,mid,target)
    else:
        return binary_search_recursive(sorted_arr,mid+1,end,target)

print_str('========初级1-冒泡排序-00:39:00=========')
def bubblesort(nums):
    for end in range(len(nums)-1,0,-1):
        for i in range(0,end):
            if nums[i]>nums[i+1]:
                tmp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = tmp
    return nums

print_str('========初级1-选择排序-00:46:00=========')
# 插入排序和选择排序的i都是从0-len(arr)
# 不同的是，选择排序j是从i-len(arr)-1往后走，后面每一个与当前i比较
def selectSort(nums):
    for i in range(0,len(nums)):
        minindx = i
        for j in range(i,len(nums)):
            if nums[j]<nums[minindx]:
                tmp = nums[minindx]
                nums[minindx] = nums[j]
                nums[j] = tmp
    return nums
print_str('========初级1-插入排序-00:50:00=========')
# 插入排序和选择排序的i都是从0-len(arr)
# 不同的是，插入排序j是从i-0往前去，一个一个位置插
def insertSort(nums):
    for i in range(0,len(nums)):
        for j in range(i,0,-1):
            if nums[j]<nums[j-1]:
                tmp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = tmp
    return nums

print_str('==========初级1-递归本质-01:33:23==========')

print_str('========初级1-合并两个有序列表-02:05:23=========')
def merge_sorted_list(sorted_arr1,sorted_arr2):
    i = 0
    j = 0
    print_str('arr1->',sorted_arr1)
    print_str('arr2->',sorted_arr2)
    arr_merge = []
    while i<len(sorted_arr1) and j<len(sorted_arr2):
        # print_str('i->',i)
        # print_str('j->',j)
        if sorted_arr1[i] <= sorted_arr2[j]:
            arr_merge.append(sorted_arr1[i])
            i += 1
        else:
            arr_merge.append(sorted_arr2[j])
            j += 1
    arr_merge.extend(sorted_arr2[j:])
    arr_merge.extend(sorted_arr1[i:])
    return arr_merge

print_str('========初级1-归并排序1=========')
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    i = len(arr)//2
    # print_str('i->',i)
    left = merge_sort(arr[:i])
    right = merge_sort(arr[i:])
    return merge_sorted_list(left,right)

print_str('========初级1-归并排序2=========')
# 原地排序。merge的时候已经吧res重新复制给arr[l:r+1]部分了
# 而当l==r的时候，就一个值也不用排序了
# 所以merge_sort最终要返回原来的arr
def merge_sort2(arr,l,r):#[7,4,6,3,9]
    if l==r:
        return
    mid = (r+l)//2
    merge_sort2(arr,l,mid)
    merge_sort2(arr,mid+1,r)
    merge_sorted_list2(arr,l,mid,r)

def merge_sorted_list2(arr,l,mid,r):
    res=[]
    i = l
    j = mid+1
    while i<=mid and j<=r:
        if arr[i]<arr[j]:
            res.append(arr[i])
            i+=1
        else:
            res.append(arr[j])
            j+=1
    res.extend(arr[i:mid+1])
    res.extend(arr[j:r+1])
    arr[l:r+1] = res


print_str('==========初级1-小和-02:27:49==========')
def smallSum(arr,l,r):
    if l==r :
        return 0
    mid = l+(r-l)//2
    left = smallSum(arr,l,mid)
    right= smallSum(arr,mid+1,r)
    m = merge(arr,l,mid,r)
    return left+right+m

def merge(arr,l,mid,r):
    res = []
    i,j=l,mid+1
    xiaohe = 0
    while i<=mid and j<=r:
        if arr[i]<arr[j]:
            xiaohe += arr[i] * (r-j+1)
        if arr[i]<=arr[j]:
            res.append(arr[i])
            i+=1
        else:
            res.append(arr[j])
            j+=1
    res.extend(arr[i:mid+1])
    res.extend(arr[j:r+1])
    arr[l:r+1]=res[:]
    return xiaohe
print_str('==========初级1-逆序对-02:27:49==========')

class Solution:
    def reversePairs(self, nums):
        if not nums: return 0
        self.cnt = 0
        self.rps = []
        self.mergeSort(nums, 0, len(nums) - 1)
        return self.cnt

    def mergeSort(self, arr, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)
        self.merge(arr, l, mid, r)

    def merge(self, arr, l, mid, r):
        i, j = l, mid + 1
        res = []
        while i <= mid and j <= r:
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i += 1
            else:
                self.cnt += mid - i + 1
                for idx in range(i, mid + 1):
                    self.rps.append([arr[idx], arr[j]])
                res.append(arr[j])
                j += 1
        res.extend(arr[i:mid + 1])
        res.extend(arr[j:r + 1])
        arr[l:r + 1] = res[:]

print_str('==========初级2-荷兰国旗问题-00:00:00==========')

def partition(arr,l,r,value):
    less,more=l-1,r+1
    cur=l
    while cur<more:
        if arr[cur]<value:
            arr[cur],arr[less+1]=arr[less+1],arr[cur]
            less+=1
            cur+=1
        elif arr[cur]>value:
            arr[cur],arr[more-1]=arr[more-1],arr[cur]
            more-=1
        else:
            cur+=1
    #返回的是小于pivot的部分最后一个元素的下标，和大于pivot的部分第一个元素下标
    return [less,more]#这个好

def parti(arr,l,r,value):
    x=-1
    for i in range(l,r+1):
        if arr[i] > value:
            continue
        else:
            arr[i],arr[x+1] = arr[x+1],arr[i]
            x+=1
    return arr

print_str('==========初级2-快排==========')

def quick_Sort(arr,l,r):
    if l<r:
        p = partition(arr,l,r,arr[l])
        quick_Sort(arr,l,p[0])
        quick_Sort(arr,p[1],r)

print_str('==========初级2-堆结构及堆排序-01:12:00==========')

class maxHeap():

    def __init__(self,arr=[]):
        self.data = arr

    def heap_sort(self,arr):
        if not arr or len(arr)<2:
            return
        for i in range(0,len(arr)):
            self.heapInsert(arr,i)#把i位置加进来，0-i之间是大根堆
        heapSize = len(arr)
        heapSize -= 1
        arr[0],arr[heapSize-1] = arr[heapSize-1],arr[0]
        while heapSize>0:
            self.heapify(arr,0,heapSize)
            heapSize-=1
            arr[0],arr[heapSize] = arr[heapSize],arr[0]

    def heapInsert(self,arr,index):
        #当前节点元素，如果比父节点大，则交换；并将父节点置为当前节点
        #优势在于插入一个元素的时间复杂度是logN；调整数组所有元素为堆结构的时间复杂度是log1+log2+...+logN=O(N)
        while arr[index] > arr[(index-1)//2]:
            arr[index],arr[(index-1)//2] = arr[(index-1)//2],arr[index]
            index = (index-1)//2

    def heapify(self,arr,index,heapSize):
        #大顶堆某个元素变小，怎么调整的过程
        #从该元素向下，进行heapify
        left = index*2+1#左孩子
        while left<heapSize:
            #从该节点左右孩子中找出最大值，并取得最大值的下标largest
            largest = left+1 if arr[left+1]>arr[left] and left+1 < heapSize else left
            #最大值和当前节点本身比较，取最大值下标
            largest = largest if arr[largest]>arr[index] else index
            #若最大值是当前节点本身，则跳出循环，结束
            if largest == index:
                break
            #否则将当前节点的值和最大值交换
            arr[largest],arr[index] = arr[index],arr[largest]
            #将当前节点置为最大值的节点，向下调整
            index = largest
            #左孩子也向下调整
            left = index*2+1

print_str('==========初级3-排序稳定性及-00:04:00==========')

print_str('==========初级3-桶排序思想解决数组相邻元素差值最大值-01:11:00==========')
#给定一个数组，求如果排序之后，相邻两数的最大差值，要求时间复杂度o(N)，不用用非比较的排序
#[3,1,6,2,7] return 3
def maxGap(arr):
    def bucket(num,lengh,min,max):
        return ((num-min)//(max-min))*lengh

    MaxNum, MinNum = max(arr), min(arr)
    if len(arr) < 2:
        return 0
    if MaxNum == MinNum:
        return 0
    hasNum, MaxNums, MinNums = [], [], []
    for i in range(0,len(arr)+1):
        hasNum.append(0)
        MaxNums.append(0)
        MinNums.append(0)
    bid = 0
    for i in range(0,len(arr)):
        bid = bucket(arr[i],len(arr),MinNum,MaxNum)
        MinNums[bid] = min(MinNums[bid],arr[i]) if hasNum[bid] else arr[i]
        MaxNums[bid] = max(MaxNums[bid],arr[i]) if hasNum[bid] else arr[i]
        hasNum[bid] = True
    res,lastMax = 0,MaxNums[0]
    for i in range(0,len(arr)+1):
        if hasNum[i]:
            res = max(res,MinNums[i]-lastMax)
            lastMax = MaxNums[i]
    return res
print_str('==========初级3-列表实现固定大小的栈和队列，及getMin--01:48:00==========')

class stack_size():
    def __init__(self,size):
        self.data = []
        self.size = size
        self.minList = []

    def push(self,val):
        # if self.size == len(self.data):
        if self.size == len(self.data):
            # raise Exception('The queue is full!')
            print('The queue is full!')
        else:
            if len(self.data)==0:
                self.data.append(val)
                self.minList.append(val)
            else:
                minVal = val if val < self.minList[-1] else self.minList[-1]
                self.minList.append(minVal)
                self.data.append(val)
            print(self.data)


    def pop(self):
        if len(self.data) == 0:
            # raise Exception('The queue is empty!')
            print('The queue is empty!')
        else:
            v = self.data.pop()
            self.minList.pop()
            print(self.data)
            return v

    def getMin(self):
        if not self.isEmpty():
            return self.minList[-1]
        else:
            return -1

    def isEmpty(self):
        return len(self.data)==0

class queue_size():
    def __init__(self,size):
        self.data = []
        self.size = size

    def push(self,val):
        if len(self.data) == self.size:
            print('The queue is full!')
        else:
            self.data.append(val)
            print(self.data)

    def poll(self):
        if len(self.data) == 0:
            print('The queue is Empty!')
        else:
            v=self.data[0]
            self.data = self.data[1:]
            print(self.data)
            return v

    def isEmpty(self):
        return len(self.data)==0
print_str('==========初级3-列表实现栈和队列==========')
class stack():
    def __init__(self):
        self.data = []

    def push(self,val):
        self.data.append(val)

    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            return -1

    def isEmpty(self):
        return len(self.data)==0

    def peek(self):
        if self.data:
            return self.data[0]
        else:
            return -1

class queue():
    def __init__(self):
        self.data = []

    def push(self,val):
        self.data.append(val)

    def poll(self):
        if self.data:
            v = self.data[0]
            self.data = self.data[1:]
            return v
        else:
            return -1

    def isEmpty(self):
        return len(self.data)==0

    def peek(self):
        if self.data:
            return self.data[0]
        else:
            return -1

print_str('==========初级4-1-猫狗队列问题-00:01:00==========')

class Pet():
    kind = ''

    def __init__(self,kind):
        self.kind = kind

    def getPetType(self):
        return self.kind

class Dog(Pet):

    def __init__(self,kind):
        super(Dog, self).__init__(kind)

class Cat(Pet):

    def __init__(self,kind):
        super(Cat, self).__init__(kind=kind)

class PetEnter():

    def __init__(self,pet,count):
        self.pet = pet
        self.count = count

    def getPet(self):
        return self.pet

    def getCount(self):
        return self.count

    def getEnterPetKind(self):
        return self.pet.getPetType()

class DogCatQueue():

    def __init__(self):
        self.dogQ = queue()
        self.catQ = queue()
        self.count = 0

    def add(self,pet):
        if 'dog' in pet.getPetType():
            self.dogQ.push(PetEnter(pet,self.count))
            self.count+=1
        elif 'cat' in pet.getPetType():
            self.catQ.push(PetEnter(pet,self.count))
            self.count+=1
        else:
            print('err,not dog not cat!')

    def pollAll(self):
        if not self.dogQ.isEmpty() and not self.catQ.isEmpty():
            if self.dogQ.peek().getCount() < self.catQ.peek().getCount():
                return self.dogQ.poll().getPet()
            else:
                return self.catQ.poll().getPet()
        elif not self.dogQ.isEmpty():
            return self.dogQ.poll().getPet()
        elif not self.catQ.isEmpty():
            return self.catQ.poll().getPet()
        else:
            print('err,queue is empty!')

    def pollDog(self):
        if not self.isDogQueueEmpty():
            return self.dogQ.poll().getPet()
        else:
            print('Dog queue is empty!')

    def pollCat(self):
        if not self.isCatQueueEmpty():
            return self.catQ.poll().getPet()
        else:
            print('Cat queue is empty!')

    def isEmpty(self):
        return self.dogQ.isEmpty() and self.catQ.isEmpty()

    def isDogQueueEmpty(self):
        return self.dogQ.isEmpty()

    def isCatQueueEmpty(self):
        return self.catQ.isEmpty()

print_str('==========初级4-1-转圈打印矩阵-00:15:00==========')
def spiralOrder(matrix):
    res=[]
    def printEdge(m,tR,tC,dR,dC):
        if tR==dR:
            for i in range(tC,dC+1):
                #print(str(m[tR][i])+' ')
                res.append(m[tR][i])
        elif tC==dC:
            for i in range(tR,dR+1):
                #print(str(m[i][tC])+' ')
                res.append(m[i][tC])
        else:
            curR=tR
            curC=tC
            while(curC!=dC):
                #print(str(m[tR][curC])+' ')
                res.append(m[tR][curC])
                curC+=1
            while(curR!=dR):
                #print(str(m[curR][tC])+' ')
                res.append(m[curR][dC])
                curR+=1
            while(curC!=tC):
                #print(str(m[tR][curC])+' ')
                res.append(m[dR][curC])
                curC-=1
            while(curR!=tR):
                #print(str(m[curR][tC])+' ')
                res.append(m[curR][tC])
                curR-=1
    if len(matrix)==0:
        return []
    tR,tC=0,0
    dR,dC=len(matrix)-1,len(matrix[0])-1
    while(tR<=dR and tC<=dC):
        printEdge(matrix,tR,tC,dR,dC)
        tR+=1
        tC+=1
        dR-=1
        dC-=1
    return res
print_str('==========初级4-1-正方形矩阵旋转90度-00:29:00==========')

def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    def rotateEdge(m,tR,tC,dR,dC):
        times = dC-tC
        tmp=0
        for i in range(0,times):
            tmp = m[tR][tC+i]
            m[tR][tC+i] = m[dR-i][tC]
            m[dR-i][tC] = m[dR][dC-i]
            m[dR][dC-i] = m[tR+i][dC]
            m[tR+i][dC] = tmp
    tR,tC=0,0
    dR,dC=len(matrix)-1,len(matrix[0])-1
    while tR<=dR and tC<=dC:
        rotateEdge(matrix,tR,tC,dR,dC)
        tR+=1
        tC+=1
        dR-=1
        dC-=1
print_str('==========初级4-2-之型打印-00:02:00==========')
def zigZagPrintMatrix(matrix):
    def printLevel(m,aR,aC,bR,bC,f):
        if f:
            while aR != bR+1:
                res.append(m[aR][aC])
                aR +=1
                aC -=1
        else:
            while bR != aR-1:
                # print('bR-bC:{0}-{1}'.format(bR,bC))
                res.append(m[bR][bC])
                bR -=1
                bC +=1
    res=[]
    aR,aC,bR,bC=0,0,0,0
    dR,dC=len(matrix)-1,len(matrix[0])-1
    fromUp = False
    while aR <= dR and bR <= dR:
        printLevel(matrix,aR,aC,bR,bC,fromUp)
        aR = aR+1 if aC== dC else aR
        aC = aC if aC== dC else aC+1
        bC = bC + 1 if bR == dR else bC
        bR = bR if bR == dR else bR+1
        fromUp = not fromUp
        print(res)

    return res

print_str('==========初级4-2-判断是否是回文链表-00:29:00==========')
# 用额外空间
def isPalindrome(head):
    nodeList=[]
    node = head
    res=True
    while node:
        nodeList.append(node.val)
        node=node.next
    node = head
    while node:
        if nodeList.pop() != node.val:
            return False
        node=node.next
    return res
print_str('==========初级4-2-判断是否是回文链表==========')
# 不用额外空间
def isPalindrome2(self, head):
    n2=head
    n1=head
    res=True
    if not head or not head.next:
        return True
    while n1.next and n2.next and n2.next.next:
        n1=n1.next
        n2=n2.next.next
    n2 = n1.next
    #奇数链表数：n1中间，n2=n1.next
    #偶数链表数：n1中间左边，n2=n1.next中间右边

    #反转后一段链表
    n3 = None
    while n2:
        tmp = n2.next
        n2.next=n3
        n3 = n2
        n2 = tmp
    # 此时n3是后一段链表的第一个

    n2 = n1#n2记住中间位置
    n4 = n3#n4记住后段的第一个Node
    n1 = head
    #前n1，后n3
    while n1 and n3:
        if n1.val != n3.val:
            res=False
            break
        n1=n1.next
        n3=n3.next
    n3=None
    while n4:
        tmp=n4.next
        n4.next=n3
        n3=n4
        n4=tmp
    n2.next = n3
    return res
print_str('==========初级4-2-链表分成比KEY小的，等于KEY的，大于KEY的三部分-00:52:00==========')
#遍历2遍
#第一次，找到第一个<,=,>KEY得节点less，equal，more
#第二次，再弄三个指针lessEnd，equalEnd，moreEnd，遍历一遍链表
#<,=,>的节点分别挂到后面，且lessEnd或者 equalEnd或者 moreEnd 往后移
#将三个链表连接在一起
def partition_node(head, target):
    firstless,firstequal,firstmore=None,None,None
    node=head
    lessEnd,equalEnd,moreEnd=None,None,None
    while node:
        if node.val==target:
            if firstequal==None:
                firstequal=node
                equalEnd=node
            else:
                equalEnd.next=node
                equalEnd=node
        elif node.val>target:
            if firstmore==None:
                firstmore=node
                moreEnd=node
            else:
                moreEnd.next=node
                moreEnd=node
        elif node.val<target:
            if firstless==None:
                firstless=node
                lessEnd=node
            else:
                lessEnd.next=node
                lessEnd=node
        node=node.next
    head=firstless if firstless else firstequal if firstequal else firstmore
    if lessEnd is not None:
        if firstequal is not None:
            lessEnd.next=firstequal
        else:
            lessEnd.next=firstmore
    if equalEnd is not None:
        equalEnd.next=firstmore
    return head

print_str('==========初级4-2-链表节点有next指针，还有random指针，怎么深度copy-01:02:00==========')
# 方法1：借助hash表，重点是找到node1Copy
# 方法2：
# 遍历head，生成node1-node1Copy-node2-node2Copy这种形式
# 再遍历一遍head，把random指针连接上，2个2个一遍历
# 最后遍历，裁剪
print_str('==========初级4-2-判断链表有无环-==========')
#用hash表存node
def detectCycle(self, head):
    node = head
    nodeSet=set()
    while node:
        if node in nodeSet:
            return node
        else:
            nodeSet.add(node)
        node=node.next

#两个指针 fast 和slow，fast一次走2，slow一次走1
#fast，slow依次遍历走，直到fast，slow相遇；
# fast归位head，并一次走1
# 下此相遇的节点就是入口节点
def detect_cycle(head):
    # 参数为头节点
    # 返回值：若存在环，则返回环入口节点val值;若不存在环，则返回False
    fast,slow=head,head
    res=False
    if not head or not head.next:
        return False
    while fast and slow and slow.next and fast.next.next:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            break
    fast=head
    while fast and slow and fast.next and slow.next:
        if fast==slow:
            return fast.val
        fast=fast.next
        slow=slow.next
    return res
print_str('==========初级4-2-判断两链表是否相交-01:28:00==========')

#两链表都无环：
# 遍历两个链表，得到len1，tail1；len2，tail2；
#  若end1！=end2，则一定不相交
#  若end1 == end2，则相交，第一个相交节点设为fNode：
#    head1先遍历|len1-len2|次，再head1，head2一起遍历，一定在fNode相交
#
#两链表一个有环，一个无环，不可能相交

#两链表都有环：3种拓补情况：
#  1。各自成环，不相交比如66
#  2。直线部分相交，共用一个环
#  3。环上相交，环上出来两个角
#head1，loop1（head1的入环节点）
#head2，loop2
# 若loop1==loop2，则是2拓补，head1--loop1之间head2--loop2之间是无环链表，复用前
# 若loop1！=loop2，继续遍历loop1，若loop1遍历一圈后都找不到==loop2的节点，则不相交；
#                 继续遍历loop1，找到==loop2的，则loop1和loop2均是相交点，返回其一即可

print_str('==========初级5-二叉树==========')

def preNodeInCre(node):
    if node == None:
        return
    print(node.value)
    preNodeInCre(node.left)
    preNodeInCre(node.right)
#完全二叉树：h-1层节点数达到最大，h层节点从左到右排列
#满二叉树：每一层的节点数达到最大值，就是满二叉树;满二叉树的深度为h，节点总数为2**h - 1,第k层节点数2**(k-1),叶子节点数2**(h-1)

#平衡树B树：根节点至少两个子节点，至多M个子节点，左右子树高度差不超过1
# 其他节点至少M/2个子节点，至多M个子节点
# 每个节点至少M/2-1个Key，至多M-1个Key，并且升序排列
# 所有叶子节点位于同一层

#B+树
# 非叶子节点Key的个数与子节点的个数相等。所有Key都出现在叶子节点。非叶子节点仅具有索引功能，跟记录有关的信息存放在叶子节点
# # 叶子节点增加链指针，所有叶子节点构成一个有序链表
# # 适用于索引与数据的分离

#平衡二叉树：它的左右子树都是平衡二叉树，且两者深度之差不超过1，且左右子树均是二叉搜索树

#前序遍历：
# #栈不为空：while循环栈不为空：head=弹栈--打印--右不为空则压栈-左不为空则压栈
def preorderTraversal(root):
    stack = [root]
    res = []
    if not root:
        return []
    while stack:
        v = stack.pop()
        res.append(v.val)
        if v.right:
            stack.append(v.right)
        if v.left:
            stack.append(v.left)
    return res
#中序遍历：
  #当前节点为空，从栈拿一个，打印，当前向右
  #当前节点不为空，当前压入栈，当前往左
def inorderTraversal(root):
    res = []
    stack = []
    if not root:
        return
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            res.append(root.val)
            root = root.right
    return res
#后序遍历
# 根据前序遍历改的，前序产出的顺序是中左右，改一下能产出中右左，用另一个栈去接受，栈依次弹出就是后序遍历
# python中反转就是模拟弹栈
def lastorderTraversal(head):
    stack = [head]
    res=[]
    if not head:
        return []
    while stack:
        head = stack.pop()
        res.append(head.val)
        if head.left:
            stack.append(head.left)
        if head.right:
            stack.append(head.right)
    res.reverse()
    return  res

#在二叉树中找到一个节点的后继节点
##新的二叉树节点类型，比普通二叉树节点结构多了一个指向父节点的parent指针。
#后继节点，中序遍历的下一个
#1。有右子树，后继节点就是右子树的最左边的节点
#2。没有右子树，当前节点依次往上=parent，直到当前节点是parent节点的左孩子节点，则当前节点的parent就是后继节点
#   也就是哪一个节点的左子树是以cur结束的
def getSuccessorNode(node):
    def getMostLeft(node):
        if not node:
            return node
        while node.left:
            node = node.left
        return node

    if not node:
        return node
    if node.right:
        return getMostLeft(node.right)
    else:
        parent = node.parent
        while parent and parent.left != node:
            node = parent
            parent = node.parent
        return parent

#前驱节点
def getPreNode(node):
    def getMostRight(node):
        if not node:
            return node
        while node.right:
            node = node.right
        return node
    if not node:
        return node
    if node.left:
        return getMostRight(node.left)
    else:
        parent = node.parent
        while parent and node != parent.right:
            node = parent
            parent = node.parent
        return parent
#

#二叉树的序列化与反序列化
#_
def serialByPre(node):
    if not node:
        return '#_'
    res = (str(node.value) + '_')
    res += serialByPre(node.left)
    res += serialByPre(node.right)
    return res

def reSerial(s):
    q = deque([t for t in s.split('_') if t])
    return reSerialByPre(q)

def reSerialByPre(q):
    value = q.popleft()
    if value == '#':
        return None
    head = Node(value)
    head.left = reSerialByPre(q)
    head.right = reSerialByPre(q)
    return head


#判断一棵树是否是平衡二叉树
# 进阶有代码

#判断一棵树是否是搜索二叉树，是否是完全二叉树
#搜索二叉树：任意节点，左子树比它小，右子树比它大
#二叉树的中序遍历，节点依次是升序的，就是搜索二叉树，否则不是
#中序遍历时候，当前值与上一个值比较，所有情况当前值>上个值，则是；否则不是
def isSouTree(node):
    if not node:
        return True
    res = True
    p = min_value
    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            v = stack.pop()
            if v.value < p:
                return False
            p = v.value
            node = v.right

    return res

#判断是否是完全二叉树
# res=False
#1。某一节点没有左节点，但有右节点，return false
#2。某一节点有左节点，但无右节点；某一节点左右节点都没有
# 此时后面遇到的节点必须都是叶子节点，res=True
#return res
def isCBT(node):
    if not node:
        return True
    q = deque()
    l,r = None,None
    leaf = False
    q.append(node)
    while q:
        head = q.popleft()
        l = head.left
        r = head.right
        if ((l == None) and (r != None)) or (leaf and ((l != None) or (r != None))):
            return False
        if l != None:
            q.append(l)
        if r != None:
            q.append(r)
        if (l == None) or (r == None):
            leaf = True
    return True


#已知一个完全二叉树，求其节点个数，要求时间复杂度低于O(N)，N为这课树的节点个数
#满二叉树高度H，节点个数为2^H-1
#1。求树的高度，最左边节点得到
#1。右子树的最左边节点是满高度的吗？
#  1。是，则整个树的左子树是满的，左边节点个数及根为2^(H-1)-1+1；右子树是完全二叉树，递归
#  2。否，则整个树的右子树是满二叉树，右边节点个数及根为2^(H-2)-1+1；左子树是完全二叉树，递归
def nodeNum(node):
    if not node:
        return 0
    return bs(node,1,mostLeftLevel(node,1))

def bs(node, level, h):
    if level == h:
        return 1
    if mostLeftLevel(node.right, level + 1) == h:
        return 2 ** (h - level) - 1 + 1 + bs(node.right, level + 1, h)
    else:
        return bs(node.left, level + 1, h) + 1 + 2 ** (h - level - 1) - 1

def mostLeftLevel(node, level):
    while node:
        level += 1
        node = node.left
    return level - 1

print('二叉树的层序遍历')
def printByLevel(node):
    if not node:
        return None
    dq = deque()
    dq.append(node)
    level = 1
    while dq:
        size = len(dq)
        print('level ' + str(level) + ':',end='')
        for i in range(size):
            node = dq.popleft()
            print(str(node.value),end=' ')
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        level += 1
        print()

print('二叉树的之型打印')
def printByZigZag(head):
    if not head:
        return None
    dq = deque()
    dq.append(head)
    lTor = True
    while dq:
        size = len(dq)
        for i in range(size):
            # 不管是l->r打印，还是r->l打印，打印同时，要保证下一层的节点保持原来直观的顺序进入到队列
            if lTor:
                node = dq.popleft()
                print(node.value,end=' ')
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            else:
                node = dq.pop()
                print(node.value,end=' ')
                if node.right:
                    dq.appendleft(node.right)
                if node.left:
                    dq.appendleft(node.left)
        print()
        lTor = not lTor

# arr1，arr2有序，打印同时存在与arr1和arr2中的元素
def printSameInTwo(arr1,arr2):
    i=0
    j=0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            print(arr1[i],end=' ')
            i += 1
            j += 1

print('深度优先，广度优先')
def depth_tree(node):
    if not node:return None
    print(node.val)
    if node.left:
        return depth_tree(node.left)
    if node.right:
        return depth_tree(node.right)

def level_tree(node):
    if not node:
        return None
    my_queue=deque([node])
    while my_queue:
        node=my_queue.popleft()
        print(node.val)
        if node.left:
            my_queue.append(node.left)
        if node.right:
            my_queue.append(node.right)


if __name__ == '__main__':
    # nums = [5,1,2,8,33,4]
    # nums=[1,3,4,2,5]#xiaohe=16
    # nums=[7,5,6,4]
    # arr1=[3,1,6,2,7]
    # arr2=[1,2,3,6,7]
    # print(quick_Sort(nums,0,len(nums)-1))
    # print(nums)
    # maxheap = maxHeap()
    # maxheap.heap_sort(nums)
    # print(nums)
    # slt = Solution()
    # print(slt.reversePairs(nums))
    # print(nums)
    # print(maxGap(arr1))

    # pet1= Pet('pet1')
    # dog1 = Dog('dog1')
    # dog2 = Dog('dog2')
    # dog3 = Dog('dog3')
    # cat1 = Cat('cat1')
    # cat2 = Cat('cat2')
    # cat3 = Cat('cat3')
    # dogcatQueue = DogCatQueue()
    # dogcatQueue.add(dog1)
    # dogcatQueue.add(cat1)
    # dogcatQueue.add(cat2)
    # dogcatQueue.add(dog2)
    # dogcatQueue.add(dog3)
    # dogcatQueue.add(cat3)
    # print(dogcatQueue.pollAll().getPetType())
    # print(dogcatQueue.pollAll().getPetType())
    # print(dogcatQueue.pollAll().getPetType())
    # print(dogcatQueue.pollAll().getPetType())
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # print(zigZagPrintMatrix(matrix))
    # arr = [7,4,5,3,9]
    # head = arrtoNodeList(arr)
    # print(isCBT(head))
    # quick_Sort(arr,0,4)
    # print(arr)
    # arr = [1,2,3,None,4,5,6]
    # head = arrtoNodeList(arr)
    # printByZigZag(head)
    arr1 = [2,3,6,2]
    arr2 = [1,3,3,12,12,25,25,36]
    # printSameInTwo(arr1,arr2)
    # quick_Sort(arr1,0,len(arr1)-1)
    # print(arr1)
    def bsl(arr,target):
        l,r=0,len(arr)-1
        while l<r:
            mid=l+(r-l)//2
            if arr[mid]==target:
                r=mid
            elif target>arr[mid]:
                l=mid+1
            else:
                r=mid-1
        if target==arr[l]:
            return l
        else:
            return -1

    def bsr(arr,target):
        l, r = 0, len(arr) - 1
        while l<r:
            mid=(l+r+1)//2
            if target==arr[mid]:
                l=mid
            elif target>arr[mid]:
                l=mid+1
            else:
                r=mid-1
        if arr[r]==target:
            return r
        else:
            return -1
    print(bsl(arr2,3))
    print(bsr(arr2,3))
    arr3=[1,3,4,2,5]
    print('xiaohe',smallSum(arr3,0,len(arr3)-1))







