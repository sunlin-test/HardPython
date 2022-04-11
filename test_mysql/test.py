# coding=utf-8
import sys,os,time

for i in range(1,7):
    print(time.time())
    print("this is show time")
    sys.stdout.flush()
    time.sleep(2)