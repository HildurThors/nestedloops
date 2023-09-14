#https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
'''

n = 5

# Outer loop for each row
for i in range(n):
    # Print spaces before the stars
    for j in range(i):
        print(" ", end="")
    # Print the stars for the row
    for k in range(n-i):
        print("*", end=" ")
    # Move to the next line
    print()

for i in range(2, n+1):
    # print spaces before the numbers
    for j in range(n - i):
        print(" ", end="")
    # print the numbers for this row
    for k in range(i):
        print('*', end=" ")
    # print a new line after each row is complete
    print()
