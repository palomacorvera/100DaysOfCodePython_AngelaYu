from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art
print(art.logo)

continues = True

dictionary = {}

while continues:
  key = input("Enter your name: ")
  value = input("Enter your amount: ")
  want_to_continue = input("Enter 'yes' if you want to continue or 'no' if you want to see the result: ")

  dictionary[key] = value
  
  if want_to_continue == 'no':
    continues = False

  clear()

highest_amount = 0

for key in dictionary:
  if int(dictionary[key]) > highest_amount:
    highest_amount = int(dictionary[key])
    highest_name = key

print(f"The winner is {highest_name} with {highest_amount}")