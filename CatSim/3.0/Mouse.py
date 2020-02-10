# Joanna Buczkowska, Mateusz Fido
#

import random
from Animal import Animal

class Mouse(Animal):
    
    '''The Mouse subclass extends Animal. It defines its own move() method, which will be similar
    for every other Animal. It provides upper and lower bounds for movement (which are the 
    garden's size, 500x500) and defines a random step of 1 in each direction (or none).'''

    def __init__(self, coordinates, n):
        super().__init__(coordinates, n)
        self.alive = True

    def move(self):
        if self.x >= 500 or self.x <= 0 or self.y >= 500 or self.y <= 0:
            self.x = self.positionsX[-1]
            self.y = self.positionsY[-1]
        else:
            self.stepx = random.randint(-1, 1)
            self.stepy = random.randint(-1, 1)
            self.positionsX.append(self.x)
            self.positionsY.append(self.y)
            self.x += self.stepx
            self.y += self.stepy
