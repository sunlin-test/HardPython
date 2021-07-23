# ---coding:utf8---

import requests
import base64
import json
import urllib



class WXForDmcTest:
    def init_param(self):
        password = 'isd@cloud'
        # cipter_pasword = self.encrypt(password, 'wxfordmc-public.pem')
        cipter_pasword = '5da50bf900bcbc17322625ea2cf65319fc6ea53753a3d21337a0fd774f50b6c0abde9c0548252addc48e1f3cca9a863e25ec8b6ecd065b9f789578e5965788f28464027d1dd927dc65497570485282502f72a96a1fe9b95f283138e04bc2684a3ffd2b5f03375a9a1354be3913dc7a88743a33e772bdabdd5b09582b396b3a9f'
        sql = 'select version();'

        self.DBConnetcion = {
            "resourceId": 'dmc-wx-cynosdb',
            "ip": '9.134.46.231',
            "port": 3306,
            "user": 'root',
            "password": cipter_pasword,
            "dbName": 'hello5',
            "charset": '',
            "collation": '',
            "timeout": 0,
            "readTimeout": 0,
            "writeTimeout": 0,
        }
        self.param_detail = {
            "appId": 25100002,
            "uin": '918700682',
            "subAccountUin": '918700682',
            "sqlType": 'user_sql',
            "sqls": base64.b64encode(sql),
            "base64Encode": True,
            "offset": 0,
            "limit": 0,
            "dbConnection": self.DBConnetcion,
            "commonRequest": {
                "databaseKind": "mysql"}
        }

        self.param_interface_detail = {
                "apiName": 'ExecuteForWX',
                # 'QToken': '',
                "para": self.param_detail
            }

        self.param_interface = {
            "interface": self.param_interface_detail
        }


        self.req_param = {
            "Version": '',
            "Region": '',
            "Zone": '',
            "Caller": '',
            "Callee": '',
            "EventId": '',
            "RequestId": '',
            "Timestamp": '',
            "Language": '',
            "ApiModule": '',
            "Interface": self.param_interface
        }

    def excute_for_wx(self,req_param):
        url = 'http://9.134.64.7:12011/interface'
        proxies = {
            "http": "http://127.0.0.1:8888"
        }
        data_json = json.dumps(req_param)
        rsp = requests.post(url,data=data_json,proxies=proxies)
        content = json.loads(rsp.text)
        # if int(content["errno"]) != 0:
        #     print "sqls:",base64.b64decode(req_param['interface']['para']['sqls'])
        #     print "rsp.text['error']:",content["error"]
        #     print '\n'
        print "sqls:", base64.b64decode(req_param['interface']['para']['sqls'])
        print "rsp:",content["error"]
        print '\n'

    def sql_test(self):
        sql_file = 'unionpk.apply.sql'
        sql_files = open(sql_file)
        sql = []
        # print "content_init:",content
        while True:
            content = sql_files.readline()

            if content == '':
                for i in range(5):
                    content = sql_files.readline()
                    if content != '':
                        print "nullcontent:",content
                        break
                if content == '':
                    break

            # print "content:",content
            while '/*' in content:
                # print 'True'
                while '*/' not in content:
                    content = sql_files.readline()
                    # print "content:",content
                content = sql_files.readline()
                if content.isspace() == True:
                    continue
            content2 = content.strip()


            if 'DELIMITER' in content2 or 'delimiter' in content2:
                print "重复调用"
                while True:
                    sql.append(content2)
                    content2 = sql_files.readline()
                    if content2 == '':
                        continue
                    # content2 = content2.strip()
                    #print "content2:",content2
                    if 'DELIMITER' in content2 or 'delimiter' in content2:
                        sql.append(content2)
                        sqls = ''.join(sql)
                        # print "sqls1:", sqls
                        self.init_param()
                        self.param_detail['sqls'] = base64.b64encode(sqls)
                        self.excute_for_wx(self.param_interface)
                        sql = []
                        break
            else:
                if content2.endswith(';') == True:
                    sql.append(content2)
                    sqls = ''.join(sql)
                    # 执行sql
                    # print "sqls2:", sqls
                    self.init_param()
                    self.param_detail['sqls'] = base64.b64encode(sqls)
                    self.excute_for_wx(self.param_interface)
                    sql = []
                else:
                    sql.append(content2)
                    continue
        sql_files.close()






if __name__ == "__main__":
    manage = WXForDmcTest()
    manage.init_param()
    # manage.sql_test()
    rsp = manage.excute_for_wx(manage.param_interface)
    print rsp