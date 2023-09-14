# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''

     1
    2 2
   3 3 3
  4 4 4 4
 5 5 5 5 5
 '''

rows = 5

for i in range(1, rows+1):
    # print spaces before the numbers
    for j in range(rows - i):
        print(" ", end="")
    # print the numbers for this row
    for k in range(i):
        print(i, end=" ")
    # print a new line after each row is complete
    print()

# ---------ÖNNUR TEGUND af píramída----------------
'''
    1
   222
  33333
 4444444
555555555
'''
rows = 5
for i in range(1, rows+1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(1, 2*i):
        print(i, end="")
    print()


rows = 5

for i in range(1, rows+1):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(i):
        print(i, end="")
    for l in range(i-1, 0, -1):
        print(i, end="")
    print()