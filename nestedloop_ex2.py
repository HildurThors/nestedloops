# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
12345
1234
123
12
1
'''

for i in range(5,0,-1):
    for j in range(i):
        print(j+1, end='')
    print()