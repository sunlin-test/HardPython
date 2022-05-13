# coding=utf-8

'''
冒泡排序
对一个序列，做从小到大排序，排序方法：
1.每轮排序，前一个和后一个元素对比，若前>后，交换两者顺序，找出最大的一个移到最后一位
2.下一轮排序，只对比除最后一位的前面的元素
'''


def bubble_sort(sort):
    for i in range(len(sort)):
        for j in range(len(sort)-i-1):
            print 'i=',i,'j=',j
            if sort[j] > sort[j + 1]:
                sort[j + 1], sort[j] = sort[j], sort[j + 1]
    return sort

print "冒泡排序方法1："
sort = [1,4,2,6,3,5]
print '排序前：',sort
bubble_sort(sort)
print '排序后：',sort

sort2 = ['ad','sb','ac','b3']
print '排序前：',sort2
bubble_sort(sort2)
print '排序后：',sort2

sort3 = [64, 34, 25, 12, 22, 11, 24]
print '排序前：',sort3
bubble_sort(sort3)
print '排序后：',sort3