#!/Users/vvguoliang/PycharmProjects python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/23 上午10:02
# @Author  : vvguoliang
# @Site    : 
# @File    : Sort.py
# @Software: PyCharm

"""
__title__ = ''
__author__ = 'vvguoliang'
__mtime__ = '2018/2/23'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏ ┓
            ┏┛┻━━━┛ ┻┓
            ┃   ☃   ┃
            ┃ ┳┛  ┗┳ ┃
            ┃    ┻   ┃
            ┗━┓    ┏━┛
              ┃    ┗━━━┓
              ┃ 神兽保佑 ┣┓
              ┃ 永无BUG！┏┛
              ┗┓┓┏━┳┓┏┛┏┛
               ┃┫┫  ┃┫┫
               ┗┻┛  ┗┻┛
"""

'''
插入排序

Insertion sort
插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，
从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。是稳定的排序方法。
插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外（让数组多一个空间才有插入的位置），
而第二部分就只包含这一个元素（即待插入元素）


当前需要排序的元素(lists[i])，跟已经排序好的最后一个元素比较(lists[i-1])，如果满足条件继续执行后面的程序，否则循环到下一个要排序的元素。
缓存当前要排序的元素的值，以便找到正确的位置进行插入。
排序的元素跟已经排序号的元素比较，比它大的向后移动(升序)。
要排序的元素，插入到正确的位置。
'''

lists = [5, 67, 8, 9, 4, 3, 6, 88, 9, 4, 6, 34, 34, 2, 6, 7, 8, 9, 9, 90, 4, 3, 6, 7, 2]


def insertion_sort(lists):
    #  插入排序
    for i in range(1, len(lists)):
        if lists[i - 1] > lists[i]:
            temp = lists[i]  # 当前需要排序的元素
            index = i  # 用来记录排序元素需要插入的位置
            while index > 0 and lists[index - 1] > temp:
                lists[index] = lists[index - 1]  # 把已经排序好的元素后移一位，留下需要插入的位置
                index -= 1
            lists[index] = temp  # 把需要排序的元素，插入到指定位置
    return lists


'''
时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：稳定
'''


def insertion_sort1(array):
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
                break
    return array


lists1 = insertion_sort1(lists)
print(lists1)

'''
希尔排序

Shell Sort

希尔排序(Shell Sort)是插入排序的一种。
也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。 
希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止

希尔排序是插入排序的扩展，通过允许非相邻的元素进行交换来提高执行效率。
希尔排序最关键的是选择步长，本程序选用Knuth在1969年提出的步长序列：1 4 13 40 121 364 1093 3280 。。。
后一个元素是前一个元素*3+1，非常方便选取，而且效率还不错
'''


def shell_sort(lists):
    # 希尔排序
    length = len(lists)
    inc = 0
    while inc <= length / 3:
        inc = inc * 3 + 1

    while inc >= 1:
        for i in range(inc, length):
            tmp = lists[i]
            for j in range(i, 0, -inc):
                if tmp < lists[j - inc]:
                    lists[j] = lists[j - inc]
                else:
                    j += inc
                    break
            lists[j - inc] = tmp
        inc //= 3
    return lists


'''
时间复杂度：O(n)
空间复杂度：O(n√n)
稳定性：不稳定
'''


def shell_sort1(array):
    gap = len(array)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(array)):
            for j in range(i % gap, i, gap):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
    return array


list1 = shell_sort1(lists)
print(list1)

'''
冒泡排序

Bubble sort

它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：稳定
'''


def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


list1 = bubble_sort(lists)
print(list1)

'''
快速排序

Fast sorting

通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

1）设置两个变量i、j，排序开始的时候：i=0，j=N-1；
2）以第一个数组元素作为关键数据，赋值给key，即key=A[0]；
3）从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，将A[j]和A[i]互换；
4）从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，将A[i]和A[j]互换；
5）重复第3、4步，直到i=j； (3,4步中，没找到符合条件的值，即3中A[j]不小于key,4中A[i]不大于key的时候改变j、i的值，使得j=j-1，i=i+1，直至找到为止。
找到符合条件的值，进行交换的时候i， j指针位置不变。另外，i==j这一过程一定正好是i+或j-完成的时候，此时令循环结束）。

时间复杂度：O(nlog₂n)
空间复杂度：O(nlog₂n)
稳定性：不稳定
'''


def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


list1 = quick_sort(lists, 0, len(lists) - 1)
print(list1)

'''
直接选择排序

Direct selection sorting

基本思想：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；
第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。

时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：不稳定
'''


def select_sort(lists):
    # 选择排序
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists


list1 = shell_sort(lists)
print(list1)

