# Minha doesn't approve

a = int(input("What is your first number? "))
b = int(input("What is your second number? "))

def add(a, b):
  print('the result is', a + b)

def sub(a, b):
  print('the result is', a - b)

def mul(a, b):
  print('the result is', a * b)

def div(a, b):
  print('the result is', a / b)

def exp(a, b):
  print('the result is', a**b)

def flo(a, b):
  print('the result is', a // b)

c = input("Choose an operator ")
if c == "+":
  add(a, b)
if c == "-":
  sub(a, b)
if c == "*":
  mul(a, b)
if c == "/":
  div(a, b)
if c == "/":
  div(a, b)
if c == "**":
  exp(a, b)
if c == "%":
  mod(a, b)
if c == "//":
  flo(a, b)  
  
