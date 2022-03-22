# coding=utf-8

import requests

get_url ="https://www.baidu.com"
response = requests.get(url=get_url)
print(response.encoding)
#response.encoding = 'utf-8'
page_text = response.content.decode('utf-8')

# python3 open()可指定encoding. python2怎么处理乱码?
"""
python3: response.encoding = 'utf-8'    page_text = response.text       with open('./baidu.html','w',encoding='utf-8') as f:
python3: page_text = response.content.decode()        with open('./baidu.html','w',encoding='utf-8') as f
python2: page_text = response.content       with open('./baidu.html','w') as f:
"""
with open('./baidu.html','w',encoding='utf-8') as f:
    f.write(page_text)