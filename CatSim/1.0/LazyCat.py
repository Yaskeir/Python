import random, math
from Cat import Cat

class LazyCat(Cat):
    def __init__(self, coordinates, n):
        super().__init__(coordinates, n)
        self.n = 0
        self.probability = 1/(1+math.exp(-0.1*n))
        self.laziness = random.uniform(0, 1)

    def mouseInteraction(self, mouse):
        distance = math.sqrt((self.x - mouse.x)**2 + (self.y - mouse.y)**2)
        if distance < 4:
            if self.probability > self.laziness:
                self.n += 1
                mouse.x = mouse.x0
                mouse.y = mouse.y0

    def move(self):
        self.step = random.randint(-10, 10)