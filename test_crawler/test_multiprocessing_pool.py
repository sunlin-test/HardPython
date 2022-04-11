# coding=utf-8

'''
进程池
指定池中最大进程数量，若<最大进程数，则新建进程处理新的请求。若>=最大进程数，则等待
不太智能，若按照girl_list中元素的顺序请求，未5+5，2+1，3+1，耗时10
若按照girl_list中的预约时长请求，5+1,5+2,3+1，耗时7
使用进程池可以用两种包
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor
'''

from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor
import threading
import os
import time

def tack(girl):
    print(f'进程号{os.getpid()}和{girl["name"]}开始交谈，父进程为{os.getppid()}，线程号{threading.current_thread()}交谈时间{girl["time"]}')
    time.sleep(girl["time"])
    print(f'进程号{os.getpid()}和{girl["name"]}交谈结束，线程号{threading.current_thread()}')


def girl_tack(list1):
    for girl in list1:
        tack(girl)

if __name__ == "__main__":
    # 客户
    girl_list1 = [{"name": "小丽", "time": 5}, {"name": "小美", "time": 2},{"name": "小爱", "time": 5}, {"name": "小花", "time": 1}
        ,{"name": "小玉", "time": 1}, {"name": "小彩", "time": 1}]
    start_time = time.time()

    # 开3个进程
    pool = Pool(3)
    # map，以序列中的每一个元素为入参调用一次函数，返回每次调用的返回值列表
    pool.map(func=tack,iterable=girl_list1)
    pool.close()
    # 只能先close()再join()
    pool.join()

    # pool = ProcessPoolExecutor(3)
    # pool.map(tack,girl_list1)
    # pool.shutdown()

    end_time = time.time()
    print("耗时:",end_time-start_time)
