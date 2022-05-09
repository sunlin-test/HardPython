# coding=utf-8

# 1. 元组和列表怎么互相转换
list1 = ['sdf','sdfa1','sdf2']
change_to_tuple = tuple(list1)
print(change_to_tuple)

list2 = ['sdf']
change_to_tuple2 = tuple(list2)
print(change_to_tuple2)

list3 = ['sdf','sdfa1','sdf2']
change_to_tuple3 = tuple((list3,))
print(change_to_tuple3)

tuple1 = ('sdf','sdfa1','sdf2')
change_to_list = list(tuple1)
print(change_to_list)

tuple2 = ('sdf','sdfa1','sdf2')
change_to_list2 = list((tuple2,))
print(change_to_list2)

# 2. 列表相加
a = [1,2,3]
b = [4,5,6]
print(a+b)

# 3. 列表的用法insert
a = [1,2,4,5,6]
a.insert(2,3)
print(a)
a.sort()
print(a)

# 4.元组定义
tuple1 = (1,)
print(tuple1)

# 5. 序列解包运算，把不定长的数据转换成list
a,*b,c=range(5)
print(a,b,c)
# 0 [1, 2, 3] 4

# 6. 对列表中的数据反向排序
a = [1,2,4,5,6]
a.reverse()
print(a)

a.sort()
print(a)

b = ['a','c','e']
b.reverse()
print(b)

b.sort()
print(b)

# 7. 元组中的元素内容可以重复，但元素不能更改，无append、pop等方法。集合的元素不能重复
tuple1 = (1,2,3)
tunple2 = tuple1*2
print(tunple2)

# 8. 字典的函数使用,get(key)，找不到返回none。info[key]找不到报错
info = {"name":'班长',"id":100,"sex":'f',"address":"北京"}
print(info.get("age"))
#print(info["age"])
print(info.get("age",18))

# 9. 关于list为入参，
a = [1,2,3,4]
b = 1
c = 2
def f(f,obj):
    f.append(5)
    obj = obj + 1
    return f,obj

print(f(a,b))
print(a,b)


a = {"name":"班长","age":18}
b = 1
c = 2
def f(f,obj):
    f['age'] = f['age'] + 1
    obj = obj + 1
    return f,obj

print(f(a,b))
print(a,b)

# 10. list取子列表,若超出范围，返回空列表[]
a = [1,2,3,4,5,6]
print(a[6:])

# 11. list排序
lis = ['apple','lemon','pear','peach']
def fn(x):
    return x[::-1]
lis.sort(key=fn,reverse=True)
print(lis)

# 12.字符串切片x[开始索引:结束索引:步长]
# 步长为负数，代表从右往左截取，开始索引>结束索引
x = 'apple'
print(x[-1:-4:-1])


# 13. 字典的浅拷贝copy()
a = {"one":1,"two":2,"three":3}
b = a.copy()
b["one"] = 12
print(b)
print(a)

b["four"] = 4
print(b)
print(a)

c = {"one":1,"two":2,"three":3,"four":[1,2,3]}
d = c.copy()
d["four"] = [1,2,3,4]
print(c)
print(d)