'''
堆排序

Heap sorting

堆排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法，它是选择排序的一种。
可以利用数组的特点快速定位指定索引的元素。堆分为大根堆和小根堆，是完全二叉树。
大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。
在数组的非降序排序中，需要使用的就是大根堆，因为根据大根堆的要求可知，最大的值一定在堆顶。


堆

在这里首先要先解释一下什么是堆，堆栈是计算机的两种最基本的数据结构。堆的特点就是FIFO(first in first out)先进先出，这里的话我觉得可以理解成树的结构。
堆在接收数据的时候先接收的数据会被先弹出。 
栈的特性正好与堆相反，是属于FILO(first in/last out)先进后出的类型。栈处于一级缓存而堆处于二级缓存中。
这个不是本文重点所以不做过多展开。

堆排序节点访问和操作定义

堆节点的访问

在这里我们借用wiki的定义来说明： 
通常堆是通过一维数组来实现的。在阵列起始位置为0的情况中 
(1)父节点i的左子节点在位置(2*i+1); 
(2)父节点i的右子节点在位置(2*i+2); 
(3)子节点i的父节点在位置floor((i-1)/2);

堆操作

堆可以分为大根堆和小根堆，这里用最大堆的情况来定义操作: 
(1)最大堆调整(MAX_Heapify):将堆的末端子节点作调整，使得子节点永远小于父节点。这是核心步骤，在建堆和堆排序都会用到。
比较i的根节点和与其所对应i的孩子节点的值。当i根节点的值比左孩子节点的值要小的时候，就把i根节点和左孩子节点所对应的值交换，
当i根节点的值比右孩子的节点所对应的值要小的时候，就把i根节点和右孩子节点所对应的值交换。然后再调用堆调整这个过程，可见这是一个递归的过程。 
(2)建立最大堆(Build_Max_Heap):将堆所有数据重新排序。建堆的过程其实就是不断做最大堆调整的过程，从len/2出开始调整，一直比到第一个节点。 
(3)堆排序(HeapSort):移除位在第一个数据的根节点，并做最大堆调整的递归运算。堆排序是利用建堆和堆调整来进行的。首先先建堆，
然后将堆的根节点选出与最后一个节点进行交换，然后将前面len-1个节点继续做堆调整的过程。直到将所有的节点取出，对于n个数我们只需要做n-1次操作
'''


def MAX_Heapify(heap, HeapSize, root):  # 在堆中做结构调整使得父节点的值大于子节点

    left = 2 * root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger], heap[root] = heap[root], heap[larger]
        MAX_Heapify(heap, HeapSize, larger)


