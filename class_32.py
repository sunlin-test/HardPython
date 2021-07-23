# coding=utf8

def create_list(max_element, step):
    i = 0
    numbers = []
    while i < max_element:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + step
        print "numbers now is ", numbers
        print "At the bottom i is %d" % i

    print "The numbers is:"

    for num in numbers:
        print num


def create_list2(max_element, step):
    numbers = []
    for i in range(0, max_element, step):
        print "At the top i is %d" % i
        numbers.append(i)
        print "numbers now is ", numbers
        print "At the bottom i is %d" % i

    print "The numbers is:"

    for num in numbers:
        print num


def create_odd_list(max_element):
    """
    find odd element between 0 and max_element,not include max_element
    :param max_element:
    :return:list
    """
    numbers = []
    for i in range(0, max_element):
        if i % 2 == 0:
            continue
        numbers.append(i)
        print "current number is ", i

    print "The odd numbers in 0 - %d is:" % max_element

    for num in numbers:
        print num

    return numbers




if __name__ == "__main__":
    # create_list(8, 2)
    # create_list2(8, 2)
    create_odd_list(10)