import numpy as np
from Cat import Cat
from Kitten import Kitten
from LazyCat import LazyCat
from MiddleCat import MiddleCat
from Mouse import Mouse
import random
import matplotlib.pyplot as plt


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


mice = [Mouse(animalFromFile("mysz.txt"), n) for n in range(0,8)]
middleCats = [MiddleCat(animalFromFile("middleCat.txt"), n) for n in range(0,8)]
lazyCats = [LazyCat(animalFromFile("leniuch.txt"), n) for n in range(0,8)]
kittens = [Kitten(animalFromFile("kociaki.txt"), n) for n in range(0,8)]


print(middleCats[3].x, middleCats[3].y)
print(lazyCats[3].x, middleCats[3].y)
print(kittens[3].x, kittens[3].y)
print(mice[3].x, mice[3].y)
print("--------------")

iterations = 0
while iterations < 199:
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


print(middleCats[3].positionsX, middleCats[3].positionsY)




'''
print(middleCats[3].x, middleCats[3].y)
print(lazyCats[3].x, middleCats[3].y)
print(kittens[3].x, kittens[3].y)
print(mice[3].x, mice[3].y)
'''
'''
middleCatsx = []
middleCatsy = []
for middleCat in middleCats:
    middleCatsx.append(middleCat.positionsX)
    middleCatsy.append(middleCat.positionsY)
plt.plot(middleCatsx, middleCatsy, 'r.')

mousex = []
mousey = []
for mouse in mice:
    mousex.append(mouse.positionsX)
    mousey.append(mouse.positionsY)
       
plt.plot(mousex, mousey, 'b.')

kittenx = []
kitteny = []
for kitten in kittens:
    kittenx.append(kitten.positionsX)
    kitteny.append(kitten.positionsY)

plt.plot(kittenx, kitteny, 'g.')


lazyCatsx = []
lazyCatsy = []
lazyCatsx0 = []
lazyCatsy0 = []
for lazyCat in lazyCats:
    lazyCatsx.append(lazyCat.positionsX)
    lazyCatsy.append(lazyCat.positionsY)
    lazyCatsx0.append(lazyCat.x0)
    lazyCatsy0.append(lazyCat.y0)
    
plt.plot(lazyCatsx, lazyCatsy, 'y.')
plt.plot(lazyCatsx0 ,lazyCatsy0  ,'k.' , label = "lazy")

plt.title('Garden')
plt.legend(title="Legend")
plt.show()
plt.show()
'''