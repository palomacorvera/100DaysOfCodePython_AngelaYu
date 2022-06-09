# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

leap = False

if year % 4 == 0:
  leap = True
  if year % 100 == 0:
    leap = False
    if year % 400 == 0:
      leap = True
    else:
      leap = False
  else:
    leap = True
else:
  leap = False

if leap:
  print(f"{year} is leap!")
else:
  print(f"{year} is not leap")