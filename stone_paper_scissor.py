#Stone Paper Scissors Game
#https://docs.python.org/3/library/random.html
import random
comp_choice = random.choice(['stone', 'paper', 'scissors'])
user_choice = input("Which one do you want to choose from 'stone', 'paper', 'scissors': \n")
print("Game Starts Now :\n")
print("Your Choice is " + user_choice)
print("Computer Choice is " + comp_choice)
if comp_choice == user_choice:
  print("TIE")
elif user_choice == 'stone' and comp_choice == 'scissors':
  print("YOU WIN")
elif user_choice == 'paper' and comp_choice == 'stone':
  print("YOU WIN")
elif user_choice == 'scissors' and comp_choice == 'paper':
  print("YOU WIN")
else:
  print("YOU LOSE :) ")