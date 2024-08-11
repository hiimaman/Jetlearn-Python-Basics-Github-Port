# ChatGPT made it my skill level this time! (Minha only didnt beleive the list thing)
import random

# A 'list' of choices
choices = ["rock", "paper", "scissors"]

# .lower() makes things lowercase
user = input("rock, paper, or scissors? ").lower()
# random.choice() chooses a random choice from a list
computer = random.choice(choices)

# Using or \ to store multiple things in one elif
if user == computer:
    print("Tie!")
elif (user == "rock" and computer == "scissors") or \
    (user == "paper" and computer == "rock") or \
    (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")

# Curly brackets to reference a variable
print(f"Computer chose: {computer}")
