# MPS Means My Personal Project
# The 8 Ball Never Lies!

import random

# Variables
questions = str(input('What is your question about your future? '))
options = ('yes', 'no')

# Random Variables
answer = random.sample(options, 1)

# Print it
print(answer)
