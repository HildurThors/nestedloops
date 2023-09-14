# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
     1
    12
   123
  1234
 12345
'''
1 / 2


n = 5  # number of rows

for i in range(1, n+1):
    # print spaces before the numbers
    for j in range(n-i):
        print(" ", end="")
    
    # print numbers
    for k in range(1, i+1):
        print(k, end="")
    
    # move to the next line

    # einnig hægt að gera k-ið svona:
    # for k in range(i, 0, -1):
    #     print(k, end='')
    print()