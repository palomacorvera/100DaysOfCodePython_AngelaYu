import art
import game_data
import random

continue_playing = True

def get_random_option():
  return game_data.data[random.randint(0, len(game_data.data) - 1)]

def get_correct_answer(option_a, option_b):
  if option_a['follower_count'] > option_b['follower_count']:
    return 'A'
  else:
    return 'B'

score = 0
  
while continue_playing:
  print(art.logo)
  
  option_a = get_random_option()
  option_b = get_random_option()

  while option_a == option_b:
    option_b = get_random_option()

  correct_answer = get_correct_answer(option_a, option_b)

  print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
  print(art.vs)
  print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")
  answer = input("Who has more followers? Type 'A' or 'B': ").upper()

  if answer == correct_answer:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    continue_playing = False 
    print(f"Sorry, that's wrong. Final score: {score}")
  