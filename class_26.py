#coding=utf-8

def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b


def substract(a,b):
    print "Substracting %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "Multiply %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "Multiply %d / %d" % (a, b)
    return a / b


print "Let's do some match with just functions!"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age:%d, Height:%d, Weight:%d, Iq:%d" % (age, height, weight, iq)

print "Here is a puzzle"
what = add(age,substract(height,multiply(weight,divide(iq, 2))))

print "That become", what,"Can you do it by hand?"
