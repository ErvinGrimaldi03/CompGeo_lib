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
from matplotlib.animation import FuncAnimation


LOWERBOUND = 0
UPPERBOUND = 3000

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


class ConvHull2:  # O(n log n)
    def __init__(self, coord):
        print(coord, '\n')
        self.coord = [Point(i) for i in coord]
        self.rep_cord = [i for i in self.coord]  # Copying the coord list for representation in graph if needed.
        self.polar_coord = []
        self.stack = []
        self.final_stack_states= []
        self.stack_states = []   # check the state of the stack. Used for representation in animation_graph

    def graham(self):
        anchor = min_i(self.coord)
        self.stack.append(anchor)
        self.coord.remove(anchor)

        self.to_polar(anchor)
        self.sort_by_angle(anchor)

        for p in self.polar_coord:
            while len(self.stack) >= 2 and self.ccw(self.stack[-2], self.stack[-1], p[0]) <= 0:
                self.stack.pop()
                self.stack_states.append(self.stack[:])  # Store state after removal
            self.stack.append(p[0])
            self.stack_states.append(self.stack[:])  # Store state after addition
            self.final_stack_states.append(self.stack[:])  # Store correct state

        # print(self.stack)

    def ccw(self, p1, p2, p3):
        return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

    def sort_by_angle(self, anchor):
        self.polar_coord.sort(key=lambda x: x[2])

    def to_polar(self, anchor):  # O(n)
        for p in self.coord:
            r = math.sqrt(((p.x - anchor.x) ** 2) + ((p.y - anchor.y) ** 2))
            thau = np.arctan2((p.y - anchor.y), (p.x - anchor.x))
            pc = (p, r, thau)
            self.polar_coord.append(pc)

    def draw(self):
        # Extract x and y coordinates of each point
        x_coords = [p.x for p in self.rep_cord]
        y_coords = [p.y for p in self.rep_cord]

        # Plot all points
        plt.scatter(x_coords, y_coords, label='Points')

        # Extract x and y coordinates of convex hull points
        hull_x = [p.x for p in self.stack] + [self.stack[0].x]
        hull_y = [p.y for p in self.stack] + [self.stack[0].y]

        # Plot convex hull
        plt.plot(hull_x, hull_y, color='red', label='Convex Hull')

        # Optionally, highlight the anchor point
        anchor = self.stack[0]
        plt.scatter([anchor.x], [anchor.y], color='green', label='Anchor Point')

        # Set labels and show plot
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Convex Hull')
        plt.legend()
        plt.show()


    def animate_draw(self, show_all_steps=True):
        fig, ax = plt.subplots()
        ax.set_xlim(LOWERBOUND - 5, UPPERBOUND + 5)
        ax.set_ylim(LOWERBOUND - 5, UPPERBOUND + 5)

        x_coords = [p.x for p in self.rep_cord]
        y_coords = [p.y for p in self.rep_cord]
        ax.scatter(x_coords, y_coords, label='Points')

        line, = ax.plot([], [], lw=2, color='red')

        def init():
            line.set_data([], [])
            return line,

        def animate(i):
            if show_all_steps:
                states = self.stack_states
                if i < len(states):
                    x_hull = [p.x for p in states[i]] + [states[i][0].x]
                    y_hull = [p.y for p in states[i]] + [states[i][0].y]
                    line.set_data(x_hull, y_hull)
            else:
                # When show_all_steps is False, directly show the final convex hull
                x_hull = [p.x for p in self.stack] + [self.stack[0].x]
                y_hull = [p.y for p in self.stack] + [self.stack[0].y]
                line.set_data(x_hull, y_hull)

            return line,

        frames = len(self.stack_states)
        anim = FuncAnimation(fig, animate, init_func=init, frames=frames, interval=200, blit=True)

        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Convex Hull Formation')
        plt.legend()
        plt.show()

        return anim

