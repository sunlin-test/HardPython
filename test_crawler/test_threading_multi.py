# coding=utf-8

'''
单进程多线程
'''

from multiprocessing import Process
from threading import Thread
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

    start_time = time.time()
    print("主进程号：",os.getpid())

    t1 = Thread(target=girl_tack,args=(girl_list1,))
    t1.start()
    t2 = Thread(target=girl_tack, args=(girl_list2,))
    t2.start()
    t3 = Thread(target=girl_tack, args=(girl_list3,))
    t3.start()

    t_list = [t1,t2,t3]
    [i.join() for i in t_list]

    end_time = time.time()
    print("耗时:",end_time-start_time)
