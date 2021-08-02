#排序+查找，重中之重#1。排序：冒泡排序，快速排序，归并排序，堆排序#2。线性查找，二分查找#3。时间，空间复杂度import randomdef print_str(a=None,b=None):    if a is not None and b is not None:        print(str(a)+str(b))    elif b is None:        print(a)print_str('========快速排序=========')def quickSort(arr):    if len(arr) < 2:        return arr    else:        pivot_index = 0        pivot = arr[pivot_index]        less_part=[i for i in arr[pivot_index+1:] if i < pivot]        grand_part=[i for i in arr[pivot_index+1:] if i > pivot]        return quickSort(less_part)+[pivot]+quickSort(grand_part)def test_quickSort():    ll=list(range(12))    random.shuffle(ll)    print_str('排序之前->',ll)    lled = quickSort(ll)    print_str('快速排序之后->',ll)    print_str('快速排序之后->',lled)test_quickSort()print_str('========合并两个有序列表=========')def merge_sorted_list(sorted_arr1,sorted_arr2):    i = 0    j = 0    print_str('arr1->',sorted_arr1)    print_str('arr2->',sorted_arr2)    arr_merge = []    while i<len(sorted_arr1) and j<len(sorted_arr2):        # print_str('i->',i)        # print_str('j->',j)        if sorted_arr1[i] <= sorted_arr2[j]:            arr_merge.append(sorted_arr1[i])            i += 1        else:            arr_merge.append(sorted_arr2[j])            j += 1    if i>=len(sorted_arr1):        arr_merge.extend(sorted_arr2[j:])    if j>=len(sorted_arr2):        arr_merge.extend(sorted_arr1[i:])    return arr_mergedef test_merge_sort():    ll2=[0,9,10]    ll1=[3,4,7,8]    lled = merge_sorted_list(ll1,ll2)    print_str('lled->',lled)test_merge_sort()print_str('========归并排序=========')def merge_sort(arr):    if len(arr) <= 1:        return arr    i = int(len(arr)//2)    print_str('i->',i)    left = merge_sort(arr[:i])    right = merge_sort(arr[i:])    return merge_sorted_list(left,right)def test_merge_sort():    ll=list(range(12))    random.shuffle(ll)    print_str('ll->',ll)    lled = merge_sort(ll)    print_str('lled->',lled)test_merge_sort()print_str('========堆排序=========')def heap_sort_use_heapq(iterable):    from heapq import heappush,heappop    items = []    for value in iterable:        heappush(items,value)    return [heappop(items) for i in range(len(items))]def test_heap_sort_use_heapq():    ll = list(range(12))    random.shuffle(ll)    print_str('ll->', ll)    lled = heap_sort_use_heapq(ll)    print_str('lled->', lled)test_heap_sort_use_heapq()print_str('========二分查找=========')def binary_search(sorted_arr,target):    if not sorted_arr:        return -1    beg,end = 0,len(sorted_arr)    while beg < end:        mid = beg+(end-beg)//2        if sorted_arr[mid] == target:            return mid        elif sorted_arr[mid]<target:            beg = mid+1        else:            end = mid-1    if beg >= end:        return -1def test_binary_search():    ll = list(range(12))    random.shuffle(ll)    print_str('排序之前->', ll)    lled = quickSort(ll)    print_str('快速排序之后->', lled)    print_str('binary_search->',binary_search(lled,11))test_binary_search()print_str('========二分查找递归实现=========')def binary_search_recursive(sorted_arr,beg,end,target):    if not sorted_arr:        return -1    if beg >= end:        return -1    # mid = int(beg+(end-beg)//2)    mid = beg+end//2    if target == sorted_arr[mid]:        return mid    elif sorted_arr[mid]>target:        return binary_search_recursive(sorted_arr,beg,mid,target)    else:        return binary_search_recursive(sorted_arr,mid+1,end,target)def test_binary_search_recursive():    ll = list(range(12))    random.shuffle(ll)    print_str('排序之前->', ll)    lled = quickSort(ll)    print_str('快速排序之后->', lled)    print_str('binary_search->',binary_search_recursive(lled,0,len(ll)-1,11))test_binary_search_recursive()