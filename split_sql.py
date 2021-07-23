import pymysql

class Table:
    def __init__(self,table_define):
        self.table_define = table_define
        print "self.table_define:",self.table_define
        self.table_name = ''
        if "CREATE TABLE" in self.table_define:
            self.table_name = self.table_define.split('`')[1]
        print self.table_name
        self.columns = []
        column_name = ''
        column_type = ''
        table = {
            "table_name": '',
            "columns":[
                {"column_name": '',
                 "column_type": ''}
            ]
        }

def sqlToJson(cursor, sql, key):
    cursor.execute(sql)
    data = cursor.fetchall()
    jsonList = []
    for i in data:
        jsonList.append(dict(zip(key, i)))
    return jsonList


if __name__ == '__main__':
    rsp = [u'tab_t1\tCREATE TABLE `tab_t1` (\\n  `c1` int(11) DEFAULT NULL,\\n  `c2` int(11) DEFAULT NULL\\n) ENGINE=InnoDB DEFAULT CHARSET=utf8\n']
    for i in rsp:
        rsp_list = i.split('\t')
    table_define = rsp_list[1].decode("unicode_escape").encode('utf8')
    test_table = Table(table_define)
    cursor = pymysql()
    sqlToJson(cursor,table_define)

