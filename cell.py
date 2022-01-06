class Cell:

    def __init__(self, isAlive=False):
        self.alive = isAlive
        self.nextGeneration = False
        self.neighbours = list()

    def grow(self):
        count = 0
        for i in self.neighbours:
            if i.alive:
                count += 1
        if (count == 2 and self.alive == True) or (count == 3):
            self.nextGeneration = True

    def afterGrow(self):
        ans = (self.alive != self.nextGeneration)
        self.alive = self.nextGeneration
        self.nextGeneration = False
