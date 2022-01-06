import time

from board import *


def main():
    print("Please, enter the size of the world in this way (left, right, bott, top) sides:")
    print("It must be integer values, split them with space")
    m = list(input().split())
    a = Board(int(m[0]), int(m[1]), int(m[2]), int(m[3]))
    check = set()
    while True:
        a.visualize()
        mask = a.forSet()
        if mask in check:
            break
        check.add(mask)
        a.grow()
        time.sleep(0.5)
    if "0" in check:
        print("everybody is dead :-(")
    else:
        print("This form will live forever ;-)")


main()
