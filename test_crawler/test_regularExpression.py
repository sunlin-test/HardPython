# coding=utf-8

import re

'''测试正则表达式函数
1. re.match()，从字符串开头匹配，即自动有^加成
2. re.search()，从整个字符串匹配
3. 如果有匹配，都返回一个re.Match对象，若想取具体匹配值，需取re.Match().group()
4. re.sub()，替换，返回一个被替换后的字符串
5. re.compile(正则表达式),返回一个re对象，以用于match、search()等
6. re.findall()，找到匹配到的所有子串，并以list返回。即返回()中的匹配内容
7. re.finditer()，返回一个迭代器，每个元素都是一个match对象，通过match.group()取具体匹配值
8. re.split()，以正则表达式匹配到的字符/字符串为分割线，分割字符串，返回分割后的list
'''

if __name__ == "__main__":
    your_string = 'www.baidu.com'
    my_string = re.match('www\.baidu',your_string)
    print(my_string)

    line = "Cats are smarter than dogs"
    match_object = re.match('(.*) are (.*?) .*',line)
    if match_object:
        print(match_object.group())
        print(match_object.group(1))
        print(match_object.group(2))
    else:
        print("No match!")

    line2 = 'www.baidu.com,baidu2'
    match_object2 = re.search('baidu',line2)
    print(type(match_object2))
    print(match_object2.group())

    # 未实现
    line3 = '<h1>test取标签值</h1>'
    match_object3 = re.search('<h1>(.*?)</h1>',line3)
    print(match_object3.group())
    pattern = re.compile('<h1>(.*?)</h1>',re.I)
    m = pattern.findall('<h1>test取标签值</h1>')
    print(m)

    # 替换
    line4 = '2004-959-559 # 这是一个电话号码'
    num = re.sub('#.*','',line4)
    print("电话号码：",num)

    num2 = re.sub('\D','',line4)
    print("电话号码：", num2)

    # compile
    pattern = re.compile('([a-z]+) ([a-z]+)',re.I)
    print(type(pattern))
    m = pattern.match("Hello World Wide Web")
    print(m.group(1))
    print(m.group(2))

    # finditer
    iters = re.finditer('\d+','sdf1212sdf122229sdfl0987')
    print(type(iters))
    for match in iters:
        print(match.group())

    # split()
    lists = re.split('\W+',"sdf,sdfs1,sdfsfd2,sdfsdf3")
    print(lists)
