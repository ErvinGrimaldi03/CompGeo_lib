import random

import numpy

from convHull_2D import ConvHull2
import numpy as np
# ---------------- #
LOWERBOUND = 0
UPPERBOUND = 30
# ----------------#

if __name__ == "__main__":
    random_coord = [(random.randint(LOWERBOUND, UPPERBOUND), random.randint(LOWERBOUND, UPPERBOUND)) for i in range(10)]

    convexHull2d = ConvHull2(random_coord)
    convexHull2d.graham()