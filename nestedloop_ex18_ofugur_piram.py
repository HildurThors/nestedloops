# https://www.ankitweblogic.com/c/exerciseonnestedloop.php

'''

 * * * * *
  * * * *
   * * *
    * *
     *
'''

n = 5

# Outer loop for each row
for i in range(n):
    # Print spaces before the stars
    for j in range(i):
        print(" ", end="")
    # Print the stars for the row
    for k in range(n-i):
        print("*", end=" ")
    # Move to the next line
    print()