# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
1
12
123
1234
12345
'''

for i in range(5+1):
    
    for j in range(i):
        print(j+1, end='')
    print()