class Point():
    def __init__(self, cord):
        self.x,self.y = cord

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y