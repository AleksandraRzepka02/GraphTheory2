#! /usr/bin/env python3

#Aleksandra Rzepka
#Calculate the square root of a number

def sqrt(x):
  """
  Calculate the square root of argument x.
  """
  #Check that x is positive.
  if x < 0:
   print("Error: negative value supplied")
   return -1
  else:
   print("Here we go...")

  #Initial guess for the square root.
  z = x / 2.0

  #Continously improve the guess.
  while abs(x - (z*z)) > 0.000001:
   z = z - (((z * z) - x) / (2 * z))

  return z

myval = 63.0

print("The square root of", myval, " is ", sqrt(myval)) 
