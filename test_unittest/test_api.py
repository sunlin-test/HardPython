# coding=utf-8

'''
获取鉴权码验证
'''

import unittest

import requests
from ddt import ddt,data,file_data

@ddt
class TestApi(unittest.TestCase):
    # 类变量
    # 通过类变量，在方法间传参
    access_token = ''

    @file_data("./get_token.yaml")
    def test_01_get_token(self, **kwargs):
        print kwargs
        url = kwargs['request']['url']
        method = kwargs['request']['method']
        data = kwargs['request']['data']
        rsp = requests.get(url,params=data)
        response = rsp.json()

        TestApi.access_token = response['access_token']
        print TestApi.access_token

    @file_data("./select_flag.yaml")
    def test_02_select_flag(self,**kwargs):
        url = kwargs['request']['url']
        method = kwargs['request']['method']
        data = kwargs['request']['data']
        data['access_token'] = TestApi.access_token
        rsp = requests.get(url, params=data)
        print rsp.json()



if __name__ == '__main__':
    unittest.main()