# Joanna Buczkowska, Mateusz Fido
#
# The main executable file for the Cat Simulation project.

import numpy as np
import random
import Animal, Cat
import matplotlib.pyplot as plt
from Kitten import Kitten
from LazyCat import LazyCat
from MiddleCat import MiddleCat
from BigCat import BigCat
from Mouse import Mouse


def animalFromFile(filename):
    '''Takes a text type file as an argument, 
    turns each String into a List of two coordinates
    and returns a List of Integers as a result.'''
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


mice = [Mouse(animalFromFile("mice.txt"), n) for n in range(0,15)]
kittens = [Kitten(animalFromFile("kittens.txt"), n) for n in range(0,6)]
middleCats = [MiddleCat(animalFromFile("middleCats.txt"), n) for n in range(0,4)]   # initialize each Animal
lazyCats = [LazyCat(animalFromFile("lazyCats.txt"), n) for n in range(0,4)]         # in a list of instances
bigCats = [BigCat(animalFromFile("bigCats.txt"), n) for n in range(0,3)]

def simulate(iterations):
    '''Takes a number of iterations as an argument and simulates
    movement of each Animal from the list. Starts with mice and
    checks for interaction with each Cat type object.'''
    frames = 0
    while frames < iterations:
        for mouse in mice:
            mouse.move()
            for bigCat in bigCats:
                bigCat.mouseInteraction(mouse)
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
        for bigCat in bigCats:
            bigCat.move()
        
        frames += 1

def plot():
    '''Plots the simulation results. Each Animal is plotted according to its type.
    Dead mice's trajectories are not plotted, only their home start point is.'''

    for middleCat in middleCats:
        plt.plot(middleCat.positionsX, middleCat.positionsY, 'r')
        plt.plot(middleCat.x0, middleCat.y0, 'r.', markersize=20)
    plt.plot(middleCat.x0, middleCat.y0,'r.', label = "middleCats")

    for mouse in mice:
        if mouse.alive:
            plt.plot(mouse.positionsX, mouse.positionsY, 'b')
        plt.plot(mouse.x0, mouse.y0, 'b.', markersize=20)
    plt.plot(mouse.x0, mouse.y0,'b.', label = "mice")

    for kitten in kittens:
        plt.plot(kitten.positionsX, kitten.positionsY, 'g')
        plt.plot(kitten.x0, kitten.y0, 'g.', markersize=20)
    plt.plot(kitten.x0, kitten.y0,'g.', label = "kittens")

    for lazyCat in lazyCats:
        plt.plot(lazyCat.positionsX, lazyCat.positionsY, 'y')
        plt.plot(lazyCat.x0, lazyCat.y0, 'y.', markersize=20)
    plt.plot(lazyCat.x0, lazyCat.y0,'y.', label = "lazyCats")

    for bigCat in bigCats:
        plt.plot(bigCat.positionsX, bigCat.positionsY, 'm')
        plt.plot(bigCat.x0, bigCat.y0, 'm.', markersize=20)
    plt.plot(bigCat.x0, bigCat.y0,'m.', label = "bigCats")

    plt.title('Garden')
    plt.legend(title="Legend", loc='center left', bbox_to_anchor=(1, 0.82))

    plt.show()

simulate(600)
plot()