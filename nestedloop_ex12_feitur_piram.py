# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
          0
        1 0 1
      2 1 0 1 2
    3 2 1 0 1 2 3
  4 3 2 1 0 1 2 3 4
5 4 3 2 1 0 1 2 3 4 5
'''

# ..............Nested loop....................

rows = 6

for i in range(rows):
    for j in range(rows - i - 1):
        print("  ", end="")
    for k in range(i + 1):
        print(str(i - k) + " ", end="")
    for l in range(1, i + 1):
        print(str(l) + " ", end="")
    print()

'''------Önnur leið------------'''
rows = 6
for i in range(rows):
    for j in range(rows - i - 1):
        print("  ", end="")
    for k in range(i + 1):
        if k == 0:
            print(str(i) + " ", end="")
        else:
            print(str(i - k) + " ", end="")
    for l in range(1, i + 1):
        print(str(l) + " ", end="")
    print()