# Joanna Buczkowska, Mateusz Fido

import random, math
from Cat import Cat

class BigCat(Cat):

    '''The BigCat subclass defines a mouseInteraction() method, whereupon finding a mouse
    they set its "alive" property to False. That mouse's movement is no longer visible after
    the simulation ends.'''

    def __init__(self, coordinates, n):
        super().__init__(coordinates, n)

    def mouseInteraction(self, mouse):
        distance = math.sqrt((self.x - mouse.x)**2 + (self.y - mouse.y)**2)
        if distance < 10:
            mouse.alive = False

    def move(self):
        if self.x >= 500 or self.x <= 0 or self.y >= 500 or self.y <= 0:
            self.x = self.positionsX[-1]
            self.y = self.positionsY[-1]
        else:
            self.stepx = random.randint(-10, 10)
            self.stepy = random.randint(-10, 10)
            self.positionsX.append(self.x)
            self.positionsY.append(self.y)
            self.x += self.stepx
            self.y += self.stepy