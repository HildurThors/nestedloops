# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
     *
    * *
   * * *
  * * * *
 * * * * *
'''
n = 5

for i in range(1, n+1):
    # print spaces before the numbers
    for j in range(n - i):
        print(" ", end="")
    # print the numbers for this row
    for k in range(i):
        print('*', end=" ")
    # print a new line after each row is complete
    print()

