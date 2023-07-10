import random
comp_roll = random.randint(1,6)
user_roll = int(input("Guess the Dice Roll:\n"))
if user_roll == comp_roll:
  print("Your guess is correct and they rolled " + str(comp_roll))
else:
  print("Your guess is wrong. They rolled " + str(comp_roll))