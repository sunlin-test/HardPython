# coding=utf-8

'''
输出乘法表
1~ 9
'''

def mutipilication_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print '{0} x {1} = {2}'.format(j,i,i*j),
        print ''


mutipilication_table()