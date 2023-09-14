# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
     1
    232
   34543
  4567654
 567898765
 '''


rows = 5

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print(i + k + 1, end="")
    for l in range(i, 0, -1):
        print(i + l, end="")
    print()