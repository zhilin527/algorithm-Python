# -*- coding: UTF-8 -*-class Node:    def __init__(self,value):        self.value = value        self.left = None        self.right = Nonedef arrtoNodeList(arr):    node_list = []    for i in range(len(arr)):        if arr[i]:            node = Node(arr[i])            node_list.append(node)        else:            node_list.append(None)    if len(node_list) > 0:        for i in range(len(arr)//2):            if 2 * i + 1 < len(node_list):                node_list[i].left = node_list[2*i+1]            else:                node_list[i].left = None            if 2*i+2 < len(node_list):                node_list[i].right = node_list[2*i+2]            else:                node_list[i].right = None    # for n in node_list:    #     print(n)    return node_list[0]if __name__ == '__main__':    arr=[1,2,3,None,5,6,None]    head = arrtoNodeList(arr)    # process(head)