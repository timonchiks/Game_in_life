from cell import *

import random


class Board:
    def __init__(self, left=1, right=51, bott=1, top=51):
        self.left = left
        self.right = right
        self.top = top
        self.bott = bott
        self.cells = {}
        for i in range(bott - 1, top + 1):
            for j in range(left - 1, right + 1):
                self.cells[i, j] = Cell(random.choice([True, False]))
                if i in [bott - 1, top] or j in [left - 1, right]:
                    self.cells[i, j].alive = False
        for i in range(bott, top):
            for j in range(left, right):
                for h1 in range(-1, 2):
                    for h2 in range(-1, 2):
                        if (h1 != 0 or h2 != 0):
                            self.cells[i, j].neighbours.append(self.cells[i + h1, j + h2])

    def visualize(self):
        print("      ", end='')
        for i in range(self.left, self.right):
            dist = ""
            for j in range(5 - len(str(i))):
                dist += " "
            print(i, end=dist)
        print()
        print("   ", end='-')
        for j in range(self.left, self.right):
            print("-----", end='')
        print()
        for i in range(self.bott, self.top):
            if (i >= 10):
                print(i, end=' ')
            else:
                print(i, end='  ')
            for j in range(self.left, self.right):
                if (self.cells[i, j].alive == True):
                    print("|", end='████')
                else:
                    print("|", end='    ')
            print("|")
            print("   ", end='-')
            for j in range(self.left, self.right):
                print("-----", end='')
            print()

    def grow(self):
        for i in range(self.bott, self.top):
            for j in range(self.left, self.right):
                self.cells[i, j].grow()
        for i in range(self.bott, self.top):
            for j in range(self.left, self.right):
                self.cells[i, j].afterGrow()

    def forSet(self):
        g = ""
        alive = False
        for i in range(self.bott, self.top):
            for j in range(self.left, self.right):
                if (self.cells[i, j].alive):
                    alive = True
                    g += str(1)
                else:
                    g += str(0)
        if not alive:
            return "0"
        else:
            return g
