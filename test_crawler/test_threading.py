# coding=utf-8

'''
  单进程单线程
  某解忧网（专门通过谈心的方式，解答客户的心事，给客户心灵鸡汤开导，排忧解难）开业当天就有3个单，是3个女的，每个女的都有自己的下单预谈时长，
  但是目前情感导师只有老板林某一个，**单进程单线程情况下，**老板要和一个女的谈完后，再接着和下一个女的谈，不能同时和2个或以上的女的谈，后面的要排队等候
————————————————
版权声明：本文为CSDN博主「深知她是一场梦」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/lgl782519197/article/details/111873584

1. os.getpid() 运行python文件时，会生成一个新进程，即主进程

'''

import time
import os,threading


def tack(girl):
    print(f'进程号{os.getpid()}和girl["name"]开始交谈，线程号{threading.current_thread()}交谈时间{girl["time"]}')
    time.sleep(girl["time"])
    print(f'进程号{os.getpid()}和girl["name"]交谈结束，线程号{threading.current_thread()}')


def girl_tack(list1):
    for girl in list1:
        tack(girl)


if __name__ == "__main__":
    # 客户
    girl_list1 = [{"name": "小丽", "time": 10},{"name": "小美", "time": 2},{"name": "小爱", "time": 20}]
    start_time = time.time()
    # 交谈
    girl_tack(girl_list1)
    end_time = time.time()
    print("耗时",end_time-start_time)




