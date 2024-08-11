# I worked my ass of making this

# Guessing Game
# Import
import random

# X and Y
x = random.randint(1, 100)
y = random.randint(1, 10)

# A and B
a = random.randint(500, 1000)
b = random.randint(100, 400)

# User Input
ans = 0
gc = 0
t = 3
while(ans != x//y and gc != 4):
  print('if x =', x, 'y = ', y,)
  ans = int(input('What would be the quotient if x was divided by y? [Input as an integer]\n'))
  if ans == x//y:
    print('good job, you guessed correctly.')
  else:
    print('try again, you have {} tries left'.format(t))
    t -= 1
    gc += 1
if gc == 4:
  print('Game Over!')
print('Next Question.')
ans2 = 0
gc2 = 0
t2 = 3
while(ans2 != a//b and gc2 != 4):
  print('if a =', a, 'b =', b)
  ans2 = int(input('What is a divided by b? [input as an integer]\n'))
  if ans2 == a//b:
    print('good job, you guessed correctly.')
  else:
    print('try again, you have {} tries left'.format(t2))
    t2 -= 1
    gc2 += 1
if gc2 == 4:
  print('Game Over!')


# Check the answers of X and Y
