import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from functools import cmp_to_key

from Point import Point


def min_point(l):
    min_y, index = float("inf"), 0

    for i in range(len(l)):
        if l[i].y < min_y:
            min_y = l[i].y
            index = i
        if l[i].y == min_y:
            if l[i].x < l[index].x:
                index = i
        return min_y, index

def direction(p0, p1, p2):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])

def distance_sq(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def compare_polar(p1, p2, p0):
    d = direction(p0, p1, p2)
    if d < 0:
        return -1
    if d > 0:
        return 1
    if d == 0:
        if distance_sq(p1, p0) < distance_sq(p2, p0):
            return -1
        else:
            return 1

class ConvHull2:
    def __init__(self, coord):
        print(coord, '\n')
        self.coord = [Point(i) for i in coord]
        self.polar_coord = []
        self.stack = []

    def cart2polar(self) -> None:
        for point in self.coord:
            x, y = point.x, point.y
            rho = np.sqrt(x ** 2 + y ** 2)
            phi = np.arctan2(y, x)
            x = (rho, phi)
            self.polar_coord.append(x)

    def graham(self):
        # 1 find the lower y-bound. Insert point to the beginning of the list and add to the stack
        p0, index = min_point(self.coord)
        self.coord[0], self.coord[index] = self.coord[index], self.coord[0]
        self.stack.append(p0)
        # 2 convert point to Polar coordinates and sort the array
        self.cart2polar()

        sorted_polar = sorted(self.coord[1:], key=cmp_to_key(lambda p1, p2: compare_polar(p1, p2, p0)))






