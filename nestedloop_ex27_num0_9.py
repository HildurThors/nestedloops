
# KÓÐINN ER EKKI RÉTTUR

for i in range(5):
    for j in range(4):
        num = i * 2 + j + 1
        if num > 10:
            num -= 10
        print(num, end="")
    print()


