# Joanna Buczkowska, Mateusz Fido
#
# The starting abstract superclass used to represent two subclasses: Cats and Mice.
# Defines two Lists holding X and Y coordinates of the object. Defines starting points
# to be read from the initializing text file. Defines the X and Y coordinates and step,
# overriden by each Cat or Mouse.

class Animal:
    def __init__(self, coordinates, n):
        self.positionsX = []
        self.positionsY = []
        self.x0 = coordinates[2*n]
        self.y0 = coordinates[2*n+1]
        self.x = self.x0
        self.y = self.y0
        self.stepx = None
        self.stepy = None