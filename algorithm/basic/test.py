# -*- coding: UTF-8 -*-
import random

class test():
    def __init__(self,name,value):
        self.value = value
        name = name

    def getName(self):
        return self.name

def quicksort_b(arr):
    if len(arr)<2:
        return arr
    provit_index = 0
    provit = arr[provit_index]
    less_part = [x for x in arr[provit_index+1:] if x < provit]
    more_part = [x for x in arr[provit_index+1:] if x > provit]
    return quicksort_b(less_part) + [provit] + quicksort_b(more_part)

def arr_merge(arr1,arr2):
    i,j=0,0
    res = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    res.extend(arr2[j:])
    res.extend(arr1[i:])
    return res

def merge_sort(arr):
    if len(arr)<2:
        return arr
    i = len(arr)//2
    left = merge_sort(arr[:i])
    right = merge_sort(arr[i:])
    return arr_merge(left,right)

def bubblesort(arr):
    for end in range(len(arr)-1,0,-1):
        for i in range(0,end):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

def partition(arr,l,r,value):
    if l > r:
        return -1
    less = l-1
    more = l+1
    cur = l
    while cur < more:
        if arr[cur] < value:
            arr[less+1],arr[cur] = arr[cur],arr[less+1]
            less +=1
            cur +=1
        elif arr[cur] > value:
            arr[more-1],arr[cur] = arr[cur],arr[more-1]
            more -=1
        else:
            cur += 1
    return [less,more]

def quicksort(arr,l,r):
    if l < r:
        p = partition(arr,l,r,arr[l])
        quicksort(arr,l,p[0])
        quicksort(arr,p[1],r)

class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def print_all(head):
    if head is not None:
        print(head.value)
        print_all(head.left)
        print_all(head.right)

if __name__ == '__main__':
    # tt = test('zhang',27)
    # print(tt.name)
    ll1 = [random.randint(1,100) for i in range(10)]
    # ll1 = quicksort(ll1)
    # ll2 = [random.randint(1,100) for i in range(6)]
    # ll2 = quicksort(ll2)
    # print(arr_merge(ll1,ll2))
    print(merge_sort(ll1))
    print(bubblesort(ll1))
    quicksort(ll1,0,len(ll1)-1)
    print(ll1)
    arr=[5,4,3,2,1,0]
    node_list = []
    for i in range(len(arr)):
        node = Node(arr[i])
        node_list.append(node)
    if len(node_list) > 0:
        for i in range(len(arr)//2):
            if 2 * i + 1 < len(node_list):
                node_list[i].left = node_list[2*i+1]
            else:
                node_list[i].left = None
            if 2*i+2 < len(node_list):
                node_list[i].right = node_list[2*i+2]
            else:
                node_list[i].right = None
        # last_indx = len(arr)//2 - 1
        # node_list[last_indx].left = node_list[2*last_indx+1]
        # if len(arr)%2==1:
        #     node_list[last_indx].right = node_list[2*last_indx+2]
    if node_list:
        print_all(node_list[2])

    # print(value)
