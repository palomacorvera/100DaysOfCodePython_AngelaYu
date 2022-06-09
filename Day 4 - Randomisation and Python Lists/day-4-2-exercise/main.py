# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

array_len = len(names)

choice = random.randint(1, array_len)

print(f"{names[choice]} is going to pay the bill today!")
