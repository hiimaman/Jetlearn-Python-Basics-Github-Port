# Minha Made Me Make A More Detailed Thing On Data Structures
# Here Is The Lists Work

# Lists Serious
fruits = ['apple', 'orange', 'plum', 'grape']
print(fruits)
# Counts The Total Amount Of Values
print(len(fruits))
# Prints Index 1 (Orange)
print(fruits[1])
# Prints Index 2 (Plum)
print(fruits[2])
# Removes Grape
fruits.remove('grape')
print(fruits)
# Adds Banana
fruits.append('banana')
print(fruits)
# Adds Pear
fruits.append('pear')
print(fruits)
# Overwrites Fruit 2 With Grapes
fruits[2] = 'grapes'
print(fruits)
# Removes Index 0
print(fruits.pop(0))
print(fruits)
# Counts The Instances Of A Value Appearing
print(fruits.count('orange'))
# Print All The Values
for i in fruits:
  print(i)

# Print All The Index Values
for i in range(len(fruits)):
  print(i, fruits[i])
