# coding=utf-8

'''
多进程单线程
'''

from multiprocessing import Process
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
    girl_list1 = [{"name": "小丽", "time": 5}, {"name": "小美", "time": 2}]
    girl_list2 = [{"name": "小爱", "time": 5}, {"name": "小花", "time": 1}]
    girl_list3 = [{"name": "小玉", "time": 1}, {"name": "小彩", "time": 1}]

    print("主进程号：",os.getpid())
    start_time = time.time()
    # (元组转换：[]列表转换为元组，同元素转换。([],)转换为元组，列表始终为一个元素。([])转换为元组，同元素转换)
    p1 = Process(target=girl_tack,args=(girl_list1,))
    p1.start()
    p2 = Process(target=girl_tack, args=(girl_list2,))
    p2.start()
    p3 = Process(target=girl_tack, args=(girl_list3,))
    p3.start()

    # 若不join()，主进程不会等子进程，自己结束
    p_list = [p1,p2,p3]
    [i.join() for i in p_list]

    end_time = time.time()
    print("耗时:",end_time-start_time)
