# coding=utf-8


import requests



# 1. 不传参发送http请求。除url，其他需以键值对传输
# response.content  以字符串获取请求的返回body,get、post请求都可用
# response.json()   以dict() 获取请求的返回body,若body无法转换将报错
param = {"wd":"test"}
header = {"User-Agent":"PostmanRuntime/7.29.0"}
proxy = {
    "https:": "https://sunlin:isd@cloud123@127.0.0.1:8020",
    "http:": "http://sunlin:isd@cloud123@127.0.0.1:8020"
}
#response = requests.get("http://www.baidu.com",params = param)
response = requests.request("get","http://www.baidu.com",params = param,proxies=proxy,verify=False)
print response.content
print type(response.text)
print response.url
print response.encoding

# 2.get响应对应的请求体
# print response.request.url
#
# param = {"name":"sunlin"}
# url = 'https://api.weixin.qq.com/cgi-bin/tags/create?access_token=54_aST60Y6Shzcz1uakRwSN8dWRD-3cVBcIrCUrONekgwu8wIghrpeDsk5sY2PoaCw8HZRKqZuQ1ASdbQSTUWIrGuOFzFhW9wSWkTf6n32awt9kM3qSXjgFNwWh5RgE10Vrsjkq2O5QS0vMHrQUGGKjADAUUY'
#
# post_response = requests.post(url,data=param)
# print type(post_response.text)
# print post_response.request.url



# 有道翻译
# 3. python2，content-Type中不能指定charset=UTF-8
print "有道翻译："
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
}

key = "environment"


data = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "16463823729419",
    "sign": "2ae76d11825d17cd06ded18ba45d40ae",
    "lts": "1646382372941",
    "bv": "c2777327e4e29b7c4728f13e47bde9a5",
    "doctype": "json",
    "version": 2.1,
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME"
}
url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
response = requests.post(url, data=data,headers=headers,proxies=proxy,verify=False)
print response.json()["translateResult"][0][0]["tgt"]
print response.status_code
# 4. response.request.body 返回post请求body
print response.request.body
print response.url
print response.encoding
print response.content
print response.text

# 通过代理


# 3.拉取图片
# https://www.baidu.com/img/pc_9c5c85e6b953f1d172e1ed6821618b91.png
response = requests.get("https://www.baidu.com/img/pc_9c5c85e6b953f1d172e1ed6821618b91.png")
img_name = "baidu_get_img.jpg"
img_path = './'
with open(img_path + img_name,'wb') as f:
    f.write(response.content)
print "保存图片完成"