"""this code is the 'Rock, Paper, Scissors' game,
will take user input and compare to computer's choice to determine a winer"""

from random import randint
from time import sleep

OPTIONS = ["R", "P", "S"]
LOST = "You lost!"
WIN = "You WIN!"

def decide_winer(user_choice, computer_choice):
  print("User's choice is: %s" % user_choice)
  print("")
  print("Computer selecting...")
  sleep(1)
  print("")
  print("Computer's choice is: %s" % computer_choice)
  
  user_choice_index = OPTIONS.index(user_choice)
  computer_choice_index = OPTIONS.index(computer_choice)
  
  if user_choice_index == computer_choice_index:
    print("You are tie!")
    return
  elif user_choice_index == 0 and computer_choice_index == 2:
    print("You have WON this round!")
    return
  elif user_choice_index == 1 and computer_choice_index == 0:
    print("You have WON this round!")
    return
  elif user_choice_index == 2 and computer_choice_index == 1:
    print("You have WON this round!")
    return
  elif user_choice_index > 2:
    print("You have selected invalid option")
    return
  else:
    print("You have lost this round!")
    return

def play_RPS():
  print("-== THE GAME HAS STARTED ==-")
  user_choice = (input("Select R for Rock, P for Paper, or S for Scissors: ")).upper()
  sleep(1)
  computer_choice = OPTIONS[randint(0, len(OPTIONS) - 1)]
  
  #calling the main function to decide winer
  decide_winer(user_choice, computer_choice)
                             
play_RPS()
