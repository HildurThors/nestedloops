# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
* * * * *
* * * *
* * *
* *
*
'''

n = 5

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print('*', end='')
    print()