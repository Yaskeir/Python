# Joanna Buczkowska, Mateusz Fido
#


import random, math
from Animal import Animal

class Cat(Animal):
    
    '''The abstract Cat type subclass. Used exclusively to 
    differentiate from the Mouse subclass. Can be used to
    plot only Cat type objects instead of every Cat subclass
    being plotted separately.'''

    def __init__(self, coordinates, n):
        super().__init__(coordinates, n)

    def mouseInteraction(self, mouse):
        pass