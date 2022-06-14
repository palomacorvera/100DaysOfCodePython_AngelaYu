#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number betweeen 1 al 100.")
difficulty = input("Choose a dificulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
  num_attempts = 10
else:
  num_attempts = 5

number = random.randint(1, 101)

def check_number(attempts, guess):
  if guess > number:
    print("Too high")
    attempts -= 1
    if attempts == 0:
      print(f"No attempts remaining. You lose. The answer was {number}")
    return attempts
  elif guess < number:
    print("Too low")
    attempts -= 1
    if attempts == 0:
      print(f"No attempts remaining. You lose. The answer was {number}")
    return attempts
  else:
    print(f"You got it! The answer was {number}")
    attempts = 0
    return attempts

while num_attempts > 0:
  print(f"You have {num_attempts} remaining to guess the number.")
  guess = int(input("Make a guess: "))
  num_attempts = check_number(num_attempts, guess)