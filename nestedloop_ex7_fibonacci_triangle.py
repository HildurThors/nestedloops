# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
Fibonacci Triangle

1
1 1
1 1 2
1 1 2 3
'''
n = 4  # number of rows in the triangle
a, b = 1, 1  # initialize the first two numbers in the sequence
print(a)  # print the first row of the triangle
print(a, b)  # print the second row of the triangle

# generate and print the remaining rows of the triangle
for i in range(3, n+1):
    print(a, end=' ')  # print the first number in the row
    for j in range(1, i-1):
        c = a + b  # calculate the next number in the sequence
        print(c, end=' ')
        a, b = b, c  # update the sequence
    c = a + b  # calculate the last number in the row
    print(c)  # print the last number in the row
    a, b = 1, 1  # reset the sequence for the next row