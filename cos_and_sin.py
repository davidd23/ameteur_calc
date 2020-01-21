import math

upper = input("Upper limit: ")
lower = input("Lower limit: ")

upper = float(upper)
lower= float(lower)

def cos_integrate(upper_bound, lower_bound):
  result = math.sin(upper_bound) - math.sin(lower_bound)
  return result

def sin_integrate(upper_bound, lower_bound):
  result = (-1 * math.cos(upper_bound)) - (-1 * math.cos(lower_bound))
  return result

option = input("sin or cos? ")
option = option.upper()

if option == "COS": 
  print(cos_integrate(upper, lower))
elif option == "SIN":
  print(sin_integrate(upper, lower))
