# coding=utf-8

'''目标：模拟monitor_db_audit.py，db造数
1. python3使用PyMysql连接mysql
2. 建立一个连接pymysql.connect()
3. 用连接建立一个游标conn.cursor()  游标是为了featchone() 一条一条返回一行结果，以好处理
4. 用游标执行sql语句，结果自动保存，通过featchone()/featchall()取结果
5. 连接关闭conn.close()
'''

import pymysql

# 实际为实例化connection对象，创建一个soket，self._sock = soket(host,port)
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='db_test1')
# 实际为：cur = cursor(connection对象)
cur = conn.cursor()
# 实际为调用conn._execute_command(sql) --self._sock.sendall().返回影响行数.若sql执行失败，抛出异常
# cur.execute("drop table if exists tab_t1")
# cur.execute("create table tab_t1 (c1 int primary key, c2 int not null);")
#cur.execute("insert into tab_t1 values(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16)")
# cur.execute("insert into tab_t1 select c1+c1m, c1+c1m from (select max(c1) c1m from tab_t1) v1, tab_t1")
cur.execute("select count(*) from pft")
rows = cur.fetchone()
cur.execute("select * from pft")
f = open('./result_ptf.txt','w')

for i in range(0,rows[0]):
    f.write(str(cur.fetchone()))
# self._sock.sendall("<iB")
conn.close()


