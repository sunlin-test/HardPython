# coding=utf-8


'''
1,2,~100的整数和
'''

def summary(a):
    sum_a = 0
    for i in range(1,a+1):
        sum_a += i
    return sum_a

a = 100
sum_a = summary(a)
print "sum=",sum_a