#dice Game between 2 players
import random
def roll_dice():
  total_dice = random.randint(1, 6) + random.randint(1,  6)
  return total_dice

def main():
  player1 = input("Enter player 1's name : \n")
  player2 = input("Enter player 2's name : \n")

  roll1 = roll_dice()
  roll2 = roll_dice()
  print(player1,"rolled", roll1)
  print(player2,"rolled", roll2)

  if roll1 > roll2:
    print("Player",player1,"WINS!")
  elif roll2 > roll1:
    print("Player",player2,"WINS!")
  else:
    print("TIE")

main()