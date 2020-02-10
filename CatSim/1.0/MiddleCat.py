from Cat import Cat
import random, math

class MiddleCat(Cat):
    def __init__(self, coordinates, n):
        super().__init__(coordinates, n)
        

    def mouseInteraction(self, mouse):
        distance = math.sqrt((self.x - mouse.x)**2 + (self.y - mouse.y)**2)
        if distance < 4:
            mouse.x = mouse.x0
            mouse.y = mouse.y0

    def move(self):
        self.step = random.randint(-10, 10)
        self.positionsX.append(self.x)
        self.positionsY.append(self.y)
        self.x += self.step
        self.y += self.step