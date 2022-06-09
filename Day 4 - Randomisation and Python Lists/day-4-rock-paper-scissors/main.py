rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

images = [rock, paper, scissors]

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

random_choice = random.randint(0,2)

if users_choice == random_choice:
  winner = "Draw!"
elif ((users_choice == 0) and (random_choice == 1)) or ((users_choice == 1) and (random_choice == 2)) or ((users_choice == 2) and (random_choice == 0)):
  winner = "You lose"
else:
  winner = "You win!"

print(f"{images[users_choice]}\nComputer chooses:\n{images[random_choice]}\n{winner}")