import math # For sqrt

# a b
# ===
# 1 1
# 1 2 < - DUPLICATES
# 1 3
# ...
# 2 1 < - DUPLICATES
# 2 2
# We want to avoid the duplicates.
# I can't assign the inner range as range(1, 25), 
    #  but if I assign it as range(a, 25), then we are avoiding this problem

# NOTE: This is a HARD problem, no worries if you don't fully understand

for a in range(1,25):
    for b in range(a, 25): # we use this range to avoid duplicate prints
        c = math.sqrt(a**2 + b**2)
        # 4.5 % 1 -> 0.5 😥
        # 4.0 % 1 -> 0.0 😎
        if c % 1 == 0:
            print(a, b)
