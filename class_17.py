# coding=utf-8

from sys import argv

script, filename = argv

print "We are going to erase %s." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")


print "Opening the file ..."
target = open(filename, "w+")

print "Truncate the file.Goodbye!"
target.truncate()

print "Now I'm ask you to three lines."
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.writelines(line1)
# target.writelines([line1,'\n', line2,'\n', line3])
# target.write("%s\n%s\n%s" % (line1,line2,line3))

print "And finally, we close it."
target.close()