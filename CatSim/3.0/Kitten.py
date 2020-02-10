# Joanna Buczkowska, Mateusz Fido

from Cat import Cat
import math, random
class Kitten(Cat):

    '''The Kitten subclass defines a small cat which reacts to a mouse encounter based on
    the distance to its own home. If the distance is small, it defends its home and sends
    the mouse back to their home. If instead it encounters the mouse further from its own 
    home, or if it strays too far from their own home, they teleport back to the starting
    location.'''

    def __init__(self, coordinates, n):
        super().__init__(coordinates, n)
        self.home_distance = math.sqrt((self.x - self.x0)**2 + (self.y - self.y0)**2)
        self.home_mouse_distance = None
        
    def mouseInteraction(self, mouse):
        distance = math.sqrt((self.x - mouse.x)**2 + (self.y - mouse.y)**2)
        if distance < 40:
            self.home_mouse_distance = math.sqrt((mouse.x-self.x0)**2+(mouse.y-self.y0)**2)
            if self.home_mouse_distance < 50:
                mouse.x = mouse.x0
                mouse.y = mouse.y0
            else:
                self.x = self.x0
                self.y = self.y0

    def move(self):
        if self.x >= 500 or self.x <= 0 or self.y >= 500 or self.y <= 0:
            self.x = self.positionsX[-1]
            self.y = self.positionsY[-1]
        elif self.home_distance > 50:
            self.x = self.positionsX[-1]
            self.y = self.positionsY[-1]
        else:
            self.stepx = random.randint(-5, 5)
            self.stepy = random.randint(-5, 5)
            self.positionsX.append(self.x)
            self.positionsY.append(self.y)
            self.x += self.stepx
            self.y += self.stepy