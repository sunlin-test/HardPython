# coding=utf-8


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# 将参数指向10
print "Or we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 将计算结果的值传递给函数参数
print "We can do math inside too:"
cheese_and_crackers(20 + 10, 5 + 10)

# 将计算结果的值传递给函数参数
print "We can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 22, amount_of_crackers + 1)



