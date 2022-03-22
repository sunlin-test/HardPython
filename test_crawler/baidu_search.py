# coding=utf-8

import requests

if __name__ == '__main__':
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
    }
    get_url = 'https://www.baidu.com/s'
    param = {
        "wd": '林高禄'
    }
    response = requests.get(url=get_url,params=param,headers=header)
    page_content = response.content.decode('utf-8')
    with open('./my_baidu_du.html','w',encoding='utf-8') as f:
        f.write(page_content)