import numpy as np
from Cat import Cat
import matplotlib.pyplot as plt
from Kitten import Kitten
from LazyCat import LazyCat
from MiddleCat import MiddleCat
from Mouse import Mouse
import random


def animalFromFile(filename):
    coordinates = []
    final = []
    with open(filename) as myfile:
        for line in myfile.readlines():
            xy = list(map(int, line.split()))
            coordinates.append(xy)

    for item in coordinates:
        for item2 in item:
            final.append(item2)
    return final


mice = [Mouse(animalFromFile("mysz.txt"), n) for n in range(0,3)]
middleCats = [MiddleCat(animalFromFile("middleCat.txt"), n) for n in range(0,4)]
lazyCats = [LazyCat(animalFromFile("leniuch.txt"), n) for n in range(0,4)]
kittens = [Kitten(animalFromFile("kociaki.txt"), n) for n in range(0,4)]


print(middleCats[1].x, middleCats[1].y)
print(lazyCats[1].x, middleCats[1].y)
print(kittens[1].x, kittens[1].y)
print(mice[1].x, mice[1].y)
print("--------------")

iterations = 0
while iterations < 600:
    for mouse in mice:
        mouse.move()
        for middleCat in middleCats:
            middleCat.mouseInteraction(mouse)
        for lazyCat in lazyCats:
            lazyCat.mouseInteraction(mouse)
        for kitten in kittens:
            kitten.mouseInteraction(mouse)
    for middleCat in middleCats:
        middleCat.move()
    for lazyCat in lazyCats:
        lazyCat.move()
    for kitten in kittens:
        kitten.move()
    
    iterations += 1


#print(middleCats[3].positionsX, middleCats[3].positionsY)


for middleCat in middleCats:
    plt.plot(middleCat.positionsX, middleCat.positionsY, 'r')

for mouse in mice:
    plt.plot(mouse.positionsX, mouse.positionsY, 'b')

for kitten in kittens:
    plt.plot(mouse.positionsX, mouse.positionsY, 'g')

for lazyCat in lazyCats:
    plt.plot(lazyCat.positionsX, lazyCat.positionsY, 'y')
    plt.plot(lazyCat.x0, lazyCat.y0, 'k.', label = "lazy")

plt.title('Garden')
plt.legend(title="Legend")
plt.show()