def Build_MAX_Heap(heap):  # 构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)  # 将堆的长度当独拿出来方便
    for i in range((HeapSize - 2) // 2, -1, -1):  # 从后往前出数
        MAX_Heapify(heap, HeapSize, i)


def HeapSort(heap):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        MAX_Heapify(heap, i, 0)
    return heap


'''
时间复杂度：O(nlog₂n)
空间复杂度：O(1)
稳定性：不稳定
'''


def HeapSort1(array):
    def heap_adjust(parent):
        child = 2 * parent + 1  # left child
        while child < len(heap):
            if child + 1 < len(heap):
                if heap[child + 1] > heap[child]:
                    child += 1  # right child
            if heap[parent] >= heap[child]:
                break
            heap[parent], heap[child] = \
                heap[child], heap[parent]
            parent, child = child, 2 * child + 1

    heap, array = array.copy(), []
    for i in range(len(heap) // 2, -1, -1):
        heap_adjust(i)
    while len(heap) != 0:
        heap[0], heap[-1] = heap[-1], heap[0]
        array.insert(0, heap.pop())
        heap_adjust(0)
    return array


list1 = HeapSort1(lists)
print(list1)

'''
归并排序

Merging sorting

归并排序是建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，
得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。

归并过程为：比较a[i]和a[j]的大小，若a[i]≤a[j]，则将第一个有序表中的元素a[i]复制到r[k]中，并令i和k分别加上1；
否则将第二个有序表中的元素a[j]复制到r[k]中，并令j和k分别加上1，如此循环下去，直到其中一个有序表取完，
然后再将另一个有序表中剩余的元素复制到r中从下标k到下标t的单元。归并排序的算法我们通常用递归实现，先把待排序区间[s,t]以中点二分，
接着把左边子区间排序，再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]。

归并排序：
    先分开再合并，分开成单个元素，合并的时候按照正确顺序合并
    
    假如我们有一个n个数的数列，下标从0到n-1
　　首先是分开的过程
    1 我们按照 n//2 把这个数列分成两个小的数列
    2 把两个小数列 再按照新长度的一半 把每个小数列都分成两个更小的
    。。。一直这样重复，一直到每一个数分开了
    比如：    6 5 4 3 2 1
        第一次 n=6 n//2=3 分成      6 5 4      3 2 1
        第二次 n=3 n//2=1 分成    6   5 4    3   2 1
        第三次 n=1的部分不分了
                n=2 n//2=1 分成     5   4      2  1
                
    之后是合并排序的过程：
    3 分开之后我们按照最后分开的两个数比较大小形成正确顺序后组合绑定
        刚刚举得例子 最后一行最后分开的数排序后绑定   变成     4 5     1 2
        排序后倒数第二行相当于把最新分开的数排序之后变成    6   4 5       3    12
    4 对每组数据按照上次分开的结果，进行排序后绑定
        6 和 4 5(两个数绑定了)  进行排序
        3 和 1 2(两个数绑定了)  进行排序
        排完后 上述例子第一行待排序的  4 5 6      1 2 3  两组数据
    5 对上次分开的两组进行排序
        拿着 4 5 6     1 2 3两个数组，进行排序，每次拿出每个数列中第一个(最小的数)比较，把较小的数放入结果数组。再进行下一次排序。
        每个数组拿出第一个数，小的那个拿出来放在第一位 1 拿出来了，   变成4 5 6    2 3
        每个数组拿出第一个书比较小的那个放在下一个位置  1 2被拿出来，  待排序 4 5 6      2
        每个数组拿出第一个书比较小的那个放在下一个位置  1 2 3 被拿出来，  待排序 4 5 6
        如果一个数组空了，说明另一个数组一定比排好序的数组最后一个大 追加就可以结果 1 2 3 4 5 6
    相当于我们每次拿到两个有序的列表进行合并，分别从两个列表第一个元素比较，把小的拿出来，在拿新的第一个元素比较，把小的拿出来
        这样一直到两个列表空了 就按顺序合并了两个列表
    
    结束

时间复杂度： 最好最坏都是 O( n log n )
稳定性：稳定
缺点：每次拆分数组都要开心的数组， 每次合并数组都要开新数组，空间复杂度很大
'''


def merge_sort(li):
    # 不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
    if len(li) == 1:
        return li

    # 取拆分的中间位置
    mid = len(li) // 2
    # 拆分过后左右两侧子串
    left = li[:mid]
    right = li[mid:]

    # 对拆分过后的左右再拆分 一直到只有一个元素为止
    # 最后一次递归时候ll和lr都会接到一个元素的列表
    # 最后一次递归之前的ll和rl会接收到排好序的子序列
    ll = merge_sort(left)
    rl = merge_sort(right)

    # 我们对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表
    # 这里我们调用拎一个函数帮助我们按顺序合并ll和lr
    return merge(ll, rl)


# 这里接收两个列表
def merge(left, right):
    # 从两个有顺序的列表里边依次取数据比较后放入result
    # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
    result = []
    while len(left) > 0 and len(right) > 0:
        # 为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    result += left
    result += right
    return result


'''
时间复杂度：O(nlog₂n)
空间复杂度：O(1)
稳定性：稳定
'''


def merge_sort1(array):
    def merge_arr(arr_l, arr_r):
        array = []
        while len(arr_l) and len(arr_r):
            if arr_l[0] <= arr_r[0]:
                array.append(arr_l.pop(0))
            elif arr_l[0] > arr_r[0]:
                array.append(arr_r.pop(0))
        if len(arr_l) != 0:
            array += arr_l
        elif len(arr_r) != 0:
            array += arr_r
        return array

    def recursive(array):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        arr_l = recursive(array[:mid])
        arr_r = recursive(array[mid:])
        return merge_arr(arr_l, arr_r)

    return recursive(array)


list1 = merge_sort1(lists)
print(list1)

'''
基数排序

Cardinality sorting

基数排序（radix sort）属于“分配式排序”（distribution sort），又称“桶子法”（bucket sort）或bin sort，顾名思义，
它是透过键值的部份资讯，将要排序的元素分配至某些“桶”中，藉以达到排序的作用，基数排序法是属于稳定性的排序，其时间复杂度为O (nlog(r)m)，
其中r为所采取的基数，而m为堆数，在某些时候，基数排序法的效率高于其它的稳定性排序法。
'''


# 基于桶排序的基数排序

def radix_sort(array):
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(array):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(array)):
            num = (array[i] // 10 ** digit) % 10
            bucket[num].append(array[i])
        array.clear()
        for i in range(len(bucket)):
            array += bucket[i]
        digit += 1
    return array


list1 = radix_sort(lists)
print(list1)

# https://www.cnblogs.com/woider/p/6835466.html  通过实验已经把排序都里出来了


'''
速度比较
'''

from random import random
from json import dumps, loads


# 生成随机数文件
def dump_random_array(file='numbers.json', size=10 ** 4):
    fo = open(file, 'w', 1024)
    numlst = list()
    for i in range(size):
        numlst.append(int(random() * 10 ** 10))
    fo.write(dumps(numlst))
    fo.close()


# 加载随机数列表
def load_random_array(file='numbers.json'):
    fo = open(file, 'r', 1024)
    try:
        numlst = fo.read()
    finally:
        fo.close()
    return loads(numlst)


dump_random_array()
# load_random_array()

from _datetime import datetime


# 显示函数执行时间
def exectime(func):
    def inner(*args, **kwargs):
        begin = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        inter = end - begin
        print('E-time:{0}.{1}'.format(
            inter.seconds,
            inter.microseconds
        ))
        return result

    return inner

import sys

@exectime
def bubble_sort(lists):
    for i in range(len(lists)):
        for j in range(i, len(lists)):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


lists1 = load_random_array()
print(bubble_sort(lists1) == sorted(lists1))