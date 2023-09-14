# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
A B C D E
A B C D
A B C
A B
A
'''
string = 'ABCDE'

for i in range(len(string)):
    for j in range(len(string)-i):
        print(string[j], end=' ')
    print()
