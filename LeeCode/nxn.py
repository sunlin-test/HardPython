# coding=utf-8

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    a = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            a[j][n - 1 - i] = matrix[i][j]
        print "第%d行旋转结束" % (i)

    matrix[:] = a

    return matrix


list = [[1,2,3],[4,5,6],[7,8,9]]
list = rotate(list)
print list

def rotate2(matrix):
    n = len(matrix)
    if n%2==0:
        k = n/2
    else:
        k = n/2+1
    for i in range(n/2):
        print i,k
        for j in range(k):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][n-i-1]
            matrix[j][n-i-1] = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
            matrix[j][n-i-1] = tmp

    return matrix

list2 = [[1,2,3],[4,5,6],[7,8,9]]
list2 = rotate2(list2)
print list2





