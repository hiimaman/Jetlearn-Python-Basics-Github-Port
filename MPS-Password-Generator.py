# MPS Means My Personal Project
# This Will Generate You A Password For ANYTHING!

import random

# Variable Lists
let = ('abcdefghijklmnopqrstuvwxyz')
num = ('12345678910')

# Variables-Normal
l1 = random.sample(let, 5)
l2 = random.sample(let, 5)
num1 = random.sample(num, 3)

# Password Variables
password = ''.join(l1 + num1 + l2)

# Printing the thing
print('your password is: ', password)
