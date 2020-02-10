# Joanna Buczkowska, Mateusz Fido

import random, math
from Cat import Cat

class LazyCat(Cat):
    
    '''The LazyCat subclass, defines own mouse encounters counter, as well as 
       a probability function for evaluating the behaviour during next mouse
       encounter. If close to a mouse, either ignores it or taps it with its paw 
       and sends it back home, depending on the probability property and random chance.'''

    def __init__(self, coordinates, n):
        super().__init__(coordinates, n)
        self.count = 0
        self.probability = 1/(1+math.exp(-0.1*self.count))
        self.laziness = random.uniform(0, 1)

    def mouseInteraction(self, mouse):
        distance = math.sqrt((self.x - mouse.x)**2 + (self.y - mouse.y)**2)
        if distance < 40:
            if self.probability > self.laziness:
                self.count += 1
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