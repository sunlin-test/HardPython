# coding=utf-8

# try:
#     print "this is a try"
#     print "this is a try2"
#     int("sdf")
#     # int("122")
#     print "this is a try3"
# except Exception as e:
#     print "this is a except"
#     print e.message
# else:
#     print "this is a else"
# finally:
#     print "this is a finally"

i = 1
while True:
    try:
        if i == 10:
            raise ValueError("我的 异常")
    except Exception as e:
        print e.message
    finally:
        i = i + 1
