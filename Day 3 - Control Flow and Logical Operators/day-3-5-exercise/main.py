# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = name1 + name2

first_digit = 0;
second_digit = 0;

first_digit += names.lower().count("t");
first_digit += names.lower().count("r");
first_digit += names.lower().count("u");
first_digit += names.lower().count("e");

second_digit += names.lower().count("l");
second_digit += names.lower().count("o");
second_digit += names.lower().count("v");
second_digit += names.lower().count("e");

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}")