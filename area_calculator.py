"""This code compute the area of a given shape, as selected 
by the user.
Pyhton 3.6.1"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
hint = "Don't forget to include the correct units! \nExiting..."
print("Calculator is starting up.")
print("%s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute))

sleep(1)

hint = "Don't forget to include the correct units! \nExiting..."

option = input("Enter C for Circle and T for Triangle: ").upper()

if option == "C":
  radius = float(input("Enter radius of a circle: "))
  # area of a circle formula = pi * (radius ** 2)
  area = pi * (radius ** 2)
  print("The pie is baking...")
  sleep(1)
  print(round(area, 2)); print(hint)
elif option == "T":
  base = float(input("Enter base of triangle: "))
  heigh = float(input("Enter heigh of triangle: "))
  # area of triangle formula = (heigh * base) / 2
  area = heigh * base / 2
  print("Uni Bi Tri...")
  sleep(1)
  print(round(area, 2)); print (hint)
else:
  print("Looks like you've entered some garbage. Program will close now..")
