# coding=utf-8

import requests
import json



def request_baidu():
    resp = requests.get("https://baidu.com")
    print resp.content

def request_csdn():
    resp = requests.get("https://www.csdn.net/")
    print type(resp)
    print resp.content
    print resp.status_code

baidu_or_csdn = raw_input("if you want baidu or csdn?")
if baidu_or_csdn == "baidu":
    request_baidu()
elif baidu_or_csdn == "csdn":
    request_csdn()
else:
    print "现只支持baidu和csdn哦！"

