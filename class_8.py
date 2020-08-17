# coding=utf-8

days = "Mon Tue Wed Thr Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\Aug"
print "Here are the days:", days
print "Here are the months:", months

print """
There's someting going on here.
with the three double-quotes.
We'll be able to type as much as we like.
# Even 4 lines if we want, or 5, or 6.
"""
# """  """ 表示多行字符串，可直接用作注释
# ""  ''必须成对
print "I \"understand\" joe"
print "I 'understand' joe"

print "I am 6'2\" tall "
print 'I am 6\'2" tall'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\a \\cat."
fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Glass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print r'I am \t a cat'
print 'I am \t a cat'

myself = r'I am \t a 猫'
print myself

