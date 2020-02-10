import numpy as np
import random
from Cat import Cat

kitty = Cat("Abby")
kitty2 = Cat("Tabby")

def list_from_file(filename):
  """Returns a list of elements stored in the file in the given filepath."""
  elements = []
  with open(filename) as myfile:
    for line in myfile.read().splitlines():
      elements.append(line)
  return elements

toylist = list_from_file("toylist.txt") # import the toylist

N = 100
for i in range(N):
  toy = random.choice(toylist) # choose a random toy 
  choice = random.randint(0, 2) # and define a choice 
  choice2 = random.randint(0, 2) # for each cat
  if choice == 0 and choice2 == 0:
    result = kitty.fight(kitty2) # if both cats like the toy, they fight for it
    if result and toy not in kitty2.hoardedToys:
      kitty.hoard(toy)
    elif not result and toy not in kitty.hoardedToys:
      kitty2.hoard(toy)
  else:
    if choice == 0:
        kitty.like(toy)
    elif choice == 1:
        kitty.hate(toy)
    if choice2 == 0:
        kitty2.like(toy)
    elif choice2 == 1:
        kitty2.hate(toy)

kitty.greeting()
kitty.listLiked()
kitty.listHated()
kitty.listHoarded()
kitty2.greeting()
kitty2.listLiked()
kitty2.listHated()
kitty2.listHoarded()
