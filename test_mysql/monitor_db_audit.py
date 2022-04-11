# coding=utf-8

'''
1. Exception.__str__() 获取异常信息
2. sys.stdout.flush() sys.stdout缓冲区刷新，及时输出  --好像没有区别
3. exit(0) 退出程序
'''

import pymysql
import random
import time
from multiprocessing import Process,Pool
import sys
import os
import json

print(len(sys.argv))
if len(sys.argv) <12:
    print("传参不足")
    exit(0)
# python monitor_db_audit.py 127.0.0.1 3306 db_test2 root 123456 select 3 10 2 10 3 2


# 数据库信息
db_ip = sys.argv[1]
db_port = int(sys.argv[2])
db_name = sys.argv[3]
user_name = sys.argv[4]
passwd = sys.argv[5]

# 操作类型
sql_mode = sys.argv[6]
# 表数量
table_counts = int(sys.argv[7])
# 表大小
table_size = int(sys.argv[8])
# 一次请求插入的行数
insert_dts = int(sys.argv[9])
# 运行时长
exec_time = int(sys.argv[10])
# 变更影响行数
update_dts = int(sys.argv[11])
# 进程数
processing_count = int(sys.argv[12])

class db_op(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(host=db_ip,port = db_port,database=db_name,user = user_name,password = passwd)
            self.cur = self.conn.cursor()
        except Exception as e:
            if e.__str__().find("Unknown database") != -1:
                self.print_error(e, "create database")
                try:
                    self.conn = pymysql.connect(host=db_ip,port = db_port,user = user_name,password = passwd)
                    self.cur = self.conn.cursor()
                    self.cur.execute("create database " + db_name)
                except Exception as e:
                    self.print_error(e,"create database")
                    exit(0)
            else:
                self.print_error(e,"connect")
                exit(0)
        try:
            self.auto_commit=1
            self.conn.autocommit(self.auto_commit)
        except Exception as e:
            self.print_error(e,"autocommit")


    def print_error(self,exception,action):
        error = {"time":time.time(),
                 "pid": os.getpid(),
                 "action": action,
                 "error": exception.__str__()
                 }
        print(json.dumps(error))
        sys.stdout.flush()



    def execute(self,sql):
        print(sql)
        try:
            self.cur.execute(sql)
        except Exception as e:
            self.print_error(e,'execute')
            return False

    def close(self):
        self.conn.close()



def get_random_longstr(lens):
    longstr = ''.join(random.sample(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'],50) * (lens//50))
    return longstr


def create_table(table_name):
    db_conn = db_op()

    sql = "drop table if exists " + table_name
    if False == db_conn.execute(sql):
        return False
    sql = "create table %s  (id integer,`keys` integer,`name` text,PRIMARY KEY(id)) PARTITION BY HASH(`id`) partitions 4" % table_name
    if False == db_conn.execute(sql):
        return False

    insert_table(table_name,table_size,db_conn)
    db_conn.close()


def insert_table(table_name,table_size,db_conn):
    sql = "insert into %s values " % table_name
    now_count = 0
    for i in range(0,table_size//insert_dts):
        insert_size = insert_dts
        if (table_size - now_count) < insert_size:
            insert_size = table_size - now_count
        value_str = []
        for j in range(0,insert_size):
            key = random.randint(0,100)
            value_str.append(("(%s,%s,'%s')")%(insert_dts * i + j,key,get_random_longstr(key)))
        #print(value_str)
        tmp_sql = sql + ','.join(value_str)
        if False == db_conn.execute(tmp_sql):
            return False
        now_count = now_count + insert_size




def update_table():
    db_conn = db_op()
    start_time = time.time()

    while True:
        if time.time() - start_time >= exec_time:
            break
        id = random.randint(1,table_size)
        sql = "update sbtest%s set name='%s' where id>%s and id<%s" % (random.randint(1,table_counts),get_random_longstr(random.randint(100,1000)),id,(id+update_dts))
        db_conn.execute(sql)
    db_conn.close()


def select_sample():
    start_time = time.time()
    db_conn = db_op()
    while True:
        if time.time() - start_time >= exec_time:
            break
        sql = "select @@version"
        if False == db_conn.execute(sql):
            return False
    db_conn.close()


if __name__ == "__main__":
    # 测试连接
    db_conn = db_op()
    del db_conn
    if sql_mode == "insert":
        for i in range(1,table_counts+1):
            table_name = 'sbtest%s' % i
            p = Process(target=create_table,args=(table_name,))
            p.start()
    elif sql_mode == "update":
        for i in range(1,processing_count+1):
            p = Process(target=update_table)
            p.start()
    elif sql_mode == "select":
        for i in range(1,table_counts+1):
            p = Process(target=select_sample)
            p.start()

        # 进程池是以指定请求为条件触发创建多进程，若调用方法无入参，iterable=[]，则无法调用


