# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

for i in range(5+1):
    for j in range(i):
        print(j+1, end='')

    print()

for i in range(5, 0, -1):
    for j in range(i-1):
        print(j+1, end='')
    print()