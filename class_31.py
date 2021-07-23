# coding=utf8

i = 0
numbers = []
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    i = i + 1
    print "numbers now is ", numbers
    print "At the bottom i is %d" % i

print "The numbers is:"

for num in numbers:
    print num
