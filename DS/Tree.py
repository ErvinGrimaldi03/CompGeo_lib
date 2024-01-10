import matplotlib.pyplot as plt
import matplotlib.patches as patches
class Point:
    """ Represents a point in 2D space """
    def __init__(self, x, y):
        self.x = x
        self.y = y

class QuadTreeNode:
    """ Represents a node in the QuadTree """
    def __init__(self, x, y, width, height):
        self.boundary = (x, y, width, height) # (x, y) is the center of the node
        self.points = []
        self.children = [None, None, None, None] # NE, NW, SE, SW

    def insert(self, point):
        if not self._in_boundary(point):
            return False

        if len(self.points) < 4:
            self.points.append(point)
            return True
        else:
            if self.children[0] is None:
                self._subdivide()

            for child in self.children:
                if child.insert(point):
                    return True

    def _in_boundary(self, point):
        x, y, w, h = self.boundary
        return (x - w/2 <= point.x <= x + w/2) and (y - h/2 <= point.y <= y + h/2)

    def _subdivide(self):
        x, y, w, h = self.boundary
        half_w, half_h = w / 2, h / 2

        # Creating 4 children: NE, NW, SE, SW
        self.children[0] = QuadTreeNode(x + half_w/2, y - half_h/2, half_w, half_h) # NE
        self.children[1] = QuadTreeNode(x - half_w/2, y - half_h/2, half_w, half_h) # NW
        self.children[2] = QuadTreeNode(x + half_w/2, y + half_h/2, half_w, half_h) # SE
        self.children[3] = QuadTreeNode(x - half_w/2, y + half_h/2, half_w, half_h) # SW

    def draw(self, ax):
        x, y, w, h = self.boundary
        rect = patches.Rectangle((x - w/2, y - h/2), w, h, fill=False)
        ax.add_patch(rect)

        # Draw points
        for point in self.points:
            ax.plot(point.x, point.y, 'ro')

        # Recursively draw children
        if self.children[0] is not None:
            for child in self.children:
                child.draw(ax)

class QuadTree:
    """ Represents the QuadTree """
    def __init__(self, boundary):
        self.root = QuadTreeNode(boundary[0], boundary[1], boundary[2], boundary[3])

    def insert(self, point):
        self.root.insert(point)

    def draw(self):
        fig, ax = plt.subplots()
        self.root.draw(ax)
        plt.show()

# Example Usage
p = Point(0,0)
quad_tree = QuadTree((0,0, 100, 100)) # Define the boundary of the root (x, y, width, height)
quad_tree.insert(Point(28, 30))
quad_tree.insert(Point(50, 50))
quad_tree.insert(Point(34, 50))
quad_tree.insert(Point(12,12))
quad_tree.insert(Point(2,32))

quad_tree.draw()