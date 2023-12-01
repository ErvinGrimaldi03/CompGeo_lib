import random

import numpy

from convHull_2D import ConvHull2
from variables import LOWERBOUND, UPPERBOUND
from ALGO.Triangulation import triangulate
import numpy as np
# ---------------- #

# ----------------#

if __name__ == "__main__":
    random_coord = [(random.randint(LOWERBOUND, UPPERBOUND), random.randint(LOWERBOUND, UPPERBOUND)) for i in range(17)]

    '''SAMPLE FOR CONVEXHULL2D '''
    convexHull2d = ConvHull2(random_coord)
    polygon = convexHull2d.hull()
    convexHull2d.draw()
    triangulate(polygon)
    # convexHull2d.animate_draw(show_all_steps=True)
    # convexHull2d.animate_draw(show_all_steps=False)


