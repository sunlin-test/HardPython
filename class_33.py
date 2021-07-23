# coding=utf8

# 对比赛排名解析：
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
name_numbers = [2, 3, 1, 0, 2, 4, 3]

ordinal = []
for i in name_numbers:
    if i == 0:
        ordinal.append(str(i + 1) + 'st')
    elif i == 1:
        ordinal.append(str(i + 1) + 'nd')
    elif i == 2:
        ordinal.append(str(i + 1) + 'rd')
    else:
        ordinal.append(str(i + 1) + 'th')

print ordinal
# The 1st animal is at 0 and is a bear.
for i in range(0,len(name_numbers)):
    print "The %s animal is at %d and is a %s" % (ordinal[i], name_numbers[i], animals[name_numbers[i]])

print '\nTurn Around: \n'

# The animal at 0 is the 1st animal and is a bear.
for i in range(0,len(name_numbers)):
    print "The animal at %d is the %s and is a %s" % (name_numbers[i], ordinal[i], animals[name_numbers[i]])


