import matplotlib.pyplot as plt
import matplotlib.patches as patches

from Point import Point

class QuadTreeNode:
    def __init__(self, origin:Point, width=100.0, height=100.0, cut=2, size=1 ):
        self.p = origin
        self.x, self.y = origin.x, origin.y
        self.w, self.h = width, height
        self.half_w, self.half_h = width/2, height/2    # Integer division is expensive, save something (Maybe)
        self.cut = cut

        self.depth = 0
        #   NW(-, -)    NE(+, -)
        #   SW(-,+)     SE(-, -)
        self.children = [None, None, None, None]  # NE, NW, SE, SW
        self.points = []
        self.len = len(self.points)

    def add(self, other:Point):
        if not self._inbound(other):
            return Exception(f"POINT OUT OF BOUNDS: \nPoint:{other} not inside Bounds:({self.w},{self.h})")

        if self.len < 2:
            self.points.append(other)
            return True

        else:
            if self.children[0] is None:
                self._subdivise()

            quadrant = self._find_quadrant(other)
            if quadrant:
                return self.children[quadrant].add(other)
            else:
                raise Exception("Impossible to find valid quadrant")

    def _find_quadrant(self, point):
        if point.x <= self.x and point.y <= self.y:
            return 1  # NW
        elif point.x > self.x and point.y <= self.y:
            return 0  # NE
        elif point.x <= self.x and point.y > self.y:
            return 3  # SW
        elif point.x > self.x and point.y > self.y:
            return 2  # SE
        return None  # In case the point is exactly on the boundary

    def _subdivise(self):
        self.children[0] = QuadTreeNode(Point((self.x + self.half_w, self.y - self.half_h)), self.half_w, self.half_h, self.cut)  # NE
        self.children[1] = QuadTreeNode(Point((self.x - self.half_w, self.y - self.half_h)), self.half_w, self.half_h, self.cut)  # NW
        self.children[2] = QuadTreeNode(Point((self.x + self.half_w, self.y + self.half_h)), self.half_w, self.half_h, self.cut)  # SE
        self.children[3] = QuadTreeNode(Point((self.x - self.half_w, self.y + self.half_h)), self.half_w, self.half_h, self.cut)  # SW
        self.depth += 1



    def _inbound(self, other:Point):
        #   -X <= OTHER.X <= X and -Y <= OTHER.Y <= Y
        return ((self.x - self.half_w <= other.x <= self.x + self.half_w) and (self.y - self.half_h <= other.y <= self.y + self.half_h))

    def _get_depth(self):
        return self.points

    def draw(self, ax):
        rect = patches.Rectangle((self.x - self.half_w, self.y - self.half_h), self.w, self.h, fill=False)
        ax.add_patch(rect)

        # Draw points
        for point in self.points:
            ax.plot(point.x, point.y, 'ro')

        # Recursively draw children
        if self.children[0] is not None:
            for child in self.children:
                child.draw(ax)



# TODO: ADD THE ABILITY TO HAVE OBJECTED CONSTRUCTED FRPM OTHER DIFFERENT TYPE OBJECTS
class QuadTree(object):
    def __init__(self, origin:Point, width, height, cut:int=2):
        self.root = QuadTreeNode(origin, width, height, 2)

    def add(self, other:Point):
        self.root.add(other)

    def draw(self):
        fig, ax = plt.subplots()
        self.root.draw(ax)
        plt.show()

    def get_depth(self):
        return self.root._get_depth()


p = Point((0,0))
quad_tree = QuadTree(p, 100, 100) # Define the boundary of the root (x, y, width, height)
quad_tree.add(Point((28, 30)))
quad_tree.add(Point((50, 50)))
quad_tree.add(Point((-34, 50)))
print(quad_tree.get_depth())
quad_tree.draw()