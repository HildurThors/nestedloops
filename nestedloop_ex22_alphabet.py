# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''
A
B C
D E F
G H I  J
K L M N O
P Q R  S T U
V W X Y Z A B
C D  E F G H I J
'''

current_letter = "A"

for i in range(1, 9):
    for j in range(i):
        print(current_letter, end=" ")
        current_letter = chr(ord(current_letter) + 1)
        if current_letter > "Z":
            current_letter = "A"
    print()
