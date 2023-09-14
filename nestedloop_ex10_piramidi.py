# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
Píramídi

     1
    121
   12321
  1234321
 123454321
'''
n = 5   # number of rows in the pattern
for i in range(1, n+1):
    # print spaces before the numbers
    for j in range(n-i):
        print(" ", end="")
    # print numbers in ascending order
    for j in range(1, i+1):
        print(j, end="")
    # print numbers in descending order
    for j in range(i-1, 0, -1):
        print(j, end="")
    print()  # move to the next line
