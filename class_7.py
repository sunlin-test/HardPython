# coding=utf-8

formatter = "%s %s %s %s"
print formatter % (1, 2, 3, 4)
print formatter % ("One", "Two", "Three", "Four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
months = "\nJan\nFeb\nMar"
print "Here are the months %r" % months
print "Here are the months %s" % months
year = repr("\n")
time = str("\n")
# repr()显示计算机处理前的对象   str()显示计算机处理后的对象?
print "repr("") results is :%r " % year
print "str() result is :%s" % time