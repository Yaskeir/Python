import numpy as np
import random

class Cat:
  """Class representing a cat."""
  def __init__(self, name):
    self.name = name
    self.favoriteToys = set()
    self.hatedToys = set()
    self.hoardedToys = set() 
    self.resolve = np.random.rand()

  def greeting(self):
    print("Hello, my name is {}!".format(self.name))

  def like(self, toy):
    if toy in self.hatedToys:
      self.hatedToys.remove(toy)
    self.favoriteToys.add(toy)
  
  def hate(self, toy):
    if toy in self.favoriteToys:
      self.hatedToys.add(toy)
      self.favoriteToys.remove(toy)

  def listLiked(self):
    counter = 0
    print("I like", end = " ")
    for i in self.favoriteToys:
      print(i, end = ", ")
      counter += 1
    print("there's {} of them.".format(counter))

  def listHated(self):
    counter = 0
    print("I dislike", end = " ")
    for i in self.hatedToys:
      print(i, end = ", ")
      counter += 1
    print("there's {} of them.".format(counter))

  def listHoarded(self):
    counter = 0
    print("I won over for myself", end = " ")
    for i in self.hoardedToys:
      print(i, end = ", ")
      counter += 1
    print("there's {} of them.".format(counter))
  
  def fight(self, hostileCat):
    '''Method called whenever there's a conflict between two cats over a toy.
    Test the randomly generated resolve of both cats. The one with the greater
    resolve takes the toy home. Generate new resolve for each cat, with the
    loser gaining a 15 percentage point boost for the next encounter.'''
    if self.resolve > hostileCat.resolve:
      self.resolve = np.random.rand()
      hostileCat.resolve = np.random.rand() + 0.15
      return True
    else:
      self.resolve = np.random.rand() + 0.15
      hostileCat.resolve = np.random.rand()
      return False

  def hoard(self, toy):
    self.hoardedToys.add(toy)

# Testing the class
if __name__ == "__main__": # current interpreted file
  Cat = Cat("Maurycy")
  Cat.like("Mouse")
  Cat.like("Rat")
  Cat.listLiked()
  Cat.hate("Rat")
  Cat.listHated()