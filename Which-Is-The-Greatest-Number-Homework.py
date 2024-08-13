# I did it myself, because I am cool now
# I just did it rn at 13/09/2024

import random

# Declares A, B and C
a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)

# Printing the variables
print(a, " ", b, " ", c, " ")

# Comparing the numbers
if a > b and a > c:
  print(a, 'is the greatest')
elif b > a and b > c:
  print(b, 'is the greatest')
elif c > a and c > b:
  print(c, 'is the greatest')
else:
  print('BUG FOUND, PLEASE FIX')
