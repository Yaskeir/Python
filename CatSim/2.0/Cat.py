import random, math
from Animal import Animal

class Cat(Animal):
    def __init__(self, coordinates, n):
        super().__init__(coordinates, n)

    def mouseInteraction(self, mouse):
        pass