# coding=utf-8

import requests
from fake_useragent import UserAgent
import json

session = requests.session()
ua = UserAgent()

# 1. 登录
login_url = 'https://www.processon.com/login/quick_login'
param = {
    "type": "account_login",
    "login_email": "1021851145@qq.com",
    "login_password": 131826
}
header = {
    "User-Agent": ua.random
}
response = session.post(url=login_url,data=param,headers=header)
print(response.content)

# 2. 历史数据拉取
history_url = 'https://www.processon.com/folder/loadfiles'
response = session.get(url=history_url,headers=header)
response.encoding='utf-8'
# response.json()，dict类型。实现为将返回的json串调用json.loads()转换为dict
history = response.json()
print(type(history))
# json.dumps(dict)，将dict转换为str
history_2 = json.dumps(history,ensure_ascii=False)
print(type(history_2))
# json.loads(json)，将json转换为dict
history_3 = json.loads(history_2)
print(type(history_3))
# json.dump(dict,file_object,ensure_ascii=False) 将dict转换为json并输出存储到打开的json文件
with open("./processon_history.json",'w',encoding='utf-8') as f:
    json.dump(history,f,ensure_ascii=False)



# 3. 登出