# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
 12345
  1234
   123
    12
     1
'''

for i in range(1, 6):
    print(' ' * (i-1), end='')
    for j in range(6-i):
        print(j+1, end='')
    print()

'''................eða...........'''

n = 5  # number of rows
for i in range(n):
    # print spaces before numbers
    print(" " * i, end="")
    # print numbers
    for j in range(n-i):
        print(j+1, end="")
    print()  # move to next line