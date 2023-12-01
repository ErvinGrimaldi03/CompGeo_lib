import random

import numpy

from convHull_2D import ConvHull2, LOWERBOUND, UPPERBOUND
import numpy as np
# ---------------- #

# ----------------#

if __name__ == "__main__":
    random_coord = [(random.randint(LOWERBOUND, UPPERBOUND), random.randint(LOWERBOUND, UPPERBOUND)) for i in range(100)]

    '''SAMPLE FOR CONVEXHULL2D '''
    # convexHull2d = ConvHull2(random_coord)
    # convexHull2d.graham()
    # convexHull2d.draw()
    # convexHull2d.animate_draw(show_all_steps=True)
    # convexHull2d.animate_draw(show_all_steps=False)


