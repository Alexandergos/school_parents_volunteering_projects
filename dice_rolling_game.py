"""This code rolls a pair of dice and asks user to 
guess, than it determines a winner"""

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(input("Guess a number: "))
  return user_guess

def roll_dice(number_of_sides=6):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("Maximum possible value is " + str(max_val))
  sleep(1)
  user_guess = get_user_guess() 
  if user_guess > max_val:
    print("Your guess is bigger than maximum possible dice value")
    return
  else:
    print("Rolling.."); sleep(2)
    print("first roll is %d" % first_roll); sleep(1)
    print("second roll is %d" % second_roll); sleep(1)
    total_roll = first_roll + second_roll
    print("total roll is %d" % total_roll)
    print("Result..."); sleep(1)
    if user_guess > total_roll:
      print("You're WON tis round!!!")
      return
    else:
      print("You've missed this one. Try again!")
      return
    
roll_dice()
