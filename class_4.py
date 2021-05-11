# coding=utf-8

my_name = "Zed A. Shaw"
my_age = 35 # not a lie
my_height = 74 # inche
my_weight = 180 # lbs
my_eyes = "Blue"
my_teech = "White"
my_hair = "Brown"

print "Let's talk about %s." % my_name
print "He's %s inches tall." % my_height
print "He's %s pounds heavy." % my_weight
print "Actually that's not too heavy."
print "His teeth usually %s depending on the coffee." % my_teech
print "If I add %d, %d, and %d, I get %d." % (my_age, my_height, my_weight,my_age + my_height + my_weight)

# 指定浮点数小数位数
print "His height is %.2f inches tall." % (1.843)
# 指定占位符宽度
print "Name:%15s, Height:%8.2f, Weight:%8d." % (my_name, my_height, my_weight)
# 指定占位符宽度(左对齐)
print "Name:%-15s, Height:%-8.2f, Weight:%-8d." % (my_name, my_height, my_weight)
# 指定占位符宽度且使用0占位
print "Name:%-15s, Height:%08.2f, Weight:%08d." % (my_name, my_height, my_weight)

# %r输入
print "Name:%15s, Height:%r, Weight:%8r." % (my_name, my_height, my_weight)

# 将英寸和磅转换成厘米和千克
# 英寸->厘米
inch = input("英寸->厘米：")
cm = 2.54 * inch
print "%r英寸 = %.2f厘米" % (inch,cm)