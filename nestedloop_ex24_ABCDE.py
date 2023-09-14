# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
outcome:
A
A B
A B C
A B C D
A B C D E
'''

string = 'ABCDE'

for i in range(len(string)):
    for j in range(i+1):
        print(string[j], end=' ')
    print()
