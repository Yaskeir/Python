import random
from Animal import Animal

class Mouse(Animal):
    def __init__(self, coordinates, n):
        super().__init__(coordinates, n)

    def move(self):
        self.step = random.randint(-1, 1)