# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
*
* *
* * *
* * * *
* * * * *
'''
n = 5

for i in range(1,n+1):
    for j in range(i):
        print('*', end='')
    print()
