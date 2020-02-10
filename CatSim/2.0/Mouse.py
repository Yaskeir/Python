import random
from Animal import Animal

class Mouse(Animal):
    def __init__(self, coordinates, n):
        super().__init__(coordinates, n)

    def move(self):
        if self.x >= 500 or self.x <= 0 or self.y >= 500 or self.y <= 0:
            self.x = self.positionsX[-1]
            self.y = self.positionsY[-1]
        self.stepx = random.randint(-1, 1)
        self.stepy = random.randint(-1, 1)
        self.positionsX.append(self.x)
        self.positionsY.append(self.y)
        self.x += self.stepx
        self.y += self.stepy