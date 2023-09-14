# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
outcome:
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
'''

str = 'ABCDE'

for i in range(len(str)):
    for j in range(len(str)-i-1):
        print(' ', end='')
    for k in range(i+1):
        print(str[k], end='')
    for l in range(i-1, -1, -1):
        print(str[l], end='')
    print('')
