class Animal:
    def __init__(self, coordinates, n):
        self.positionsX = []
        self.positionsY = []
        self.x0 = coordinates[2*n]
        self.y0 = coordinates[2*n+1]
        self.x = self.x0
        self.y = self.y0
        self.step = None