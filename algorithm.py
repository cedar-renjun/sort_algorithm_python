#! /usr/bin/env python3
# coding = utf-8

import random
import math

###############################################################################
def sort_fun_0(d):
    n = len(d)

    for i in range(0, n):
        min_idx = i
        min_raw = i
        for j in range(i+1, n):
            if d[j] < d[min_idx]:
                min_idx = j
        if min_idx != min_raw:
            d[min_raw],d[min_idx] = (d[min_idx], d[min_raw])
    
    return d

###############################################################################
def sort_fun_1(d):

    length = len(d)

    for index in range(length):
        # 标志位
        flag = True
        for j in range(1, length - index):
            if d[j - 1] > d[j]:
                d[j - 1], d[j] = d[j], d[j - 1]
                flag = False
        if flag:
            # 没有发生交换，直接返回list
            return d
    return d

###############################################################################
def sort_fun_2(d):

    n = len(d)

    for i in range(1, n):

        pre_idx = i-1
        cur_val = d[i]
        
        while (pre_idx >= 0) and (d[pre_idx] > cur_val):
            d[pre_idx+1] = d[pre_idx]
            pre_idx -= 1
        
        d[pre_idx+1] = cur_val

    return d

###############################################################################
# shell sort
def sort_fun_3(d):

    n = len(d)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            j = i
            while (j - gap) >= 0:
                if d[j] < d[j-gap]:
                    d[j],d[j-gap] = d[j-gap],d[j]
                    j -= gap
                else:
                    break
        gap = gap//2

    return d

#merge sort
def merge(left,right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    if left:
        result += left
    if right:
        result += right

    return result

def merge_sort(d):

    if len(d) <= 1:
        return d

    mid = len(d)//2
    left = d[:mid]
    right = d[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

###############################################################################
def sort_fun_4(d):
    return merge_sort(d)

###############################################################################

def quick_sort(d):
    if len(d) <= 1:
        return d
    
    left = []
    right = []
    mid = []
    pivot = random.choice(d)

    for i in d:
        if i == pivot:
            mid.append(i)
        elif i < pivot:
            left.append(i)
        else:
            right.append(i)
    
    return quick_sort(left) + mid + quick_sort(right)

def sort_fun_5(d):
    return quick_sort(d)

###############################################################################
#Heap Sort

def heap_sort(d):
    pass

def sort_fun_6(d):
    return d

###############################################################################
# count sort

def count_set(d):
    
    bucket = [0] * (max(d) -min(d) + 1)
    for i in d:
        bucket[i] += 1

    res = []
    for i in range(len(bucket)):
        while bucket[i] > 0:
            res.append(i)
            bucket[i] -= 1

    return res

def sort_fun_7(d):
    return count_set(d)

###############################################################################
def sort_fun_8(d):
    return d
    
###############################################################################
def sort_fun_9(d):
    return d

funs_set = [
    sort_fun_0,
    sort_fun_1,
    sort_fun_2,
    sort_fun_3,
    sort_fun_4,
    sort_fun_5,
    sort_fun_6,
    sort_fun_7,
    sort_fun_8,
    sort_fun_9,
]

def my_sort_fun(d, idx):
    return funs_set[idx](d)

def test_sort(fun, idx):
    data_size = 1000
    data_raw = []
    for i in range(0, data_size):
        data_raw.append(random.randint(-1000,1000))
        
    #Sort data
    data_sort = fun(data_raw, idx)

    # Test data set
    test_flag = 0
    for i in range(0, data_size - 1):
        if data_sort[i] > data_sort[i+1]:
            test_flag = 1
            break

    return test_flag

for i in range(10):
    res = test_sort(my_sort_fun, i)
    if res:
        print('[%s] Failure' % i)
    else:
        print('[%s] Success' % i)
