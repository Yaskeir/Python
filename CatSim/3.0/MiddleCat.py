# Joanna Buczkowska, Mateusz Fido

from Cat import Cat
import random, math

class MiddleCat(Cat):

    '''The regular type of Cat. Taps the encountered mouse with its paw and sends
    it back home.'''

    def __init__(self, coordinates, n):
        super().__init__(coordinates, n)
        

    def mouseInteraction(self, mouse):
        distance = math.sqrt((self.x - mouse.x)**2 + (self.y - mouse.y)**2)
        if distance < 40:
            mouse.x = mouse.x0
            mouse.y = mouse.y0

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