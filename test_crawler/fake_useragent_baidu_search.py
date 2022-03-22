# coding=utf-8

from fake_useragent import UserAgent
import requests

ua = UserAgent()
print(ua.random)

get_url = 'https://www.baidu.com/s'
param = {
    "wd": "林高禄"
}
header = {
    "User-Agent": ua.random
}
response = requests.get(url=get_url,params=param,headers=header)
response.encoding = 'utf-8'
data = response.content.decode()

with open('./baidu_fack_useragent.html','w',encoding='utf-8') as f:
    f.write(data)