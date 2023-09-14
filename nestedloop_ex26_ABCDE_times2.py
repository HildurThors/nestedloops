# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''

ABCDEDCBA
ABCD DCBA
ABC   CBA
AB     BA
A       A
'''
string = 'ABCDE'

for i in range(len(string)):
    # Print the first part of the string
    for j in range(len(string)-i):
        print(string[j], end=' ')
    for k in range(i*2):
        print(' ', end=' ')
    for l in range(len(string)-1-i, -1, -1):
        print(string[l], end=' ')
    print()











