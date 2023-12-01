'''
REQUIREMENTS FOR GRAHAM SCAN

- find anchor
- sort by polar coordinates based on anchor
- loop and get the smallest point
'''

import math

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from functools import cmp_to_key
from Point import Point


def min_i(coords: list[Point]) -> Point:  # O(n)
    if coords == []:
        raise ValueError("coords cannot be empty")
    min_y = float("inf")
    min_i = None
    for p in coords:
        x = p.x
        y = p.y
        if y < min_y:
            min_y = y
            min_i = p
        elif y == min_y:
            if x < min_i.x:
                min_i = p
    return min_i


class ConvHull2:
    def __init__(self, coord):
        print(coord, '\n')
        self.coord = [Point(i) for i in coord]
        self.rep_cord = [i for i in self.coord]  # Copying the coord list for representation in graph if needed.
        self.polar_coord = []
        self.stack = []

    def graham(self):
        anchor = min_i(self.coord)
        self.stack.append(anchor)
        self.coord.remove(anchor)

        self.to_polar(anchor)
        self.sort_by_angle(anchor)
        print(self.polar_coord)
    def sort_by_angle(self, anchor):
        self.polar_coord.sort(key=lambda x: x[2])

    def to_polar(self, anchor):  # O(n)
        for p in self.coord:
            r = math.sqrt(((p.x - anchor.x) ** 2) + ((p.y - anchor.y) ** 2))
            thau = np.arctan2((p.y - anchor.y), (p.x - anchor.x))
            pc = (p, r, thau)
            self.polar_coord.append(pc)

# Luca: Y, Y
