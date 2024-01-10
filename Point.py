class Point():
    def __init__(self, cord, opt=None):
        if not opt:
            self.x,self.y = cord
        else:
            self.x, self.y = cord, opt

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"