# Declares A and B and C variables
a = int(input('Enter your first number\n'))
b = int(input('\nEnter your second number\n'))
c = input('\nEnter your operator\nAddition\nSubtraction\nMultiplication\nFloor Devision\nExponent\nModulo\nDivision\n\n').lower()

# The Question Answers
if c == '+' or c == 'addition':
  print(a + b)
elif c == '/' or c == 'division':
  print(a / b)
elif c == '-' or c =='subtraction':
  print(a - b)
elif c == '*' or c == 'x' or c == 'multiplication':
  print(a * b)
elif c == '**' or c == 'exponent':
  print( a ** b)
elif c == '//' or c == 'floor devision':
  print(a // b)
elif c == '%' or c == 'modulo':
  print(a % b)
else:
  print('That is not an option\nPlease restart and choose a valid option')
